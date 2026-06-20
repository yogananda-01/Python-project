n1=int(input('enter the first number: ' ))
n2=int(input('enter the Second number: ' ))
print('The options are : ')
print('1.Addition')
print('2.Subraction')
print('3.Multiplication')
print('4.Dicision')
ch=int(input('Enter your choice form (1-4): '))
if ch==1:
    print("The addition of two numbers are: ",n1+n2)
elif ch==2:
    print("The subraction of two numbers are: ",n1-n2)
elif ch==3:
    print("The multiplication of two numbers are: ",n1*n2)
elif ch==4:
    print("The division of two numbers are: ",n1/n2)
else:
    print('Invalid choice')
