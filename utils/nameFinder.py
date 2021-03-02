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
