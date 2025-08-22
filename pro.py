# items=['apple','orange','banana','mango','jackfruit']
# for i in items:
#     print(i)
# item = [
#     {'name': 'apple', 'quantity': 10, 'price': 500},
#     {'name': 'orange', 'quantity': 8, 'price': 400}]
# for data in item:
#     name=data['name']
#     quantity=data['quantity']
#     price=data['price']
#     print(f"name:{name},quantity:{quantity},price:{price}") 

# item=[]
# newitem=int(input("number of items:"))
# for i in range(newitem):
#  itemname=input("enter name of item:")
#  itemquantity=int(input("enter the quantity:"))
#  itemprice=int(input("enter the price:"))
#  item.append({'name':itemname,'quantity':itemquantity,'price':itemprice})
# for items in item:
#  name=items['name']
#  quantity=items['quantity']
#  price=items['price']
#  print(f"name: {name}, quantity: {quantity}, price: {price}")



item=[]
newitem=int(input("number of items:"))
for i in range(newitem):
  itemname=input("enter name of item:")
  itemquantity=int(input("enter the quantity:"))
  itemprice=int(input("enter the price:"))
  if itemprice>50:
   discount=itemprice*0.1
   itemprice -= discount
  else:
   itemprice +=10
  item.append({'name':itemname,'quantity':itemquantity,'price':itemprice})
print(item)
