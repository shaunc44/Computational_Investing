import csv




orders_reader = csv.reader(open('orders.csv', 'r'), delimiter=',')
for row in orders_reader:
	print row





#marketsim(cash, orders_file)