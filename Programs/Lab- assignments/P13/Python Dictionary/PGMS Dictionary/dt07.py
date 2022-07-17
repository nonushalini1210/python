def test1():
     dt01={1:'one',2:'two',4:'four'}
     print('Dictionary example')
     print(dt01)
     del dt01[8]
     print (dt01)     
def test2():
     a= 8
     dt01={1:'one',2:'two',4:'four'}
     print('Dictionary example')
     print(dt01)
     try:
         del dt01[a]
     except:
          print('Key: ',a,' not found in dictionary')
     print (dt01)     
def main():
     test1()
     test2()
main()
