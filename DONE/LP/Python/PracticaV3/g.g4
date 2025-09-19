grammar g;

// Programa 
program 
    :   statement* EOF
    ;

// Sentències
statement
    :   assign comment? NL*                         #AssignSt
    |   expr comment? NL*                           #ExprSt
    |   comment NL*                                 #Com
    ;
// Assignació 
assign 
    :   ID '=:' assign_expr
    ;

// Expressions possibles dins de l'assignació tant de variables, com de funcions 
assign_expr
    :   <assoc=right> assign_expr '@:' assign_expr  #AsExpr
    |   expr                                        #NormalExpr
    |   uop                                         #OnlyUnitary
    ;
  
// Expressions vàlides com a operacions dins del programa. 
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

// Expressio regular per els IDs
ID
    :   [A-Za-z] [A-Za-z0-9_]*
    ;

// Tots els operadors binaris que es demanen.
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

// Operador flip
flip 
    : '~'
    ;

// Operadors unaris.
uop
    : ']'
    | 'i.'
    | BOP ':'
    | BOP '/'
    | '#'
    ;

// Tipus base de G
numList
    : num+
    ;
// Cada element de numList
num
    : NEG? NUM
    ;
// Símbol que representa la negació 
NEG
    : '_'
    ;

//Comentaris 
comment
    :   COMMENT
    ;

COMMENT
    : 'NB.' ~[\r\n]*
    ;

// Expressió regular que captura els enters
NUM 
    : [0-9]+ 
    ;

// Salts de linia
NL  
    : [\r\n]+ 
    ;

// Espais en blanc 
WS  
    : 
    [ \t]+ -> skip
    ;
