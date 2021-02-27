from os import path
from utils.showMessage import showError

def aParser(argumentVariable):
    if "," in argumentVariable:
        argumentVariable = argumentVariable.split(",")

        for argument in argumentVariable:
            if path.exists(argument): pass
            else:
                showError(exceptionRule="Options Error" , Message=f"There's no file or directory: {argument}")
                return False

        return argumentVariable
    else:
        if path.exists(argumentVariable): return argumentVariable
        else:
            showError(exceptionRule="Options Error" , Message=f"There's no file or directory: {argumentVariable}")
            return False