from antlr4 import *
from ListaComasLexer import ListaComasLexer
from ListaComasParser import ListaComasParser

# Entradas de prueba
inputs = ["1,2,3", "5,10,15"]

for input_text in inputs:
    print(f"\nProbando con: {input_text}")
    input_stream = InputStream(input_text)

    # Crear lexer
    lexer = ListaComasLexer(input_stream)

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
    parser = ListaComasParser(token_stream)

    # Regla inicial
    tree = parser.lista()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))