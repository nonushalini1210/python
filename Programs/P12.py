def main():
    filenamein='/Users/varunmehta/Desktop/Desktop - Varun’s MacBook Air/CIS 103/Programs/rainfall.txt'
    infile=open(filenamein,'r')
    line=infile.readline()
    rcdcnt=0
    month_list = []
    rainfall_list = []
    while line !='':
        rcdcnt=rcdcnt+1
        line=line.strip()
        try:
            # print ('Record before split',line)
            (month,rainfall)=line.split(':')
            #print('month: ' +month)
            #print('rainfall amount:' +rainfall)
            month_list.append(month)
            rainfall_list.append(float(rainfall))
            
            
        except:
            print(' rainfall should be number OR Data Error\n')
        line = infile.readline()
    print('Rainfall for Chicago (2017):\n')
    for x in range(0,len(month_list),1):
        print(month_list[x], ':  ', rainfall_list[x])
    highest = max(rainfall_list)
    highest_index=rainfall_list.index(highest)
    highest_month =month_list[highest_index]
    lowest =min(rainfall_list)
    lowest_index=rainfall_list.index(lowest)
    lowest_month=month_list[lowest_index]
    total =sum(rainfall_list)
    average =total/len(rainfall_list)
    print('\nHighest: ', highest_month ,' ', highest)
    print('Lowest: ' ,lowest_month ,' ', lowest)
    print('Total: ',round(total,2))
    print('Average: ',round(average,2))
    
main()
