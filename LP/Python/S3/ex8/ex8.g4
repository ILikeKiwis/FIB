grammar ex8;

program
    : (func)* main EOF
    ;

func 
    : 'function' ID '(' paramList? ')' NL (statement)* 'end' NL
    ;

paramList
    : ID (',' ID)*
    ;

main
    : 'main' NL (statement)* 'end' NL*
    ;

statement 
    : assign NL
    | write NL
    | cond NL*
    | while NL*
    | funcCall NL
    | retSt NL
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

funcCall
    : ID '(' arglist? ')'
    ;

arglist
    : expr (',' expr)*
    ; 

retSt
    : 'return' expr
    ;

expr 
    : <assoc=right> expr '^' expr   #Pot
    | expr ('*' | '/') expr         #MultDiv
    | expr ('+' | '-') expr         #SumSub
    | NUM                           #Num
    | funcCall                      #fExpr
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
