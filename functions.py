import os
import shutil


def GetFilesFromDir(chosenDir):
    """
    Returns a file/files from the chosen directory ("chosenDir")
    """
    files = os.listdir(chosenDir)
    print('Found: {}'.format(files))
    return files


def CreateDir(chosenDir):
    """ Create directory at ("chosenDir") """
    path = chosenDir
    os.makedirs(path)
    print('Created directory: {}'.format(path))


def DestroyDir(chosenDir):
    """ Destroy a directory at path ("chosenDir") """
    os.rmdir(chosenDir)
    print('Destroyed directory {}'.format(chosenDir))


def CheckDirExists(chosenDir):
    if os.path.exists(chosenDir):
        return False
    return True


def MoveFile(filePath, destinationPath):
    """ Moves a file from its ("filePath") to the ("destinationPath").
        \nDirectory will be created automatically if path doesn't exist.
     """
    if not os.path.exists(destinationPath):
        CreateDir(destinationPath)

    shutil.move(filePath, destinationPath)
    print('Moved file {} to {}'.format(filePath, destinationPath))
