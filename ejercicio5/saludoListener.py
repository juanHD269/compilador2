# Generated from saludo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .saludoParser import saludoParser
else:
    from saludoParser import saludoParser

# This class defines a complete listener for a parse tree produced by saludoParser.
class saludoListener(ParseTreeListener):

    # Enter a parse tree produced by saludoParser#saludo.
    def enterSaludo(self, ctx:saludoParser.SaludoContext):
        pass

    # Exit a parse tree produced by saludoParser#saludo.
    def exitSaludo(self, ctx:saludoParser.SaludoContext):
        pass



del saludoParser