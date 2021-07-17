# Day_12_03_sklearn.py
from sklearn import datasets, svm
import numpy as np

iris = datasets.load_iris()

clf = svm.SVC()
clf.fit(iris['data'], iris['target'])

print('acc :', clf.score(iris['data'], iris['target']))     # acc : 0.9733333333333334

y_hats = clf.predict(iris['data'])
print(y_hats)

equals = (y_hats == iris['target'])
print(equals)       # True : 정답, False: 오답

print('acc :', np.mean(equals))     # 평균 계산, acc : 0.9733333333333334
