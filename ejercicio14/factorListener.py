# Generated from factor.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .factorParser import factorParser
else:
    from factorParser import factorParser

# This class defines a complete listener for a parse tree produced by factorParser.
class factorListener(ParseTreeListener):

    # Enter a parse tree produced by factorParser#expr.
    def enterExpr(self, ctx:factorParser.ExprContext):
        pass

    # Exit a parse tree produced by factorParser#expr.
    def exitExpr(self, ctx:factorParser.ExprContext):
        pass


    # Enter a parse tree produced by factorParser#term.
    def enterTerm(self, ctx:factorParser.TermContext):
        pass

    # Exit a parse tree produced by factorParser#term.
    def exitTerm(self, ctx:factorParser.TermContext):
        pass


    # Enter a parse tree produced by factorParser#factor.
    def enterFactor(self, ctx:factorParser.FactorContext):
        pass

    # Exit a parse tree produced by factorParser#factor.
    def exitFactor(self, ctx:factorParser.FactorContext):
        pass



del factorParser