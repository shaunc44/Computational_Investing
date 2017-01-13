import csv
import pandas as pd
import numpy as np
import datetime as dt
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da


orders = csv.reader( open('orders.csv', 'rU'), delimiter=',' )


#Create orders list
orders_list = []
for row in orders:
	orders_list.append(row)


#Remove duplicates from orders list
orders_unique = []
for sublist in orders_list:
	if sublist not in orders_unique:
		orders_unique.append(sublist)


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


#Convert date list to list of ints
ls_date_ints = []
for i in ls_dates:
	ls_date_ints.append(map(int, i))


#Add 16 hrs to dates timestamps
ls_dates_ts = []
for date in ls_date_ints:
	date = ( dt.datetime(date[0], date[1], date[2]) + dt.timedelta(hours=16) )
	ls_dates_ts.append(date)
#print ls_dates_ts


#Store beginning and ending order dates
begin_date = min(ls_date_ints)
end_date = max(ls_date_ints)


#use NYSE dates function create array w right number elements for each date
#Subtract 3 from the start date to get previous adj close
dt_start = dt.datetime( begin_date[0], begin_date[1], begin_date[2] )
#Add 1 to end date to get adj close price
dt_end = dt.datetime( end_date[0], end_date[1], (end_date[2] + 1) )
ldt_timestamps = du.getNYSEdays( dt_start, dt_end, dt.timedelta(hours=16) )


#pull data from Yahoo Finance
c_dataobj = da.DataAccess('Yahoo', cachestalltime=0)
c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_sym_unique, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))


#Create prices array from start_date to end_date
prices_array = d_data['actual_close']
print prices_array


#Create trades matrix (Pandas DataFrame)
df_trades = pd.DataFrame( index = ldt_timestamps, columns = ls_sym_unique )
df_trades.fillna( 0, inplace = True )
#print df_trades


#Iterate over orders file to add # of shares to trades matrix
count = -1
for date1 in ldt_timestamps:
	count += 1
	for date2, qty, sym, trade in zip( ls_dates_ts, order_qty_ls, ls_symbols, ls_trades ):
		if date2 == date1:
			for i in range( len(ls_sym_unique) ):
				if sym == ls_sym_unique[i] and trade == 'Buy' and df_trades[ls_sym_unique[i]].ix[ldt_timestamps[count]] != 0:
						df_trades[ls_sym_unique[i]].ix[ldt_timestamps[count]] = df_trades[ls_sym_unique[i]].ix[ldt_timestamps[count]] + qty
				elif sym == ls_sym_unique[i] and trade == 'Sell' and df_trades[ls_sym_unique[i]].ix[ldt_timestamps[count]] != 0:
						df_trades[ls_sym_unique[i]].ix[ldt_timestamps[count]] = df_trades[ls_sym_unique[i]].ix[ldt_timestamps[count]] - qty
				elif sym == ls_sym_unique[i] and trade == 'Buy' and df_trades[ls_sym_unique[i]].ix[ldt_timestamps[count]] == 0:
						df_trades[ls_sym_unique[i]].ix[ldt_timestamps[count]] = qty
				elif sym == ls_sym_unique[i] and trade == 'Sell' and df_trades[ls_sym_unique[i]].ix[ldt_timestamps[count]] == 0:
						df_trades[ls_sym_unique[i]].ix[ldt_timestamps[count]] = -qty
#print df_trades


#Create cash time series
ts_cash = pd.Series( 0, index = ldt_timestamps )
#print ts_cash


#Create running cash total
cash_balance = 1000000
for x in range( len(ldt_timestamps) ):
	for i in range(4):
		if df_trades[ls_sym_unique[i]].ix[ldt_timestamps[x]] > 0:
			ts_cash[x] = ( cash_balance - ( prices_array[ls_sym_unique[i]].ix[ldt_timestamps[x]] * df_trades[ls_sym_unique[i]].ix[ldt_timestamps[x]] ) )
			cash_balance = ts_cash[x]
		else:
			ts_cash[x] = ( cash_balance - ( prices_array[ls_sym_unique[i]].ix[ldt_timestamps[x]] * df_trades[ls_sym_unique[i]].ix[ldt_timestamps[x]] ) )
			cash_balance = ts_cash[x]


#Append cash to trades matrix
df_trades_w_cash = df_trades
df_trades_w_cash['Cash'] = ts_cash
#print df_trades_w_cash


#Create array of shares owned (holdings) on each date
df_holdings = pd.DataFrame( index = ldt_timestamps, columns = ls_sym_unique )
df_holdings.fillna( 0, inplace = True )
#Set initial holdings on day 0
for j in range(4):
	df_holdings[ls_sym_unique[j]].ix[ldt_timestamps[0]] = df_trades[ls_sym_unique[j]].ix[ldt_timestamps[0]]
#Set holdings on days 1 through 239
for z in range( len(ldt_timestamps[1:]) ):
	for i in range(4):
		df_holdings[ls_sym_unique[i]].ix[ldt_timestamps[z+1]] = df_holdings[ls_sym_unique[i]].ix[ldt_timestamps[z]] + df_trades[ls_sym_unique[i]].ix[ldt_timestamps[z+1]]

print df_holdings


#Iterate through shares owned array,check prices, update holding value
#holding_values = np.dot(prices_array, df_holdings)
#print holding_values
portfolio_value = pd.Series( 0, index = ldt_timestamps )
for x, price, holding in zip( range(len(ldt_timestamps)), prices_array, df_holdings ):
	for z in range( len(ls_sym_unique ) ):
		portfolio_value[x] = prices_array[ls_sym_unique[z]].ix[ldt_timestamps[x]] * df_holdings[ls_sym_unique[z]].ix[ldt_timestamps[x]]

print portfolio_value

#Create a value array (equal values of all equites you are holding)


#Combine value + cash = total fund value


#marketsim(cash, orders_file)





