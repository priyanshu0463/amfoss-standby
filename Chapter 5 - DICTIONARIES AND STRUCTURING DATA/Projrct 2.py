print('Inventory:')
def displayInventory(ls):
    s=0
    for k,v in ls.items():
        print(v,k)
        s=s+v
    print('Total no. of items:',s)

ls={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(ls)

