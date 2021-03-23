'''
Serverity: 
Description: 
Author: 
'''

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

        '''
        scan code here
        '''

    linesCount = 0
