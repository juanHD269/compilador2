import sys
from antlr4 import *
from antlr_generated.WhileLangLexer import WhileLangLexer
from antlr_generated.WhileLangParser import WhileLangParser
from semantic_visitor import SemanticVisitor

def main(argv):
    if len(argv) < 2:
        print("Uso: python3 main.py <archivo_de_prueba>")
        return

    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = WhileLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = WhileLangParser(stream)
    
    # Generar el árbol desde la regla inicial (ej. program)
    tree = parser.program()

    # Ejecutar el Visitor
    print(f"--- Analizando: {argv[1]} ---")
    visitor = SemanticVisitor()
    visitor.visit(tree)
    print("--- Análisis finalizado ---")

if __name__ == '__main__':
    main(sys.argv)