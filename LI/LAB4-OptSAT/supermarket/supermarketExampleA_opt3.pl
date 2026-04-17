% example: 4 employees are needed at the checkout on hour 1, one employee on hour 2, two employees on hour 3, etc.
employeesNeeded( checkout,   [4,1,2,4,2,1,1,4,1,1,3,2,4,2,1,2,1,3,2,3,4,1,3,1,2,3,1,3,4,3,2,3,4,2,3,1,4,4,1,4,2,2,1,4,3,3,3,2,2,3,4,4,1,3,3,3,4,4,1,1,2,3,3,3,3,2,1,3,1,1,3,2] ).
employeesNeeded( restocking, [1,2,1,3,1,4,3,1,3,1,4,3,2,2,1,2,1,2,1,1,2,1,2,1,1,3,1,2,2,4,3,2,4,4,4,1,2,4,4,2,4,4,4,3,2,2,1,3,2,1,3,3,2,3,3,3,1,4,1,1,3,1,2,3,3,1,4,4,3,3,2,1] ).
employeesNeeded( orders,     [2,4,2,1,1,1,4,1,1,4,1,3,2,4,1,1,4,1,4,3,1,3,2,4,4,2,4,2,1,1,4,3,1,2,2,2,1,1,3,1,1,1,2,2,4,1,1,3,4,4,2,3,2,4,3,1,1,1,3,4,2,2,4,4,3,1,1,2,1,4,3,2] ).

employees([e01,e02,e03,e04,e05,e06,e07,e08,e09,e10,e11,e12]).

notAvailable(e01,[6,13,14,16,21,35,37,41,59]).
notAvailable(e02,[14,34,40,45,48,52,58,65,70,72]).
notAvailable(e03,[8,11,13,27,30,38,50,51,70]).
notAvailable(e04,[4,12,16,17,26,30,42,45,48,55,71]).


%% EXAMPLE OUTPUT with cost 18:
%% 
%%                       10        20        30        40        50        60        70  
%%               123456789012345678901234567890123456789012345678901234567890123456789012
%% 
%% employee e01: ------------------------------o-------o-----o----o----o--------------o--
%% employee e02: ------o--o-o--------------o--ooo-----oo---oo-----o----o---o----o--------
%% employee e03: -o----o--o-o-o--o-------o-----oo-oo-o-oo-oooo--oo--o-oo-oooo--o-------o-
%% employee e04: -oo---o--o--oo----oo-o-oo-o-o-oooooo-rr-o--r----oooooo-o-r-o--ooo--o-o--
%% employee e05: oooooooooooooo--o-oo-o-ooooo-r--rr-o-rr-r-r-o--ooooooo-r-r-oooooooooooo-
%% employee e06: oo-r--r-r-rr-oo-o-oooooooooo-r--rrr-rrr-r-r-ooooo-rr-o-r-r-oooooo-rr-ooo
%% employee e07: -r-r-rr-r-rrrr--ooo-r-oo-r-rrrrrrrr-rrrrrrrrr--r--rrrrrrrrr-r--rr-rrrr-o
%% employee e08: rrrrrrrrr-rrrr-o-r-rrrr--r-rrrrrrrrr-c-rrrrrrr-rrrrrrrr-c-o-r-rrr-rrrrr-
%% employee e09: c--c-r-c-rr-c--rrrr-c-rrrrr-c-r-c-r-cc-c-r-c-rrrr-cc-rr-cc--rrrrrrrrrrrr
%% employee e10: c--c-r-c--c-c-rr-cccc-c--c-ccc-cc-c-cc-c-r-cccc--ccc-ccccc-r-cccc--c--c-
%% employee e11: c-ccc--c--cccc-c-cccc-c-cc-cccccccc-cc-ccc-ccccccccc-ccccc--cccccc-c--cc
%% employee e12: cccccccccccccccccc-cccccccccccccccccc-cccccccccccccc-ccccccccccccccccccc
