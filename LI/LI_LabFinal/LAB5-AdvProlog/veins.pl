solucio(L):-
    L = [ [1,_,_,_,_,_], [2,_,_,_,_,_], [3,_,_,_,_,_], [4,_,_,_,_,_], [5,_,_,_,_,_] ],
    % [numcasa,color,profesió,animal,beguda,pais]
    % 1 - El que viu a la casa vermella és del Perú
    member([_, red, _, _, _, peru], L),
    % 2 - Al francès li agrada el gos
    member([_, _, _, dog, _, france], L),
    % 3 - El pintor és japonès
    member([_, _, pintor, _, _, japan], L),
    % 4 - Al xinès li agrada el rom
    member([_, _, _, _, rum, china], L),
    % 5 - L'hongarès viu en la primera casa
    member([1, _, _, _, _, hungary], L),
    % 6 - Al de la casa verda li agrada el conyac
    member([_, green, _, _, conyac, _], L),
    % 7 - La casa verda està just a l'esquerra de la blanca
    member([G_House, green, _, _, _, _], L),
    member([W_House, white, _, _, _, _], L),
    G_House is W_House-1,
    % 8 - L'escultor cria caragols
    member([_, _, sculptor, snail, _, _], L),
    % 9 - El de la casa groga és actor
    member([_, yellow, actor, _, _, _], L),
    % 10 - El de la tercera casa beu cava
    member([3, _, _, _, cava, _], L),
    % 11 - El que viu al costat de l'actor té un cavall
    member([Actor_House, _, actor, _, _, _], L),
    member([Horse_House, _, _, horse, _, _], L),
    %A1 is A+1,
    %A2 is A-1,
    %member(N, [Actor_House+1, Actor_House-1]),
    %Horse_House is N,
    (Horse_House is Actor_House+1 ; Horse_House is Actor_House-1),
    % 12 - L'hongarès viu al costat de la casa blava
    member([B_House, blue, _, _, _, _], L),
    member([Hungary_House, _, _, _, _, hungary], L),
    (Hungary_House is B_House+1 ; Hungary_House is B_House-1),
    % 13 - Al notari l'agrada el whisky
    member([_, _, notary, _, whisky, _], L),
    % 14 - El que viu al costat del metge té un esquirol
    member([Doc_House, _, doc, _, _, _], L),
    member([Sq_House, _, _, sq, _, _], L),
    (Sq_House is Doc_House+1 ; Sq_House is Doc_House-1),
    % 15 - El que té un gat no és a qui agrada la cervesa
    member([Cat_House, _, _, cat, _, _], L),
    member([Beer_House, _, _, _, beer, _], L),
    not(Cat_House is Beer_House),
    %Cat_House \= Beer_House,
    displaySol(L), halt.

displaySol(L):- member(P,L), write(P), nl, fail.
displaySol(_).

	    
