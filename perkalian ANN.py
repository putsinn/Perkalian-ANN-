import numpy as np 
from sklearn.linear_model import LinearRegression
import pandas as pd

#Database
# x = Data, y = Target
#x = [[1], [3], [5], [7], [9]]
#y = [2, 6, 10, 14, 18]
FileDB = 'perkalian.txt'
Database = pd.read_csv(FileDB, sep=",", header=0)
print ("-------------------------")
print (Database)
#x = Data, y = Target
x = Database[[u'Feature']]
y = Database.Target

regr = LinearRegression().fit(x,y)
regr.score(x, y)

#data Uji 
predict = np.array ([[1100]])

#Menampilkan Data Prediksi
print ("Prediksi")
print ("input = " , predict)
print ("output = " , regr.predict(predict))
