def main():
      dt01={}
      akey = 'x'
      print('hit enter key to quit')
      while akey !='':
            akey = input('Enter key value: ')
            if len(akey) == 0:
                done = 0
            else:
                 avalue =input('Enter value for key: ')
                 dt01[akey]=avalue
      print(' -------------------------')
      print('number of entries is: ',len(dt01))
      print('\n',dt01)
main()
