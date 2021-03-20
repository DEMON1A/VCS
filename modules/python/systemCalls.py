'''
Serverity: info
Description: Python Command Execution Detector
Author: We All Created It <3.
'''
import re

detectVariables = [
    'import os',
    'from os import'
]

linesCount = 0
systemImported = False

from utils.showIssue import showIssue

def vScan(filePath):
    global linesCount, systemImported

    fileLines = open(filePath , 'r').readlines()

    for singleLine in fileLines:
        linesCount += 1
        singleLine = singleLine.rstrip('\n')

        for dVariable in detectVariables:
            if dVariable in singleLine:
                systemImported = True
                showIssue(Serverity="info" , lineCount=linesCount , Line=singleLine , Message="Python OS is used on the code" , filePath=filePath)
            else:
                pass

        if systemImported:
            systemUsed = re.match(r"..*\.(system)\(.*\)" , singleLine)
            if systemUsed != None:
                if "'" and '"' not in systemUsed.group():
                    showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="Python OS is used with a user controlled variable" , filePath=filePath)
                else:
                    showIssue(Serverity="info" , lineCount=linesCount , Line=singleLine , Message="Python OD is used on the code" , filePath=filePath)

        execFinder = re.match(r".*exec\(.*\)" , singleLine)
        if execFinder != None:
            if "'" and '"' not in execFinder.group():
                showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="Python exec is used with a user controlled variable" , filePath=filePath)
            else:
                showIssue(Serverity="info" , lineCount=linesCount , Line=singleLine , Message="Python exec is used on the code" , filePath=filePath)

    linesCount = 0
    systemImported = False
