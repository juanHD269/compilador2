from antlr4 import *
from instrctionLexer import instrctionLexer
from instrctionParser import instrctionParser

# Entradas de prueba
inputs = ["print x", "print 5"]

for input_text in inputs:
    print(f"\nProbando con: {input_text}")
    input_stream = InputStream(input_text)

    # Crear lexer
    lexer = instrctionLexer(input_stream)

    # Crear stream de tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("TOKENS:")

    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = None
            if hasattr(lexer, 'ID') and token.type == lexer.ID:
                token_name = 'ID'
            elif hasattr(lexer, 'NUM') and token.type == lexer.NUM:
                token_name = 'NUM'
            elif hasattr(lexer, 'WS') and token.type == lexer.WS:
                token_name = 'WS'
            elif token.type < len(lexer.literalNames) and lexer.literalNames[token.type] and lexer.literalNames[token.type] != "<INVALID>":
                token_name = lexer.literalNames[token.type]

            print(f"Texto: '{token.text}'  Tipo: {token_name}")

    # Crear parser
    parser = instrctionParser(token_stream)

    # Regla inicial
    tree = parser.stat()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))
