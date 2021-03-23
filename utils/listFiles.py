from os import scandir

def listFiles(dirPath):
    pathsList = []
    dirsList = []

    filesList = scandir(f"{dirPath}/")
    for singleFile in filesList:
        if singleFile.is_dir() == True:
            dirsList.append(singleFile.path)
        else:
            pathsList.append(singleFile.path)

    while len(dirsList) != 0:
        for singleDir in dirsList:
            filesList = scandir(f"{singleDir}")
            for singleFile in filesList:
                if singleFile.is_dir() == True:
                    dirsList.append(singleFile.path)
                else:
                    pathsList.append(singleFile.path)

            dirsList.remove(singleDir)

    return pathsList
