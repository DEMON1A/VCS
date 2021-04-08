# vulnerableCodeScanner (VCS) :dizzy:
- a Static Code Vulnerability Scanner Works On Analyzing The Code Lines To Find Insecure Functions And Supports External Scanning Modules.

Table of Contents
=================

- [What's VCS?](#whats-vcs-thinking)
- [How To Use VCS?](#how-to-use-vcs-confused)
- [What Issues VCS is Scanning?](#what-vulnerabilities-vcs-is-scanning-confused)
    * [Python](#python)
    * [PHP](#php)
    * [Ruby](#ruby)
    * [Nodejs](#nodejs)
- [What Languages VCS Can Scan?](#what-languages-vcs-can-scan-no_mouth)
- [Did VCS Found a Real Issue Before?](#did-vcs-found-a-real-issue-before-huh-yawning_face)
    * [References](#references)
- [Writing Your Own VCS Module](#writing-your-own-vcs-module-open_mouth)
- [What's New?](#whats-new)
- [Security](#security)
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
#### Python:
- Insecure YAML deserialization **[high]**
- Flask Enabled Debug Mode **[medium]**
- Sqlite3 SQL Injection **[high]**
- Command Injection With OS/exec **[high]**
- XML Parsing Denial Of Service **[high]**
- Django XSS With Safe Enabled **[high]**
- Hardcoded Secrets **[high]**

#### PHP:
- GET/POST Parameters Usage **[DEBUG/INFO]**
- Hardcoded Secrets **[high]**

#### Ruby:
- Insecure YAML deserialization **[high]**
- Ruby Open File Remote Code Execution **[high]**
- Hardcoded Secrets **[high]**

#### Nodejs:
- Insecure Unserlization - (node-serialization) **[high]**
- Insecure Unserlization - (funcster) **[high]**
- Hardcoded Secrets **[high]**


## What Languages VCS Can Scan? :no_mouth:
![python](https://github.com/abranhe/programming-languages-logos/blob/master/src/python/python_32x32.png?raw=true)
![php](https://github.com/abranhe/programming-languages-logos/blob/master/src/php/php_32x32.png?raw=true)
![ruby](https://github.com/abranhe/programming-languages-logos/blob/master/src/ruby/ruby_32x32.png?raw=true)
![javascript](https://github.com/abranhe/programming-languages-logos/blob/master/src/javascript/javascript_32x32.png?raw=true)

## Did VCS Found a Real Issue Before Huh? :yawning_face:
- Yeah It Did, I Was Able To Find Arbitrary Code Execution On SimBA After Manually Checking VCS Hits. VCS Did Point That There's an Insecure YAML deserialization Happens On Code Using Unsafe Loader.

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
- Insecure Yaml Deserialization Detector For Ruby Based On Regex.
- Hardcoded Secrets Finder In PHP Based On String Compare.
- Nodejs Insecure Unserlization That Leads To Code Injection. Based On ReGex.
- Nodejs stringFinder Util That Could Be Used To Track functionsObjects.
- Nodejs Inseucre Unserlization Detector On funcster Based On ReGex.
- XML Parsing DoS Detector For Python Based On Both String Comparing and ReGex.
- Django Possible XSS Detector When Safe is Used On The Template Based On ReGex.
- Faster Command Execution Scan With Less Invalid Results Based On Both String Comparing and ReGex.
- Ruby Kernal File Open Remote Code Execution Based On Both String Comparing and ReGex.
- Configurations File To Use Your Own Options That Includes Using PHP Modules and Send Discord Messages.
- Discord Notifications Support Using Webhooks To Save VCS Hits.
- Subfolders Support For Directory Option Increases The Scanning Area.

## Security
- You're responsible for the files inside your disk. code injections are possible if an attacker is able to add a malicious python/php file inside your modules folder. we can't do anything to avoid that since this's how the program is working. otherwise. VCS is using a secure functions and multiple layers of validation befoe doing anything important. and all of the tests inside the tests folder is meant to be vulnerable so VCS users can test the modules and see that they're working.

- If you believe you found a security issue on VCS feel free to contact me via the contact information on my github account. or you can open an issue on github with it.

## Found VCS Helpful? :heartbeat:
- Giving it a :star: will be great. and i will be really thankful for that. otherwise, you can support us via the sponser links on the repository to keep VCS working and **available to public** :heart:
