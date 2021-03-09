'''
this util script is used with the variables tracker to detect the variable
name so the tracker can find it inside the code. i did build it using basic
replace functions.
'''

def nameStringFinder(reGexResults):
    for singleCharacter in reGexResults:
        if singleCharacter != "(":
            reGexResults = reGexResults[1:]
        else:
            break

    nameString = reGexResults.replace('(' , '').replace(')' , '')
    return nameString

def nodejsStringFinder(reGexResults):
    reGexResults = reGexResults.replace('var ' , '')
    reGexResults = reGexResults.split('=')[0]
    reGexResults = reGexResults.strip()

    return reGexResults
