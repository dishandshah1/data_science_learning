import os

def navigate(directory):
    try:
        for dirpath, dirname, filenames in os.walk(directory):
            print(dirpath,dirname,filenames)
    except Exception as e:
        print(e)
        print("invalid address")

navigate(232)
