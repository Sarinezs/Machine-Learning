from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD
import matplotlib.pyplot as plt

train_path  = './Training'
test_path  = './test'

train_images = ImageDataGenerator().flow_from_directory(train_path,
                                                        target_size=(227,227),
                                                        batch_size = 32)

train_images = ImageDataGenerator().flow_from_directory(train_path,
                                                        target_size=(227,227),
                                                        batch_size = 32)

base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(227,227,3))

for layer in base_model.layers:
  layer.trainable = False

# base_model.summary()

last_layer = base_model.get_layer('conv5_block3_out')
last_output = last_layer.output

x = Flatten()(last_output)

x = Dense(100, activation='relu', name='FC_dense')(x)
x = Dense(5, activation='softmax', name='softmax')(x)

new_model = Model(inputs=base_model.input, outputs = x)
# new_model.summary()

new_model.compile(SGD(learning_rate=0.00004), loss='categorical_crossentropy', metrics=['accuracy'])

history = new_model.fit(train_images, steps_per_epoch=1, epochs=3, validation_data=train_images, validation_split=0.1)

plt.plot(history.history['loss'], label='training loss')
plt.plot(history.history['val_loss'], label='validation loss')
plt.title('Training')
plt.xlabel('Epochs')
plt.ylabel('loss')
plt.legend()
plt.grid(True)
plt.show()
