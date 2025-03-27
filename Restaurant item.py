Gaji = {  
    "pizza":40,
    "pasta":50,
    "burger":60,
    "salad":70,
    "coffee":80,
}

#Greet
print("welcom to PYTHON Restaurant")
print("prizze:Rs40\npasta: Rs50\nbueger: Rs60\nsalad: Rs70\ncoffee: Rs80")

order_total = 0

item_1 = input("Enter the name of item you to order =")
if item_1 in Gaji:
    order_total +=Gaji[item_1]   #0+50
    print(f"your item {item_1} has been added to your order")

else:
    print(f"ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (yas/No)") 
if another_order =="yas":
    item_2 = input("Enter the name of second item = ")
    if item_2 in Gaji:
        order_total += Gaji[item_2] 
        print(f"item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available!") 

print(f"The total amount of items is to pay {order_total}")                




##CALCULATOR

# def add(a,b):
#     return a+b

# def subtract (a,b):
#     return a-b

# def multipiy(a,b):
#     return a*b

# def divide(a,b):
#     if b!=0:
#         return a/b
#     else:
#         return"Error! Division by zero"    

# def modulas(a,b):
#     return a%b

# def calculater():
#     print("welcome to the python calculater!")
#     print("select operation:")
#     print("1.add")
#     print("2.subtract")
#     print("3.multipiy")
#     print("4.divide")
#     print("5.modulas")
    



###GET USING INPUT(2)

# choice =input("enter choice (1/2/3/4/5):")

# if choice in ['1','2','3','4','5']:
#     num1=float(input("enter first number:"))
#     num2 = float(input("enter second number:"))

#     if choice =='1':
#         print("the result is:{add(num1,num2)}")
#     elif choice=='2':
#         print("the result is :{subtract(num1,num2)}")
#     elif choice =='3':
#         print("the result is:{ multiply(num1,num2)}") 
#     elif choice =='4':
#         print("the result is:{divide(num1,num2)}")     
#     elif choice =='5':   
#         print("the result is:{modulas(num1.num2)}")       
#     else:
#         print("invalid input.please a valid operation.")    




### PROJECT (3)-> Game

# import random

# target=random.randint(1,100)

# while True:
#     userchoice =input("Guess targer or Quit(Q):")
#     if(userchoice=="Q"):
#         break

#     userchoice =int(userchoice)
#     if(userchoice==target):
#         print("success: correct Guess!!")
#         break

#     elif(userchoice<target):
#         print("your number was too small. Take a bigger guess..")
#     else: 
#         print("your number was too big .Target a smaller guess..")
# print("-----GAME OVER-----")           

    

### PROJECT(4)->Password

# import random
# import string

# pass_len=8
# charvalues=string.ascii_letters+string.digits+string.punctuation

# password=""
# for i in range(pass_len):
#     password+=random.choice(charvalues)

# print("your random password is: ",password)    