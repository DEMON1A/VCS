import re

detectVariables = [
    'import sqlite3',
    'from sqlite3 import'
]


blockedVariables = ['']

linesCount = 0

from utils.showIssue import showIssue

def vScan(filePath):
    global linesCount

    fileLines = open(filePath , 'r').readlines()

    for singleLine in fileLines:
        singleLine = singleLine.rstrip('\n')
        linesCount += 1

        for dVariable in detectVariables:
            if dVariable in singleLine:
                showIssue(Serverity="info" , lineCount=linesCount , Line=singleLine , Message="The program is using sqlite3 in the code" , filePath=filePath)
        reResults = re.search(r'^..*(execute)\s?\(()..*()\)' , singleLine)
        if reResults != None:
            if "%" in singleLine:
                if "%d" in singleLine or "%s" in singleLine:
                    showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="SQL command is getting executed with unsafe user input" , filePath=filePath)

            externalVariables = re.search(r'\{..*\}' , singleLine)
            if externalVariables != None:
                showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="SQL command is getting executed with unsafe user input" , filePath=filePath)

    linesCount = 0