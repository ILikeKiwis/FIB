%% ----------- [5 points] ---------- %%

symbolicOutput(0).  % set to 1 for debugging: to see symbolic output only; 0 otherwise.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% There is a list of activities to be planned.
%% Each activity should take place
%%   - on one day within the specified range,
%%   - in one of the compatible venues, and
%%   - it requires a minimum number of people, who must be skilled at that activity.
%%
%% People can do   several activities, but at most one at a time.
%% Venues can hold several activities, but at most one at a time.
%%
%% Complete the missing Prolog code (indicated with %...) so that given the input data,
%% the program finds a valid timetable:
%% for each activity who will do it, and when and where it will take place.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% ==== Example input (timetablingEx1_sat.pl):

%% %% There are 2 days: 1 and 2.
%% numDays(2).

%% %% There are 3 venues: 1, 2 and 3.
%% numVenues(3).

%% %% There are 4 activities.
%% %% E.g., activity 1 needs at least 3 people and can take place from day 1 to day 2 at venues 2 or 3.
%% activity(1, 3, 1, 2, [2, 3]).
%% activity(2, 2, 1, 1, [2, 3]).
%% activity(3, 1, 1, 2, [1, 3]).
%% activity(4, 2, 2, 2, [1, 2]).

%% activity(Ai, P, di, df, [V]) 
%% Ai activity number
%% P number of people
%% di, df, initial and final day
%% V Compat ven


%% %% There are 5 people.
%% %% E.g., person 1 can do activities 1, 2, 3.
%% person(1, [1, 2, 3]).
%% person(2, [2]).
%% person(3, [2, 3]).
%% person(4, [1, 4]).
%% person(5, [1, 2, 3, 4]).

%% person(Pi, [Ai]) Person number Pi does activites [Ai]

%% ==== end input.

%% ==== And one posible output:

%% activity(1)-day(1)-venue(3):people([1,4,5])
%% activity(2)-day(1)-venue(2):people([2,3])
%% activity(3)-day(2)-venue(3):people([3])
%% activity(4)-day(2)-venue(2):people([4,5])

%% day(1)-person(1):activities([1])
%% day(2)-person(1):activities([])
%% day(1)-person(2):activities([2])
%% day(2)-person(2):activities([])
%% day(1)-person(3):activities([2])
%% day(2)-person(3):activities([3])
%% day(1)-person(4):activities([1])
%% day(2)-person(4):activities([4])
%% day(1)-person(5):activities([1])
%% day(2)-person(5):activities([4])

%% day(1)-venue(1):activities([])
%% day(2)-venue(1):activities([])
%% day(1)-venue(2):activities([2])
%% day(2)-venue(2):activities([4])
%% day(1)-venue(3):activities([1])
%% day(2)-venue(3):activities([3])

%% ==== end output.


%%%%%% Some helpful definitions to make the code cleaner:

person(P) :- person(P, _).

day(D)   :- numDays(  NumDays),   between(1, NumDays,   D).
venue(V) :- numVenues(NumVenues), between(1, NumVenues, V).

activity(A)          :- activity(A, _, _, _, _).
activityNeeds( A, N) :- activity(A, N, _, _, _).
activityDay(   A, D) :- activity(A, _, B, E, _), between(B, E, D), day(D).
activityVenue( A, V) :- activity(A, _, _, _, L), member(V, L), venue(V).
activityPerson(A, P) :- person(P, L), member(A, L).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% 1.- Declare SAT variables to be used

% "person P does activity A on day D"
satVariable( activityOnDayByPersonVar(A, D, P) ):- activityDay(A, D), activityPerson(A, P).

% "person P does activity A"
satVariable( activityByPersonVar(A, P) ):- activityPerson(A, P).

% "activity A is done at venue V"
satVariable( activityOnDayAtVenueVar(A, D, V) ):- activityDay(A, D), activityVenue(A, V).

% "activity A is done at venue V"
satVariable( activityAtVenueVar(A, V) ):- activityVenue(A, V).

% "activity A is done on day D"
satVariable( activityOnDayVar(A, D) ):- activityDay(A, D).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 2. Generate SAT clauses:

writeClauses :-
    eachActivityHasExactlyOneDay,
    eachActivityHasExactlyOneVenue,
    eachActivityHasEnoughPeople,
    eachPersonAtMostOneActivityAtATime,
    eachVenueAtMostOneActivityAtATime,
    definitionActivityOnDayByPerson,
    definitionActivityOnDayAtVenue,
    true,!.

eachActivityHasExactlyOneDay :-
    activity(A),
    findall(activityOnDayVar(A, D), activityDay(A, D), Lits),
    exactly(1, Lits),
    fail.
eachActivityHasExactlyOneDay.

eachActivityHasExactlyOneVenue :-
    activity(A),
    findall(activityAtVenueVar(A, V), activityVenue(A, V), Lits),
    exactly(1, Lits),
    fail.
eachActivityHasExactlyOneVenue.

eachActivityHasEnoughPeople :-
    activityNeeds(A, N),
    findall(activityByPersonVar(A, P), activityPerson(A, P), Lits),
    atLeast(N, Lits),
    fail.
eachActivityHasEnoughPeople.

eachPersonAtMostOneActivityAtATime :-
    person(P),
    day(D),
    findall(activityOnDayByPersonVar(A, D, P), (activityPerson(A, P), activityDay(A, D)), Lits),
    atMost(1, Lits), 
    fail.
eachPersonAtMostOneActivityAtATime.
    

eachVenueAtMostOneActivityAtATime:- 
    venue(V),
    day(D),
    findall(activityOnDayAtVenueVar(A, D, V), (activityVenue(A, V), activityDay(A, D)), Lits),
    atMost(1, Lits), 
    fail.
eachVenueAtMostOneActivityAtATime.
    

definitionActivityOnDayByPerson :- 
    activityPerson(A, P),
    activityDay(A, D),
    expressAnd(activityOnDayByPersonVar(A, D, P), [activityByPersonVar(A, P), activityOnDayVar(A, D)]),
    fail.
definitionActivityOnDayByPerson.

    

definitionActivityOnDayAtVenue:-
    activityDay(A, D),
    activityVenue(A, V), 
    expressAnd(activityOnDayAtVenueVar(A, D, V), [activityOnDayVar(A, D), activityAtVenueVar(A, V)]),
    fail.
definitionActivityOnDayAtVenue.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 3. This predicate displays a given solution M:

%% displaySol(M):- write(M), nl, nl, fail.
displaySol(M):- activity(A),
                member(activityAtVenueVar(A, V), M),
                member(activityOnDayVar(  A, D), M),
                findall(P, member(activityByPersonVar(A, P), M), L),
                write(activity(A)-day(D)-venue(V):people(L)), nl,
                fail.
displaySol(_):- nl, fail.
displaySol(M):- person(P),
                day(D),
                findall(A, member(activityOnDayByPersonVar(A, D, P), M), L),
                write(day(D)-person(P):activities(L)), nl,
                fail.
displaySol(_):- nl, fail.
displaySol(M):- venue(V),
                day(D),
                findall(A, member(activityOnDayAtVenueVar(A, D, V), M), L),
                write(day(D)-venue(V):activities(L)), nl,
                fail.
displaySol(_):- nl, !.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Everything below is given as a standard library, reusable for solving
%%    with SAT many different problems.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%% Cardinality constraints on arbitrary sets of literals Lits: ===========================

exactly(K,Lits) :- symbolicOutput(1), write( exactly(K,Lits) ), nl, !.
exactly(K,Lits) :- atLeast(K,Lits), atMost(K,Lits),!.

atMost(K,Lits) :- symbolicOutput(1), write( atMost(K,Lits) ), nl, !.
atMost(K,_)    :- K < 0, writeOneClause([]), !.
atMost(K,Lits) :-   % l1+...+ln <= k:  in all subsets of size k+1, at least one is false:
      negateAll(Lits,NLits),
      K1 is K+1,    subsetOfSize(K1,NLits,Clause), writeOneClause(Clause), fail.
atMost(_,_).

atLeast(K,Lits) :- symbolicOutput(1), write( atLeast(K,Lits) ), nl, !.
atLeast(K,Lits) :- length(Lits, Len), Len < K, writeOneClause([]), !.
atLeast(K,Lits) :-  % l1+...+ln >= k: in all subsets of size n-k+1, at least one is true:
      length(Lits,N),
      K1 is N-K+1,  subsetOfSize(K1, Lits,Clause), writeOneClause(Clause), fail.
atLeast(_,_).

negateAll([], []).
negateAll([Lit|Lits], [NLit|NLits]) :- negate(Lit,NLit), negateAll(Lits, NLits), !.

negate(-Var,  Var) :- !.
negate( Var, -Var) :- !.

subsetOfSize(0,_,[]) :- !.
subsetOfSize(N,[X|L],[X|S]) :- N1 is N-1, length(L,Leng), Leng>=N1, subsetOfSize(N1,L,S).
subsetOfSize(N,[_|L],   S ) :-            length(L,Leng), Leng>=N,  subsetOfSize( N,L,S).


%%%%%%% Express equivalence between a variable and a disjunction or conjunction of literals ===

% Express that Var is equivalent to the disjunction of Lits:
expressOr(Var, Lits) :- symbolicOutput(1), write( Var ), write(' <--> or('), write(Lits), write(')'), nl, !.
expressOr(Var, Lits) :- member(Lit,Lits), negate(Lit,NLit), writeOneClause([NLit,Var]), fail.
expressOr(Var, Lits) :- negate(Var,NVar), writeOneClause([NVar|Lits]),!.

%% expressOr(a,[x,y]) genera 3 clausulas (como en la Transformación de Tseitin):
%% a == x v y
%% x -> a       -x v a
%% y -> a       -y v a
%% a -> x v y   -a v x v y

% Express that Var is equivalent to the conjunction of Lits:
expressAnd(Var, Lits) :- symbolicOutput(1), write( Var ), write(' <--> and('), write(Lits), write(')'), nl, !.
expressAnd(Var, Lits) :- member(Lit,Lits), negate(Var,NVar), writeOneClause([NVar,Lit]), fail.
expressAnd(Var, Lits) :- findall(NLit, (member(Lit,Lits), negate(Lit,NLit)), NLits), writeOneClause([Var|NLits]), !.


%%%%%%% main: =================================================================================

main:-  current_prolog_flag(os_argv, Argv),
        nth0(1, Argv, InputFile),
        main(InputFile), !.
main:-  write('Usage: $ ./<executable> <example>          or ?- main(<example>).'), nl, halt.

main(InputFile):-
        symbolicOutput(1), !,
        consult(InputFile),
        writeClauses, halt.   % print the clauses in symbolic form and halt Prolog
main(InputFile):-
        consult(InputFile),
        initClauseGeneration,
        tell(clauses), writeClauses, told,          % generate the (numeric) SAT clauses and call the solver
        tell(header),  writeHeader,  told,
        numVars(N), numClauses(C),
        write('Generated '), write(C), write(' clauses over '), write(N), write(' variables. '),nl,
        shell('cat header clauses > infile.cnf',_),
        write('Calling solver....'), nl,
        shell('kissat -v infile.cnf > model', Result),  % if sat: Result=10; if unsat: Result=20.
        treatResult(Result),!.

treatResult(20) :- write('Unsatisfiable'), nl, halt.
treatResult(10) :- write('Solution found: '), nl, see(model), symbolicModel(M), seen, displaySol(M), nl,nl,halt.
treatResult( _) :- write('cnf input error. Wrote anything strange in your cnf?'), nl,nl, halt.


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
