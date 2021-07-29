import sys

#print("All Command line arguments = ",sys.argv)
#print("type of sys.argv = ",type(sys.argv))
#print("Number of command line argement = ",len(sys.argv))

if(len(sys.argv)!=3):
    print("copy is not possible")
    print("argument mismatch, please only enter src and dest file names")
else:
    try:
        f1=open(sys.argv[1],mode="r")
    except(FileNotFoundError) as err:
        print("Source file not found")
        print("copy not possible")
        exit()
    f2=open(sys.argv[2],mode="w")

    data=f1.read()
    f2.write(data)
    print("file copied")

    f1.close()
    f2.close()

