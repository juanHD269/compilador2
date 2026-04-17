# Generated from WhileLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,115,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,55,8,5,10,5,12,5,
        58,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,68,8,6,10,6,12,6,71,9,
        6,1,6,1,6,1,6,1,6,5,6,77,8,6,10,6,12,6,80,9,6,1,6,3,6,83,8,6,1,7,
        1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,99,8,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,110,8,9,10,9,12,9,113,9,9,
        1,9,0,1,18,10,0,2,4,6,8,10,12,14,16,18,0,4,1,0,1,2,1,0,16,17,1,0,
        14,15,1,0,18,21,120,0,21,1,0,0,0,2,33,1,0,0,0,4,35,1,0,0,0,6,41,
        1,0,0,0,8,43,1,0,0,0,10,48,1,0,0,0,12,61,1,0,0,0,14,84,1,0,0,0,16,
        87,1,0,0,0,18,98,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,
        0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,5,0,0,1,26,1,1,
        0,0,0,27,34,3,4,2,0,28,34,3,8,4,0,29,34,3,10,5,0,30,34,3,12,6,0,
        31,34,3,14,7,0,32,34,3,16,8,0,33,27,1,0,0,0,33,28,1,0,0,0,33,29,
        1,0,0,0,33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,
        36,3,6,3,0,36,37,5,22,0,0,37,38,5,13,0,0,38,39,3,18,9,0,39,40,5,
        12,0,0,40,5,1,0,0,0,41,42,7,0,0,0,42,7,1,0,0,0,43,44,5,22,0,0,44,
        45,5,13,0,0,45,46,3,18,9,0,46,47,5,12,0,0,47,9,1,0,0,0,48,49,5,3,
        0,0,49,50,5,8,0,0,50,51,3,18,9,0,51,52,5,9,0,0,52,56,5,10,0,0,53,
        55,3,2,1,0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,
        0,57,59,1,0,0,0,58,56,1,0,0,0,59,60,5,11,0,0,60,11,1,0,0,0,61,62,
        5,4,0,0,62,63,5,8,0,0,63,64,3,18,9,0,64,65,5,9,0,0,65,69,5,10,0,
        0,66,68,3,2,1,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,
        1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,82,5,11,0,0,73,74,5,5,0,0,
        74,78,5,10,0,0,75,77,3,2,1,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,
        0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,81,83,5,11,0,0,82,
        73,1,0,0,0,82,83,1,0,0,0,83,13,1,0,0,0,84,85,5,6,0,0,85,86,5,12,
        0,0,86,15,1,0,0,0,87,88,5,7,0,0,88,89,5,12,0,0,89,17,1,0,0,0,90,
        91,6,9,-1,0,91,92,5,8,0,0,92,93,3,18,9,0,93,94,5,9,0,0,94,99,1,0,
        0,0,95,99,5,22,0,0,96,99,5,23,0,0,97,99,5,24,0,0,98,90,1,0,0,0,98,
        95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,0,99,111,1,0,0,0,100,101,10,
        6,0,0,101,102,7,1,0,0,102,110,3,18,9,7,103,104,10,5,0,0,104,105,
        7,2,0,0,105,110,3,18,9,6,106,107,10,4,0,0,107,108,7,3,0,0,108,110,
        3,18,9,5,109,100,1,0,0,0,109,103,1,0,0,0,109,106,1,0,0,0,110,113,
        1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,19,1,0,0,0,113,111,1,
        0,0,0,9,23,33,56,69,78,82,98,109,111
    ]

class WhileLangParser ( Parser ):

    grammarFileName = "WhileLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'string'", "'while'", "'if'", 
                     "'else'", "'break'", "'continue'", "'('", "')'", "'{'", 
                     "'}'", "';'", "'='", "'+'", "'-'", "'*'", "'/'", "'>'", 
                     "'<'", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "INT_TYPE", "STRING_TYPE", "WHILE", "IF", 
                      "ELSE", "BREAK", "CONTINUE", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "SEMI", "ASSIGN", "PLUS", "MINUS", "MULT", 
                      "DIV", "GT", "LT", "EQ", "NE", "ID", "NUMBER", "STRING", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDecl = 2
    RULE_type = 3
    RULE_assignment = 4
    RULE_whileStatement = 5
    RULE_ifStatement = 6
    RULE_breakStatement = 7
    RULE_continueStatement = 8
    RULE_expr = 9

    ruleNames =  [ "program", "statement", "varDecl", "type", "assignment", 
                   "whileStatement", "ifStatement", "breakStatement", "continueStatement", 
                   "expr" ]

    EOF = Token.EOF
    INT_TYPE=1
    STRING_TYPE=2
    WHILE=3
    IF=4
    ELSE=5
    BREAK=6
    CONTINUE=7
    LPAREN=8
    RPAREN=9
    LBRACE=10
    RBRACE=11
    SEMI=12
    ASSIGN=13
    PLUS=14
    MINUS=15
    MULT=16
    DIV=17
    GT=18
    LT=19
    EQ=20
    NE=21
    ID=22
    NUMBER=23
    STRING=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(WhileLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.StatementContext,i)


        def getRuleIndex(self):
            return WhileLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = WhileLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4194526) != 0)):
                    break

            self.state = 25
            self.match(WhileLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileLangParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ContinueStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def continueStatement(self):
            return self.getTypedRuleContext(WhileLangParser.ContinueStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStatement(self):
            return self.getTypedRuleContext(WhileLangParser.IfStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def whileStatement(self):
            return self.getTypedRuleContext(WhileLangParser.WhileStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(WhileLangParser.AssignmentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class BreakStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def breakStatement(self):
            return self.getTypedRuleContext(WhileLangParser.BreakStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)


    class DeclStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varDecl(self):
            return self.getTypedRuleContext(WhileLangParser.VarDeclContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclStmt" ):
                listener.enterDeclStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclStmt" ):
                listener.exitDeclStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclStmt" ):
                return visitor.visitDeclStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = WhileLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                localctx = WhileLangParser.DeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.varDecl()
                pass
            elif token in [22]:
                localctx = WhileLangParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.assignment()
                pass
            elif token in [3]:
                localctx = WhileLangParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.whileStatement()
                pass
            elif token in [4]:
                localctx = WhileLangParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.ifStatement()
                pass
            elif token in [6]:
                localctx = WhileLangParser.BreakStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.breakStatement()
                pass
            elif token in [7]:
                localctx = WhileLangParser.ContinueStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 32
                self.continueStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(WhileLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(WhileLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = WhileLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.type_()
            self.state = 36
            self.match(WhileLangParser.ID)
            self.state = 37
            self.match(WhileLangParser.ASSIGN)
            self.state = 38
            self.expr(0)
            self.state = 39
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(WhileLangParser.INT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(WhileLangParser.STRING_TYPE, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = WhileLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(WhileLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = WhileLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(WhileLangParser.ID)
            self.state = 44
            self.match(WhileLangParser.ASSIGN)
            self.state = 45
            self.expr(0)
            self.state = 46
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(WhileLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(WhileLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(WhileLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(WhileLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(WhileLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.StatementContext,i)


        def getRuleIndex(self):
            return WhileLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = WhileLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(WhileLangParser.WHILE)
            self.state = 49
            self.match(WhileLangParser.LPAREN)
            self.state = 50
            self.expr(0)
            self.state = 51
            self.match(WhileLangParser.RPAREN)
            self.state = 52
            self.match(WhileLangParser.LBRACE)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4194526) != 0):
                self.state = 53
                self.statement()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(WhileLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(WhileLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(WhileLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(WhileLangParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(WhileLangParser.LBRACE)
            else:
                return self.getToken(WhileLangParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(WhileLangParser.RBRACE)
            else:
                return self.getToken(WhileLangParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(WhileLangParser.ELSE, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = WhileLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(WhileLangParser.IF)
            self.state = 62
            self.match(WhileLangParser.LPAREN)
            self.state = 63
            self.expr(0)
            self.state = 64
            self.match(WhileLangParser.RPAREN)
            self.state = 65
            self.match(WhileLangParser.LBRACE)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4194526) != 0):
                self.state = 66
                self.statement()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(WhileLangParser.RBRACE)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 73
                self.match(WhileLangParser.ELSE)
                self.state = 74
                self.match(WhileLangParser.LBRACE)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4194526) != 0):
                    self.state = 75
                    self.statement()
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 81
                self.match(WhileLangParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(WhileLangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = WhileLangParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(WhileLangParser.BREAK)
            self.state = 85
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(WhileLangParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = WhileLangParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(WhileLangParser.CONTINUE)
            self.state = 88
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(WhileLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)

        def MULT(self):
            return self.getToken(WhileLangParser.MULT, 0)
        def DIV(self):
            return self.getToken(WhileLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class CompareExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)

        def GT(self):
            return self.getToken(WhileLangParser.GT, 0)
        def LT(self):
            return self.getToken(WhileLangParser.LT, 0)
        def EQ(self):
            return self.getToken(WhileLangParser.EQ, 0)
        def NE(self):
            return self.getToken(WhileLangParser.NE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareExpr" ):
                listener.enterCompareExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareExpr" ):
                listener.exitCompareExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExpr" ):
                return visitor.visitCompareExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(WhileLangParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(WhileLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(WhileLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(WhileLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(WhileLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = WhileLangParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 91
                self.match(WhileLangParser.LPAREN)
                self.state = 92
                self.expr(0)
                self.state = 93
                self.match(WhileLangParser.RPAREN)
                pass
            elif token in [22]:
                localctx = WhileLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 95
                self.match(WhileLangParser.ID)
                pass
            elif token in [23]:
                localctx = WhileLangParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 96
                self.match(WhileLangParser.NUMBER)
                pass
            elif token in [24]:
                localctx = WhileLangParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.match(WhileLangParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 111
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 109
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = WhileLangParser.MulDivExprContext(self, WhileLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 101
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 102
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = WhileLangParser.AddSubExprContext(self, WhileLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 103
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 104
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 105
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = WhileLangParser.CompareExprContext(self, WhileLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 106
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 107
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 108
                        self.expr(5)
                        pass

             
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




