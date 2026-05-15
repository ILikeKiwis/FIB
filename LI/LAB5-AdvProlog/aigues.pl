main :- EstatInicial = [0, 0],    EstatFinal = [0, 4],
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

% Rellenar
unPas(1, [X, _], [X, 8]).
unPas(1, [_, Y], [5, Y]).

% Vaciar
unPas(1, [X, _], [X, 0]).
unPas(1, [_, Y], [0, Y]).

% Pasar
% X -> Y
unPas(1, [X, Y], [XS, YS]) :- 
        X \= 0, 
        YS is min(X + Y, 8),
        XS is X - (YS - Y).
        
unPas(1, [X, Y], [XS, YS]) :- 
        Y \= 0, 
        XS is min(X + Y, 5),
        YS is Y - (XS - X).
 
 
