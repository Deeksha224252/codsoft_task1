print("")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
 
    choice = int(input("Please enter your choice: "))
     
    return choice
 
def add_contact(pb):
    
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(int(input("Enter number: ")))
        if i == 2:
            dip.append(str(input("Enter e-mail address: ")))
        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
        if i == 4:
            dip.append(
                str(input("Enter category(Family/Friends/Work/Others): ")))
    pb.append(dip)
    
    return pb
 
def remove_existing(pb):
    
    query = str(input("Please enter the name of the contact you wish to remove: "))
    temp = 0
   
     
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            
             
            print(pb.pop(i))
          
             
            print("This query has now been removed")
            return pb
