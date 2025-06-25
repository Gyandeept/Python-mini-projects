#since we have to add dishes with their prices
#so we can use dictionary and conditional statement

#Define the menu of restaurant

menu = {
   'pizza' :40,
   'pasta' :50,
   'burger' :60,
   'salad' :70,
   'coffee' :80,
}

#Greet
print("welcome to our restaurant")
print("pizza : RS 40\npasta : RS 50 \nburger : RS 60\nsalad : RS 70\ncoffee : RS 80")

order_total = 0
#0+
item_1 = input("Enter the name of your item you want to order =")
if item_1 in menu:
    order_total +=menu[item_1] #0+item_1
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available yet")

another_order =input("Do you want to add another item ? (yes/no ")
if another_order == "yes":
    item_2 =input("enter the another item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available!")
print(f"the total amount of item to pay {order_total}")    
