:- use_module(library(clpfd)).

example( 0,  26, [1,2,5,10]           ).  % Solució: [1,0,1,2]
example( 1, 361, [1,2,5,13,17,35,157] ).

main :- 
    example(0, Amount, Coins),
    nl, write('Paying amount '), write(Amount), write(' using the minimal number of coins of values '), write(Coins), nl, nl,

%1: Variables i dominis:
    length(Coins, N), 
    length(Vars,  N),           % obté una llista de N variables prolog
    Vars ins 0..Amount,

%2: Constraints:
    scalar_product(Coins, Vars, #=, Amount),
    sum(Vars, #=, ExprSum),

%3: Labeling:
    labeling([min(ExprSum)], Vars),

%4: Escrivim el resultat:
    NumCoins is ExprSum,
    write('We need '), write(NumCoins), write(' coins.'),
    nl, write(Vars), nl, nl, halt.
