#!/usr/bin/env python2.7
from __future__ import print_function, unicode_literals
import sys

from utils import selections
from PyInquirer import style_from_dict, Token, prompt
from termcolor import colored

if __name__ == '__main__':

    # styling for questions and answer
    style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '',
        Token.Answer: '#2196f3 bold',
        Token.Question: '',
    })

    # loop to give it a REPL feel
    while True:
        print('')
        print(
            colored(
                '==========================================================================',
                'blue'))
        print(
            colored(
                'Bluzelle CLI',
                'blue') +
            ' - ' +
            colored(
                'An easy way to load sample data into the Bluzelle Database',
                'yellow'))
        print(
            colored(
                '==========================================================================',
                'blue'))
        print('')

        # top level questions
        topquestions = [{'type': 'rawlist',
                         'name': 'topactions',
                         'message': 'What would you like to do? (select a number)',
                         'choices': ['Insert Random Sample Data',
                                     'Insert Sample Data from a File',
                                     'Drop all keys from a UUID',
                                     'Exit'],
                         'filter': lambda val: val.lower()}]

        topanswers = prompt(topquestions, style=style)

        # depending on selection, execute insert or drop functions
        if(topanswers['topactions'] == 'insert random sample data'):
            selections.randomInsert()
        elif(topanswers['topactions'] == 'insert sample data from a file'):
            selections.fileInsert()
        elif(topanswers['topactions'] == 'drop all keys from a uuid'):
            selections.dropAll()
        elif(topanswers['topactions'] == 'exit'):
            sys.exit()
