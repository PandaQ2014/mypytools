import os
import json
from PIL import Image
import random,string

def setwallpapermain():
    configfile = open('./config/config.json',encoding='utf-8')
    config = json.loads(configfile.read())
    cachepath = config['path']
    threshold = config['threshold']
    wallpaperPath = config['wallpaper']
    wallpaperBlurPath = config['wallpaperBlur']
    print (cachepath)
    datafiles = os.listdir(cachepath)
    for datafile in datafiles:
        temppath = os.path.join(cachepath,datafile)
        if not os.path.isdir(temppath):
            if(isWallpaper(temppath)):
                if(isWallpaperBlur(temppath,threshold)):
                   replaceWallpaperBlur(temppath,wallpaperBlurPath)
                else:
                    replaceWallpaper(temppath,wallpaperPath)
                    

def isWallpaperBlur(filepath,th):
    filesize = os.path.getsize(filepath)
    filesize = filesize/float(1024)
    if(filesize < th):
        return True
    else:
        return False

def replaceWallpaperBlur(filepath,wallpaperBlurPath):
    size = os.path.getsize(filepath)
    newsize = os.path.getsize(wallpaperBlurPath)
    os.remove(filepath)
    newfile = open(filepath,'xb')
    sourcefile = open(wallpaperBlurPath,'rb')
    if(newsize < size):
        buf = sourcefile.read(newsize)
        newfile.write(buf)
        length = size - newsize
        randomstr = getStr(length)
        newfile.write(bytes(randomstr,encoding='ascii'))
    else:
        buf = sourcefile.read(newsize)
        newfile.write(buf)
    newfile.close()
    sourcefile.close()
def getStr(length):
    temp = ''
    for i in range(length):
        temp = temp + 'A'
    return temp

def replaceWallpaper(filepath,wallpaperPath):
    size = os.path.getsize(filepath)
    newsize = os.path.getsize(wallpaperPath)
    os.remove(filepath)
    newfile = open(filepath,'xb')
    sourcefile = open(wallpaperPath,'rb')
    if(newsize < size):
        buf = sourcefile.read(newsize)
        newfile.write(buf)
        length = size - newsize
        randomstr = getStr(length)
        newfile.write(bytes(randomstr,encoding='ascii'))
    else:
        buf = sourcefile.read(newsize)
        newfile.write(buf)
    newfile.close()
    sourcefile.close()
def isWallpaper(filepath):
    try:
        img = Image.open(filepath)
    except Exception as err:
        print(err)
        return False
    w , h = img.size
    if(w==1920 and h==1280):
        return True
    else:
        return False





if __name__=='__main__':
    setwallpapermain()