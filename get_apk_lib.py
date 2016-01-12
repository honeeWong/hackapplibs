'''
TOOLS: tools for get apks lib.
AUTOR: why
DATA : 20160109
'''
import os
import sys
import shutil

'''
    MODIFY IT FOR YOU PATH
'''
RAR_CMD = 'D://progra~1/WinRAR/winrar.exe'
PATH = 'D://py_tools/get_apk_lib/apk'
LIBPATH = 'D://py_tools/get_apk_lib/lib'

'''
    MAIN FUNCTION
'''
def rename(dirname = PATH):    
    listFile = os.listdir(dirname)    
    print(listFile)
    for file in listFile:
        filename = os.path.splitext(file)
        if(filename[1] == '.apk'):
            name = filename[0] + '.zip'
            print(name)
            os.rename(os.path.join(dirname, file),os.path.join(dirname,name))
    
    
def unzip(dirname = PATH,cmd = RAR_CMD):
    listFile = os.listdir(dirname)
    CMD = cmd + ' x {} {}'
    os.chdir(dirname)
    for file in listFile:
        filename = os.path.splitext(file)
        if(filename[1] == '.zip'):
            rarCmd = CMD.format(file,(filename[0]+os.sep))
            print(rarCmd)
            os.system(rarCmd)

def restname(dirname = PATH):    
    listFile = os.listdir(dirname)
    for file in listFile:
        filename = os.path.splitext(file)
        if(filename[1] == '.zip'):
            name = filename[0] + '.apk'
            print(name)
            os.rename(os.path.join(dirname, file),os.path.join(dirname,name))      
    
def findlib(dirname = PATH):
    listFile = os.listdir(dirname)   
    libdir = dirname + os.sep + 'alllib'
    if not os.path.exists(libdir):
        os.mkdir(libdir)
    for file in listFile:          
        fulldirfile=os.path.join(os.path.abspath(dirname),file)
        if os.path.isdir(fulldirfile):
            #print(file + ' is path')
            os.chdir(fulldirfile)
            if os.path.exists('lib'):
                print(file + ' have lib')
                directdir = '../alllib/{}_lib'.format(file)
                shutil.move('lib',directdir)
            os.chdir('..')
            try:
                shutil.rmtree(fulldirfile)
            except:
                pass
            
def sort(dirname = PATH):
    libdir = dirname + os.sep + 'alllib'
    os.chdir(libdir)
    libfolderlist = os.listdir(libdir)
    for folder in libfolderlist:
        fulldirfile = os.path.join(libdir,folder)
        print("APK NAME: ",fulldirfile)
        os.chdir(fulldirfile)
        listlib = os.listdir(fulldirfile)
        for libfolder in listlib:
            print('HAVE LIB FOLDER: ',libfolder)
            if not (libfolder == 'x86' and libfolder == 'x64'):
                rootlib = os.path.join(fulldirfile,libfolder)
                os.chdir(rootlib)
                alllib = os.listdir(rootlib) 
                for lib in alllib:
                    srclibname = os.path.join(rootlib,lib)
                    #print(srclibname)
                    tarlibname = os.path.join(LIBPATH,lib)
                    print('USERFUL LIB: ',srclibname)
                    #print(tarlibname)
                    shutil.copy(srclibname,tarlibname)
    print("all lib will be copy to lib folder ,\
    if you want to find the base lib ,please into 'apk/alllib'")
                
                
            
            
def main():
    
    '''
        something for extend
    '''
    '''
    if not os.path.exists(RAR_CMD):
        print("winrar.exe is not exists, please input rar path likes: 'c://Progra~1/WinRAR/winrar' \n")        
        cmd = input('rar path: ')
        if not os.path.exists(cmd):
            print('input error rar path exit !')
            exit()
            
    print("please input apk file absoult path likes: 'D://apk'")
    path = input("apk path: ")
    if not os.path.exists(path):
        print('input error apk path exit !')
        exit()
    '''    
    path = PATH
    rename(path)
    unzip(path)
    findlib(path)
    restname(path)
    sort(path)    
    anykey = input("Sucessful ! please input Enter key to exit!")
    if anykey:    
        print('quit')
        exit()
        
    
if __name__ == '__main__':
    main()