def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i]=inventory[i]+1
        else:
            inventory[i]=1
    return inventory
    
print('Inventory:')

def displayInventory(ls):
    s=0
    for k,v in ls.items():
        print(v,k)
        s=s+v
    print('Total no. of items:',s)
            
    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
