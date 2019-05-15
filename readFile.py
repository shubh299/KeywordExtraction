
def readFile(filePath):
    fileObj = open(filePath,"r")
    if fileObj.mode == "r":
        return fileObj.read()