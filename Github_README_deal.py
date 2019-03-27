# coding=utf-8
import os

def re_README(file):
    f = open(file, encoding="utf-8")
    urls = []
    for i in f.readlines():
        i = i.strip("\n").strip("  ")
        i = i + "  " + "\n"
        urls.append(i)
    f.close()

    with open(file, "w+", encoding="utf-8") as f:
        for i in urls:
            f.write(i)
    f.close()
def list_file(dir_name):
    files=os.listdir(dir_name)
    new_file=os.path.abspath(dir_name)
    for file in files:
        file=new_file+"\\"+file
        if os.path.isdir(file):
            list_file(file)
            #print(file)
        elif "README.md" in file:
            print(file)
            re_README(file)

dir_name=os.path.dirname(__file__)
print(dir_name)
list_file(dir_name)



