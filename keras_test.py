from keras.models import Sequencial
from keras.layers import Dense, Activation, Noise, Dropout
from random_data import generateData



model = Sequencial()
model.add(Dense(32, input_shape=(200,)))
model.add(Dense(7, input_shape=(32,),activation='softmax')
#model.add(GaussianNoise(stddev))
#model.add(GaussianDropout(0.5))

#keras.layers.noise.GaussianNoise(stddev)
#keras.layers.noise.GaussianDropout(0.5)


model.compile()

test_data = generateData(200)

fit(self, test_data, 'Array', batch_size=200, epochs=50, verbose=2, callbacks=None)
