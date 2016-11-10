import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


#calculate portfolio daily rets everyday and put in list??
def avg_daily_return():
	avg_daily_rets = 0
	for i in range(len(ls_symbols)):
		avg_daily_rets += (np.mean(daily_returns[:,i]) * allocations[i])
		#print avg_daily_rets
	return avg_daily_rets


def volatility():
	stdev_daily_rets = 0
	for i in range(len(ls_symbols)):
		stdev_daily_rets = (np.std(daily_returns[:,i]) * allocations[i])
		#print stdev_daily_rets
	return stdev_daily_rets


def sharpe_ratio():
	k = math.sqrt(252)
	sharpe = k * (avg_daily_return()/volatility())
	return sharpe

def optimal_alloc():
	#length of alloc list only 4
	#alloc list total must = 1.0 (if statement)
	#iterate by 0.1 segments
	#verify sharpe ratio is highest
	for alloc1 in allocations:


def total_return():
	tot_ret = 0
	for i in range(len(ls_symbols)):
		tot_ret += ( (na_price[-1,i]/na_price[0,i]) * allocations[i] )
	return tot_ret


def simulate(*args):
	print "Start Date: ", dt_start.strftime("%B %d, %Y")
	print "End Date: ", dt_end.strftime("%B %d, %Y")
	print "Symbols: ", ls_symbols
	print "Optimal Allocations: ", allocations #how to insert optimal allocations?
	print "Avg Daily Return: ", avg_daily_return()
	print "Volatility (stdev of daily rets): ", volatility()
	print "Sharpe Ratio: ", sharpe_ratio()
	print "Cumulative Return: ", total_return()


ls_symbols = ['AAPL', 'GLD', 'GOOG', 'XOM']
allocations = [0.4, 0.4, 0.0, 0.2]
dt_start = dt.datetime(2011, 1, 1)
dt_end = dt.datetime(2011, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)


c_dataobj = da.DataAccess('Yahoo', cachestalltime=0)
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
#print na_rets[-1,3]

#Call simulation program
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



