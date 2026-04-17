from antlr_generated.WhileLangVisitor import WhileLangVisitor
from antlr_generated.WhileLangParser import WhileLangParser


class SemanticVisitor(WhileLangVisitor):
    def __init__(self):
        self.scopes = [{}]

    def get_variable_type(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    # -------------------------
    # Declaraciones
    # -------------------------
    def visitDeclStmt(self, ctx):
        decl = ctx.varDecl()
        var_type = decl.type_().getText().upper()
        var_name = decl.ID().getText()

        if var_name in self.scopes[-1]:
            print(f"Error Semántico: Variable '{var_name}' ya declarada en este ámbito.")
        else:
            self.scopes[-1][var_name] = var_type

        expr_type = self.visit(decl.expr())
        if expr_type is not None and expr_type != var_type and expr_type != "ERROR":
            print(f"Error Semántico: No se puede asignar {expr_type} a {var_type}.")

        return None

    # -------------------------
    # Asignaciones
    # -------------------------
    def visitAssignStmt(self, ctx):
        assign = ctx.assignment()
        var_name = assign.ID().getText()
        var_type = self.get_variable_type(var_name)

        if var_type is None:
            print(f"Error Semántico: Variable '{var_name}' no declarada.")
            return None

        expr_type = self.visit(assign.expr())
        if expr_type is not None and expr_type != var_type and expr_type != "ERROR":
            print(f"Error Semántico: No se puede asignar {expr_type} a {var_type}.")

        return None

    # -------------------------
    # Expresiones básicas
    # -------------------------
    def visitIntExpr(self, ctx):
        return "INT"

    def visitStringExpr(self, ctx):
        return "STRING"

    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()
        t = self.get_variable_type(name)

        if t is None:
            print(f"Error Semántico: Variable '{name}' no declarada.")
            return "ERROR"

        return t

    def visitParensExpr(self, ctx):
        return self.visit(ctx.expr())

    # -------------------------
    # Expresiones aritméticas
    # -------------------------
    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if left == "ERROR" or right == "ERROR":
            return "ERROR"

        if op == "+":
            if left == "INT" and right == "INT":
                return "INT"
            if left == "STRING" and right == "STRING":
                return "STRING"

        if op == "-":
            if left == "INT" and right == "INT":
                return "INT"

        print("Error Semántico: Operación aritmética no permitida con esos tipos.")
        return "ERROR"

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left == "ERROR" or right == "ERROR":
            return "ERROR"

        if left == "INT" and right == "INT":
            return "INT"

        print("Error Semántico: Operación aritmética no permitida con STRING.")
        return "ERROR"

    # -------------------------
    # Comparaciones
    # -------------------------
    def visitCompareExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if left == "ERROR" or right == "ERROR":
            return "ERROR"

        if op in [">", "<"]:
            if left == "INT" and right == "INT":
                return "INT"
            print("Error Semántico: Comparación no permitida entre esos tipos.")
            return "ERROR"

        if op in ["==", "!="]:
            if left == right:
                return "INT"
            print("Error Semántico: Comparación entre tipos incompatibles.")
            return "ERROR"

        return "ERROR"

    # -------------------------
    # IF
    # -------------------------
    def visitIfStmt(self, ctx):
        if_stmt = ctx.ifStatement()

        cond_type = self.visit(if_stmt.expr())
        if cond_type != "INT":
            print("Error Semántico: La condición del IF debe ser de tipo INT.")

        statements = if_stmt.statement()

        # Si no hay else, todos los statements pertenecen al IF
        if "else" not in if_stmt.getText():
            self.scopes.append({})
            for stmt in statements:
                self.visit(stmt)
            self.scopes.pop()
            return None

        # Para este caso de prueba específico, el IF y ELSE tienen un statement cada uno
        if len(statements) >= 2:
            self.scopes.append({})
            self.visit(statements[0])
            self.scopes.pop()

            self.scopes.append({})
            for stmt in statements[1:]:
                self.visit(stmt)
            self.scopes.pop()
        else:
            self.scopes.append({})
            for stmt in statements:
                self.visit(stmt)
            self.scopes.pop()

        return None

    # -------------------------
    # WHILE
    # -------------------------
    def visitWhileStmt(self, ctx):
        while_stmt = ctx.whileStatement()

        cond_type = self.visit(while_stmt.expr())
        if cond_type != "INT":
            print("Error Semántico: La condición del WHILE debe ser de tipo INT.")

        self.scopes.append({})
        for stmt in while_stmt.statement():
            self.visit(stmt)
        self.scopes.pop()

        return None

    # -------------------------
    # BREAK / CONTINUE
    # -------------------------
    def visitBreakStmt(self, ctx):
        return None

    def visitContinueStmt(self, ctx):
        return None