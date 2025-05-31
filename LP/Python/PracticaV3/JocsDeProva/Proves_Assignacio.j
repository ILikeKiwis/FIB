x =: 1 2 3              

x               NB. Resultat esperat 1 2 3 

y =: x + x      NB. Podem assignar variables amb expresions 

y               NB. Resultat esperat 2 4 6 

inc =: 1 + ]    NB. Definim una funció bàsica 

z =: inc y      NB. Assignem a una variable el resultat d'aplicar la funció a una variable.

z               NB. Resultat esperat 3 5 7 

+/ z            NB. Fem un fold de z. Resultat esperat 3 + 5 + 7 = 15

fact =: */ @: inc @: i.     NB. Funció simple per calcular el factorial d'un número.
fact 5          NB. Resultat esperat 120.

