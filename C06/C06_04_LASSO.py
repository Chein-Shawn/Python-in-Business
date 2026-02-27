import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Lasso
# LASSO: least absolute shrinkage and selection operator，又譯最小絕對值收斂和選擇算子、套索算法

bike = pd.read_csv("gongguan_underfitting.csv") # 時段 + 上班與否 + 氣溫 + 雨量

X = bike.drop(["lent"], axis = 1)
y = bike["lent"]

lm_basic = LinearRegression()                         # 使用全部 27 個自變數

# 4-fold crossvalidation: cv = 4
print(cross_val_score(lm_basic, X, y, cv = 4).mean()) # R^2 = 0.75112

# max_iter = 1000000: maximum iteration
lm_lasso = Lasso(alpha = 0.001, max_iter = 1000000)   # LASSO alpha = 0.001
print(cross_val_score(lm_lasso, X, y, cv = 4).mean()) # R^2 = 0.75114
lm_lasso = Lasso(alpha = 0.005, max_iter = 1000000)   # LASSO alpha = 0.005
print(cross_val_score(lm_lasso, X, y, cv = 4).mean()) # R^2 = 0.75116
lm_lasso = Lasso(alpha = 0.01, max_iter = 1000000)    # LASSO alpha = 0.01
print(cross_val_score(lm_lasso, X, y, cv = 4).mean()) # R^2 = 0.75092
