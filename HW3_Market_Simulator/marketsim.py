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

print orders_unique[2][2]

#Create symbols list?

#Create date list?


#marketsim(cash, orders_file)