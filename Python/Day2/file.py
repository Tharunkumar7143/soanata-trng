def myfile():
    try:
        c=open("tharun.txt.txt", 'r')
        print(c.read())
    except(FileNotFoundError):
        return "not exists"
f=myfile()
print(f)