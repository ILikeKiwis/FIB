grammar g;

// Programa 
program 
    :   statement* EOF
    ;

// Las sentencias
statement
    :   assign comment? NL*                         #AssignSt
    |   expr comment? NL*                           #ExprSt
    |   comment NL*                                 #Com
    ;
// Assignacion 
assign 
    :   ID '=:' assign_expr
    ;

assign_expr
    :   <assoc=right> assign_expr '@:' assign_expr  #AsExpr
    |   expr                                        #NormalExpr
    |   uop                                         #OnlyUnitary
    ;
  

expr
    :   <assoc=right> expr BOP flip* expr           #BinaryOP
    |   <assoc=right> uop expr                      #UnitaryOP
    |   <assoc=right> ID expr                       #IdValue  
    |   '('expr')'                                  #Prio
    |   numList                                     #List  
    |   <assoc=right> expr '#' flip* expr           #FilterOP
    |   ']'                                         #Identity
    |   ID                                          #Id
    ;   


ID
    :   [A-Za-z] [A-Za-z0-9_]*
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
    | '@:'
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
    : NEG? NUM
    ;
NEG
    : '_'
    ;

comment
    :   COMMENT
    ;

COMMENT
    : 'NB.' ~[\r\n]*
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
