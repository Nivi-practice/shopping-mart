cart=[]
print("Hi sir Welcome")
print("1 for add item")
print("2 for remove item")
print("3 for update")
print("4 for view")
print("5 for search")
print("6 for slice item")
print("7 for sort item")
print("8 for exit")
choice=int(input("enter your choice:"))
if choice==1:
    item = input("Enter item to add: ")
    cart.append(item)
    print("item added to cart.")
elif choice == '2':
     item = input("Enter item to remove: ")
     if item in cart:
      cart.remove(item)
      print("item removed from cart.")
     else:
      print("item not found in cart.")
      
      

 