from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np

digit=datasets.load_digits()
x_train,x_test,y_train,y_test = train_test_split(digit.data,digit.target,train_size=0.6)

s=svm.SVC(gamma=0.001)
s.fit(x_train,y_train)

res=s.predict(x_test)

conf=np.zeros((10,10))
for i in range(len(res)):
    conf[res[i]][y_test[i]]+=1
print(conf)

no_correct=0
for i in range(10):
    no_correct+=conf[i][i]
accuracy=no_correct/len(res)

print("테스트 접합에 대한 정확률은",accuracy*100,"%입니다.")