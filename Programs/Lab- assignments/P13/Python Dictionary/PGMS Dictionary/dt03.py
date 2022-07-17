def main():
     # set up dictionary
     dt01 = { 1: 'one',
              2: 'two',
              3: 'three',
              4: 'four'}
     print('Dictionary example')
     print(dt01)
     v01 = dt01[2]
     print('Value for 2 is: ',v01)
     a=4
     v02 = dt01[a]
     print('Value for ', a, ' is: ',v02)
     print('-----------')
     for v88 in dt01:
          print(v88, ' - ',dt01[v88])
main()
