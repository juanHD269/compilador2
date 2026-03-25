from antlr4 import *
from saludoLexer import saludoLexer
from saludoParser import saludoParser

# Entradas de prueba
inputs = ["hola Juan", "hola Maria"]

for input_text in inputs:
    print(f"\nProbando con: {input_text}")
    input_stream = InputStream(input_text)

    # Crear lexer
    lexer = saludoLexer(input_stream)

    # Crear stream de tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("TOKENS:")

    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type]

            if token_name is None:
                token_name = lexer.literalNames[token.type]

            print(f"Texto: {token.text}  Tipo: {token_name}")

    # Crear parser
    parser = saludoParser(token_stream)

    # Regla inicial
    tree = parser.saludo()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))