'''
Serverity: high
Description: Node Serialization Code Injection Detector
Author: We All Created It <3.
'''

import re

detectVariables = []
blockedVariables = ['']
linesCount = 0

detectNodeSerialization = r"^..*require\((\'|\")funcster(\'|\")..*"
detectSerializationFunction = ".*VARIABLE\.(deepDeserialize)..*"
nodeSerializationUsed = False

from utils.showIssue import showIssue
from utils.nameFinder import nodejsStringFinder

def vScan(filePath):
    global linesCount , detectSerializationFunction

    fileLines = open(filePath , 'r').readlines()
    for singleLine in fileLines:
        linesCount += 1
        singleLine = singleLine.rstrip('\n')

        reGexResults = re.match(detectNodeSerialization , singleLine)
        if reGexResults != None:
            serializeObject = nodejsStringFinder(reGexResults=reGexResults.group())
            nodeSerializationUsed = True
            showIssue(Serverity="info" , lineCount=linesCount , Line=singleLine , Message="Nodejs Serialization is used on the code" , filePath=filePath)

        if nodeSerializationUsed:
            detectSerializationFunction = detectSerializationFunction.replace('VARIABLE' , serializeObject)
            reGexResults = re.match(detectSerializationFunction , singleLine)

            if reGexResults != None:
                reGexString = reGexResults.group()
                if "'" and '"' not in reGexString:
                    showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="The Nodejs code is unserializing a user controlled input" , filePath=filePath)
                else:
                    showIssue(Serverity="low" , lineCount=linesCount , Line=singleLine , Message="The Nodejs code is unserializing a static variable" , filePath=filePath)

    linesCount = 0
