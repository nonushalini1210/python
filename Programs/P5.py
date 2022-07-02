def main():
    print('\n'*2)
    name=input('please enter your name: ')
    account_number=input('please enter your account number: ')
    payment_amount=input('please enter your payment amount: ')
    print('\n'*2)
    if(len(name)== 0):
        message='Name cannot be blank'
    elif(len(name)<3):
        message='Name to short'
    elif(name.isalnum()):
        message='Valid'
    else:
        message='Name must be alphabetic'
    print('Name: ',name,' ',  message)
    if(len(account_number)==0):
        message='Account number cannot be blank Message'
    elif(len(account_number)!=9):
         message=' Account number must be 9 digit'
    elif(account_number.isnumeric()):
         message='Valid'
    else:
        message='Account number must be numeric'
    print('Account Number: ',account_number,' ',message)
    if(len(payment_amount)==0):
        message='Payment cannot be blank'
    elif(not payment_amount.isnumeric()):
        message='Payment must be numeric'
    elif(int(payment_amount)==0):
        message='Payment cannot be zero'
    elif(int(payment_amount)<0):
        message='Payment cannot be negative'
    else:
        message='Valid'
    print('Payment: ',payment_amount,' ',message)


main()
