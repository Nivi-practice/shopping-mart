items=['apple','orange','banana','mango','jackfruit']
print(items)
print(items[1])
print(items[0:3])
items.append("papaya")
print(items)
if "banana" in items:
    print("banana found")
else:
    print("not found")
fruit=input("enter the fruit")
if fruit in items:
    print("found")
else:
    items.append(fruit)
print(items)

while(1):
 print("1.add 2.view 3.exit")
choice=input("enter your choice:")
if choice==1:
    item=input("enter item to be added")
    items.append("item")
elif choice==2:
    print(items)
elif choice==3:
    print("exiting...")
else:
     print("invalid")

