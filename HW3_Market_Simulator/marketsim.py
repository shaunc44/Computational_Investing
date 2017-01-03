import csv
import numpy as np
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da
import datetime as dt


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
begin_date = min(date_list2)
end_date = max(date_list2)


#use NYSE dates function to create array with right number of elements for each date used in test
#Use only one nyse timestamp below *******
ls_symbols = ['AAPL', 'GLD', 'GOOG', 'XOM']
dt_start = dt.datetime(2011, 1, 1)
dt_end = dt.datetime(2011, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))



#Use adjusted close
#Read data into PANDAS dataframe and create daily prices array with symbols as columns and dates as rows
#Iterate over orders, check prices, update cash($ not invested)




#marketsim(cash, orders_file)

