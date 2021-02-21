import os as _os
import time as _time
import shutil as _shutil
import datetime as _dateTime

def GetFilesFromDir(chosenDir):
    """ Returns a file/files from the chosen directory. """
    files = _os.listdir(chosenDir)
    for f in files:
        print('Found: {}'.format(f))
    return files


def CreateDir(chosenDir):
    """ Create directory at a chosen directory. """
    if _os.path.exists(chosenDir):
        print('Directory: {} already exists!'.format(chosenDir))
        return
    path = chosenDir
    _os.makedirs(path)
    print('Created directory: {}'.format(path))


def DestroyDir(chosenDir):
    """ Destroy a directory at a chosen directory. """
    _os.rmdir(chosenDir)
    print('Destroyed directory: {}'.format(chosenDir))


def CheckDirExists(chosenDir):
    if _os.path.exists(chosenDir):
        return False
    return True


def MoveFile(filePath, destinationPath):
    """ Moves a file from its ("filePath") to the ("destinationPath").
        Directory will be created automatically if path doesn't exist. """
    if not _os.path.exists(destinationPath):
        CreateDir(destinationPath)

    _shutil.move(filePath, destinationPath)
    print('Moved file "{}" to "{}"'.format(filePath, destinationPath))


DEFAULTPATH = _os.getcwd()
RANDOMFILESPATH = DEFAULTPATH + '\\RandomFiles\\'
SORTEDFILESPATH = DEFAULTPATH + '\\SortedFiles\\'

print('Working path: {}'.format(DEFAULTPATH))
print('Random files path: {}'.format(RANDOMFILESPATH))
print('Sorted files path: {}'.format(SORTEDFILESPATH))

CreateDir(RANDOMFILESPATH)
CreateDir(SORTEDFILESPATH)

gotFiles = GetFilesFromDir(RANDOMFILESPATH)

for file in gotFiles:
    temp = _dateTime.datetime.fromtimestamp(
        _os.path.getctime(RANDOMFILESPATH + file))
    date = temp.strftime("%Y_%m_%d")
    MoveFile(RANDOMFILESPATH + file, '{}{}'.format(SORTEDFILESPATH, date))

input("Press Enter to exit...")
