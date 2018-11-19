import os

def search(dir):
    filenames=os.listdir(dir)
    for filename in filenames:
        fullfilenames=os.path.join(dir,filename)
        print(fullfilenames)

search("C:/")