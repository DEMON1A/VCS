# vulnerableCodeScanner (VCS) :dizzy:
- a Static Code Vulnerability Scanner Works On Analyzing The Code Lines To Find Insecure Functions And Supports External Scanning Modules.

## What's VCS? :thinking:
- VCS is a Simple Code-Analysis Tool Works On Scanning Every Single Line Of Code On Files And Compare The Code Functions With Vulnerable Cases Using Both **( String Comparing And ReGex )**. Then Show The Issue/Injection-Point To The User With Cool Logging System. It Also Supports External Scan Modules Written In Python. You're Able To Right Your Own Scanning Module And You're Free To Use All Python Modules Inside Of It. 

## How To Use VCS? :confused:
- VCS Doesn't Have a Lot Of Options. But Here's The Available Tool Options

```
-f , --file: a Single File That Contains The Code You Want To Scan
-d , --dir: a Hall Folder That Contains The Code You Want To Scan
-l , --language: The Language The Code Written In and There's a Tool Module For It
-x , --exclude: Exclude a Scan Script -- Comming Soon --
```
- For Basic Usage. Just Use This Commnand:
```
python3 vCode.py -f code.py
```

## What Vulnerabilities VCS is Scanning? :confused:
- in The Current Time. VCS is Scanning Only The Following Issues
```
Insecure YAML desearilization
Flask Enabled Debug Mode
Sqlite3 SQL Injection
Command Injection With OS/exec
```

- It Will Be More Scans Soon. We Still Need To Write More Modules.

## Did VCS Found a Real Issue Before Huh? :yawning_face:
- Yeah It Did, I Was Able To Find Arbitrary Code Execution On SimBA After Manually Checking VCS Hits. VCS Did Point That There's an Insecure YAML desearilization Happens On Code Using Unsafe Loader.

![result](https://i.imgur.com/vqPDbe0.png)

### References:
- https://github.com/418sec/huntr/pull/1959

## Writing Your Own VCS Module :open_mouth:
- In VCS, All You Need To Create Your Own Module is Two Simple Things. First Of All Let's Say You're Module Gonna Scan Python Code. That Means You Should Put Your Module Under `/modules/python/{name}.py`. And If It's Gonna Scan Other Languages Like `php`. Then You Should Place It at: `/modules/php/{name}.py`. Simple Right?

- The Second Thing Here is That You Need Create a Function Inside Your Python Code Called `vScan()` and It Should Take One Argument Called: `filePath`. When Calling Your Module From The Modules Folder. The Main Script is Calling It With The filePath The User Provided To Scan. To Aviod These Weird Stuff. I Wrote a Simple Template You Can Find On `/templates/module.py`. Go and See The Modules I Made To Get an Idea

```python
'''
:import any python module you want.
'''

detectVariables = [
    '',
    ''
]

blockedVariables = ['']
linesCount = 0

from utils.showIssue import showIssue

def vScan(filePath):
    global linesCount

    fileLines = open(filePath , 'r').readlines()
    for singleLine in fileLines:
        linesCount += 1
        singleLine = singleLine.rstrip('\n')

        '''
        your scan code here
        '''

    linesCount = 0
```

## Found This Tool Helpful? :heartbeat:
- Giving it a Star :star: Will Be Great. And I Will Be Really Thankful For That. 
