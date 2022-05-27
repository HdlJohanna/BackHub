import os,sys,shutil

def getDiskSpace(path:os.PathLike="/"):
    return shutil.disk_usage(path)

def backup(src:os.PathLike,dest:os.PathLike):
    try:
        if os.path.exists(dest):
            recursivelyRenameAllFiles(dest)
        shutil.copytree(src,dest)
        return len(os.listdir(dest))
    except Exception as ex:
        return ex

    

def recursivelyRenameAllFiles(src):
    for root,dir,file in os.walk(src):
        print(root,dir,file)
        try:
            os.rename(dir,getFileNameWithoutOverwriting(dir))
        except:
            pass
        try:
            os.rename(file,getFileNameWithoutOverwriting(file))
        except:
            pass
        
def getFileNameWithoutOverwriting(__name):
    return __name+"_"
