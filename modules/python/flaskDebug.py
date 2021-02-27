import re

linesCount = 0

from utils.showIssue import showIssue

def vScan(filePath):
    global linesCount

    fileLines = open(filePath , 'r').readlines()

    for singleLine in fileLines:
        linesCount += 1
        singleLine = singleLine.rstrip('\n')

        reResults = re.search(r"^..*(run)\s?\(()..*()\)" , singleLine)
        if reResults != None:
            if "debug=True" in singleLine:
                showIssue(Serverity="medium" , lineCount=linesCount , Line=singleLine ,Message="Flask debug mode is enabled on the code" , filePath=filePath)
            else:
                pass

    linesCount = 0