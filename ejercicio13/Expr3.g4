grammar Expr3;

expr: term ((PLUS | MINUS) term)* ;

term: factor ((MUL | DIV) factor)* ;

factor: NUM ;

PLUS: '+' ;
MINUS: '-' ;
MUL: '*' ;
DIV: '/' ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;