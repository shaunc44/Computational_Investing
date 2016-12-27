import csv



dates = []
symbols = []
orders_no_dupl = []

orders_reader = csv.reader(open('orders.csv', 'rU'), delimiter=',')
#print orders_reader[1]
for row in orders_reader:
	#print row
	#dates.append(''.join(row[0:3]))
	#add if stmt to check is row = other rows???
	orders_no_dupl.append(row)

	#dates.append(row[0:3])
	#symbols.append(row[3])

#Remove duplicates from lists (why??)
#orders_no_dupl = list(set(orders_no_dupl))
#dates = set(dates)
#symbols = list(set(symbols))
b = list()
for sublist in orders_no_dupl:
	if sublist not in orders_no_dupl:
		b.append(sublist)

print b
print orders_no_dupl


'''
print dates
print symbols
'''





#marketsim(cash, orders_file)