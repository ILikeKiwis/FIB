grammar exprs;

root : expr
     ;

expr : expr '+' expr    #suma
     | NUM              #numero
     ;
    
NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;