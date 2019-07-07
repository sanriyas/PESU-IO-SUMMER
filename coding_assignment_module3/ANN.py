from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
import numpy as np

np.random.seed(2)
#dataset included in folder
dataset = np.loadtxt('C:\\Users\Sanriya\Desktop\pima_indian_diabetes.csv', delimiter=',',skiprows=1)
data = dataset[:,0:8]
output = dataset[:,8]

x_train, x_test, y_train, y_test = train_test_split(data, output, test_size=0.2, random_state=2)

model = Sequential()
model.add(Dense(15, input_dim=8, activation='relu')) #input layer
model.add(Dense(10, activation='relu'))              #hidden layer
model.add(Dense(1, activation='sigmoid'))            #output layer. possible output are (0,1) hence sigmoid
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])
model.fit(x_train, y_train, epochs = 100,batch_size = 10 , validation_data=(x_test, y_test))

loss,acc=model.evaluate(x_test, y_test)
print("\nAccuracy: ",acc," Loss: ",loss)

from sklearn.metrics import confusion_matrix
y_pred=model.predict_classes(x_test)
matrix=confusion_matrix(y_test,y_pred)
print("\nConfusion Matrix: \n",matrix)
