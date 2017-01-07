import csv
import pandas as pd
import numpy as np
import datetime as dt
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da


orders = csv.reader(open('orders.csv', 'rU'), delimiter=',')


#Create orders list
orders_list = []
for row in orders:
	orders_list.append(row)


#Remove duplicates from orders list
orders_unique = []
for sublist in orders_list:
	if sublist not in orders_unique:
		orders_unique.append(sublist)
#print orders_unique


#Create symbols & dates list
ls_symbols = [] #remove duplicate symbols??????
ls_dates = []
for row in orders_unique:
	ls_symbols.append(row[3])
	ls_dates.append(row[0:3])


#Remove duplicates from symbols list
ls_sym_unique = []
for sym in ls_symbols:
	if sym not in ls_sym_unique:
		ls_sym_unique.append(sym)


#Convert date list to list of ints
ls_date_ints = []
for i in ls_dates:
	ls_date_ints.append(map(int, i))
#print ls_date_ints

ls_dates_ts = []
for date in ls_date_ints:
	date = ( dt.datetime(date[0], date[1], date[2]) + dt.timedelta(hours=16) )
	ls_dates_ts.append(date)
	#print date
	#print ls_dates_ts


#Build NUMPY ARRAY for these dates, or numpy array with symbols, dates and values ??????????????
begin_date = min(ls_date_ints)
end_date = max(ls_date_ints)
#print begin_date


#use NYSE dates function to create array with right number of elements for each date used in test
#Subtract 3 from the start date to get previous adj close
dt_start = dt.datetime( begin_date[0], begin_date[1], begin_date[2] )
#print dt_start
#Add 1 to end date to get adj close price
dt_end = dt.datetime( end_date[0], end_date[1], (end_date[2] + 1) )
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
#print ldt_timestamps


#pull data from Yahoo Finance
c_dataobj = da.DataAccess('Yahoo', cachestalltime=0)
c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_sym_unique, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))


#Use adjusted close
#Read adj close prices into PANDAS dataframe and create daily prices array with symbols as columns and dates as rows
#This will create our prices array from start_date to end_date
prices_array = d_data['actual_close']
#print prices_array


#Iterate over orders (csv file), check prices (price array), update array of cash ($ not invested)
#Need to compare the date from orders file vs dates in timestamps to run the cash for loop **** NEXT STEP
cash = 1000000
'''
for order in orders_unique:
	if orders_unique[4] = 'Buy':
		cash = cash - orders_unique[5] * price???
'''
#prices_array[ls_sym_unique[]]

'''
for i in ldt_timestamps:
	if ldt_timestamps[i] == ls_date_ts[i]:
		print 'true'
	else:
		print 'false'
'''

if ldt_timestamps[0] == ls_dates_ts[0]:
	print 'True'

#Create a value array (equal values of all equites you are holding)


#marketsim(cash, orders_file)





