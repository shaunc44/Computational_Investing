import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import itertools


#standard deviation of the portfolio
def volatility():
	stdev_daily_rets = 0
	for i in range(len(ls_symbols)):
		stdev_daily_rets += ( np.std(daily_returns[:,i]) * allocation[i] )
	return stdev_daily_rets


#avg daily portfolio return
def avg_daily_return():
	avg_daily_rets = 0
	for i in range(len(ls_symbols)):
		avg_daily_rets += ( (np.mean(daily_returns[:,i])) * allocation[i] )
	return avg_daily_rets


#sharpe ratio of the portfolio
def sharpe_ratio():
	k = math.sqrt(252)
	sharpe = k * ( avg_daily_return() / volatility() )
	return sharpe


#total portfolio return
def total_return():
	tot_ret = 0
	for i in range(len(ls_symbols)):
		tot_ret += ( (na_price[-1,i]/na_price[0,i]) * opt_alloc[i] )
	return tot_ret


#simulation function to output data from input funcions 
def simulate(*args):
	print "Start Date: ", dt_start.strftime("%B %d, %Y")
	print "End Date: ", dt_end.strftime("%B %d, %Y")
	print "Symbols: ", ls_symbols
	print "Optimal Allocations: ", opt_alloc
	print "Sharpe Ratio: ", opt_sharpe
	print "Volatility (stdev of daily rets): ", volatility()
	print "Avg Daily Return: ", avg_daily_return()
	print "Cumulative Return: ", total_return()


#inputs (stock symbols, dates)
ls_symbols = ['AAPL', 'GLD', 'GOOG', 'XOM']
dt_start = dt.datetime(2011, 1, 1)
dt_end = dt.datetime(2011, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

#print dt_start

#pull data from Yahoo Finance
c_dataobj = da.DataAccess('Yahoo', cachestalltime=0)
c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))


#na means Numpy Array
na_price = d_data['close'].values
#normalize prices to easily compare stocks
na_normalized_price = na_price / na_price[0,:]
#make copy of normalized_price instead of reference
na_rets = na_normalized_price.copy()
daily_returns = tsu.returnize0(na_rets)


#allocation inputs
allocation = []
#combos = [[0.4, 0.2, 0.1, 0.3], [0.3, 0.3, 0.2, 0.2]]
combos = [[1.0, 0.0, 0.0, 0.0], [0.9, 0.1, 0.0, 0.0], [0.8, 0.1, 0.1, 0.0], [0.8, 0.2, 0.0, 0.0], [0.7, 0.1, 0.1, 0.1], [0.7, 0.2, 0.1, 0.0], [0.7, 0.3, 0.0, 0.0], [0.6, 0.4, 0.0, 0.0], [0.6, 0.3, 0.1, 0.0], [0.6, 0.2, 0.2, 0.0], [0.6, 0.2, 0.1, 0.1], [0.5, 0.5, 0.0, 0.0], [0.5, 0.4, 0.1, 0.0], [0.5, 0.3, 0.2, 0.0], [0.5, 0.3, 0.1, 0.1], [0.5, 0.2, 0.2, 0.1], [0.4, 0.4, 0.2, 0.0], [0.4, 0.4, 0.1, 0.1], [0.4, 0.3, 0.3, 0.0], [0.4, 0.3, 0.2, 0.1], [0.4, 0.2, 0.2, 0.2], [0.3, 0.3, 0.3, 0.1], [0.3, 0.3, 0.2, 0.2]]

opt_sharpe = 0
opt_alloc = []
#For-loop isolates best allocation based on highest sharpe ratio
for i in range(len(combos)):
	#permutations create all allocation arrangements
	allocations = list(itertools.permutations(combos[i]))
	#print allocations

	for j in range(len(allocations)):
		allocation = list(allocations[j])
		#print allocation
		temp_sharpe = sharpe_ratio()
		#print temp_sharpe

		if temp_sharpe > opt_sharpe:
			opt_sharpe = temp_sharpe
			opt_alloc = allocation
			#print opt_alloc

allocation = opt_alloc


#Call simulation program
simulate(dt_start, dt_end, ls_symbols)



'''
#Try to set this up later when you have more time
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
