"""
File: parserapp.py
View for the infix expression parser.
Handles user interaction.
"""

from parsers import Parser

class ParserView(object):

    def run(self):
        parser = Parser()
        while True:
            sourceStr = raw_input("Enter an infix expression: ")
            if sourceStr == "": break
            try:
                parser.parse(sourceStr)
                print parser.parseStatus()
            except Exception, e:
                print "Error:"
                print e

ParserView().run()
