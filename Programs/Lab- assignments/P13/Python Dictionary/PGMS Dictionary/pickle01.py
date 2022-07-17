import pickle
set01=set([10, 20,30, 40]) 
outfile = open('c:/data6/pgmdata/picklefile.dat', 'wb')
pickle.dump(set01,outfile)
outfile.close()
