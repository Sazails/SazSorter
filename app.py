import functions as func

import os
import time
import datetime

DEFAULTPATH = os.getcwd()
RANDOMFILESPATH = DEFAULTPATH + '\\RandomFiles\\'
SORTEDFILESPATH = DEFAULTPATH + '\\SortedFiles\\'

print('Working path: {}'.format(DEFAULTPATH))
print('Random files path: {}'.format(RANDOMFILESPATH))
print('Sorted files path: {}'.format(SORTEDFILESPATH))

gotFiles = func.GetFilesFromDir(RANDOMFILESPATH)

for file in gotFiles:
    #data = time.ctime(os.path.getctime(RANDOMFILESPATH + file))
    temp = datetime.datetime.fromtimestamp(
        os.path.getctime(RANDOMFILESPATH + file))
    date = temp.strftime("%Y_%m_%d")
    func.MoveFile(RANDOMFILESPATH + file,
                  '{}{}'.format(SORTEDFILESPATH, date))
