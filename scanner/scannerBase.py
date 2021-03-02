from os import listdir
from scanner.scansStarter import startScan
from scanner.phpStarter import phpStart

from utils.showMessage import showError

languagesList = ['python' , 'php' , 'nodejs']

def scannerBase(filePath , Language):
    if Language == "all":
        modulesList = listdir('modules/')
        __MODULES__ = []
        __PHP_MODULES__ = []

        for languageDir in modulesList:
            languageModules = listdir(f'modules/{languageDir}')

            for singleFile in languageModules:
                if singleFile.endswith('.py'):
                    __MODULES__.append(f'{languageDir}.{singleFile}')
                elif singleFile.endswith('.php'):
                    __PHP_MODULES__.append(f'{languageDir}/{singleFile}')
                else:
                    pass
    else:
        if Language in languagesList:
            modulesList = listdir(f'modules/{Language}/')
            __MODULES__ = []
            __PHP_MODULES__ = []

            for singleModule in modulesList:
                if singleModule.endswith('.py'):
                    __MODULES__.append(f'{singleModule}')
                elif singleModule.endswith('.php'):
                    __PHP_MODULES__.append(f'{Language}/{singleModule}')
                else:
                    pass
        else:
            showError(exceptionRule="Importing Error" , Message="We don't have scanning scripts for this language")
            exit()

    startScan(filePath=filePath , Modules=__MODULES__)
    phpStart(filePath=filePath , phpScripts=__PHP_MODULES__)
