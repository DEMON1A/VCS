'''
this scanner module is used to run php scan modules. so users can write their own
scan module in PHP rather than python. that will be helpful for users who don't
know python and want to write their own modules.

your PHP module should return a clear output that consists of the show issue arguments
rather than that the scanner will ignore your script output. sounds cool?

if you don't have PHP on your system, go ahead and install it before running this
tool.
'''

import subprocess

from utils.commandInjection import validateCharacters
from utils.showMessage import showError
from utils.showIssue import showIssue

def phpStart(filePath , phpScripts):
    for phpScript in phpScripts:
        fileValidation = validateCharacters(theString=filePath)
        phpValidation = validateCharacters(theString=phpScript)

        if fileValidation and phpValidation: pass
        else: showError(exceptionRule="Security Error" , Message="One Of You Inputs Contains Disallowed Characters."); exit()

        systemCommand = f"php modules/{phpScript} {filePath}"

        Process = subprocess.Popen(systemCommand , shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        processOutput = Process.communicate()[0].decode('UTF-8')
        outputLinesCount = countLines(Output=processOutput)

        if processOutput.split('\n')[-1] == "False" or processOutput.split('\n')[-1] == '':
            pass
        elif "," in processOutput:
            try:
                if outputLinesCount == 1:
                    outputMessage = processOutput.split(',')

                    Serverity = outputMessage[0]
                    lineCount = outputMessage[1]
                    codeLine = outputMessage[2]
                    Message = outputMessage[3]

                    codeLine = codeLine.replace('COMMA' , ',')

                    showIssue(Serverity=Serverity , lineCount=lineCount , Line=codeLine , Message=Message , filePath=filePath)
                else:
                    processLines = processOutput.split('\n')
                    for singleItem in processLines:
                        outputMessage = singleItem.split(',')

                        Serverity = outputMessage[0]
                        lineCount = outputMessage[1]
                        codeLine = outputMessage[2]
                        Message = outputMessage[3]

                        showIssue(Serverity=Serverity , lineCount=lineCount , Line=codeLine , Message=Message , filePath=filePath)
            except Exception:
                showError(exceptionRule="Module Error" , Message="Your PHP Module Did Return Invalid Issues Format")
        else:
            showError(exceptionRule="Module Error" , Message="Your PHP Module Did Return Invalid Output We Can't Parse")

def countLines(Output):
    if "\n" in Output:
        realOutput = Output.split('\n')
        return len(realOutput)
    else:
        return 1
