grammar exprs;

root
    : expr
    ;
    
expr
    : <assoc=right> expr '^' expr
    | expr '/' expr
    | expr '*' expr 
    | expr '-' expr
    | expr '+' expr
    | INT
    ;

INT
    : [0-9]+
    ;

WS
    : [ \t\n\r]+ -> skip
    ;
