from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser

# Entrada de prueba
input_text = """x = 5
y = 10
print x + y
print (x + y) * 2"""
print(f"Probando con:\n{input_text}")
input_stream = InputStream(input_text)

# Crear lexer
lexer = CalcLexer(input_stream)

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
parser = CalcParser(token_stream)

# Regla inicial
tree = parser.prog()

print("ÁRBOL SINTÁCTICO:")
print(tree.toStringTree(recog=parser))
