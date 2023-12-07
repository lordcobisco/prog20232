from sklearn.svm import SVC 
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer

x = [[1,2],[3,4],[5,6]]
y = [1,0,0]
clf = OneVsRestClassifier (estimator=SVC(
    gamma='scale', random_state= 0))

modelo = clf.fit(x,y)        #Modelo de classificador. Ex: ele pode ser usado para comparar se uma pessoa está realizando a IM ou não como deveria.

for i in range (len(y)):
    print (modelo.predict([x[i]]),y[i]) #função de predição
