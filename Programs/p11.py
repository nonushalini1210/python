from datetime import date
from datetime import time
from datetime import datetime
def logpgm(cond):
    dt = datetime.today()
    dts = str(dt) + '\n'
    if cond == 0:
        ps = 'program started '+ '\n'
    else:
        ps = '\nprogram ended '+ '\n' 
    print(ps) 
    print(dts)
    return
def main():
    logpgm(0)
    print('\ngrading system\n')
    filenamein='/Users/varunmehta/Desktop/Desktop - Varun’s MacBook Air/CIS 103/Programs/points.txt'
    filenameout='/Users/varunmehta/Desktop/Desktop - Varun’s MacBook Air/CIS 103/Programs/grade.txt'
    filenameout1='/Users/varunmehta/Desktop/Desktop - Varun’s MacBook Air/CIS 103/Programs/error.txt'
    rcdcnt=0
    infile=open(filenamein,'r')
    outfile=open(filenameout,'w')
    outfile1=open(filenameout1,'w')
    line=infile.readline()
    while line !='':
        rcdcnt=rcdcnt+1
        line=line.strip()
        try:
            # print ('Record before split',line)
            (studid,name,points)=line.split(',')
            print('Id: ' +studid)
            print('Name:' +name)
            print('Points:' +points)
            points=int(points)
            if(points< 0):
                print('Points can not be negative\n')
                outfile1.write(line + ' Points can not be negative\n')
            elif(points>=900)and(points<=1000):
                grade = 'A'
                print('Grade:' +grade+'\n')
                outfile.write(line + ','+grade+'\n')
            elif(points>=800)and(points<=899):
                 grade = 'B'
                 print('Grade:' +grade+'\n')
                 outfile.write(line + ','+grade+'\n')
            elif(points>=700)and(points<=799):
                grade = 'C'
                print('Grade:' +grade+'\n')
                outfile.write(line + ','+grade+'\n')
            elif(points>=600)and(points<=699):
                grade = 'D'
                print('Grade:' +grade+'\n')
                outfile.write(line + ','+grade+'\n')
            elif(points>=0)and(points<=599):
                grade = 'F'
                print('Grade:' +grade+'\n')
                outfile.write(line + ','+grade+'\n')
            else:
                print(' Points not in range\n')
                outfile1.write(line + ' Points not in range\n')
            
        except:
            print(' Points should be number OR Data Error\n')
            outfile1.write(line + ' Points should be number OR Data Error\n')
        line = infile.readline()
    infile.close()
    outfile.close()
    outfile1.close()
    #print('\n'+ 'Number of records read: ' + str(rcdcnt))
    logpgm(1)
main()
