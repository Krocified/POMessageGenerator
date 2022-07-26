import csv

csvFile = open('tnt.csv')
csvReader = csv.reader(csvFile)

txtFile = open('tnt.txt', 'w')

total = 0
for i, row in enumerate(csvReader): 
    if i==0:
        continue
    name = row[0]
    qty = row[1]
    price = row[2]
    subtotal = row[3]
    total += float(subtotal)
    txtEntry = qty + "x " + name + " @" + price + " = " + subtotal + '\n'
    txtFile.write(txtEntry)

txtFile.write("\nTotal: " + str(total))

csvFile.close()
txtFile.close()