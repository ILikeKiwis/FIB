grammar g;

program
    : statement* EOF
    ;

statement
    : expr NL*                              #ExprSt
    | assign NL*                            #AssignSt
    ;

assign
    : ID '=:' expr
    ;

expr
    : <assoc=right> expr '#' flip* expr     #FilterOp
    | <assoc=right> expr BOP flip* expr     #BinaryOp
    | uop expr                              #UnitaryOp
    | numList                               #List
    | '(' expr ')'                          #Prio
    ;


BOP 
    : '+'
    | '-'
    | '*'
    | '%'
    | '^'
    | '|'  
    | ','
    | '{' 
    ;

flip 
    : '~'
    ;

uop
    : ']'
    | 'i.'
    | BOP ':'
    | BOP '/'
    | '#'
    ;

numList
    : NUM+  
    ;

COMMENT
    : 'NB.' ~[\r\n]* -> skip
    ;

NUM 
    : [0-9]+ 
    ;

NL  
    : [\r\n]+ 
    ;

WS  
    : 
    [ \t]+ -> skip
    ;
