"""
File: parsers.py

Defines Parser
"""

from tokens import Token
from scanner import Scanner

class Parser(object):

    def parse(self, sourceStr):
        self._completionMessage = "No errors"
        self._parseSuccessful = True
        self._scanner = Scanner(sourceStr)
        self._expression()
        self._accept(self._scanner.get(), Token.EOE,
                     "symbol after end of expression")
   
    def parseStatus(self):
        return self._completionMessage
    
    def _accept(self, token, expected, errorMessage):
        if token.getType() != expected:
            self._fatalError(token, errorMessage)

    def _fatalError(self, token, errorMessage):
        self._parseSuccessful = False
        self._completionMessage = "Parsing error -- " + \
                                  errorMessage + \
                                  "\nExpression so far = " + \
                                  self._scanner.stringUpToCurrentToken()
        raise Exception, self._completionMessage

    def _expression(self):
        """Syntax rule:
        expression = term { addingOperator term }  """           
        self._term()
        token = self._scanner.get()
        while token.getType() in (Token.PLUS, Token.MINUS):
            self._scanner.next()
            self._term()
            token = self._scanner.get()

    def _term(self):
        """Syntax rule:
        term = factor { multiplyingOperator factor }  """           
        self._factor()
        token = self._scanner.get()
        while token.getType() in (Token.MUL, Token.DIV):
            self._scanner.next()
            self._factor()
            token = self._scanner.get()

    def _factor(self):
        """Syntax rule:
        factor = number | "(" expression ")  """"          
        token = self._scanner.get()
        if token.getType() == Token.INT:
            self._scanner.next()
        elif token.getType() == Token.L_PAR:
            self._scanner.next()
            self._expression()
            self._accept(self._scanner.get(),
                         Token.R_PAR,
                         "')' expected")
            self._scanner.next()
        else:
            self._fatalError(token, "bad factor")

