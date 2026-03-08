#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
#include <list>
using namespace std;

#define UNDEF -1
#define TRUE 1
#define FALSE 0

uint numVars;
uint numClauses;
vector<vector<int>> clauses;
vector<int> model;
vector<int> modelStack;
uint indexOfNextLitToPropagate;
uint decisionLevel;
unordered_map<int, list<uint>> occurList;

class ConflictCounter {

    private:
    multimap<int, int> order;   // counter, id // ordered counters
    unordered_map<int, int> lookup; // id, counter // lookup table for faster updates
    int updates = 0;
    public:

    void insert(const int& id, const int& c = 0) {
        if (lookup.find(id) != lookup.end()) return;
        order.emplace(c, id);
        lookup[id] = c;
    }

    void update(const int& id, const int& c) {
        auto pos = lookup.find(id);
        if (pos == lookup.end()) return;
        auto range = order.equal_range(pos->second);
        for(auto it = range.first; it != range.second; ++it) {
            if (it->second == id){
                order.erase(it);
                order.emplace(c, id);
                lookup[id]=c;
                break;
            }
        }
        
        updates++;

        if (updates >= 500000)  this->divideOlder();
    }

    void inc(const int& id) {
        int c = lookup[id];
        this->update(id, c+1);
    }

    void divideOlder() {
        for (auto it = lookup.begin(); it != lookup.end(); ++it) {
            updates = 0;
            this->update(it->first, it->second / 2);
        }
    }

    int nextToDecide() {
        if (order.empty()) return 0;
        for (auto it = order.rbegin(); it != order.rend(); ++it) {
            if (model[it->second] == UNDEF) return it ->second;
        }
        return 0;
    }

    void print() {
        for (auto it = order.rbegin(); it != order.rend(); ++it){
            cout << it->second << " : " << it->first << endl;
        }
    }

    /*void printUp() {
        cout << updates << endl;
    }*/

};

ConflictCounter ConfCtr;

void readClauses()
{
    // Skip comments
    char c = cin.get();
    while (c == 'c')
    {
        while (c != '\n')
            c = cin.get();
        c = cin.get();
    }
    // Read "cnf numVars numClauses"
    string aux;
    cin >> aux >> numVars >> numClauses;
    clauses.resize(numClauses);
    // Read clauses
    for (uint i = 0; i < numClauses; ++i)
    {
        int lit;
        while (cin >> lit and lit != 0) {
            clauses[i].push_back(lit);
            occurList[lit].push_back(i);
            ConfCtr.insert(abs(lit));
        }

    }
}

int currentValueInModel(int lit)
{
    if (lit >= 0)
        return model[lit];
    else
    {
        if (model[-lit] == UNDEF)
            return UNDEF;
        else
            return 1 - model[-lit];
    }
}

void setLiteralToTrue(int lit)
{
    modelStack.push_back(lit);
    if (lit > 0)
        model[lit] = TRUE;
    else
        model[-lit] = FALSE;
}

bool propagateGivesConflict()
{
    while (indexOfNextLitToPropagate < modelStack.size())
    {
        // Miramos clausulas que aparece el lit
        for (uint i : occurList[-modelStack[indexOfNextLitToPropagate]])
        {
            bool someLitTrue = false;
            int numUndefs = 0;
            int lastLitUndef = 0;
            // Comprobamos si ninguno es True 
            for (uint k = 0; not someLitTrue and k < clauses[i].size(); ++k)
            {
                int val = currentValueInModel(clauses[i][k]);
                if (val == TRUE)
                    someLitTrue = true;
                else if (val == UNDEF)
                {
                    ++numUndefs;
                    lastLitUndef = clauses[i][k];
                }
            }
            if (not someLitTrue and numUndefs == 0){
                for (uint k = 0; k < clauses[i].size(); ++k) {
                    ConfCtr.inc(abs(clauses[i][k]));
                }
                return true; // conflict! all lits false
            }
            else if (not someLitTrue and numUndefs == 1)
            {
                setLiteralToTrue(lastLitUndef);
            }
        }
        ++indexOfNextLitToPropagate;
    }
    return false;
}
void backtrack()
{
    uint i = modelStack.size() - 1;
    int lit = 0;
    while (modelStack[i] != 0)
    { // 0 is the DL mark
        lit = modelStack[i];
        model[abs(lit)] = UNDEF;
        modelStack.pop_back();
        --i;
    }
    // at this point, lit is the last decision
    modelStack.pop_back(); // remove the DL mark
    --decisionLevel;
    indexOfNextLitToPropagate = modelStack.size();
    setLiteralToTrue(-lit); // reverse last decision
}

// Heuristic for finding the next decision literal:
int getNextDecisionLiteral()
{
    return ConfCtr.nextToDecide();        // reurns 0 when all literals are defined
}

void checkmodel()
{
    for (uint i = 0; i < numClauses; ++i)
    {
        bool someTrue = false;
        for (uint j = 0; not someTrue and j < clauses[i].size(); ++j)
            someTrue = (currentValueInModel(clauses[i][j]) == TRUE);
        if (not someTrue)
        {
            cout << "Error in model, clause is not satisfied:";
            for (uint j = 0; j < clauses[i].size(); ++j)
                cout << clauses[i][j] << " ";
            cout << endl;
            exit(1);
        }
    }
}

int main()
{
    readClauses(); // reads numVars, numClauses and clauses
    model.resize(numVars + 1, UNDEF);
    indexOfNextLitToPropagate = 0;
    decisionLevel = 0;

    // Take care of initial unit clauses, if any
    for (uint i = 0; i < numClauses; ++i)
        if (clauses[i].size() == 1)
        {
            int lit = clauses[i][0];
            int val = currentValueInModel(lit);
            if (val == FALSE)
            {
                cout << "UNSATISFIABLE" << endl;
                //ConfCtr.printUp();
                return 20;
            }
            else if (val == UNDEF)
                setLiteralToTrue(lit);
        }

    // DPLL algorithm
    while (true)
    {
        while (propagateGivesConflict())
        {
            if (decisionLevel == 0)
            {
                cout << "UNSATISFIABLE" << endl;
                //ConfCtr.printUp();
                return 20;
            }
            backtrack();
        }
        int decisionLit = getNextDecisionLiteral();
        if (decisionLit == 0)
        {
            checkmodel();
            cout << "SATISFIABLE" << endl;
            //ConfCtr.printUp();
            return 10;
        }
        // start new decision level:
        modelStack.push_back(0); // push mark indicating new DL
        ++indexOfNextLitToPropagate;
        ++decisionLevel;
        setLiteralToTrue(decisionLit); // now push decisionLit on top of the mark
    }
}
