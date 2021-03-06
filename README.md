# vulnerableCodeScanner (VCS) :dizzy:
- a Static Code Vulnerability Scanner Works On Analyzing The Code Lines To Find Insecure Functions And Supports External Scanning Modules.

Table of Contents
=================

- [What's VCS?](#whats-vcs-thinking)
- [How To Use VCS?](#how-to-use-vcs-confused)
- [What Issues VCS is Scanning?](#what-vulnerabilities-vcs-is-scanning-confused)
- [Did VCS Found a Real Issue Before?](#did-vcs-found-a-real-issue-before-huh-yawning_face)
- [Writing Your Own VCS Module](#writing-your-own-vcs-module-open_mouth)
- [What's New?](#whats-new)
- [Support VCS](#found-this-tool-helpful-heartbeat)

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
- **Most** Of VCS Scans Only Applies For Python Codes. Other Modules For Other Languages Will Be There Soon.

## What Languages VCS Can Scan?
![python](https://github.com/abranhe/programming-languages-logos/blob/master/src/python/python_32x32.png?raw=true)
![php](https://github.com/abranhe/programming-languages-logos/blob/master/src/php/php_32x32.png?raw=true)
![ruby](https://github.com/abranhe/programming-languages-logos/blob/master/src/ruby/ruby_32x32.png?raw=true)

## Did VCS Found a Real Issue Before Huh? :yawning_face:
- Yeah It Did, I Was Able To Find Arbitrary Code Execution On SimBA After Manually Checking VCS Hits. VCS Did Point That There's an Insecure YAML desearilization Happens On Code Using Unsafe Loader.

### References:
- https://github.com/418sec/huntr/pull/1959

## Writing Your Own VCS Module :open_mouth:
- In VCS, All You Need To Create Your Own Module is Two Simple Things. First Of All Let's Say You're Module Gonna Scan Python Code. That Means You Should Put Your Module Under `/modules/python/{name}.py`. And If It's Gonna Scan Other Languages Like `php`. Then You Should Place It at: `/modules/php/{name}.py`. Simple Right?

- The Second Thing Here is That You Need Create a Function Inside Your Python Code Called `vScan()` and It Should Take One Argument Called: `filePath`. When Calling Your Module From The Modules Folder. The Main Script is Calling It With The filePath The User Provided To Scan. To Aviod These Weird Stuff. I Wrote a Simple Template You Can Find On `/templates/module.py`. Go and See The Modules I Made To Get an Idea

- By Now, VCS Does Support Modules Written On PHP. All You Have Todo is Using The PHP Template On The `/templates/` Folder.

## What's New?
- PHP Modules Support
- Variables Tracker To Detect Varaibles Used On Insecure Functions
- Advanced SQL Injection Scanner With More Ways To Detect It.
- More Utils To Use Inside Your Code That Includes Variables Tracker, stringName Finder, ..etc
- Faster Scans With More Threading!
- PHP GET/POST Parameters Usage Detector Based On Regex.

## Found This Tool Helpful? :heartbeat:
- Giving it a Star :star: will be great. and i will be really thankful for that. otherwise, you can support us via the sponser links on the repository to keep VCS working and **available for public** :heart: 
