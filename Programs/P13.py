def main():
    # set up dictionary
    dt01 = { 1: 'I',
             2: 'II',
             3: 'III',
             4: 'IV',
             5: 'V',
             6: 'VI',
             7: 'VII',
             8: 'VIII',
             9: 'IX',
             10: 'X',
             11: 'XI',
             12: 'XII',
             13: 'XIII',
             14: 'XIV',
             15: 'XV',
             16: 'XVI',
             17: 'XVII',
             18: 'XVIII',
             19: 'XIX',
             20: 'XX',
             21: 'XXI',
             22: 'XXII',
             23: 'XXIII',
             24: 'XXIV'}             
    print('\nDictionary Table')
    print(dt01)
    ans=input('want to add to dictionary (yes/no)')
    while (ans=='yes' or ans=='y'):
        try:
            key=int(input('enter key value:'))
            value=input('enter roman value for key:')
            if (key<=0):
                break
            else:
                dt01[key]=value
        except:
            print('number must be integer, positive and greater than zero')
        ans=input('\nwant to add again (yes/no)')
    print('\nDictionary Table')
    print(dt01)
    ans='yes'
    while (ans=='yes' or ans=='y'):
        try:
            number=int(input('enter any number:'))
            if (number>0):
                if  number in dt01:
                    print('roman number equivalent is:',dt01[number])
                else:
                    print('number not found')
            else:
                print('number must be integer, positive and greater than zero')
        except:
            print('number must be integer, positive and greater than zero')
        ans=input('\nlook up another number (yes/no):')

main()
