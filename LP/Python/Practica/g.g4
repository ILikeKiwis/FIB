grammar g;

program
    : statement* EOF
    ;

statement
    : assign NL*                            #AssignSt
    | expr NL*                              #ExprSt
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
    | ID                                    #Id
    ;

ID
  : [A-Za-z] [A-Za-z0-9_]* 
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
    | '<'
    | '>'
    | '>='
    | '<='
    | '='
    | '<>'
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
    : num+
    ;

num
    : neg? NUM
    ;
neg
    : '_'
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
