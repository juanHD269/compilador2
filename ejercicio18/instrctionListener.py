# Generated from instrction.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .instrctionParser import instrctionParser
else:
    from instrctionParser import instrctionParser

# This class defines a complete listener for a parse tree produced by instrctionParser.
class instrctionListener(ParseTreeListener):

    # Enter a parse tree produced by instrctionParser#stat.
    def enterStat(self, ctx:instrctionParser.StatContext):
        pass

    # Exit a parse tree produced by instrctionParser#stat.
    def exitStat(self, ctx:instrctionParser.StatContext):
        pass


    # Enter a parse tree produced by instrctionParser#expr.
    def enterExpr(self, ctx:instrctionParser.ExprContext):
        pass

    # Exit a parse tree produced by instrctionParser#expr.
    def exitExpr(self, ctx:instrctionParser.ExprContext):
        pass



del instrctionParser