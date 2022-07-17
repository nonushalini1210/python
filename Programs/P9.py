def main():
    ans='y'
    while((ans=='y') or (ans== 'Y')):
        try:
             print('Option: T = temperture, D = distance, W = weight')
             option=input('Select option: ')
             if(option == 'D'):
                 mile=float(input('enter the distance in miles'))
                 kilometer=mile*1.6093444
                 print('distance in kilometer= ' ,kilometer)
             elif(option == 'W'):  
                 pound=float(input('enter the weight in poundss'))
                 kilogram=pound*0.45359237
                 print('weight in kilogram= ' ,kilogram)
             elif(option =='T'):
                 fahrenheit=float(input('enter the temperature in fahrenheit'))
                 celsius= (fahrenheit-32)*5/9
                 print('temperature in celsius= ' ,celsius)
             else:
                 print('Invaild code')
        except(ValueError, TypeError):
            print('DATA ERROR')
        except:
            print('unknown error')
        print('-------------------')    
        ans=input('Again y/n?')
    print('***done')
main()
      
    


