import re

detectVariables = [
    'import sqlite3',
    'from sqlite3 import'
]

blockedVariables = ['']
linesCount = 0

from utils.showIssue import showIssue
from utils.variableTracker import Tracker
from utils.pythonSemicolon import semicolonParser
from utils.nameFinder import nameStringFinder

def vScan(filePath):
    global linesCount

    fileLines = open(filePath , 'r').readlines()
    fileLines = semicolonParser(fileLines=fileLines)

    for singleLine in fileLines:
        singleLine = singleLine.rstrip('\n')
        linesCount += 1

        for dVariable in detectVariables:
            if dVariable in singleLine:
                showIssue(Serverity="info" , lineCount=linesCount , Line=singleLine , Message="The program is using sqlite3 on the code" , filePath=filePath)

        reResults = re.search(r'^..*(execute)\s?\(()..*()\)' , singleLine)
        if reResults != None:
            if "+" in singleLine:
                realLines = singleLine.split('+')
                for Item in realLines:
                    if "'" not in singleLine and '"' not in Item:
                        nameString = nameStringFinder(reResults.group())
                        trackerResult = Tracker(nameString=nameString , fileLines=fileLines)

                        if len(trackerResult) != 0:
                            for singleResult in trackerResult:
                                if "%" in singleResult:
                                    if "%d" in singleLine or "%s" in singleLine:
                                        showIssue(Serverity="high" , lineCount=linesCount , Line=singleResult , Message="SQL command is getting executed with unsafe user input" , filePath=filePath)

                                externalVariables = re.search(r'\{..*\}' , singleResult)
                                if externalVariables != None:
                                    showIssue(Serverity="high" , lineCount=linesCount , Line=singleResult , Message="SQL command is getting executed with unsafe user input" , filePath=filePath)
                    elif "%" in Item:
                        if "%d" in Item or "%s" in Item:
                            showIssue(Serverity="high" , lineCount=linesCount , Line=Item , Message="SQL command is getting executed with unsafe user input" , filePath=filePath)

                    externalVariables = re.search(r'\{..*\}' , Item)
                    if externalVariables != None:
                        showIssue(Serverity="high" , lineCount=linesCount , Line=Item , Message="SQL command is getting executed with unsafe user input" , filePath=filePath)

            else:
                if "'" not in singleLine and '"' not in singleLine:
                    nameString = nameStringFinder(reResults.group())
                    trackerResult = Tracker(nameString=nameString , fileLines=fileLines)

                    if len(trackerResult) != 0:
                        for singleResult in trackerResult:
                            if "%" in singleResult:
                                if "%d" in singleLine or "%s" in singleLine:
                                    showIssue(Serverity="high" , lineCount=linesCount , Line=singleResult , Message="SQL command is getting executed with unsafe user input" , filePath=filePath)

                            externalVariables = re.search(r'\{..*\}' , singleResult)
                            if externalVariables != None:
                                showIssue(Serverity="high" , lineCount=linesCount , Line=singleResult , Message="SQL command is getting executed with unsafe user input" , filePath=filePath)
                elif "%" in singleLine:
                    if "%d" in singleLine or "%s" in singleLine:
                        showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="SQL command is getting executed with unsafe user input" , filePath=filePath)

                externalVariables = re.search(r'\{..*\}' , singleLine)
                if externalVariables != None:
                    showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="SQL command is getting executed with unsafe user input" , filePath=filePath)

    linesCount = 0
