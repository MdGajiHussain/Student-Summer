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