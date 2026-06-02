%                      [m1, c1, m2, c2, boatSide]
main :- EstatInicial = [3, 3, 0, 0, left],    EstatFinal = [0, 0, 3, 3, right],
        between(0, 1000, CostMax),                  % Busquem solució de cost 0; si no, de 1, etc.
        cami(CostMax, EstatInicial, EstatFinal, [EstatInicial], Cami),
        reverse(Cami, Cami1), write(Cami1), write(' amb cost '), write(CostMax), nl, halt.

cami(0, E, E, C, C).                                % Cas base: quan l'estat actual és l'estat final.
cami(CostMax, EstatActual, EstatFinal, CamiFinsAra, CamiTotal) :-
        CostMax > 0, 
        unPas(CostPas, EstatActual, EstatSeguent),  % En B.1 i B.2, CostPas és 1.
        \+ member(EstatSeguent, CamiFinsAra),
        CostMax1 is CostMax-CostPas,
        cami(CostMax1, EstatSeguent, EstatFinal, [EstatSeguent|CamiFinsAra], CamiTotal).

unPas(1, [M1, C1, M2, C2, left], [M1S, C1S, M2S, C2S, right]) :-
        move(PM, PC),
        PM =< M1,
        PC =< C1,
        M1S is M1-PM, C1S is C1-PC,
        M2S is M2+PM, C2S is C2+PC,
        estatValid([M1S, C1S, M2S, C2S]).

unPas(1, [M1, C1, M2, C2, right], [M1S, C1S, M2S, C2S, left]) :-
        move(PM, PC),
        PM =< M2,
        PC =< C2,
        M1S is M1+PM, C1S is C1+PC,
        M2S is M2-PM, C2S is C2-PC,
        estatValid([M1S, C1S, M2S, C2S]).

move(2,0).
move(0,2).
move(1,1).
move(1,0).
move(0,1).

estatValid([M1, C1, M2, C2]) :-
        entre0i3(M1), entre0i3(C1), entre0i3(M2), entre0i3(C2),
        M1 + M2 =:= 3,
        C1 + C2 =:= 3,
        segur(M1, C1),
        segur(M2, C2).

segur(0, _).
segur(M, C) :- M >= C.

entre0i3(X) :- between(0, 3, X).

