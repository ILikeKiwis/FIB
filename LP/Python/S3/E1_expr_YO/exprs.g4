grammar exprs;

root
    : expr
    ;
    
expr
    : <assoc=right> expr '^' expr   #pot
    | expr '/' expr                 #div
    | expr '*' expr                 #mul
    | expr '-' expr                 #resta
    | expr '+' expr                 #suma
    | INT                           #numero
    ;

INT
    : [0-9]+
    ;

WS
    : [ \t\n\r]+ -> skip
    ;
