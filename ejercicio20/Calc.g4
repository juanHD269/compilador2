grammar Calc;

prog: stat+ ;

stat
    : ID ASSIGN expr
    | PRINT expr
    ;

expr: term ((PLUS | MINUS) term)* ;

term: factor ((MUL | DIV) factor)* ;

factor
    : NUM
    | ID
    | LPAREN expr RPAREN
    ;

ASSIGN: '=' ;
PRINT: 'print' ;
PLUS: '+' ;
MINUS: '-' ;
MUL: '*' ;
DIV: '/' ;
LPAREN: '(' ;
RPAREN: ')' ;
ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;