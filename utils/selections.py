from utils import bluzelleServices
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

#styling for questions and answer
style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

#validates if a number is entered as an answer
class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end

#function determines what set of questions should be presented 
#depending if the user wants to load from a sample file or not
def randomInsert(fileLoad):
    print('')
    print('')
    print('Dataset Seed Script for Bluzelle Database (Insert Sample Data Into Testnet)')
    print('---------------------------------------------------------------------------')

    if fileLoad == False:
        questions = [
            {
                'type': 'input',
                'name': 'urlData',
                'message': 'Enter the Bluzelle Address (default: test.network.bluzelle.com): '
            },
            {
                'type': 'input',
                'name': 'portData',
                'message': 'Enter the Bluzelle Port (default: 51010): '
            },
            {
                'type': 'input',
                'name': 'uuidData',
                'message': 'Enter a Custom UUID (ex. bluzellenamespace123): '
            },
            {
                'type': 'input',
                'name': 'quantity',
                'message': 'How many records do you want to insert?',
                'validate': NumberValidator,
                'filter': lambda val: int(val)
            }
        ]

        answers = prompt(questions, style=style)

        if answers['urlData'] != '':
            urlAnswer = answers['urlData']
        else:
            urlAnswer = 'test.network.bluzelle.com'

        if answers['portData'] != '':
            portAnswer = answers['portData']
        else:
            portAnswer = '51010'

        bluzelleServices.seedBluzelle(urlAnswer,portAnswer,answers['uuidData'],answers['quantity'],'')
    elif fileLoad == True:
        questions = [
            {
                'type': 'input',
                'name': 'urlData',
                'message': 'Enter the Bluzelle Address (default: test.network.bluzelle.com): '
            },
            {
                'type': 'input',
                'name': 'portData',
                'message': 'Enter the Bluzelle Port (default: 51010): '
            },
            {
                'type': 'input',
                'name': 'uuidData',
                'message': 'Enter a Custom UUID (ex. bluzellenamespace123): '
            },
            {
                'type': 'input',
                'name': 'filePath',
                'message': 'Enter the path to your delimited file (.csv file): '
            }
        ]

        answers = prompt(questions, style=style)

        if answers['urlData'] != '':
            urlAnswer = answers['urlData']
        else:
            urlAnswer = 'test.network.bluzelle.com'

        if answers['portData'] != '':
            portAnswer = answers['portData']
        else:
            portAnswer = '51010'

        bluzelleServices.seedBluzelle(urlAnswer,portAnswer,answers['uuidData'],0,answers['filePath'])

#prompted questions for selecting the drop keys option
def dropAll():
    print('')
    print('')
    print('Drop all keys in a uuid (THIS ACTION IS IRREVERSIBLE.  YOU\'VE BEEN WARNED!)')
    print('---------------------------------------------------------------------------')

    questions = [
        {
            'type': 'input',
            'name': 'urlData',
            'message': 'Enter the Bluzelle Address (default: test.network.bluzelle.com): '
        },
        {
            'type': 'input',
            'name': 'portData',
            'message': 'Enter the Bluzelle Port (default: 51010): '
        },
        {
            'type': 'input',
            'name': 'uuidData',
            'message': 'Enter the UUID to drop records from: '
        }
    ]

    answers = prompt(questions, style=style)

    if answers['urlData'] != '':
        urlAnswer = answers['urlData']
    else:
        urlAnswer = 'test.network.bluzelle.com'

    if answers['portData'] != '':
        portAnswer = answers['portData']
    else:
        portAnswer = '51010'

    bluzelleServices.dropAllBluzelle(urlAnswer,portAnswer,answers['uuidData'])