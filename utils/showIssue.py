from colorama import init
from termcolor import colored
from datetime import datetime

from utils.showMessage import showError

def detectColor(Serverity):
    if Serverity.lower() == "high":
        stringColor = "red"
    elif Serverity.lower() == "medium":
        stringColor = "yellow"
    elif Serverity.lower() == "low":
        stringColor = "magenta"
    elif Serverity.lower() == "info":
        stringColor = "blue"
    else:
        showError(exceptionRule="Report Error" , Message=f"You did use an invalid serverity on your module: {Serverity}")
        exit()

    return stringColor

def showIssue(Serverity , lineCount , Line , Message , filePath):
    init()

    dateString = datetime.today().strftime('%Y-%m-%d')

    realPath = filePath.replace('//' , '/')
    headLine = '<' + '-' * 30 + f'[{realPath}]'  + '-' * 30 + '>'
    headLine = colored(headLine , 'green' , attrs=['bold'])

    dateHeader = f"[{dateString}]"
    dateHeader = colored(dateHeader , 'yellow' , attrs=['bold'])

    serverityHeader = f"[{Serverity}]"
    serverityColor = detectColor(Serverity=Serverity)
    serverityHeader = colored(serverityHeader , serverityColor , attrs=['bold'])

    lineCountHeader = f"[line: {str(lineCount)}]"
    lineCountHeader = colored(lineCountHeader , 'green')

    messageHeader = f"{Message}"
    messageHeader = colored(messageHeader , 'cyan' , attrs=['bold'])

    codeColor = colored(Line , 'yellow' , attrs=['bold'])

    lineHeader = f"[Code]: "
    lineHeader = colored(lineHeader , 'red' , attrs=['bold'])
    lineHeader = lineHeader + codeColor

    finalMessage = f"{headLine}\n{dateHeader}:{serverityHeader}: {messageHeader} \t{lineCountHeader}\n{lineHeader}\n{headLine}\n\n"
    print(finalMessage)