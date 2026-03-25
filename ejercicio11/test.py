from antlr4 import *
from Expr1Lexer import Expr1Lexer
from Expr1Parser import Expr1Parser

# Entradas de prueba
inputs = ["1+2+3", "5+6+7+8"]

for input_text in inputs:
    print(f"\nProbando con: {input_text}")
    input_stream = InputStream(input_text)

    # Crear lexer
    lexer = Expr1Lexer(input_stream)

    # Crear stream de tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("TOKENS:")

    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = None
            # Prefer named token types (symbolicNames) over literal strings
            if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] and lexer.symbolicNames[token.type] != "<INVALID>":
                token_name = lexer.symbolicNames[token.type]
            elif token.type < len(lexer.literalNames) and lexer.literalNames[token.type] and lexer.literalNames[token.type] != "<INVALID>":
                token_name = lexer.literalNames[token.type]
            elif hasattr(lexer, 'NUM') and token.type == lexer.NUM:
                token_name = 'NUM'

            print(f"Texto: {token.text}  Tipo: {token_name} (type={token.type})")

    # Crear parser
    parser = Expr1Parser(token_stream)

    # Regla inicial
    tree = parser.expr()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))