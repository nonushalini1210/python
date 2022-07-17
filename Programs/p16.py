import sys
sys.setrecursionlimit(5000)
def Sum(n):
    if n == 1:
        return n
    else:
        return n + Sum(n-1)
def main():
    ans = 'y'
    while(ans == 'y'):
        try:
            numb=input('\nenter number: ')
            if(len(numb)>0):
                numb = int(numb)
                if numb < 0:
                    print('number cannot be negative')
                else:
                    a = Sum(numb)
                    print('Sum is:',a)
            else:
                print('number cannot be blank')
            
        except:
            print('Invalid input detected.')
        print('--------------')
        ans = input('Another number (y/n): ')
        
main()
