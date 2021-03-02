'''
i wrote this script to secure the proceses running on the phpStarter and other stuff
it's using OS exec so any bash characters can escape from the real command leading
to code execution.

and we don't really want to be insecure when we're writing a security tool xd
'''

escapeList = [
    '`',
    '"',
    "'",
    '$',
    '(',
    ')',
    '{',
    '}',
    '&',
    ';',
    '|'
]

def validateCharacters(theString):
    for singleCharacter in theString:
        if singleCharacter in escapeList: return False
        else: pass

    return True
