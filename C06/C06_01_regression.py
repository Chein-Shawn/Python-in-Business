# ===============================================
# import libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
# ===============================================




# ===============================================
# loading the data
bike = pd.read_csv("gongguan.csv") # read the data
print(bike.head()) # take a look at the data

# construct a regression model
lm = LinearRegression() 

# using precipitation as the independent variable
# reshape(-1, 1) 的作用是將陣列轉換為 「不限列數，但只有 1 欄」 的二維陣列
lent = bike["lent"].values.reshape(-1, 1) # reshape the data
pre = bike["precipitation"].values.reshape(-1, 1)

# train the model
lm.fit(pre, lent) 

# take a look at the model
print("Coefficients:", lm.coef_) 
print("Intercept:   ", lm.intercept_)
print("R Square:    ", lm.score(pre, lent)) # R^2
# ===============================================




# ===============================================
# using temperature as the independent variable
temp = bike["temperature"].values.reshape(-1, 1)

lm.fit(temp, lent) 

print("Coefficients:", lm.coef_)
print("Intercept:   ", lm.intercept_)
print("R Square:    ", lm.score(temp, lent))
# ===============================================




# ===============================================
# adding the squared temperature
temp = bike["temperature"].values.reshape(-1, 1)
tempSq = pow(temp, 2)
X_temp = np.hstack((temp, tempSq))  # be something like a nx2 matrix

lm.fit(X_temp, lent) 

print("Coefficients:", lm.coef_)
print("Intercept:   ", lm.intercept_)
print("R Square:    ", lm.score(X_temp, lent))
# ===============================================




# ===============================================
# using all variables we have
working = bike["workingday"].values.reshape(-1, 1) 

# hour 實際上是類別變數，不是數值變數, 要當作dummy variable處理
# 24x1 matrix becomes 24x2 matrix that contains 0 and 1 in the column to indicate whether it is that hour
hourFactor = pd.get_dummies(bike["hour"]) # creating dummy variables

X_full = np.hstack((hourFactor, working, temp, tempSq, pre)) 

lm.fit(X_full, lent)

print("Coefficients:", lm.coef_)
print("Intercept:   ", lm.intercept_)
print("R Square:    ", lm.score(X_full, lent))
# ===============================================





# ===============================================
# bike_future = pd.read_csv("gongguan_future.csv") 
bike_future = pd.read_csv("gongguan.csv") 
print(bike_future.head())

hourFactor = pd.get_dummies(bike_future["hour"]) 
working = bike_future["workingday"].values.reshape(-1, 1) 
temp = bike_future["temperature"].values.reshape(-1, 1)
tempSq = pow(temp, 2)
pre = bike_future["precipitation"].values.reshape(-1, 1)

X_future = np.hstack((hourFactor, working, temp, tempSq, pre)) 

lent_predict = lm.predict(X_future)

print(lent_predict)
# ===============================================



# ===============================================
# visualizing the result
import matplotlib.pyplot as pyplot

pyplot.plot(bike["temperature"].values, bike["lent"].values, "bo")
pyplot.plot(temp, lent_predict, "ro")
pyplot.show()
# ===============================================
