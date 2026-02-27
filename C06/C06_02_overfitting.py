import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

bike = pd.read_csv("gongguan_overfitting.csv") # 或 _underfitting、_overfitting 兩個檔案 

X = bike.drop(["lent"], axis = 1) # 自變數
y = bike["lent"]                  # 應變數

train_X, valid_X, train_y, valid_y = train_test_split(X, y, test_size = 0.3)

lm = LinearRegression()
lm.fit(train_X, train_y) # 用訓練資料建構迴歸模型
print("R Square:    ", lm.score(train_X, train_y)) # 訓練誤差

predicted_y = lm.predict(valid_X) # 代入驗證資料集的自變數，求得預測值
rss = ((predicted_y - valid_y) ** 2).mean()
tss = ((valid_y.mean() - valid_y) ** 2).mean()
print(1 - rss / tss) # 驗證誤差
