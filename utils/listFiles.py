from os import listdir

def listFiles(dirPath):
    files = listdir(f"{dirPath}/")
    return files