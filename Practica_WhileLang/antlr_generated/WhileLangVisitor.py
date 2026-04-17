# Generated from WhileLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .WhileLangParser import WhileLangParser
else:
    from WhileLangParser import WhileLangParser

# This class defines a complete generic visitor for a parse tree produced by WhileLangParser.

class WhileLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WhileLangParser#program.
    def visitProgram(self, ctx:WhileLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#DeclStmt.
    def visitDeclStmt(self, ctx:WhileLangParser.DeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#AssignStmt.
    def visitAssignStmt(self, ctx:WhileLangParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#WhileStmt.
    def visitWhileStmt(self, ctx:WhileLangParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#IfStmt.
    def visitIfStmt(self, ctx:WhileLangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#BreakStmt.
    def visitBreakStmt(self, ctx:WhileLangParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#ContinueStmt.
    def visitContinueStmt(self, ctx:WhileLangParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#varDecl.
    def visitVarDecl(self, ctx:WhileLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#type.
    def visitType(self, ctx:WhileLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#assignment.
    def visitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#whileStatement.
    def visitWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#ifStatement.
    def visitIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#breakStatement.
    def visitBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#continueStatement.
    def visitContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#StringExpr.
    def visitStringExpr(self, ctx:WhileLangParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:WhileLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#IdExpr.
    def visitIdExpr(self, ctx:WhileLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#CompareExpr.
    def visitCompareExpr(self, ctx:WhileLangParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#ParensExpr.
    def visitParensExpr(self, ctx:WhileLangParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#IntExpr.
    def visitIntExpr(self, ctx:WhileLangParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:WhileLangParser.AddSubExprContext):
        return self.visitChildren(ctx)



del WhileLangParser