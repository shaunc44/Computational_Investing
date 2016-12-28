import csv
import numpy as np


trades = csv.reader(open('orders.csv', 'rU'), delimiter=',')

#Create a NUMPY array for the dates list? orders list?

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
print date_list

#Put first and last date in a variable
begin_date = min(date_list)
print begin_date

end_date = min(date_list)
print end_date


#use NYSE dates function to create array with right number of elements for each date used in test
#Use adjusted close
#Read data into PANDAS dataframe and create daily prices array with symbols as columns and dates as rows
#Iterate over orders, check prices, update cash($ not invested)




#marketsim(cash, orders_file)


