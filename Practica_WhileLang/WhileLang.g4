grammar WhileLang;

program: statement+ EOF;

statement: varDecl          #DeclStmt
         | assignment       #AssignStmt
         | whileStatement   #WhileStmt
         | ifStatement      #IfStmt
         | breakStatement   #BreakStmt
         | continueStatement #ContinueStmt;

// Agregamos declaración de variables (Necesario para el Caso 1 y 4)
varDecl: type ID ASSIGN expr SEMI;

type: INT_TYPE | STRING_TYPE;

assignment: ID ASSIGN expr SEMI;

whileStatement: WHILE LPAREN expr RPAREN LBRACE statement* RBRACE;

ifStatement: IF LPAREN expr RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?;

breakStatement: BREAK SEMI;

continueStatement: CONTINUE SEMI;

// Expresiones con etiquetas para el Visitor
expr: LPAREN expr RPAREN           #ParensExpr
    | expr (MULT | DIV) expr       #MulDivExpr
    | expr (PLUS | MINUS) expr     #AddSubExpr
    | expr (GT | LT | EQ | NE) expr #CompareExpr
    | ID                           #IdExpr
    | NUMBER                       #IntExpr
    | STRING                       #StringExpr;

// --- LEXER ---

INT_TYPE: 'int';
STRING_TYPE: 'string';
WHILE: 'while';
IF: 'if';
ELSE: 'else';
BREAK: 'break';
CONTINUE: 'continue';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

GT: '>';
LT: '<';
EQ: '==';
NE: '!=';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
// Regla para reconocer texto entre comillas
STRING: '"' (~["\r\n])* '"'; 

WS: [ \t\r\n]+ -> skip;