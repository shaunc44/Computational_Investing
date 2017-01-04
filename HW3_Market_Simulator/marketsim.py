import csv
import pandas as pd
import numpy as np
import datetime as dt
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da


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


#Convert date list to list of ints
date_list2 = []
for i in date_list:
	#print map(int, i)
	date_list2.append(map(int, i))


#Put first and last date in a variable
#Build NUMPY ARRAY for these dates??????????????
begin_date = min(date_list2)
#print begin_date
#begin_date = begin_date - 1
end_date = max(date_list2)


#use NYSE dates function to create array with right number of elements for each date used in test
#Use only one nyse timestamp below *******
ls_symbols = ['AAPL', 'GLD', 'GOOG', 'XOM'] # = symbol_list
dt_start = dt.datetime( begin_date[0], begin_date[1], (begin_date[2] - 1) ) #add plus 1 here?, = begin_date
dt_end = dt.datetime( end_date[0], end_date[1], (end_date[2] + 1) ) #and here too?
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

print symbol_list
#print ls_symbols
print dt_start
print dt_end



#Use adjusted close
#Read data into PANDAS dataframe and create daily prices array with symbols as columns and dates as rows
#Iterate over orders, check prices, update cash($ not invested)




#marketsim(cash, orders_file)

