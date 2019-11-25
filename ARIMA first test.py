from sklearn.metrics import mean_squared_error
import pandas as pd
import math as m
from statsmodels.tsa.arima_model import ARIMA

# данные в БД о продаже одной группы товаров в одном торговом павильоне
# выгружаем из Oracl'а данные в csv, парсим в series
# выгрузка из oracle - OraData.py

#задача перебора гиперпараметров для отыскания модели ARIMA с наименьшей ошибкой RMSE

series = pd.series.from_csv('testARIMA.csv', header=0)
VL = series.values # значения

def select_ARIMA(VL, arr):

    learn = VL[0:int(len(X) * 1/2)]  # учим на первой половине
    test = VL[int(len(X) * 1/2):]  #тестим на второй

	hist = [x for x in learn]
    # с помощью ARIMA предсказываем ряд (thinkable) на текущих гиперпараметрах

	thinkable = list()
	for t in range(len(test)):
		model = ARIMA(hist, order=arr)
		model_fit = model.fit(disp=0)
		now_think = model_fit.forecast()[0]
		thinkable.append(now_think)
		hist.append(test[t])

	# считаем ошибку между предсказанием и тестовой выборкой (test)
	mse = mean_squared_error(test, thinkable)
	rmse = m.sqrt(mse)
	return rmse


# матрица всевозможных значений гиперпараметров
P = 12; D = 4; Q=12
#отталкиваемся от предварительных значений 12, 4, 12
set_mtrix=[]
for p in range(P):
    for d in range(D):
        for q in range(Q):
            set_mtrix.append((p,d,q))
print(set_mtrix)

# best_rmse ~ INF
best_rmse = 100000000; target_select = (0,0,0)
for selection in set_mtrix:
    try:
        # считаем на текущей выборке гиперпараметров
        rmse = select_ARIMA(VL, selection)
        if rmse < best_rmse:
            best_rmse = rmse
            target_select = selection
            print("current best values:",best_rmse, target_select)
    except:
        continue
print("best_rmse = ", best_rmse)
print("target_select = ", target_select)






