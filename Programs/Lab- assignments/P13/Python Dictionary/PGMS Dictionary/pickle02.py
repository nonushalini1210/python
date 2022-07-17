import pickle
infile1 = open('c:/data6/pgmdata/picklefile.dat', 'rb')
set1 = pickle.load(infile1)
print(set1)
infile1.close()
