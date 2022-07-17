import pickle
def main():
    infile1=open('c:/data6/pgmdata/pk2file.dat','rb')
    set02=pickle.load(infile1)
    print('set02: ',set02)
    infile1.close()
main()
