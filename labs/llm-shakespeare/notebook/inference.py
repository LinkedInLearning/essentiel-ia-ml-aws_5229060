import tensorflow as tf
import numpy as np

vocab = sorted(set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!&?.:;,'- \n"))
char2idx = {u: i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim, batch_input_shape=[batch_size, None]),
        tf.keras.layers.LSTM(rnn_units, return_sequences=True, stateful=True),
        tf.keras.layers.Dense(vocab_size)
    ])
    return model

def model_fn(model_dir):
    model = build_model(len(vocab), 256, 1024, batch_size=1)
    model.load_weights(f"{model_dir}/variables/variables")
    return model

def predict_fn(input_data, model):
    input_text = input_data['inputs']
    input_eval = [char2idx[s] for s in input_text]
    input_eval = tf.expand_dims(input_eval, 0)

    text_generated = []
    temperature = 1.0
    model.reset_states()

    for i in range(100):
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0)
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1, 0].numpy()

        input_eval = tf.expand_dims([predicted_id], 0)
        text_generated.append(idx2char[predicted_id])

    return ''.join(text_generated)