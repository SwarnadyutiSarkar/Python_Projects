import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import regularizers

# Parameters
vocab_size = 10000
max_length = 200
embedding_dim = 128
lstm_units = 64
batch_size = 32
epochs = 5

# Load IMDb movie reviews dataset
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=vocab_size)

# Pad sequences to have consistent length
train_data = pad_sequences(train_data, maxlen=max_length)
test_data = pad_sequences(test_data, maxlen=max_length)

# Original LSTM model
model = Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_length),
    LSTM(lstm_units, dropout=0.2, recurrent_dropout=0.2),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the original LSTM model
model.fit(train_data, train_labels, batch_size=batch_size, epochs=epochs, validation_data=(test_data, test_labels))

# Evaluate the original LSTM model
loss, accuracy = model.evaluate(test_data, test_labels)
print(f"Original Test Loss: {loss:.4f}")
print(f"Original Test Accuracy: {accuracy*100:.2f}%")

# Build and train Bidirectional LSTM model
model_bidirectional = Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_length),
    Bidirectional(LSTM(lstm_units, dropout=0.2, recurrent_dropout=0.2)),
    Dense(1, activation='sigmoid')
])

model_bidirectional.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_bidirectional.fit(train_data, train_labels, batch_size=batch_size, epochs=epochs, validation_data=(test_data, test_labels))

# Build and train Stacked LSTM model
model_stacked = Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_length),
    LSTM(lstm_units, dropout=0.2, recurrent_dropout=0.2, return_sequences=True),
    LSTM(lstm_units, dropout=0.2, recurrent_dropout=0.2),
    Dense(1, activation='sigmoid')
])

model_stacked.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_stacked.fit(train_data, train_labels, batch_size=batch_size, epochs=epochs, validation_data=(test_data, test_labels))

# Download and load GloVe embeddings (run this code outside of the main script)
# !wget http://nlp.stanford.edu/data/glove.6B.zip
# !unzip glove.6B.zip

# Load GloVe embeddings
embeddings_index = {}
with open('glove.6B.100d.txt', encoding='utf-8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs

# Create embedding matrix
embedding_matrix = np.zeros((vocab_size, embedding_dim))
for word, i in word_index.items():
    if i < vocab_size:
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector

# Use GloVe embeddings in the model
model_glove = Sequential([
    Embedding(vocab_size, embedding_dim, weights=[embedding_matrix], input_length=max_length, trainable=False),
    LSTM(lstm_units, dropout=0.2, recurrent_dropout=0.2),
    Dense(1, activation='sigmoid')
])

model_glove.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_glove.fit(train_data, train_labels, batch_size=batch_size, epochs=epochs, validation_data=(test_data, test_labels))

# Build and train Regularized LSTM model with Early Stopping
model_regularized = Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_length),
    LSTM(lstm_units, dropout=0.2, recurrent_dropout=0.2, kernel_regularizer=regularizers.l2(0.01)),
    Dense(1, activation='sigmoid')
])

model_regularized.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
early_stopping = EarlyStopping(monitor='val_loss', patience=2)
model_regularized.fit(train_data, train_labels, batch_size=batch_size, epochs=epochs, validation_data=(test_data, test_labels), callbacks=[early_stopping])

# Generate predictions from multiple models
pred1 = model.predict(test_data)
pred2 = model_bidirectional.predict(test_data)
pred3 = model_stacked.predict(test_data)

# Average predictions
ensemble_pred = (pred1 + pred2 + pred3) / 3

# Evaluate ensemble predictions
ensemble_loss, ensemble_accuracy = model.evaluate(test_data, test_labels)
print(f"Ensemble Test Loss: {ensemble_loss:.4f}")
print(f"Ensemble Test Accuracy: {ensemble_accuracy*100:.2f}%")
