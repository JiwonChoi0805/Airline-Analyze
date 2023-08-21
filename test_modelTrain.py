from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from keras.models import load_model

from sklearn.datasets import load_boston
from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt

#학습정보 지정
epoch_num = 500  
learn_rate = 0.005  
neuron_num = 10 

do_train = True  


X, y = load_boston(return_X_y=True)

X_shape = X.shape  

boston_scaler = MinMaxScaler()  
norm_X = boston_scaler.fit_transform(X)  

if do_train:

    norm_X_train = norm_X[:-50]
    y_train = y[:-50]

    norm_X_test = norm_X[-50:]
    y_test = y[-50:]

#모델 생성
    model = Sequential()  
    model.add(Dense(neuron_num, input_dim=X_shape[1], activation='tanh'))  
    model.add(Dense(neuron_num, activation='tanh'))  
    model.add(Dense(1, activation="linear")) 
    model.summary() 

    adam_optimizer = Adam(lr=learn_rate, beta_1=0.9, beta_2=0.999, amsgrad=False) 
    model.compile(loss='mse', optimizer=adam_optimizer) 

    # hist = model.fit(norm_X_train, y_train, epochs=epoch_num)
    hist = model.fit(norm_X_train, y_train, verbose=0, epochs=epoch_num)

    plt.figure(1)
    plt.title('Learning Curve')
    plt.plot(hist.history['loss'])
    plt.show()

    y_est_train = model.predict(norm_X_train) 

    plt.figure(2)
    plt.title('Estimation on Train Dataset')
    plt.plot(y_train, label='answer', c='b')  
    plt.plot(y_est_train, label='estimation', c='r')
    plt.legend() 
    plt.show()

#데이터 추정하기
    y_est_test = model.predict(norm_X_test) 

    plt.figure(3)
    plt.title('Estimation on Test Dataset')
    plt.plot(y_test, label='answer', c='b')
    plt.plot(y_est_test, label='estimation', c='r')
    plt.legend() 
    plt.show()

    model.save('my_model.hdf5') 
else:
    model =  load_model('my_model.hdf5')

    y_est = model.predict(norm_X) 

    plt.figure()
    plt.title('Estimation on Whole Dataset')
    plt.plot(y, c='b')  
    plt.plot(y_est, c='r') 
    plt.show()()