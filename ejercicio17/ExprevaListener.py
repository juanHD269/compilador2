# Generated from Expreva.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprevaParser import ExprevaParser
else:
    from ExprevaParser import ExprevaParser

# This class defines a complete listener for a parse tree produced by ExprevaParser.
class ExprevaListener(ParseTreeListener):

    # Enter a parse tree produced by ExprevaParser#expr.
    def enterExpr(self, ctx:ExprevaParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprevaParser#expr.
    def exitExpr(self, ctx:ExprevaParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprevaParser#term.
    def enterTerm(self, ctx:ExprevaParser.TermContext):
        pass

    # Exit a parse tree produced by ExprevaParser#term.
    def exitTerm(self, ctx:ExprevaParser.TermContext):
        pass



del ExprevaParser