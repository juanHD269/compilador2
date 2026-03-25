from antlr4 import *
from SumaRestaLexer import SumaRestaLexer
from SumaRestaParser import SumaRestaParser

# Entradas de prueba
inputs = ["5+3", "8-2"]

for input_text in inputs:
    print(f"\nProbando con: {input_text}")
    input_stream = InputStream(input_text)

    # Crear lexer
    lexer = SumaRestaLexer(input_stream)

    # Crear stream de tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("TOKENS:")

    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = None
            if token.type < len(lexer.literalNames) and lexer.literalNames[token.type] and lexer.literalNames[token.type] != "<INVALID>":
                token_name = lexer.literalNames[token.type]
            elif token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] and lexer.symbolicNames[token.type] != "<INVALID>":
                token_name = lexer.symbolicNames[token.type]

            # Cubrir casos donde ANTLR genera T__n para literales y el arreglo symbolicNames no contiene el token
            if token_name is None:
                if hasattr(lexer, 'NUM') and token.type == lexer.NUM:
                    token_name = 'NUM'
                elif hasattr(lexer, 'WS') and token.type == lexer.WS:
                    token_name = 'WS'

            print(f"Texto: {token.text}  Tipo: {token_name} (type={token.type})")

    # Crear parser
    parser = SumaRestaParser(token_stream)

    # Regla inicial
    tree = parser.expr()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))