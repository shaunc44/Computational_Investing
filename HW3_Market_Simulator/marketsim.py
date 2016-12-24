import csv



dates = []
symbols = []

orders_reader = csv.reader(open('orders.csv', 'r'), delimiter=',')
for row in orders_reader:
	#print row
	#dates.append(''.join(row[0:3]))
	dates.append(row[0:3])
	symbols.append(row[3])

#Remove duplicates from lists (why??)
#dates = set(dates)
#symbols = list(set(symbols))


print dates
print symbols






#marketsim(cash, orders_file)