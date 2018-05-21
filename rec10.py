'''

rec10.py

name: Jared Schuller


Lets go shopping
'''

import pickle

DES_SHOPPER = 'mom'
list_CHOICES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
list_DES = ["2", "3", "4", "8"]
ADD_SHOP = 1
ADD_DONT = 2
REM_SHOP = 3
REM_DONT = 4
SHOW_FOOD = 5
SHOW_SHOP = 6
SHOW_DONT = 7
PRINT = 8
QUIT = 9
CHANGE_DES = 10
ADD_FAM = 11
ADD_FOOD = 12

def loadInfo():
    listFood = []
    listFam = []
    desShop = ' '
    
    pFile = open("fileFood.pkl", 'r')
    endFile = False
    while endFile == False:
        try:
            item = pickle.load(pFile)
            listFood += [item]
        except EOFError:
            endFile = True
    pFile.close()

    listFam = []
    pFile = open("fileFam.pkl", 'r')
    endFile = False
    while endFile == False:
        try:
            item = pickle.load(pFile)
            listFam += [item]
        except EOFError:
            endFile = True
    pFile.close()

    pFile = open("fileDes.pkl", 'r')
    desShop = pickle.load(pFile)
    pFile.close()

    return listFood, listFam, desShop

def saveInfo(listFood, listFam, desShop):
     pFile = open("fileFood.pkl", 'w')
     for item in listFood:
         pickle.dump(item, pFile)
     pFile.close()

     pFile = open("fileFam.pkl", 'w')
     for item in listFam:
         pickle.dump(item, pFile)
     pFile.close()

     pFile = open("fileDes.pkl", 'w')
     pickle.dump(desShop, pFile)
     pFile.close()

def makeDontBuyLists(listFam):
    dontBuyLists = {}
    for person in listFam:
        dontBuyLists[person] = []

    return dontBuyLists

def getName(listFam):
    test = True
    while test:
        name = raw_input("Please enter your name: ")
        if name in listFam:
            print "Welcome to the shopping list system"
            test = False
        else:
            print "User not in family"
            
    return name

def checkFood(item, listFood):
    if item in listFood:
        return True
    else:
        return False

def isDes(name, desShop):
    if name == desShop:
        return True
    else:
        return False

def addItem(dontBuyLists, shopList, listFood, desShop):
    test = True
    while test:
        item = raw_input("Enter the item to add to SHOPPING LIST: ")
        if checkFood(item, listFood):
            if item in dontBuyLists[desShop]:
                print "Item is on DONT BUY LIST."
            elif item in shopList:
                print "Item already on SHOPPING LIST."
            else:
                print "Item added to SHOPPING LIST"
                test = False
        else:
            print "INVALID ITEM"

    return item

def addDont(dontBuyLists, listFood, name):
    test = True
    while test:
        item = raw_input("Enter an item to add to DONT BUY LIST: ")
        if checkFood(item, listFood):
            if item in dontBuyLists[name]:
                print "Item already in DONT BUY LIST"
            else:
                print "Item added to DONT BUY LIST"
                test = False
        else:
            print "INVALID ITEM"

    return item

def remItem(shopList, listFood):
    test = True
    while test:
        item = raw_input("Enter the item to remove from SHOPPING LIST: ")
        if checkFood(item, listFood):
            if item in shopList:
                print "Item removed from SHOPPING LIST:"
                test = False
            else:
                print "Item is not in SHOPPING LIST"
        else:
            print "INVALID ITEM"

    return item

def remDont(dontBuyLists, listFood, name):
    test = True
    while test:
        item = raw_input("Enter the item to remove from DON'T BUY LIST: ")
        if checkFood(item, listFood):
            if item in dontBuyLists[name]:
                print "Item removed from DON'T BUY LIST"
                test = False
            else:
                print "Item is not in DON'T BUY LIST"
        else:
            print "INVALID ITEM"

    return item

def changeDes( listFam ):
    test = True
    while test:
        item = raw_input("Enter new designated shopper: ")
        if item in listFam:
            print item, "is new designated shopper."
            test = False
        else:
            print "invalid entry"
    return item

def addFam( listFam):
    test = True
    while test:
        item = raw_input("Enter new family member: ")
        if item in listFam:
            print "Person already in family"
        else:
            print item, "added to family"
            test = False
    return item

def addFood(listFood):
    test = True
    while test:
        item = raw_input("Enter new food item: ")
        if item in listFood:
            print "Item alread in food list"
        else:
            print item, "added to food list"
            test = False
    return item
        

def printList(shopList, dontBuyLists, name):
    for i in shopList:
        if i not in dontBuyLists[name]:
            print i

def dispMenu(choiceList, name, desShop):
    test = True
    while test:
        print '''Choose an option:
            1. Add a food item to SHOPPING LIST
            2. Add a food item to DON'T BUY LIST
            3. Remove item from SHOPPING LIST
            4. Remove item from DON'T BUY LIST
            5. Display a list of all foods
            6. View SHOPPING LIST
            7. View DON'T BUY LIST
            8. Print SHOPPING LIST and quit.
            9. Restart
            10. Change Designated Shopper.
            11. add family member
            12. add food item
            '''

        choice = raw_input("Enter your choice :")
        if choice in choiceList:
            if choice in list_DES:
                if isDes(name, desShop) == True:
                    test = False
                else:
                    print "You don't have authorization for this choice"
            elif choice == '10':
                if name == 'mom':
                    test = False
                else:
                    print "You must be Mom to select this choice"
            else:
                test = False
        else:
            print "NOT VALID CHOICE"
            
    return int(choice)
        
def calcMenu(choice, shopList, dontBuyLists, listFood, listFam, desShop, name):
    out = 0
    
    if choice == ADD_SHOP:
        shopList += [addItem(dontBuyLists, shopList, listFood, desShop)]

    elif choice == ADD_DONT:
        dontBuyLists[name] += [addDont(dontBuyLists, listFood, name)]

    elif choice == REM_SHOP:
        shopList.remove(remItem(shopList, listFood))

    elif choice == REM_DONT:
        dontBuyLists[name].remove(remDont(dontBuyLists, listFood, name))

    elif choice == SHOW_FOOD:
        print"======FOOD LIST======="
        print listFood
        print"======FOOD LIST======="

    elif choice == SHOW_SHOP:
        print"======SHOPPING LIST======="
        print shopList
        print"======SHOPPING LIST======="

    elif choice == SHOW_DONT:
        print"======DON'T BUY LIST======="
        print dontBuyLists[name]
        print"======DON'T BUY LIST======="

    elif choice == PRINT:
        printList(shopList, dontBuyLists, name)
        out = 1
    elif choice == QUIT:
        out = 2
        
    elif choice == CHANGE_DES:
        desShop = changeDes(listFam)

    elif choice == ADD_FAM:
        listFam += [addFam(listFam)]

    elif choice == ADD_FOOD:
        listFood += [addFood(listFood)]

    return out, desShop, listFam, listFood


def main():
    list_dontBuy = []
    list_shop = []

    listFood, listFam, desShop = loadInfo()
    dontBuyLists = makeDontBuyLists(listFam)
    name = getName(listFam)
    test = True
    while test:
        out, desShop, listFam, listFood = calcMenu(dispMenu(list_CHOICES, name, desShop), list_shop, dontBuyLists, listFood, listFam, desShop, name)
        if out == 1:
            test = False
        elif out == 2:
            name = getName(listFam)
    saveInfo(listFood, listFam, desShop)

main()
