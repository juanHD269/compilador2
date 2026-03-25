grammar Expreva;

expr: term (PLUS term)* ;

term: ID | NUM ;

PLUS: '+' ;
ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;