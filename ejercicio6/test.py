from antlr4 import *
from Saludo2Lexer import Saludo2Lexer
from Saludo2Parser import Saludo2Parser

# Entradas de prueba
inputs = ["hola Juan", "buenosdias Pedro"]

for input_text in inputs:
    print(f"\nProbando con: {input_text}")
    input_stream = InputStream(input_text)

    # Crear lexer
    lexer = Saludo2Lexer(input_stream)

    # Crear stream de tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("TOKENS:")

    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = None
            if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type]:
                token_name = lexer.symbolicNames[token.type]
            if token_name is None and token.type < len(lexer.literalNames) and lexer.literalNames[token.type]:
                token_name = lexer.literalNames[token.type]

            print(f"Texto: {token.text}  Tipo: {token_name}")

    # Crear parser
    parser = Saludo2Parser(token_stream)

    # Regla inicial
    tree = parser.saludo()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))