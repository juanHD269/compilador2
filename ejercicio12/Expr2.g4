grammar Expr2;

expr: term (PLUS term)* ;

term: factor (MUL factor)* ;

factor: NUM ;

PLUS: '+' ;
MUL: '*' ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;