import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd


ls_symbols = ["GOOG", "AAPL", "GLD", "XOM"]
#Change dates to HW reqs
dt_start = dt.datetime(2010, 1, 1)
dt_end = dt.datetime(2010, 1, 15)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))

na_price = d_data['close'].values


plt.clf()
plt.plot(ldt_timestamps, na_price)


'''
allocations = [0.4, 0.4, 0.0, 0.2] #should this be a list, and here?
dt_start = dt.datetime(2011, 1, 1)
dt_end = dt.datetime(2011, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

#clear cache on this line??
c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))
'''


'''
def simulation():
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

simulation()
'''