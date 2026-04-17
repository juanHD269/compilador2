# Generated from WhileLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .WhileLangParser import WhileLangParser
else:
    from WhileLangParser import WhileLangParser

# This class defines a complete listener for a parse tree produced by WhileLangParser.
class WhileLangListener(ParseTreeListener):

    # Enter a parse tree produced by WhileLangParser#program.
    def enterProgram(self, ctx:WhileLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by WhileLangParser#program.
    def exitProgram(self, ctx:WhileLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by WhileLangParser#DeclStmt.
    def enterDeclStmt(self, ctx:WhileLangParser.DeclStmtContext):
        pass

    # Exit a parse tree produced by WhileLangParser#DeclStmt.
    def exitDeclStmt(self, ctx:WhileLangParser.DeclStmtContext):
        pass


    # Enter a parse tree produced by WhileLangParser#AssignStmt.
    def enterAssignStmt(self, ctx:WhileLangParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by WhileLangParser#AssignStmt.
    def exitAssignStmt(self, ctx:WhileLangParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by WhileLangParser#WhileStmt.
    def enterWhileStmt(self, ctx:WhileLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by WhileLangParser#WhileStmt.
    def exitWhileStmt(self, ctx:WhileLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by WhileLangParser#IfStmt.
    def enterIfStmt(self, ctx:WhileLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by WhileLangParser#IfStmt.
    def exitIfStmt(self, ctx:WhileLangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by WhileLangParser#BreakStmt.
    def enterBreakStmt(self, ctx:WhileLangParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by WhileLangParser#BreakStmt.
    def exitBreakStmt(self, ctx:WhileLangParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by WhileLangParser#ContinueStmt.
    def enterContinueStmt(self, ctx:WhileLangParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by WhileLangParser#ContinueStmt.
    def exitContinueStmt(self, ctx:WhileLangParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by WhileLangParser#varDecl.
    def enterVarDecl(self, ctx:WhileLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by WhileLangParser#varDecl.
    def exitVarDecl(self, ctx:WhileLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by WhileLangParser#type.
    def enterType(self, ctx:WhileLangParser.TypeContext):
        pass

    # Exit a parse tree produced by WhileLangParser#type.
    def exitType(self, ctx:WhileLangParser.TypeContext):
        pass


    # Enter a parse tree produced by WhileLangParser#assignment.
    def enterAssignment(self, ctx:WhileLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by WhileLangParser#assignment.
    def exitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by WhileLangParser#whileStatement.
    def enterWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#whileStatement.
    def exitWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#ifStatement.
    def enterIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#ifStatement.
    def exitIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#breakStatement.
    def enterBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#breakStatement.
    def exitBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#continueStatement.
    def enterContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#continueStatement.
    def exitContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#StringExpr.
    def enterStringExpr(self, ctx:WhileLangParser.StringExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#StringExpr.
    def exitStringExpr(self, ctx:WhileLangParser.StringExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:WhileLangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:WhileLangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#IdExpr.
    def enterIdExpr(self, ctx:WhileLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#IdExpr.
    def exitIdExpr(self, ctx:WhileLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#CompareExpr.
    def enterCompareExpr(self, ctx:WhileLangParser.CompareExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#CompareExpr.
    def exitCompareExpr(self, ctx:WhileLangParser.CompareExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#ParensExpr.
    def enterParensExpr(self, ctx:WhileLangParser.ParensExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#ParensExpr.
    def exitParensExpr(self, ctx:WhileLangParser.ParensExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#IntExpr.
    def enterIntExpr(self, ctx:WhileLangParser.IntExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#IntExpr.
    def exitIntExpr(self, ctx:WhileLangParser.IntExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:WhileLangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:WhileLangParser.AddSubExprContext):
        pass



del WhileLangParser