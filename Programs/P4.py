def main():
    no_of_pounds=float(input('enter pounds to purchase'))
    if (no_of_pounds>=10) and (no_of_pounds<=99.99):
        discount = no_of_pounds * .10 
    elif (no_of_pounds>=100) and (no_of_pounds<=999.99):
        discount = no_of_pounds * .20
    elif (no_of_pounds>=1000) and (no_of_pounds<=9999.99):
         discount = no_of_pounds * .30
    elif (no_of_pounds>=10000):
        discount = no_of_pounds * .40
    else:
        discount = 0
    
    gross_sales = no_of_pounds * .99
    total_sales = gross_sales - discount

    print('number of pounds purchased =', no_of_pounds)
    print('gross sales=',gross_sales)
    print('discount=',discount)
    print('total sales=',total_sales)
    
main()
    
    
