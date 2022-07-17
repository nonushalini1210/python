def main():
     dt02={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}
     print('Dictionary example')
     print(dt02,'\n')
     print(dt02.keys(),'\n')
     print(dt02.values(),'\n')
     input('enter key to continue')
     dt99=dt02.copy()
     print('dt99 copy of dt02')
     print(dt99)
     input('enter key to continue')
     dt02.clear()
     print('dt02 is cleared')
     print(dt02)
main()

