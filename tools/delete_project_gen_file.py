import os
import shutil


class DeleteFile:

    def __init__(self):
        print("_init_")
        # os.chdir("C:\\zdnuist\\loocha_git_ws\\Campus")

    
    def deleteFile(self, path):
        if os.path.isfile(path):
            if path.find(".classpath") != -1 or path.find(".project") != -1 :
                print(path)
                try:
                    os.remove(path)
                except:
                    print("error")
            
        else:
            if path.find(".settings") != -1 :
                shutil.rmtree(path)
            else:
                self.listFile(path)

    def listFile(self, rootdir):
        list = os.listdir(rootdir)
        for i in range(0, len(list)) : 
            path = os.path.join(rootdir ,list[i])
            self.deleteFile(path)

if __name__=='__main__':
    deleteFile = DeleteFile()
    deleteFile.listFile("C:\\zdnuist\\loocha_git_ws\\Campus")







