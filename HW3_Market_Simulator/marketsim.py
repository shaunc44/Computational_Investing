import csv
import pandas as pd
import numpy as np
import datetime as dt
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da


orders = csv.reader(open('orders.csv', 'rU'), delimiter=',')
#print orders

orders_df = pd.read_csv('orders.csv')
#print orders_df
#for i in orders_df:
#	print i


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


#Add order quantities to list
order_qty_ls = []
for x in orders_unique:
	order_qty_ls.append(int(x[5]))
#print order_qty_ls


#Create list of trades: buy or sell
ls_trades = []
for trade in orders_unique:
	ls_trades.append(trade[4])
#print ls_trades


#Create symbols & dates list
ls_symbols = []
ls_dates = []
for row in orders_unique:
	ls_symbols.append(row[3])
	ls_dates.append(row[0:3])
#print ls_symbols


#Remove duplicates from symbols list
ls_sym_unique = []
for sym in ls_symbols:
	if sym not in ls_sym_unique:
		ls_sym_unique.append(sym)
#print ls_sym_unique
#print ls_dates


#Convert date list to list of ints
ls_date_ints = []
for i in ls_dates:
	ls_date_ints.append(map(int, i))


#Add 16 hrs to dates timestamps
ls_dates_ts = []
for date in ls_date_ints:
	date = ( dt.datetime(date[0], date[1], date[2]) + dt.timedelta(hours=16) )
	ls_dates_ts.append(date)
	#print date
#print ls_dates_ts[0]
#print ls_dates_ts


'''
#Create dates & orders list
dates_orders_ls = []
for date in ls_dates_ts:
	for qty in order_qty_ls:
		print date
		print qty
date_qty_array = ls_dates_ts[0].append(order_qty_ls[0])
print date_qty_array
'''


#Build NUMPY ARRAY for these dates, or numpy array with symbols, dates and values ??????????????
begin_date = min(ls_date_ints)
end_date = max(ls_date_ints)
#print begin_date


#use NYSE dates function to create array with right number of elements for each date used in test
#Subtract 3 from the start date to get previous adj close
dt_start = dt.datetime( begin_date[0], begin_date[1], begin_date[2] )
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


#Create trades matrix (Pandas DataFrame)
df_trades = pd.DataFrame(index = ldt_timestamps, columns = ls_sym_unique )
df_trades.fillna( 0, inplace = True )
#df_trades[ls_sym_unique[1]].ix[ldt_timestamps[1]] = 0
#print df_trades


date_qty_array = []
for date, qty in zip(ls_dates_ts, order_qty_ls):
	date_qty_array.append(date)
	date_qty_array.append(qty)
#print date_qty_array[2]



#Iterate over orders file to add values to trades matrix
count = -1
for date1 in ldt_timestamps:
	count += 1
	#print count
	for date2, qty, sym, trade in zip( ls_dates_ts, order_qty_ls, ls_symbols, ls_trades ):
		if date1 == date2:
			if sym == ls_sym_unique[0] and trade == 'Buy':
				df_trades[ls_sym_unique[0]].ix[ldt_timestamps[count]] = qty
			elif sym == ls_sym_unique[0] and trade == 'Sell':
				df_trades[ls_sym_unique[0]].ix[ldt_timestamps[count]] = -qty
			elif sym == ls_sym_unique[1] and trade == 'Buy':
				df_trades[ls_sym_unique[1]].ix[ldt_timestamps[count]] = qty
			elif sym == ls_sym_unique[1] and trade == 'Sell':
				df_trades[ls_sym_unique[1]].ix[ldt_timestamps[count]] = -qty
			elif sym == ls_sym_unique[2] and trade == 'Buy':
				df_trades[ls_sym_unique[2]].ix[ldt_timestamps[count]] = qty
			elif sym == ls_sym_unique[2] and trade == 'Sell':
				df_trades[ls_sym_unique[2]].ix[ldt_timestamps[count]] = -qty
			elif sym == ls_sym_unique[3] and trade == 'Buy':
				df_trades[ls_sym_unique[3]].ix[ldt_timestamps[count]] = qty
			else:
				df_trades[ls_sym_unique[3]].ix[ldt_timestamps[count]] = -qty

#df_trades[ls_sym_unique[1]].ix[ldt_timestamps[1]] = 0
#print df_trades


#Need to compare the date from orders file vs dates in timestamps to run the cash for loop **** NEXT STEP
cash = 1000000
df_trades['Cash'] = range( 1, len( df_trades ) + 1 )
print df_trades





#Create a value array (equal values of all equites you are holding)

#marketsim(cash, orders_file)





