'''
Serverity: high
Description: Insecure YAML Deserialization Detector On Ruby
Author: We All Created It <3.
'''
import re

detectVariables = []
blockedVariables = ['']
linesCount = 0

detectYAMLPattern = r"^require..*(\'|\")yaml(\'|\")"
insecureProcessingPattern = r"^YAML(\.|\:\:)load(..*)"

from utils.showIssue import showIssue

def vScan(filePath):
    global linesCount

    fileLines = open(filePath , 'r').readlines()
    for singleLine in fileLines:
        linesCount += 1
        singleLine = singleLine.rstrip('\n')

        detectResults = re.search(detectYAMLPattern , singleLine)
        if detectResults != None:
            showIssue(Serverity="info" , lineCount=linesCount , Line=singleLine , Message="Unsafe YAML is imported on the ruby code" , filePath=filePath)

        processingResults = re.search(insecureProcessingPattern , singleLine)
        if processingResults != None:
            showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="Insecure YAML processing is happening on the ruby code" , filePath=filePath)

    linesCount = 0
