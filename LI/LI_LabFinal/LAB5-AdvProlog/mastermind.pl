
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Mastermind és un joc on un jugador (defensor) s'inventa un codi
%% secret i l'altre jugador (atacant) ha d'esbrinar-ho. El codi és
%% una seqüència de 4 colors a triar entre vermell (v), blau (b),
%% groc (g), lila (l), taronja (t) i marró (m). L'atacant té un
%% nombre finit d'intents per a trencar el codi. En cada intent,
%% l'atacant preguntarà per una seqüència de 4 colors i el defensor
%% respondrà amb dos números (E,D), sent E el nombre de colors que
%% l'atacant ha encertat en la posició Exacta, i D el nombre de
%% colors que ha encertat però en una posició Diferent.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%% C1. Construeix un predicat resposta(Codi, Intent, E, D) que, donat
%% un Codi i un Intent calculi els números E, D de la resposta.

resposta(C,A,E,D) :-
    exactes(C, A, E),
    encertsTotals(C, A, T),
    D is T-E.

color(v).
color(b).
color(g).
color(l).
color(t).
color(m).

codi([C1,C2,C3,C4]) :-
    color(C1), color(C2), color(C3), color(C4).

exactes([], [], 0).
exactes([X|C], [Y|A], E) :-
    exactes(C, A, E1),
    (X == Y -> E is E1+1 ; E = E1).

encertsTotals(C, A, T) :-
    findall(Min, (color(Col), compta(Col, C, NC), compta(Col, A, NA), Min is min(NC, NA)), Ms),
    sum_list(Ms, T).

compta(_, [], 0).
compta(X, [Y|L], N) :-
    compta(X, L, N1),
    (X == Y -> N is N1+1 ; N = N1).


%% C2. Volem ara ajudar l'atacant a guanyar el joc, suggerint-li
%% intents. Assumeix que ens donen una clàusula de la forma:

intents([ [ [v,b,g,l], [1,1] ], [ [m,t,g,l], [1,0] ], [ [g,l,g,l], [0,0] ], [ [v,b,m,m], [1,1] ], [ [v,t,b,t], [2,2] ]]).

%% que representa l'històric dels intents fets fins ara per
%% l'atacant. Construeix un nou predicat nouIntent(A) que genera un
%% nou intent A tal que, si A fora el codi a descobrir, llavors tots
%% els intents en l'històric tindrien com a resposta la que justament
%% vam obtenir. O, dit d'un altra manera, el nou intent A només podrà
%% ser el codi secret si és consistent amb el que trobem a l'històric.

nouIntent(A) :-
    codi(A),
    intents(H),
    consistentAmbHistoric(A, H).

consistentAmbHistoric(_, []).
consistentAmbHistoric(Codi, [[Intent,[E,D]]|Resta]) :-
    resposta(Codi, Intent, E, D),
    consistentAmbHistoric(Codi, Resta).
