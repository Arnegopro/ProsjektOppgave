from keras.models import Sequential
from keras.layers import Dense, Activation, BatchNormalization, GaussianNoise, GaussianDropout
from random_data import generateData


#Sequential model
model = Sequential()

#Densing ("Transmitter")
model.add(Dense(32, input_shape=(200,)))
model.add(Dense(7, input_shape=(32,),activation='softmax'))
#Normalization
model.add(BatchNormalization())
#Adding noise (channel simulation)
model = GaussianNoise(0.5)(model)
model = GaussianDropout(0.5)(model)
#Densing ("Receiver")
model.add(Dense(32, input_shape=(7,),activation='softmax'))
model.add(Dense(200, input_shape=(32,)))


model.compile()

test_data = generateData(200)

fit(self, test_data, 'Array', batch_size=200, epochs=50, verbose=2, callbacks=None)
