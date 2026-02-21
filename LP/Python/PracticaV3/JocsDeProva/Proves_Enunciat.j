1 2 3                               NB. Resultat esperat 1 2 3

1 1 1 + 1 2 3                       NB. Resultat esperat 2 3 4 

1 + 1 2 3                           NB. Resultat esperat 2 3 4 

1 1 + 1 2 3                         NB. Resultat esperat lenght error 0

5 + 2 * 3                           NB. Resultat esperat 11

5 * 2 + 3                           NB. Resultat esperat 25

(5 * 2) + 3                         NB. Resultat esperat 13 

_1 * 2 3                            NB. Resultat esperat _2 _3

5 - 2                               NB. Resultat esperat 3

2 * 3                               NB. Resultat esperat 6

6 % 2                               NB. Resultat esperat 3

2 | 7                               NB. Resultat esperat 1

2 ^ 3                               NB. Resultat esperat 8

] 1                                 NB. Resultat esperat 1

1 , 2 3                             NB. Resultat esperat 1 2 3 

# 1 2                               NB. Resultat esperat 2

1 0 1 0 # 1 2 3 4                   NB. Resultat esperat 1 3

0 2 { 2 3 4                         NB. Resultat esperat 2 4

i. 4                                NB. Resultat esperat 0 1 2 3 

+: 1 2 3                            NB. Resultat esperat 2 4 6 

+/ 1 2 3                            NB. Resultat esperat 6

7 | ~ 2                             NB. Resultat esperat 1

x =: 1 2 3                          
1 + x                               NB. Resultat esperat 2 3 4 

square =: *:
square 1 2 3 4                      NB. Resultat esperat 1 4 9 16

mod2 =: 2 | ]
mod2 i. 4                           NB. Resultat esperat 0 1 0 1

eq0 =: 0 = ]
parell =: eq0 @: mod2
parell i. 6                         NB. Resultat esperat 1 0 1 0 1 0

inc =: 1 + ]
test =: +/ @: inc @: i.
test 3                              NB. Resultat esperat 6

