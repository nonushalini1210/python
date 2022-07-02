def spacer():
   print('Table_codes: A = add, S = subtract, M = multiple, D = divide')
   table_code=input('Select table code: ')
   number_table=float(input('Enter number for table: '))
   if (len(table_code)==0):
        print('Table Code cannot be blank')
   elif (table_code=='A'):
        print('Add')
        for a in range(1,11,1):
            print(number_table+a,' = ', number_table, ' + ',a)
   elif (table_code=='S'):
        print('subtract')
        for a in range(1,11,1):
            print(number_table-a,' = ', number_table, ' - ',a)
   elif (table_code=='M'):
        print('Multiple')
        for a in range(1,11,1):
            print(number_table*a, ' = ', number_table, ' * ',a)
   elif (table_code=='D'):
        print('Divide')
        for a in range(1,11,1):
            print(round(number_table/a, 2), ' = ', number_table, ' / ',a)
   else:
       print('invaild code')
spacer()           
       
