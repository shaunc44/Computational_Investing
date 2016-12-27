import csv


orders_reader = csv.reader(open('orders.csv', 'rU'), delimiter=',')

#Create orders list
orders_list = []
for row in orders_reader:
	orders_list.append(row)

#Remove duplicates from orders list
orders_unique = []
for sublist in orders_list:
	if sublist not in orders_unique:
		orders_unique.append(sublist)

#Create symbols list
symbol_list = []
for sym in orders_unique:
	symbol_list.append(sym[3])
#print symbol_list

#Create date list
date_list = []
for date in orders_unique:
	date_list.append(date[0:3])
#print date_list




#marketsim(cash, orders_file)