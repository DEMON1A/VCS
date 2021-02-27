import optparse
import concurrent.futures

from utils.optionsValidator import oValidator
from utils.argumentParser import aParser
from utils.printFunctions import printlnStr
from utils.listFiles import listFiles

from scanner.scannerBase import scannerBase

def collectOptions():
    optionsParser = optparse.OptionParser()
    optionsParser.add_option("-f" , "--file" , default=False , dest="file" , help="The Code File You Want To Scan.")
    optionsParser.add_option("-d" , "--dir" , default=False , dest="dir" , help="The Directory That Contains The Code You Want To Scan.")
    optionsParser.add_option("-l" , "--language" , default="all" , dest="language" , help="The Language The Code Gonna Scan.")
    optionsParser.add_option("-x" , "--exclude" , default=False , dest="exclude" , help="Exclude a Scan From The List.")

    toolOptions,_ = optionsParser.parse_args()
    return toolOptions

def mainFunction(Options):
    __OPTIONS__, __LIST__ = oValidator(Options=Options)

    try:
        if "file" in __LIST__:
            fileOptions = __OPTIONS__['file']
            fileOptions = aParser(argumentVariable=fileOptions)

            if type(fileOptions) == list:
                for singleFile in fileOptions:
                    scannerBase(filePath=singleFile)
            elif not fileOptions:
                exit()
            else:
                scannerBase(filePath=fileOptions , Language=__OPTIONS__['language'])
        elif "dir" in __LIST__:
            dirOptions = __OPTIONS__['dir']
            dirOptions = aParser(argumentVariable=dirOptions)

            if type(dirOptions) == list:
                for singleDir in dirOptions:
                    dirFiles = listFiles(singleDir)
                    for singleFile in dirFiles:
                        scannerBase(filePath=f"{singleDir}/{singleFile}" , Language=__OPTIONS__['language'])
            else:
                dirFiles = listFiles(dirOptions)
                for singleFile in dirFiles:
                    scannerBase(filePath=f"{dirOptions}/{singleFile}" , Language=__OPTIONS__['language'])
    except Exception as e:
        printlnStr(e)

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as optionsCollector:
        toolOptions = optionsCollector.submit(collectOptions)
        toolOptions = toolOptions.result()

    with concurrent.futures.ThreadPoolExecutor() as mainThreader:
        _ = mainThreader.submit(mainFunction , toolOptions)