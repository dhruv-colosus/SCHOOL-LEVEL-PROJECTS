import csv

fields=["sports,competition,prizes_won"]
details=[]
with open('F:\school level python\practice.csv','r') as f:
    reader=csv.reader(f,delimiter='-')
    for row in reader:
        print(row)  
        details.append(row) 
    f.close()       
    

with open('F:\school level python\inal_details.csv','w') as d:
    fields=["sports,competition,prizes_won"]
    csv_w=csv.writer(d,delimiter="-")
    csv_w.writerow(fields)
    for i in details:
        csv_w.writerow(i)

    print("file created")         

        


    
    