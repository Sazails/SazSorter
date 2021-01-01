import functions as func

import os as _os
import time as _time
import datetime as _dateTime

DEFAULTPATH = _os.getcwd()
RANDOMFILESPATH = DEFAULTPATH + '\\RandomFiles\\'
SORTEDFILESPATH = DEFAULTPATH + '\\SortedFiles\\'

print('Working path: {}'.format(DEFAULTPATH))
print('Random files path: {}'.format(RANDOMFILESPATH))
print('Sorted files path: {}'.format(SORTEDFILESPATH))

func.CreateDir(RANDOMFILESPATH)
func.CreateDir(SORTEDFILESPATH)

gotFiles = func.GetFilesFromDir(RANDOMFILESPATH)

for file in gotFiles:
    temp = _dateTime.datetime.fromtimestamp(
        _os.path.getctime(RANDOMFILESPATH + file))
    date = temp.strftime("%Y_%m_%d")
    func.MoveFile(RANDOMFILESPATH + file, '{}{}'.format(SORTEDFILESPATH, date))
