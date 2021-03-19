# \.(open)\(.*\)
# (open)\(.*\)

'''
Serverity: high
Description: Ruby Command Execution Via Filename Detector
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

        reGexResults = re.match(r"(\.open|open)\(.*\)", singleLine)
        if reGexResults != None:
        	argumentsString = reGexResults.group()
        	argumentsRe = re.search(r"\(.*\)", argumentsString).group()
        	argumentsRe = argumentsRe.replace('(', '').replace(')', '')

        	if "," in argumentsRe: argumentPath = argumentsRe.split(',')[0]
        	else: argumentPath = argumentsRe

        	if "'" and '"' not in argumentPath:
        		showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="Ruby Kernal Open is Used With User Controlled Input." , filePath=filePath)
        	elif "#{" in argumentPath:
        		showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="Ruby Kernal Open is Used With User Controlled Input." , filePath=filePath)
        	else:
        		pass

    linesCount = 0
