import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import itertools


#sharpe ratio of the portfolio
def sharpe_ratio():
	k = math.sqrt(252)
	sharpe = k * ( avg_daily_return() / volatility() )
	return sharpe


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
		avg_daily_rets += ( np.mean(daily_returns[:,i]) * allocation[i] )
	return avg_daily_rets


#total portfolio return
def total_return():
	tot_ret = 0
	for i in range(len(ls_symbols)):
		tot_ret += ( (na_price[-1,i]/na_price[0,i]) * allocation[i] )
	return tot_ret


#simulation function to output data from input funcions 
def simulate(*args):
	print "Start Date: ", dt_start.strftime("%B %d, %Y")
	print "End Date: ", dt_end.strftime("%B %d, %Y")
	print "Symbols: ", ls_symbols
	print "Optimal Allocations: ", allocation
	print "Sharpe Ratio: ", opt_sharpe #sharpe_ratio()
	print "Volatility (stdev of daily rets): ", volatility()
	print "Avg Daily Return: ", avg_daily_return()
	print "Cumulative Return: ", total_return()


#inputs (stock symbols, dates)
ls_symbols = ['AXP', 'HPQ', 'IBM', 'HNZ']
dt_start = dt.datetime(2010, 1, 1)
dt_end = dt.datetime(2010, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)


#allocation inputs
allocation = []
combos = [[1, 0, 0, 0], [0.9, 0.1, 0, 0], [0.8, 0.1, 0.1, 0], [0.8, 0.2, 0, 0], [0.7, 0.1, 0.1, 0.1], [0.7, 0.2, 0.1, 0], [0.7, 0.3, 0, 0], [0.6, 0.4, 0, 0], [0.6, 0.3, 0.1, 0], [0.6, 0.2, 0.2, 0], [0.6, 0.2, 0.1, 0.1], [0.5, 0.5, 0, 0], [0.5, 0.4, 0.1, 0], [0.5, 0.3, 0.2, 0], [0.5, 0.3, 0.1, 0.1], [0.5, 0.2, 0.2, 0.1], [0.4, 0.4, 0.2, 0], [0.4, 0.3, 0.3, 0], [0.4, 0.3, 0.2, 0.1], [0.4, 0.2, 0.2, 0.2]]


#for-loops to determine optimal allocation
#need to enter initial allocation somewhere to run sharpe????
#maybe just set opt_sharpe to 0 initially
opt_sharpe = 0 #put this inside of the for-loop???
for i in range(len(combos)):
	allocations = list(itertools.permutations(combos[i]))
	#print allocations
	#print len(allocations)

	#put another for-loop here to iterate over possible combos???
	allocation = list(allocations[0])

	sr = sharpe_ratio()
	if sr > opt_sharpe:
		opt_sharpe = sr
	return opt_sharpe
	print allocation

'''
combo_01 = [0.0, 0.0, 0.0, 1.0]
allocations = list(itertools.permutations(combo_01))
print allocations
allocation = list(allocations[0])
print allocation
'''

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


#Call simulation program
simulate(dt_start, dt_end, ls_symbols)






#Try to set this up later when you have more time
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


'''
def optimal_alloc():
	#how to iter over 4 parts of list (nested for loops)
	#verify sharpe ratio is highest
	#opt_sharpe = sharpe_ratio()

	def drange(start, stop, step):
		i = start
		while i < stop:
			yield i
			i += step
	#for i in drange(0.0, 1.0, 0.1):
	#	print i

	for stock in allocation:
		for i in drange(0.0, 1.0, 0.1):
			allocation[0] -= i
			allocation[1] += i
			print allocation
			#sr = sharpe_ratio()
			#if sr > opt_sharpe:
			#	opt_sharpe = sr
			#return opt_sharpe
	#return allocation #for other functions to work

allocation = [1, 0, 0, 0]

optimal_alloc()
'''