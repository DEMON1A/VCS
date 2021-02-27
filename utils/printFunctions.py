from colorama import init
from termcolor import colored

def printlnStr(Content):
    Content = str(Content)
    print(Content)

def printlnInt(Content):
    Content = int(Content)
    print(Content)

def printlnColored(Content , Color):
    init()
    coloredMessage = colored(Content , Color , attrs=['bold'])
    print(coloredMessage)