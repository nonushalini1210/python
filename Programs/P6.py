def spacer():
    print('Table codes: A = add, S = subtract, M = multiple, D = divide')
    table_code=input('Select table code: ')
    table_num=input('Enter number for table:')
    if(table_num.isnumeric()):
        table_num=int(table_num)
    if(len(table_code)== 0):
        table_name ='Table Code cannot be blank'
    elif(table_code == 'A'):
        table_name = 'add'
    elif(table_code == 'S'):
        table_name = 'subtract'
    elif(table_code == 'M'):
        table_name = 'multiple'
    elif(table_code == 'D'):
        table_name = 'divide'
    else:
        table_name = 'Invalid Table Code'
    print(table_name)

    if(table_code =='A') or (table_code =='S') or (table_code =='M') or (table_code =='D'):
        for a in range(1,11,1):
            print(table_num+a,' = ',table_num,' + ', a)
spacer()            

