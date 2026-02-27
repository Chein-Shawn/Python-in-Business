import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

bike = pd.read_csv("gongguan_underfitting.csv") 

X = bike.drop(["lent"], axis = 1)
y = bike["lent"]

lm = LinearRegression()
print(cross_val_score(lm, X, y, cv = 4).mean()) # 4-fold 交互驗證後的驗證 R^2
