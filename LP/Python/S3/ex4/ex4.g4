grammar ex4;



program 
    : statement* EOF
    ;

statement
    : assign NL
    | write NL
    | cond 
    | while 
    ;

assign 
    : ID ':=' expr
    ;

write
    : 'write' expr
    ;

cond
    : 'if' boolexpr 'then' NL statement* 'end' 
    ;

while
    : 'while' boolexpr 'do' NL statement* 'end' 
    ;

boolexpr
    : expr '=' expr                 
    | expr '<>' expr                
    | expr '<=' expr                
    | expr '>=' expr                
    | expr '<' expr                 
    | expr '>' expr                 
    ;

expr 
    : <assoc=right> expr '^' expr   #Pot
    | expr ('*' | '/') expr         #MultDiv
    | expr ('+' | '-') expr         #SumSub
    | NUM                           #Num
    | ID                            #Id
    ;

NUM
    : [0-9]+
    ;

ID
    : [a-zA-Z]+
    ;

NL 
    : [\r\n]+ 
    ;

WS 
    : [ \t]+ -> skip
    ;
