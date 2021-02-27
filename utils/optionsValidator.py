from utils.showMessage import showError

def oValidator(Options):
    optionsList = {}
    callsList = []

    if Options.file != False:
        fileOption = Options.file
        optionsList['file'] = fileOption
        callsList.append("file")

    if Options.dir != False:
        dirOption = Options.dir
        optionsList['dir'] = dirOption
        callsList.append("dir")

    if Options.language != False:
        languageOption = Options.language
        optionsList['language'] = languageOption
        callsList.append("language")

    if Options.exclude != False:
        excludeOption = Options.exclude
        optionsList['exclude'] = excludeOption
        callsList.append("exclude")


    if Options.file != False and Options.dir != False:
        showError(exceptionRule="Options Error" , Message="You Can't Use Both -file and -dir. Only Use One Of Them.")
        exit()
    elif Options.file == False and Options.dir == False:
        showError(exceptionRule="Options Error" , Message="You Should Use One Of The Options -file , -dir")
    else:
        return optionsList, callsList