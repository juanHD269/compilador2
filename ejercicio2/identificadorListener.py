# Generated from identificador.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .identificadorParser import identificadorParser
else:
    from identificadorParser import identificadorParser

# This class defines a complete listener for a parse tree produced by identificadorParser.
class identificadorListener(ParseTreeListener):

    # Enter a parse tree produced by identificadorParser#id.
    def enterId(self, ctx:identificadorParser.IdContext):
        pass

    # Exit a parse tree produced by identificadorParser#id.
    def exitId(self, ctx:identificadorParser.IdContext):
        pass



del identificadorParser