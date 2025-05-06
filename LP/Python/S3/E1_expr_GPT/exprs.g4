
grammar exprs;

expr    :   addExpr;

addExpr
        : addExpr '+' mulExpr   #suma
        | addExpr '+' mulExpr   #resta 
        | mulExpr               #toMul
        ;

mulExpr
        : mulExpr '*' powExpr   #mult
        | mulExpr '/' powExpr   #div
        | powExpr               #toPow
        ;

powExpr
        : NUM '^' powExpr      #pow
        | NUM                  #toNUM
        ;

NUM     : [0-9]+ ;
WS      : [ \t\n\r]+ -> skip ;