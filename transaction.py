import json 

trnsaction = []

def add_transaction (date,description,amount) :

# transaction with global 
    global trnsaction
# open file to read history of transaction 
    with open ("transaction.json" , 'r') as file :
        # check if any error in reading file 
        try :
            trnsaction = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print ("no old data found")


        if not trnsaction:
                id = 1

        else :
                
                # get lenght of the transaction list
                trnsaction_len = len(trnsaction)
                # assign new id as len + 1
                id = trnsaction_len + 1

        trnsaction.append(f'"id":"{id}","date" : "{date}","description":"{description}","amount":"{amount}"')
        
    with open ("transaction.json" , 'w') as file :
        json.dump(trnsaction,file,indent=4)

# add_transaction("2020-02-15","description 01",20000)       
        
def load_transaction () :
    global transaction

    try : 
        with open ("transaction.json" , 'r') as file :
            trnsaction = json.load(file)

            for item in trnsaction :
                print(item)

    except (FileExistsError,json.JSONDecodeError) :
        print ("Data Not Found or No such file or directory")

def update_transaction (id,date,description,amount) :
     
     search = f'"id":"{id}"'
     print(search)
    
     
     global trnsaction

     # open file to read file history to update 

     with open ("transaction.json" , 'r') as file :
        trnsaction = json.load(file)

        for item in trnsaction :
            # print (item)
            if search in item:
                print (item)
                trnsaction.remove(item)
                trnsaction.append(f'"id":"{id}","date" : "{date}","description":"{description}","amount":"{amount}"')
                print ("founded data and updated ...!")
                break
            else :
                print ("no such data found")

        
        with open ("transaction.json" , 'w') as file :
            json.dump(trnsaction,file,indent=4)


def delete_transaction (id) :
    
    with open ("transaction.json" , 'r') as file :
        transaction = json.load(file)

        search = f'"id":"{id}"'

        for item in transaction :
            if search in item :
                transaction.remove(item)
                print("Data Founded ....!")
                print ("Data removed ....!")
                break
            
            else : 
                print ("no such data found")

    

    with open ("transaction.json" , 'w') as file :
        json.dump(transaction,file,indent=4)


def summary (expenses) :
    trnsaction = []

    with open ("transaction.json" , 'r') as file :
        trnsaction = json.load(file)

        total = 0

        for item in trnsaction :
            item = json.loads("{" + item + "}")
            total += int(item["amount"])
        print (f"Total Amount : {total}")
        print (f"Total Expenses : {expenses}")
        print (f"Net Income : {total - expenses}")








    



        