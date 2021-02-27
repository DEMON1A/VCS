detectVariables = [
    'import yaml',
    'from yaml import load',
    'yaml.load',
    'yaml.FullLoader',
    'yaml.Loader',
]

blockedVariables = ['yaml.SafeLoader' , 'SafeLoader']
linesCount = 0

from utils.showIssue import showIssue

def vScan(filePath):
    global linesCount
    breakLoop = False

    fileLines = open(filePath , 'r').readlines()

    for singleLine in fileLines:
        linesCount += 1
        singleLine = singleLine.rstrip('\n')

        for dVariable in detectVariables:
            if dVariable in singleLine:
                for blockedItem in blockedVariables:
                    if blockedItem not in singleLine: pass
                    else: breakLoop = True

                if breakLoop: break
                else: pass

                if "import" in singleLine:
                    showIssue(Serverity="info" , lineCount=linesCount , Line=singleLine , Message="YAML is imported on the python script" , filePath=filePath)
                elif "from yaml" in singleLine:
                    showIssue(Serverity="low" , lineCount=linesCount , Line=singleLine , Message="Insecure YAML loader is imported on the code." , filePath=filePath)
                else:
                    showIssue(Serverity="high" , lineCount=linesCount , Line=singleLine , Message="Insecure YAML loader is used to proccess files" , filePath=filePath)
            else:
                pass

    linesCount = 0