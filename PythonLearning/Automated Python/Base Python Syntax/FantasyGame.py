import pprint

def printInv(inv):
    print('Inventory:')
    total=0
    for x,y in inv.items():
        print(x,y)#str(x)+' '+str(y))
        total+=y
    print('\nTotal number of items: '+str(total))

inventory={'rope':1,'torch':6,'gold coin':42, 'dagger':1,'arrow':12}
printInv(inventory)
