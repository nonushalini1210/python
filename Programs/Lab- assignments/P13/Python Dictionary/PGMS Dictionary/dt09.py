def main():
     dt01={1:'one',2:'two',3:'three',  
           4:'four',7:'seven',10: 'ten'}
     print('Dictionary example')
     print(dt01)
     a=1
     while a > 0:
         a = int(input('enter a number: '))
         if a in dt01:
            print(a, ' in dictionary')
         else:
            print(a, ' not in dictionary')
main()

