#coding=utf-8
with open("temp.txt",encoding="utf-8") as f:
    for i in f.readlines():
        i=i.rstrip("\n").split(" 	")[0]
        i=i.replace("-","_")
        #i="def "+i+"(url):\n"+"    "+"headers = {'User-Agent': get_user_agent()}"
        print(i+"(url)")
f.close()
