def main():
     # set up dictionary
     dt01 = { 1: 'one',
              2: 'two',
              4: 'four'}
     print('Dictionary example')
     print(dt01)
     a = 5
     b = 'five'
     dt01[a] = b
     print(dt01)
     input('enter key to continue')
     dt01[8] = 'eight'
     print(dt01)
     input('enter key to continue')
     del dt01[8]
     print (dt01)
main()
