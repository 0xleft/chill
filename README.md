# About

This is an experiment to learn more about neural network architectures.

## Explore

Feel free to explore:
* [data transformation](data.ipynb)
* [experimental training](training.ipynb)
* [final model training](training_count.ipynb)

## Final

```
Epoch 22/22
131/131 [==============================] - 14s 106ms/step - loss: 0.0806 - accuracy: 0.9761 - val_loss: 0.5511 - val_accuracy: 0.8929
```

90% accuracy on the validation set is pretty good. I'm happy with this result.

## Model

```
model.add(Conv2D(128, (11, 11), input_shape=(150, 150, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, (5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, (5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(200, (1, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(2048, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(2048, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(2048, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(len(classes), activation='softmax'))
```