'''
Serverity: high
Description: Django Template Engine Safe Arguments Detector
Author: We All Created It <3.
'''
import re

detectVariables = ['']
blockedVariables = ['']
linesCount = 0

from utils.showIssue import showIssue

def vScan(filePath):
    global linesCount

    fileLines = open(filePath , 'r').readlines()
    for singleLine in fileLines:
        linesCount += 1
        singleLine = singleLine.rstrip('\n')

        ReGexResults = re.match(r"..*\{..*\|(.*safe)..*\}" , singleLine)
        if ReGexResults != None:
            showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="Safe is used on the django template that could lead to possible XSS" , filePath=filePath)

    linesCount = 0
