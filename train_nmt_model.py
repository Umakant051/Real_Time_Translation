import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Sample Data (Replace with actual data)
input_sequences = ["Hello", "How are you?", "Good morning"]
output_sequences = ["Hola", "¿Cómo estás?", "Buenos días"]

# Tokenization
input_vocab = set(" ".join(input_sequences).split())
output_vocab = set(" ".join(output_sequences).split())

input_word2idx = {word: idx + 1 for idx, word in enumerate(input_vocab)}  # Reserve 0 for padding
output_word2idx = {word: idx + 1 for idx, word in enumerate(output_vocab)}
output_idx2word = {idx: word for word, idx in output_word2idx.items()}

# Convert text to sequences
def text_to_sequence(text, word2idx):
    return [word2idx[word] for word in text.split()]

input_sequences_idx = [text_to_sequence(text, input_word2idx) for text in input_sequences]
output_sequences_idx = [text_to_sequence(text, output_word2idx) for text in output_sequences]

# Padding sequences
max_input_len = max(len(seq) for seq in input_sequences_idx)
max_output_len = max(len(seq) for seq in output_sequences_idx)

input_sequences_idx = pad_sequences(input_sequences_idx, maxlen=max_input_len, padding='post')
output_sequences_idx = pad_sequences(output_sequences_idx, maxlen=max_output_len, padding='post')

# Shift output sequences for teacher forcing
decoder_input_sequences = output_sequences_idx[:, :-1]
decoder_output_sequences = output_sequences_idx[:, 1:]

# Model Parameters
embedding_dim = 256
latent_dim = 256

# Encoder
encoder_inputs = Input(shape=(max_input_len,))
encoder_embedding = Embedding(input_dim=len(input_vocab) + 1, output_dim=embedding_dim)(encoder_inputs)
encoder_lstm, state_h, state_c = LSTM(latent_dim, return_state=True)(encoder_embedding)

# Decoder
decoder_inputs = Input(shape=(max_output_len - 1,))
decoder_embedding = Embedding(input_dim=len(output_vocab) + 1, output_dim=embedding_dim)(decoder_inputs)
decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_embedding, initial_state=[state_h, state_c])
decoder_dense = Dense(len(output_vocab) + 1, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

# Define Model
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)

# Compile the Model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the Model
model.fit([input_sequences_idx, decoder_input_sequences], decoder_output_sequences, epochs=10, batch_size=2)

# Save the Model
model.save('nmt_model.keras')
print("Model saved as nmt_model.keras")



