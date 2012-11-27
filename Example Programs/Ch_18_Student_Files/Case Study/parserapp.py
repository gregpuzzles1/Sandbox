"""
File: parserapp.py
View for the infix expression parser.
Handles user interaction.
"""

from parser import Parser

class ParserView(object):

    def run(self):
        parser = Parser()
        while True:
            sourceStr = raw_input("Enter an infix expression: ")
            if sourceStr == "": break
            try:
                tree = parser.parse(sourceStr)
                print "Prefix:", tree.prefix()
                print "Infix:", tree.infix()
                print "Postfix:", tree.postfix()
                print "Value:", tree.value()
            except Exception, e:
                print "Error:"
                print e

ParserView().run()
