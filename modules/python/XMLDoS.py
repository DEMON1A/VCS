'''
Serverity: high
Description: Python XML Parsing DoS Detector.
Author: We All Created It <3.
'''
import re

detectVariables = [
    'import xml',
    'from xml import',
    'from xml.etree.ElementTree import',
    'import xml.etree.ElementTree'
]

blockedVariables = ['']
xmlUsed = False
linesCount = 0

from utils.showIssue import showIssue

def vScan(filePath):
    global linesCount

    fileLines = open(filePath , 'r').readlines()
    for singleLine in fileLines:
        linesCount += 1
        singleLine = singleLine.rstrip('\n')

        for dVairable in detectVariables:
            if dVairable in singleLine:
                xmlUsed = True
                showIssue(Serverity="low" , lineCount=linesCount , Line=singleLine , Message="Insecure XML Parsing is Used On The Python Code." , filePath=filePath)
            else:
                pass

        if xmlUsed:
            reResults = re.match(r"^..*(etree\.ElementTree)\.(parse)..*" , singleLine)
            if reResults != None:
                showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="Insecure XML Parsing is Used On The Code." , filePath=filePath)
            else:
                _reResults = re.match(r"^..*(parse)..*" , singleLine)
                if _reResults != None:
                    showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="Insecure XML Parsing is Used On The Code." , filePath=filePath)
                else:
                    pass


    linesCount = 0
