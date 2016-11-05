import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


ls_symbols = ['AAPL', 'GLD', 'GOOG', 'XOM']
allocations = [0.4, 0.4, 0.0, 0.2]
dt_start = dt.datetime(2011, 1, 1)
dt_end = dt.datetime(2011, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

#clear cache on this line??
c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))


#na means Numpy Array
na_price = d_data['close'].values
#normalized prices of each stock so plot isn't skewed
na_normalized_price = na_price / na_price[0,:]
#print na_normalized_price

#make copy of normalized_price instead of reference
na_rets = na_normalized_price.copy()
daily_returns = tsu.returnize0(na_rets)
#print len(daily_returns)

'''
#Figure out how to apply weights to for loop results below
weighted_ret = 0
for i in range(len(allocations)):
	weighted_ret += np.mean(daily_returns[:,i]) * allocations[i]
	#print np.std(daily_returns[:,i])
print weighted_ret
'''
#print len(allocations)

annual_ret_stock1 = np.mean(daily_returns[:,0]) * len(daily_returns)
annual_ret_stock2 = np.mean(daily_returns[:,1]) * len(daily_returns)
annual_ret_stock3 = np.mean(daily_returns[:,2]) * len(daily_returns)
annual_ret_stock4 = np.mean(daily_returns[:,3]) * len(daily_returns)
print annual_ret_stock1
print annual_ret_stock2
print annual_ret_stock3
print annual_ret_stock4

'''
print annual_ret_stock1 * allocations[0] + annual_ret_stock2 * allocations[1] + annual_ret_stock3 * allocations[2] + annual_ret_stock4 * allocations[3]
'''

print annual_ret_stock1 * allocations[0]
print annual_ret_stock2 * allocations[1]
print annual_ret_stock3 * allocations[2]
print annual_ret_stock4 * allocations[3]

avg_daily_rets = np.mean(daily_returns)
#print avg_daily_rets * len(daily_returns)
stdev_daily_rets = np.std(daily_returns)
#print stdev_daily_rets


def simulate(*args):
	#put in list??
	'''
	adj_closing_prices = []
	adj_closing_prices = ls_keys[3]
	print adj_closing_prices
	na_price = d_data['close'].values
	#normalized_price
	'''

	print "Start Date: ", dt_start.strftime("%B %d, %Y")
	print "End Date: ", dt_end.strftime("%B %d, %Y")
	print "Symbols: ", ls_symbols
	print "Optimal Allocations: ", allocations #how to insert optimal allocations?
	print "Sharpe Ratio: "
	print "Volatility (stdev of daily rets): ", stdev_daily_rets
	print "Avg Daily Return: ", avg_daily_rets
	print "Cumulative Return: "


simulate(dt_start, dt_end, ls_symbols, allocations)



'''
plt.clf() #Clear the plot
plt.plot(ldt_timestamps, na_price) #plot data
plt.legend(ls_symbols)
plt.ylabel('Adjusted Close')
plt.xlabel('Date')
plt.savefig('adjustedclose.pdf', format='pdf')

#na_normalized_price = na_price / na_price[0,:]
#print na_normalized_price

plt.clf() #Clear the plot
plt.plot(ldt_timestamps, na_normalized_price) #plot data
plt.savefig('normalized.pdf', format='pdf')
'''