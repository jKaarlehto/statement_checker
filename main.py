import csv
statament1 = { "file":"revolut.csv","key":"Amount", "delimiter":",","match":"top-up"}
statement2 = { "file":"nordea.csv","key":"Maara", "delimiter":";","match":"revolut"}
statements = [statament1, statement2]
amount = 0
for statement in statements :
    print("Parsing " + statement["file"])
    with open(statement["file"], newline='') as file:
        transactions = csv.DictReader(file, delimiter=statement["delimiter"])
        fieldnames = transactions.fieldnames
         
        for row in transactions:
            for fieldname in fieldnames:
                transaction_event  =str(row[fieldname]).lower() 
                if statement["match"].lower() in transaction_event:
                    amount = amount + float(row[statement["key"]].replace(",","."))
                    with open('Differences.txt','a') as output:
                        output.write("Transactionn event:\n")
                        output.writelines(str(row)+"\n")  
                        output.write("Balance difference: " + str(amount)+"\n\n")
                        
                    
                    
