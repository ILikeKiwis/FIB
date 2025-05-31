NB. Comencem amb els operadors aritmètics requerits, +, -, *, %, |, ^

1 2 3 + 1 2 3 + 1 2 3           NB. Resultat esperat 3 6 9

2 * 2 - 1                       NB. Resultat esperat 2

NB. Ús de parèntesis
(2 * 2) - 1                     NB. Resultat esperat 3

2 4 6 * 2 4 6 - 1               NB. Resultat esperat 2 12 30

(2 4 6 * 2 4 6 ) - 1            NB. Resultat esperat 3 15 35

2 - 3                           NB. Resultat esperat _1

4 5 6 - 5                       NB. Resultat esperat _1 0 1

36 30 24 % 6                    NB. Resultat esperat 6 5 4 

35 29 23 % 6                    NB. Resultat esperat 5 4 3 

2 | 7 6 5                       NB. Resultat esperat 1 0 1 

2 3 4 5 | 12                    NB. Resultat esperat 0 0 0 2

1 2 3 ^ 2                       NB. Resultat esperat 1 4 9

2 ^ 1 2 3                       NB. Resultat esperat 2 4 8 

1 2 3 ^ 1 2 3                   NB. Resultat esperat 1 4 27

NB. Operadors relacionals, 1 és true 0 és false.

1 2 3 < 1                       NB. Resultat esperat 0 0 0 

1 2 3 <= 1                      NB. Resultat esperat 1 0 0 

1 2 3 > 1                       NB. Resultat esperat 0 1 1 

1 2 3 >= 1                      NB. Resultat esperat 1 1 1 

1 2 3 = 1                       NB. Resultat esperat 1 0 0 

1 2 3 <> 1                      NB. Resultat esperat 0 1 1 

1 2 3 < 4 5 6                   NB. Resultat esperat 1 1 1 

1 2 7 <= 4 5 6                  NB. Resultat esperat 1 1 0      

1 2 3 > 4 5 6                   NB. Resultat esperat 0 0 0

1 2 3 >= 4 5 6                  NB. Resultat esperat 0 0 0 

1 2 3 = 4 5 6                   NB. Resultat esperat 0 0 0 

1 2 3 <> 4 5 6                  NB. Resultat esperat 1 1 1 

NB. , fa la contatenació i flip cambia l'ordre dels operands 

1 2 ,~ 3 4                      NB. Resultat esperat 3 4 1 2 

NB. La operació filtre amb una màscara.

1 2 3 4 # 1 2 3 4               NB. Resultat esperat 1 2 2 3 3 3 4 4 4 4 

