import pickle
def main():
    set01 = set([2,4,6,8,10,12,14,16,18,20,22,24,26])
    print('set01: ',set01)
    outfile1 =  open('c:/data6/pgmdata/pk2file.dat', 'wb')
    pickle.dump(set01,outfile1)
    outfile1.close()
main()
