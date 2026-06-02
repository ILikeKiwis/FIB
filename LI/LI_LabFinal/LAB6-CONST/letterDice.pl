:- use_module(library(clpfd)).

%% A (6-sided) "letter dice" has on each side a different letter.
%% Find four of them, with the 24 letters abcdefghijklmnoprstuvwxy such
%% that you can make all the following words: bake, onyx, echo, oval,
%% gird, smug, jump, torn, luck, viny, lush, wrap, fame.

% Some helpful predicates:

word( [b,a,k,e] ).
word( [o,n,y,x] ).
word( [e,c,h,o] ).
word( [o,v,a,l] ).
word( [g,i,r,d] ).
word( [s,m,u,g] ).
word( [j,u,m,p] ).
word( [t,o,r,n] ).
word( [l,u,c,k] ).
word( [v,i,n,y] ).
word( [l,u,s,h] ).
word( [w,r,a,p] ).
word( [f,a,m,e] ).

% num(?X, ?N)   "La lletra X és a la posició N de la llista"
num(X, N) :- nth1( N, [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,r,s,t,u,v,w,x,y], X ).
%                                        1                   2
%                      1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4

main :-
%1: Variables i dominis:
    length(Assign, 24),
    Assign ins 1..4,
%2: Constraints:
    global_cardinality(Assign, [1-6,2-6,3-6,4-6]),
        forall(word([A,B,C,D]),
                     ( num(A, NA), num(B, NB), num(C, NC), num(D, ND),
                         nth1(NA, Assign, DA),
                         nth1(NB, Assign, DB),
                         nth1(NC, Assign, DC),
                         nth1(ND, Assign, DD),
                         all_distinct([DA,DB,DC,DD]) )),
%3: Labeling:
    labeling([ffc], Assign),
    findall(N, nth1(N, Assign, 1), D1),
    findall(N, nth1(N, Assign, 2), D2),
    findall(N, nth1(N, Assign, 3), D3),
    findall(N, nth1(N, Assign, 4), D4),
%4: Escrivim el resultat:
    writeN(D1), nl,
    writeN(D2), nl,
    writeN(D3), nl,
    writeN(D4), nl, halt.
    
writeN(D) :- findall(X, (member(N,D),num(X,N)), L), write(L), nl, !.
