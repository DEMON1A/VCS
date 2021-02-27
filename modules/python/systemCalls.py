detectVariables = [
    'import os',
    'os.system',
    'os.spawn',
    'os.popen',
    'from os import system',
    'from os import popen',
    'from os import spawn',
    'exec('
]

linesCount = 0

from utils.showIssue import showIssue

def vScan(filePath):
    global linesCount

    fileLines = open(filePath , 'r').readlines()

    for singleLine in fileLines:
        linesCount += 1
        singleLine = singleLine.rstrip('\n')

        for dVariable in detectVariables:
            if dVariable in singleLine:
                if "'" not in singleLine and '"' not in singleLine and "import" not in singleLine:
                    showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="OS/exec is used on this script with user controlled input" , filePath=filePath)
                elif "+" in singleLine:
                    inputVariables = singleLine.split('+')
                    for singleInput in inputVariables:
                        if "'" not in singleInput and '"' not in singleInput:
                            showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="OS/exec is used on this script with user controlled input" , filePath=filePath)
                        else:
                            pass
                else:
                    showIssue(Serverity="info" , lineCount=linesCount , Line=singleLine , Message="OS/exec is used on this python script." , filePath=filePath)
            else:
                pass

    linesCount = 0