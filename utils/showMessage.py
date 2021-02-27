from colorama import init
from termcolor import colored

def showError(exceptionRule , Message):
    init()

    ruleColored = colored(exceptionRule , 'yellow' , attrs=['bold'])
    messageColored = colored(Message , 'red' , attrs=['bold'])

    errorMessage = f"{ruleColored}: {messageColored}"
    print(errorMessage)

def showGood(goodRule , Message):
    init()

    ruleColored = colored(goodRule , 'yellow' , attrs=['bold'])
    messageColored = colored(Message , 'green' , attrs=['bold'])

    errorMessage = f"{ruleColored}: {messageColored}"
    print(errorMessage)