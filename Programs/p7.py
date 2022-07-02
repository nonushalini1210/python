def main():
    x=5
    ans='y'
    print('calorie calculation')

    while((ans=='y') or (ans== 'Y')):
        x=5
        print('-------------------')
        running_time=int(input('Enter running time in minutes'))
        if(running_time<5):
           print('time must be greater than 5 minutes')
        else:
            while(x<=running_time):
                print('Minutes: ', x ,' burns ', 4.9 * x,' calories ')
                x=x+5
        print('-------------------')    
        ans=input('Again y/n?')
    print('***done')

main()
