grammar g;

// Programa 
program 
    :   statement* EOF
    ;

// Las sentencias
statement
    :   assign NL*                              #AssignSt
    |   expr NL*                                #ExprSt
    ;
// Assignacion 
assign 
    :   ID '=:' expr
    ;

expr
    :   <assoc=right> major BOP flip* expr      #BinaryOP
    |   major                                   #MajorOrMinor
    ;   

major
    :   ID major                                #IdValue  
    |   minor                                   #ToMinor
    ;

minor 
    :   numList                                 #List  
    |   minor '#' flip* minor                   #FilterOP
    |   uop minor                               #UnitaryOP
    |   ']'                                     #Identity
    |   uop                                     #OnlyUnitary
    |   '('expr')'                              #Prio
    |   ID                                      #Id
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
