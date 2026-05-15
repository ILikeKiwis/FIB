
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
    ...


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
    ...
