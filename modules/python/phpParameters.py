'''
Serverity: information
Description: Simple Module Created To Find Places On The PHP Code Where Parameters is Used
Author: We All Created It <3.
'''

import re

detectVariables = []
blockedVariables = ['']
linesCount = 0

from utils.showIssue import showIssue

def vScan(filePath):
    global linesCount

    fileLines = open(filePath , 'r').readlines()
    for singleLine in fileLines:
        linesCount += 1
        singleLine = singleLine.rstrip('\n')

        rPatternGET = r"^..*\$(_GET)\[..*"
        rPatternPOST = r"^..*\$(_POST)\[..*"

        getResults = re.match(rPatternGET , singleLine)
        if getResults != None:
            showIssue(Serverity="info" , lineCount=linesCount , Line=singleLine , Message="PHP GET Parameter is Used On The Code." , filePath=filePath)

        postResults = re.match(rPatternPOST , singleLine)
        if postResults != None:
            showIssue(Serverity="info" , lineCount=linesCount , Line=singleLine , Message="PHP POST Parameter is Used On The Code." , filePath=filePath)

    linesCount = 0
