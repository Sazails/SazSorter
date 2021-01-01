import os as _os
import shutil as _shutil


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
