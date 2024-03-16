from transaction import * 
import sys

def runApp () :
    while True :
        print ("Welcome to Expense Tracker")
        print ("1. Add Transaction")
        print ("2. Load Transaction")
        print ("3. Update Transaction")
        print ("4. Delete Transaction")
        print ("5. Summary")
        print ("6. Exit")

        choice = input ("Enter your choice : ")

        if choice == "1" : 
            date = input ("Enter Date (YYYY:MM:DD) : ")
            description = input ("Enter Description : ")
            amount = input ("Enter Amount : ")
            add_transaction(date,description,amount)
        elif choice == "2" :
            load_transaction()

        elif choice == "3" :
            id = input ("Enter ID : ")
            date = input ("Enter Date (YYYY:MM:DD) : ")
            description = input ("Enter Description : ")
            amount = input ("Enter Amount : ")
            update_transaction(id,date,description,amount)

        elif choice == "4" :
            id = input ("Enter ID : ")
            delete_transaction(id)

        elif choice == "5" :
            summary()

        elif choice == "6" :
            exit()
        else :
            print ("Invalid Choice")



def exit () :
    print ("Exiting the program")
    sys.exit(0)

if __name__ == "__main__" :
    runApp()






    


