import importlib
import concurrent.futures

from utils.showMessage import showError

def startScan(filePath , Modules):
    try:
        for Module in Modules:
            Module = Module.replace('.py' , '')
            importVariable = f"modules.{Module}"
            with concurrent.futures.ThreadPoolExecutor() as moduleStarter:
                moduleFunction = importlib.import_module(importVariable)
                _ = moduleStarter.submit(moduleFunction.vScan , filePath)
    except Exception as e:
        showError(exceptionRule="Module Error" , Message=f"Exception On Your Module > {str(e)}")
        exit()
