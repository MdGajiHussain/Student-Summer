
choice =input("enter choice (1/2/3/4/5):")

if choice in ['1','2','3','4','5']:
    num1=float(input("enter first number:"))
    num2 = float(input("enter second number:"))

    if choice =='1':
        print("the result is:{add(num1,num2)}")
    elif choice=='2':
        print("the result is :{subtract(num1,num2)}")
    elif choice =='3':
        print("the result is:{ multiply(num1,num2)}") 
    elif choice =='4':
        print("the result is:{divide(num1,num2)}")     
    elif choice =='5':   
        print("the result is:{modulas(num1.num2)}")       
    else:
        print("invalid input.please a valid operation.")  