'''
this module is used to parse python lines that contains `;` into multiple
lines to help the static code analysis process to be stronger. a developer using
semicolons in his/her code can make VCS miss results.

this module only apply for python. don't use it with another languages.

to avoid false results and messing with the code when semicolon is used inside strings.
the script is using reGex validation to get all stuff inside strings and if the semicolon is a part
of a string. it will ignore it. otherwise if it's outside strings. the program gonna
split it into parts then consider then as multiple lines of code.
'''
import re

def validateLine(singleLine):
    doubleQuoteStrings = re.findall(r'\"..*\"' , singleLine)
    singleQuoteStrings = re.findall(r"\'..*\'" , singleLine)

    if len(doubleQuoteStrings) != 0:
        for singleItem in doubleQuoteStrings:
            if ";" in singleItem: return False
            else: pass

    if len(singleQuoteStrings) != 0:
        for singleItem in doubleQuoteStrings:
            if ";" in singleItem: return False
            else: pass

    return True

def semicolonParser(fileLines):
    linesList = []

    for singleLine in fileLines:
        if ";" in singleLine:
            shouldI = validateLine(singleLine=singleLine)
            if shouldI:
                realLines = singleLine.split(';')
                for singleItem in realLines:
                    linesList.append(singleItem.strip())
            else:
                linesList.append(singleLine)
        else:
            linesList.append(singleLine)

    return linesList
