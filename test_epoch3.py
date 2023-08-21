import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.layers import Activation, Dense, Dropout
from keras.models import Sequential, load_model
from keras import optimizers
from keras.utils.np_utils import to_categorical
import tensorflow as tf

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 784)[:6000]
X_test = X_test.reshape(X_test.shape[0], 784)[:1000]
y_train = to_categorical(y_train)[:6000]
y_test = to_categorical(y_test)[:1000]

model = Sequential()
model.add(Dense(256, input_dim=784))
model.add(Activation("sigmoid"))
#여기서는 Dropout을 사용하지 않는다
model.add(Dense(10))
model.add(Activation("softmax"))

sgd = tf.optimizers.SGD(lr=0.1)

model.compile(optimizer=sgd, loss="categorical_crossentropy",
metrics=["accuracy"])

def funcA():
  global epochs
  epochs=5

def funcB():
  global epochs
  epochs=10

def funcC():
  global epochs
  epochs=60

funcA()
#funcB()
#funcC()

history=model.fit(X_train, y_train, batch_size=32, epochs=epochs,
                  verbose=1, validation_data=(X_test, y_test))

plt.plot(history.history["accuracy"], label="acc", ls="-", marker="o")
plt.plot(history.history["val_accuracy"], label="val_acc", ls="-", marker="x")
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend(loc="best")
plt.show()

score=model.evaluate(X_test, y_test, verbose=0)
print("evaluate loss: {0[0]}\nevaluate acc:{0[1]}".format(score))

