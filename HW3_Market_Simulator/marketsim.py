import csv


trades = csv.reader(open('orders.csv', 'rU'), delimiter=',')

#Create orders list
orders_list = []
for row in trades:
	orders_list.append(row)

#Remove duplicates from orders list
orders_unique = []
for sublist in orders_list:
	if sublist not in orders_unique:
		orders_unique.append(sublist)

#Create symbols & dates list
symbol_list = []
date_list = []
for row in orders_unique:
	symbol_list.append(row[3])
	date_list.append(row[0:3])

#print symbol_list
#print date_list



#marketsim(cash, orders_file)