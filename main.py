
import datetime

def menuDisplay():
    print('=============================')
    print('= Inventory Management Menu =')
    print('=============================')
    print('(1) Update Inventory')
    print('(2) Search Item in Inventory')  
    print('(3) Print Inventory Report')
    print('(4) Quit')
    CHOICE = int(input("Enter choice: "))
    menuSelection(CHOICE)

def menuSelection(CHOICE):
    if CHOICE == 1:
        updateInventory()
        menuDisplay()
    elif CHOICE == 2:
        searchInventory()
        menuDisplay()
    elif CHOICE == 3:
        printInventory()
        menuDisplay()
    elif CHOICE == 4:
        exit()

def hospital(index,item_description,item_quantity):
    item_quantity = item_quantity[1:]
    list = open('hospital.txt', 'r').readlines()
    list[index] = list[index].strip().split(",")
    if item_description == 'HC':
        list[index][2] = str(int(list[index][2]) + int(item_quantity))
        list[index] = ",".join(list[index])
        list[index] = list[index] + "\n"
    elif item_description == 'FS':
        list[index][4] = str(int(list[index][4]) + int(item_quantity))
        list[index] = ",".join(list[index])
        list[index] = list[index] + "\n"
    elif item_description == 'MS':
        list[index][6] = str(int(list[index][6]) + int(item_quantity))
        list[index] = ",".join(list[index])
        list[index] = list[index] + "\n"
    elif item_description == 'GL':
        list[index][8] = str(int(list[index][8]) + int(item_quantity))
        list[index] = ",".join(list[index])
        list[index] = list[index] + "\n"
    elif item_description == 'GW':
        list[index][10] = str(int(list[index][10]) + int(item_quantity))
        list[index] = ",".join(list[index])
        list[index] = list[index] + "\n"
    elif item_description == 'SC':
        list[index][12] = str(int(list[index][12]) + int(item_quantity))
        list[index] = ",".join(list[index])
        list[index] = list[index] + "\n"
    file = open("hospital.txt","w")
    file.writelines(list)
    file.close

def updateInventory():
    print("Updating Inventory")
    print("==================")
    correctCode = False
    while correctCode == False:
        sh_code = input('Enter supplier/hospital code: ')
        if sh_code == "s111" or sh_code == "h111" or sh_code == "s222" or sh_code == "h222" or sh_code == "s333" or sh_code == "h333":
            correctCode = True
        else:
            print("Incorrect supplier/hospital code")
    correct = False
    while correct == False:
        item_description = input('Enter item code to update: ')
        if item_description == "HC" or item_description == "FS" or item_description == "MS" or item_description == "GL" or item_description == "GW" or item_description == "SC":
            correct = True
        else:
            print("Incorrect item code")
    corNum = False
    while corNum == False: 
        item_quantity = input("Enter the updated quantity. Enter - for Terminate: ")
        if sh_code == "h111" or sh_code == "h222" or sh_code == "h333":
            if item_quantity.startswith("-") and item_quantity[1:].isdigit():
                corNum = True
            else:
                print("Incorrect number")
        elif sh_code == "s111" or sh_code == "s222" or sh_code == "s333":
            if item_quantity.isdigit() == True:
                corNum = True
            else:
                print("Incorrect number")
        else:
            print("Incorrect number")

    file = open("ppe.txt" , "r").readlines()
    count = 0
    for line in file:
        line = line.strip().split(",")
        if line[0] == item_description:
            if (int(line[2]) + int(item_quantity)) >= 0:
                line[2] = str(int(line[2]) + int(item_quantity)) + "\n"
                file[count] = ",".join(line)
            else:
                print("Result will be less than ZERO!!!")
        count += 1
    if sh_code[0] == "s":
        list = open('supplier.txt', 'r').readlines()
        if sh_code == "s111":
            list[0] = list[0].strip().split(",")
            if item_description == "HC":
                list[0][2] = str(int(list[0][2]) + int(item_quantity))
                list[0] = ",".join(list[0])
                list[0] = list[0] + "\n"
            elif item_description == "FS":
                list[0][4] = str(int(list[0][4]) + int(item_quantity)) + "\n"
                list[0] = ",".join(list[0])
        elif sh_code == "s222":            
            list[1] = list[1].strip().split(",")
            if item_description == "MS":
                list[1][2] = str(int(list[1][2]) + int(item_quantity))
                list[1] = ",".join(list[1])
                list[1] = list[1] + "\n"
            elif item_description == "GL":
                list[1][4] = str(int(list[1][4]) + int(item_quantity)) + "\n"
                list[1] = ",".join(list[1])
        elif sh_code == "s333":
            list[2] = list[2].strip().split(",")
            if item_description == "GW":
                list[2][2] = str(int(list[2][2]) + int(item_quantity))
                list[2] = ",".join(list[2])
                list[2] = list[2] + "\n"
            elif item_description == "SC":
                list[2][4] = str(int(list[2][4])+int(item_quantity)) + "\n"
                list[2] = ",".join(list[2])
        write = open('supplier.txt', 'w')
        write.writelines(list)
        write.close()      
    if sh_code[0] == "h":
        if sh_code == 'h111':
            hospital(0,item_description,item_quantity)       
        elif sh_code == 'h222':
            hospital(1,item_description,item_quantity)
        elif sh_code == 'h333':
            hospital(2,item_description,item_quantity)       
    write = open('ppe.txt', 'w')
    write.writelines(file)
    write.close()
    date = str(datetime.date.today())
    writed = open("distribution.txt","a")
    writed.write("\n" + sh_code + "," + item_description + "," + item_quantity+ "," + date)
    writed.close

def supMenu():
    filed = open("distribution.txt","r").readlines()
    files = open("supplier.txt","r")
    back = False
    while back == False:
        print("""

(1) Search by Item Code
(2) Search by Supplier Code
(3) Print All Supplier Transaction
(4) Back
        
        """)
        choice = input("Please enter choice: ")
        if choice == "1":
            correct = False
            while correct == False:
                item_description = input('Enter item code: ')
                if item_description == "HC" or item_description == "FS" or item_description == "MS" or item_description == "GL" or item_description == "GW" or item_description == "SC":
                    correct = True
                else:
                    print("Incorrect item code")
            for index in filed:
                index = index.strip().split(",")
                if index[1] == item_description:
                    if index[0] == "s111" or index[0] == "s222" or index[0] == "s333":
                        print(index[1] + " Added by: " + index[0] + " Quantity: " + index[2] + " Date: " + index[3])
            for index in files:
                index = index.strip().split(",")
                if index[1] == item_description:
                    print("\nIn Total Added " + index[2] + " in "  + item_description)
                elif index[3] == item_description:
                    print("\nIn Total Added " + index[4] + " in " + item_description)
            back = True
        elif choice == "2":
            correct = False
            while correct == False:
                s_code = input('Enter supplier code: ')
                if s_code == "s111" or s_code == "s222" or s_code == "s333":
                    correct = True
                else:
                    print("Incorrect Supplier code")
            for index in filed:
                index = index.strip().split(",")
                if index[0] == s_code:
                    print(index[1] + " Added by: " + index[0] + " Quantity: " + index[2] + " Date: " + index[3])
            for index in files:
                index = index.strip().split(",")
                if index[0] == s_code:
                    print("\nIn Total " + s_code + " added "  + index[2] + " of "+index[1]+" and "+ index[4] + " of "+index[3])
            back = True
        elif choice == "3":
            for index in filed:
                index = index.strip().split(",")
                if index[0] == "s111" or index[0] == "s222" or index[0] == "s333":
                    print(index[1] + " Added by: " + index[0] + " Quantity: " + index[2] + " Date: " + index[3])
            back = True
        elif choice == "4":
            back = True
        else:
            print("Incorrect Input!")

def hosMenu():
    filed = open("distribution.txt","r").readlines()
    fileh = open("hospital.txt","r")
    back = False
    while back == False:
        print("""

(1) Search by Item Code
(2) Search by Hospital Code
(3) Print All Hospital Transaction
(4) Print All Available Stock
(5) Back
        
        """)
        choice = input("Please enter choice: ")
        if choice == "1":
            correct = False
            while correct == False:
                item_description = input('Enter item code: ')
                if item_description == "HC" or item_description == "FS" or item_description == "MS" or item_description == "GL" or item_description == "GW" or item_description == "SC":
                    correct = True
                else:
                    print("Incorrect item code")
            for index in filed:
                index = index.strip().split(",")
                if index[1] == item_description:
                    if index[0] == "h111" or index[0] == "h222" or index[0] == "h333":
                        print(index[1] + " Taken by: " + index[0] + " Quantity: " + index[2] + " Date: " + index[3])
            for index in fileh:
                index = index.strip().split(",")
                if index[1] == item_description:
                    print("\nIn Total Taken " + index[2] + " by "  + index[0])
                elif index[3] == item_description:
                    print("\nIn Total Added " + index[4] + " by "  + index[0])
                elif index[5] == item_description:
                    print("\nIn Total Added " + index[6] + " by "  + index[0])
                elif index[7] == item_description:
                    print("\nIn Total Added " + index[8] + " by "  + index[0])
                elif index[9] == item_description:
                    print("\nIn Total Added " + index[10] + " by "  + index[0])
                elif index[11] == item_description:
                    print("\nIn Total Added " + index[12] + " by "  + index[0])
            back = True
        elif choice == "2":
            correct = False
            while correct == False:
                h_code = input('Enter Hospital code: ')
                if h_code == "h111" or h_code == "h222" or h_code == "h333":
                    correct = True
                else:
                    print("Incorrect hospital code")
            for index in filed:
                index = index.strip().split(",")
                if index[0] == h_code:
                    print(index[1] + " Taken by: " + index[0] + " Quantity: " + index[2] + " Date: " + index[3])
            for index in fileh:
                index = index.strip().split(",")
                if index[0] == h_code:
                    print("\nItems in stock:")
                    print(index[1] + ": " + index[2],index[3] + ": " + index[4],index[5] + ": " + index[6],index[7] + ": " + index[8],index[9] + ": " + index[10],index[11] + ": " + index[12],)
            back = True        
        elif choice == "3":
            for index in filed:
                index = index.strip().split(",")
                if index[0] == "h111" or index[0] == "h222" or index[0] == "h333":
                    print(index[1] + " Taken by: " + index[0] + " Quantity: " + index[2] + " Date: " + index[3])
            back = True      
        elif choice == "4":
            for index in fileh:
                index = index.strip().split(",")
                print("\nItems in "+ index[0] +" stock:")
                print(index[1] + ": " + index[2],index[3] + ": " + index[4],index[5] + ": " + index[6],index[7] + ": " + index[8],index[9] + ": " + index[10],index[11] + ": " + index[12],)
            back = True        
        elif choice == "5":
            back = True
        else:
            print("Incorrect Input!")

def searchInventory():
    back = False
    while back == False:
        print("""

(1) Search by Supplier
(2) Search by Hospital
(3) Back 
    
        """)
        choice = input("Please enter your choice: ")
        if choice == "1":
            supMenu()
        elif choice == "2":
            hosMenu()
        elif choice == "3":
            back = True
        else:
            print("Incorrect Input!")
        
def printInventory():
    file = open("ppe.txt","r").readlines()
    back = False
    while back == False:
        print("""

(1) Print Inventory in Ascending Order
(2) Print Inventory Less than 25 Items
(3) Back        
        """)
        choice = input("Please Enter choice: ")
        if choice == "1":
            print("===========================")
            newfile = []
            for index in file:
                index = index.strip().split(",")
                newfile.append(index)
            newfile = sorted(newfile, key = lambda number: int(number[2]), reverse = True)
            for index in newfile:
                print(index[0] + ": " + index[2])
            print("===========================")
            back = True
        elif choice == "2":
            print("===========================")
            for index in file:
                index = index.strip().split(",")
                if int(index[2]) <= 25:
                    print(index[0] + ": " + index[2])
            print("===========================")
            back = True
        elif choice == "3":
            back = True
        else:
            print("Incorrect Input!")

menuDisplay()