
symbolicOutput(0).  % set to 1 for DEBUGGING: to see symbolic output only; 0 otherwise.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% To use this prolog template for other optimization problems, replace the code parts 1,2,3,4 below. %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% The supermarket has a number of employees for performing different tasks.
%% These tasks are planned every 72 opening hours, according to a forecast
%% of the tasks to be done every hour.
%% No employee can perform two different tasks during the same hour or on two consecutive hours.
%% Some employees are not available on certain hours.
%% We want to assign all tasks (which employee does what task when) and
%% we want to find the minimal K such that no employee works more than
%% K consecutive hours.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%% begin input example supermarketExampleA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% % example: 4 employees are needed at the checkout on hour 1, one employee on hour 2, etc.
%% employeesNeeded( checkout,       [4,1,2,4,2,1,1,4,1,1,3,2,4,2,1,2,1,3,2,3,4,1,3,1,2,3,1,3,4,3,2,3,4,2,3,1,4,4,1,4,2,2,1,4,3,3,3,2,2,3,4,4,1,3,3,3,4,4,1,1,2,3,3,3,3,2,1,3,1,1,3,2] ).
%% employeesNeeded( restocking,     [1,2,1,3,1,4,3,1,3,1,4,3,2,2,1,2,1,2,1,1,2,1,2,1,1,3,1,2,2,4,3,2,4,4,4,1,2,4,4,2,4,4,4,3,2,2,1,3,2,1,3,3,2,3,3,3,1,4,1,1,3,1,2,3,3,1,4,4,3,3,2,1] ).
%% employeesNeeded( orders,         [2,4,2,1,1,1,4,1,1,4,1,3,2,4,1,1,4,1,4,3,1,3,2,4,4,2,4,2,1,1,4,3,1,2,2,2,1,1,3,1,1,1,2,2,4,1,1,3,4,4,2,3,2,4,3,1,1,1,3,4,2,2,4,4,3,1,1,2,1,4,3,2] ).
%%
%% employees([e01,e02,e03,e04,e05,e06,e07,e08,e09,e10,e11,e12]).
%%
%% notAvailable(e01,[6,13,14,16,21,35,37,41,59]).
%% notAvailable(e02,[14,34,40,45,48,52,58,65,70,72]).
%% notAvailable(e03,[8,11,13,27,30,38,50,51,70]).
%% notAvailable(e04,[4,12,16,17,26,30,42,45,48,55,71]).

%%%%%%% end input example supermarketExampleA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% EXAMPLE OUTPUT with cost 18:
%% 
%%                       10        20        30        40        50        60        70  
%%               123456789012345678901234567890123456789012345678901234567890123456789012
%% 
%% employee e01: ------------------------------o-------o-----o----o----o--------------o--
%% employee e02: ------o--o-o--------------o--ooo-----oo---oo-----o----o---o----o--------
%% employee e03: -o----o--o-o-o--o-------o-----oo-oo-o-oo-oooo--oo--o-oo-oooo--o-------o-
%% employee e04: -oo---o--o--oo----oo-o-oo-o-o-oooooo-rr-o--r----oooooo-o-r-o--ooo--o-o--
%% employee e05: oooooooooooooo--o-oo-o-ooooo-r--rr-o-rr-r-r-o--ooooooo-r-r-oooooooooooo-
%% employee e06: oo-r--r-r-rr-oo-o-oooooooooo-r--rrr-rrr-r-r-ooooo-rr-o-r-r-oooooo-rr-ooo
%% employee e07: -r-r-rr-r-rrrr--ooo-r-oo-r-rrrrrrrr-rrrrrrrrr--r--rrrrrrrrr-r--rr-rrrr-o
%% employee e08: rrrrrrrrr-rrrr-o-r-rrrr--r-rrrrrrrrr-c-rrrrrrr-rrrrrrrr-c-o-r-rrr-rrrrr-
%% employee e09: c--c-r-c-rr-c--rrrr-c-rrrrr-c-r-c-r-cc-c-r-c-rrrr-cc-rr-cc--rrrrrrrrrrrr
%% employee e10: c--c-r-c--c-c-rr-cccc-c--c-ccc-cc-c-cc-c-r-cccc--ccc-ccccc-r-cccc--c--c-
%% employee e11: c-ccc--c--cccc-c-cccc-c-cc-cccccccc-cc-ccc-ccccccccc-ccccc--cccccc-c--cc
%% employee e12: cccccccccccccccccc-cccccccccccccccccc-cccccccccccccc-ccccccccccccccccccc


%%%%%%% Some helpful definitions to make the code cleaner: ====================================

task(T):-          employeesNeeded(T,_).
needed(T,H,N):-    employeesNeeded(T,L), nth1(H,L,N).
employee(E):-      employees(L), member(E,L).
hour(H):-          between(1,72,H).
blocked(E,H):-     notAvailable(E,L), member(H,L).
available(E,H):-   hour(H), employee(E), \+blocked(E,H).

%%%%%%% End helpful definitions ===============================================================


%%%%%%%  1. Declare SAT variables to be used: =================================================

satVariable( does(E,T,H) ) :-  available(E, H), task(T).  %  means:  "employee E does task T at hour H"     (MANDATORY)
satVariable( works(E, H) ) :-  available(E, H).


%%%%%%%  2. Clause generation for the SAT solver: =============================================

% This predicate writeClauses(MaxCost) generates the clauses that guarantee that
% a solution with cost at most MaxCost is found

writeClauses(infinite) :- !, writeClauses(72),!.
writeClauses(MaxConsecutiveHours) :-
    atLeastKEmployeesOnTaskOnHour, 
        atMostOneTaskPerHour,
        linkWorksWithDoes,
    respectBreakBetweenTasks,
        respectMaxConsecutiveHours(MaxConsecutiveHours),
    
    true,!.
writeClauses(_) :- told, nl, write('writeClauses failed!'), nl,nl, halt.

atLeastKEmployeesOnTaskOnHour :-
        task(T),
        hour(H),
        needed(T,H,N),
        findall(does(E,T,H), available(E,H), Lits),
        exactly(N,Lits),
        fail.
atLeastKEmployeesOnTaskOnHour.

atMostOneTaskPerHour :-
        available(E,H),
        task(T1),
        task(T2),
        T1 @< T2,
        writeOneClause([ -does(E,T1,H), -does(E,T2,H) ]),
        fail.
atMostOneTaskPerHour.

linkWorksWithDoes :-
        available(E,H),
        findall(does(E,T,H), task(T), Lits),
        expressOr(works(E,H), Lits),
        fail.
linkWorksWithDoes.

respectBreakBetweenTasks :-
        available(E,H),
        H < 72,
        H1 is H+1,
        available(E,H1),
        task(T1),
        task(T2),
        T1 \= T2,
        writeOneClause([ -does(E,T1,H), -does(E,T2,H1) ]),
        fail.
respectBreakBetweenTasks.

respectMaxConsecutiveHours(MaxConsecutiveHours) :-
        employee(E),
        Start is 1,
        End is 72-MaxConsecutiveHours,
        between(Start,End,H),
        HEnd is H+MaxConsecutiveHours,
        findall(works(E,Hh), (between(H,HEnd,Hh), available(E,Hh)), Window),
        atMost(MaxConsecutiveHours, Window),
        fail.
respectMaxConsecutiveHours(_).


%%%%%%%  3. DisplaySol: this predicate displays a given solution M: ===========================

% displaySol(M) :- write(M), nl, fail.
displaySol(M) :- nl,nl,
    write('                      10        20        30        40        50        60        70  '), nl,
    write('              123456789012345678901234567890123456789012345678901234567890123456789012'), nl,
    employee(E), nl, write('employee '), write(E), write(': '), hour(H), writeIfBusy(E,H,M), fail.
displaySol(_) :- nl,nl,!.

writeIfBusy(E,H,M) :- member( does(E, checkout,    H), M),  write('c'),!.
writeIfBusy(E,H,M) :- member( does(E, restocking,  H), M),  write('r'),!.
writeIfBusy(E,H,M) :- member( does(E, orders,      H), M),  write('o'),!.
writeIfBusy(_,_,_) :- write('-'),!.


%%%%%%%  4. This predicate computes the cost of a given solution M: ===========================

% Here the sort predicate is used to remove repeated elements of the list:
costOfThisSolution(M,Cost) :-
        findall(Run, (employee(E), maxRunEmployee(E,M,Run)), Runs),
        max_list(Runs, Cost), !.

maxRunEmployee(E,M,Run) :-
        findall(H, member(works(E,H),M), WorkedHours),
        longestConsecutive(WorkedHours, Run).

longestConsecutive([], 0).
longestConsecutive([H|Hs], MaxRun) :-
        longestConsecutive(Hs, H, 1, 1, MaxRun).

longestConsecutive([], _, Cur, Max, MaxOut) :-
        MaxOut is max(Cur, Max).
longestConsecutive([H|Hs], Prev, Cur, Max, MaxOut) :-
        ( H =:= Prev+1 -> Cur1 is Cur+1 ; Cur1 = 1 ),
        Max1 is max(Max, Cur1),
        longestConsecutive(Hs, H, Cur1, Max1, MaxOut).


%%%%%%% =======================================================================================



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Everything below is given as a standard library, reusable for solving
%%    with SAT many different problems.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%% Cardinality constraints on arbitrary sets of literals Lits: ===========================

exactly(K,Lits) :- symbolicOutput(1), write( exactly(K,Lits) ), nl, !.
exactly(K,Lits) :- atLeast(K,Lits), atMost(K,Lits),!.

atMost(K,Lits) :- symbolicOutput(1), write( atMost(K,Lits) ), nl, !.
atMost(K,_) :- K < 0, writeOneClause([]), !.    % unsatisfiable
atMost(K,Lits) :-   % l1+...+ln <= k:  in all subsets of size k+1, at least one is false:
      negateAll(Lits,NLits),
      K1 is K+1,    subsetOfSize(K1,NLits,Clause), writeOneClause(Clause),fail.
atMost(_,_).

atLeast(K,Lits) :- symbolicOutput(1), write( atLeast(K,Lits) ), nl, !.
atLeast(K,Lits) :- length(Lits,N), K > N, writeOneClause([]), !.    % unsatisfiable
atLeast(K,Lits) :-  % l1+...+ln >= k: in all subsets of size n-k+1, at least one is true:
      length(Lits,N),
      K1 is N-K+1,  subsetOfSize(K1, Lits,Clause), writeOneClause(Clause),fail.
atLeast(_,_).

negateAll( [], [] ).
negateAll( [Lit|Lits], [NLit|NLits] ) :- negate(Lit,NLit), negateAll( Lits, NLits ),!.

negate( -Var,  Var) :- !.
negate(  Var, -Var) :- !.

subsetOfSize(0,_,[]) :- !.
subsetOfSize(N,[X|L],[X|S]) :- N1 is N-1, length(L,Leng), Leng>=N1, subsetOfSize(N1,L,S).
subsetOfSize(N,[_|L],   S ) :-            length(L,Leng), Leng>=N,  subsetOfSize( N,L,S).


%%%%%%% Express equivalence between a variable and a disjunction or conjunction of literals ===

% Express that Var is equivalent to the disjunction of Lits:
expressOr( Var, Lits ) :- symbolicOutput(1), write( Var ), write(' <--> or('), write(Lits), write(')'), nl, !.
expressOr( Var, Lits ) :- member(Lit,Lits), negate(Lit,NLit), writeOneClause([ NLit, Var ]), fail.
expressOr( Var, Lits ) :- negate(Var,NVar), writeOneClause([ NVar | Lits ]),!.

%% expressOr(a,[x,y]) genera 3 clausulas (como en la Transformación de Tseitin):
%% a == x v y
%% x -> a       -x v a
%% y -> a       -y v a
%% a -> x v y   -a v x v y

% Express that Var is equivalent to the conjunction of Lits:
expressAnd( Var, Lits) :- symbolicOutput(1), write( Var ), write(' <--> and('), write(Lits), write(')'), nl, !.
expressAnd( Var, Lits) :- member(Lit,Lits), negate(Var,NVar), writeOneClause([ NVar, Lit ]), fail.
expressAnd( Var, Lits) :- findall(NLit, (member(Lit,Lits), negate(Lit,NLit)), NLits), writeOneClause([ Var | NLits]), !.


%%%%%%% main: =================================================================================

main :- current_prolog_flag(os_argv, Argv),
        nth0(1, Argv, InputFile),
        main(InputFile), !.
main :-  write('Usage: $ ./<executable> <example>          or ?- main(<example>).'), nl, halt.

main(InputFile) :-
        symbolicOutput(1), !,
        consult(InputFile),
        writeClauses(infinite), halt.   % print the clauses in symbolic form and halt
main(InputFile):-
        consult(InputFile),
        told, write('Looking for initial solution with arbitrary cost...'), nl,
        initClauseGeneration,
        tell(clauses), writeClauses(infinite), told,
        tell(header),  writeHeader, told,
        numVars(N), numClauses(C),
        write('Generated '), write(C), write(' clauses over '), write(N), write(' variables. '),nl,
        shell('cat header clauses > infile.cnf',_),
        write('Launching kissat...'), nl,
        shell('kissat -v infile.cnf > model', Result),  % if sat: Result=10; if unsat: Result=20.
        treatResult(Result,[]),!.

treatResult(20,[]       ):- write('No solution exists.'), nl, halt.
treatResult(20,BestModel):-
        nl,costOfThisSolution(BestModel,Cost), write('Unsatisfiable. So the optimal solution was this one with cost '),
        write(Cost), write(':'), nl, displaySol(BestModel), nl,nl,halt.
treatResult(10,_):- %   shell('cat model',_),
        nl,write('Solution found '), flush_output,
        see(model), symbolicModel(M), seen,
        costOfThisSolution(M,Cost),
        write('with cost '), write(Cost), nl,nl,
        displaySol(M), 
        Cost1 is Cost-1,   nl,nl,nl,nl,nl,  write('Now looking for solution with cost '), write(Cost1), write('...'), nl,
        initClauseGeneration, tell(clauses), writeClauses(Cost1), told,
        tell(header),  writeHeader,  told,
        numVars(N),numClauses(C),
        write('Generated '), write(C), write(' clauses over '), write(N), write(' variables. '),nl,
        shell('cat header clauses > infile.cnf',_),
        write('Launching kissat...'), nl,
        shell('kissat -v infile.cnf > model', Result),  % if sat: Result=10; if unsat: Result=20.
        treatResult(Result,M),!.
treatResult(_,_):- write('cnf input error. Wrote something strange in your cnf?'), nl,nl, halt.


initClauseGeneration:-  %initialize all info about variables and clauses:
        retractall(numClauses(   _)),
        retractall(numVars(      _)),
        retractall(varNumber(_,_,_)),
        assert(numClauses( 0 )),
        assert(numVars(    0 )),     !.

writeOneClause([]) :- symbolicOutput(1),!, nl.
writeOneClause([]) :- countClause, write(0), nl.
writeOneClause([Lit|C]) :- w(Lit), writeOneClause(C),!.
w(-Var) :- symbolicOutput(1), satVariable(Var), write(-Var), write(' '),!.
w( Var) :- symbolicOutput(1), satVariable(Var), write( Var), write(' '),!.
w(-Var) :- satVariable(Var),  var2num(Var,N),   write(-), write(N), write(' '),!.
w( Var) :- satVariable(Var),  var2num(Var,N),             write(N), write(' '),!.
w( Lit) :- told, write('ERROR: generating clause with undeclared variable in literal '), write(Lit), nl,nl, halt.


% given the symbolic variable V, find its variable number N in the SAT solver:
:- dynamic(varNumber / 3).
var2num(V,N) :- hash_term(V,Key), existsOrCreate(V,Key,N),!.
existsOrCreate(V,Key,N) :- varNumber(Key,V,N),!.                            % V already existed with num N
existsOrCreate(V,Key,N) :- newVarNumber(N), assert(varNumber(Key,V,N)), !.  % otherwise, introduce new N for V

writeHeader :- numVars(N),numClauses(C), write('p cnf '),write(N), write(' '),write(C),nl.

countClause :-     retract( numClauses(N0) ), N is N0+1, assert( numClauses(N) ),!.
newVarNumber(N) :- retract( numVars(   N0) ), N is N0+1, assert(    numVars(N) ),!.

% Getting the symbolic model M from the output file:
symbolicModel(M) :- get_code(Char), readWord(Char,W), symbolicModel(M1), addIfPositiveInt(W,M1,M),!.
symbolicModel([]).
addIfPositiveInt(W,L,[Var|L]) :- W = [C|_], between(48,57,C), number_codes(N,W), N>0, varNumber(_,Var,N),!.
addIfPositiveInt(_,L,L).
readWord( 99,W) :- repeat, get_code(Ch), member(Ch,[-1,10]), !, get_code(Ch1), readWord(Ch1,W),!. % skip line starting w/ c
readWord(115,W) :- repeat, get_code(Ch), member(Ch,[-1,10]), !, get_code(Ch1), readWord(Ch1,W),!. % skip line starting w/ s
readWord( -1,_) :-!, fail. %end of file
readWord(C, []) :- member(C,[10,32]), !. % newline or white space marks end of word
readWord(Char,[Char|W]) :- get_code(Char1), readWord(Char1,W), !.

%%%%%%% =======================================================================================
