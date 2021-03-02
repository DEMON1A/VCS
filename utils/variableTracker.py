'''
this function is used with scan modules to detect external variables used
on functions. you can always use this function inside your scan module
'''

def Tracker(nameString , fileLines):
    linesList = []

    for singleLine in fileLines:
        singleLine = singleLine.rstrip('\n')

        if f"{nameString}=" in singleLine.replace(' ' , ''):
            linesList.append(singleLine)

    return linesList
