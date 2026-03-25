from antlr4 import *
from Expr2Lexer import Expr2Lexer
from Expr2Parser import Expr2Parser

# Entradas de prueba
inputs = ["3+4*5", "2*3+4"]

for input_text in inputs:
    print(f"\nProbando con: {input_text}")
    input_stream = InputStream(input_text)

    # Crear lexer
    lexer = Expr2Lexer(input_stream)

    # Crear stream de tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("TOKENS:")

    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = None
            if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] and lexer.symbolicNames[token.type] != "<INVALID>":
                token_name = lexer.symbolicNames[token.type]
            elif token.type < len(lexer.literalNames) and lexer.literalNames[token.type] and lexer.literalNames[token.type] != "<INVALID>":
                token_name = lexer.literalNames[token.type]
            elif hasattr(lexer, 'NUM') and token.type == lexer.NUM:
                token_name = 'NUM'

            print(f"Texto: {token.text}  Tipo: {token_name}")

    # Crear parser
    parser = Expr2Parser(token_stream)

    # Regla inicial
    tree = parser.expr()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))