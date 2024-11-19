inventory=[
    ('laptop',5, 30000),
    ('headphone',15,500),
    ('mouse',50,150),
    ('keyboard',20,150),
    ('monitor',5,3000)
    ]
higheststockvalue=0
itemwithhigheststockvalue=None
for item in inventory:
    itemname,quantity,unitprice=item
    stockvalue=quantity*unitprice
    print('the total value of item is',stockvalue)
    print(itemname,quantity,unitprice)
    if stockvalue>higheststockvalue:
        higheststockvalue=stockvalue
        itemwithhigheststockvalue=itemname
    print('highest stock value is:',higheststockvalue)
    print('item with highest stock value is:',itemwithhigheststockvalue)


