import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd


ls_symbols = ["GOOG", "AAPL", "GLD", "XOM"]
allocations = [0.2, 0.3, 0.4, 0.1]
dt_start = dt.datetime(2011, 1, 1)
dt_end = dt.datetime(2011, 1, 31)
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
#make copy of normalized_price instead of reference
na_rets = na_normalized_price.copy()
print tsu.returnize0(na_rets)
#print na_normalized_price


'''
def simulate(*args):
	#put in list??
	adj_closing_prices = []
	adj_closing_prices = ls_keys[3]
	print adj_closing_prices
	na_price = d_data['close'].values
	#normalized_price

	return st_dev
	return daily_ret_portfolio
	return sharpe_ratio
	return total_ret_portfolio

simulate(dt_start, dt_end, ls_symbols, allocations)
'''


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