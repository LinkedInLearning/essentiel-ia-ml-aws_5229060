# common libraries
import os
import numpy as np
import tarfile

# aws libraries
import boto3

# SageMaker related
import sagemaker
from sagemaker.tensorflow import TensorFlowModel

# tensorflow related
import tensorflow as tf
from tensorflow.keras import layers


# === 1. Download & Preprocess Shakespeare Dataset ===

path_to_file = tf.keras.utils.get_file("shakespeare.txt", 
                                       "https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt")

text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
vocab = sorted(set(text))

char2idx = {u: i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)
text_as_int = np.array([char2idx[c] for c in text])

seq_length = 100
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
sequences = char_dataset.batch(seq_length + 1, drop_remainder=True)

def split_input_target(chunk):
    return chunk[:-1], chunk[1:]

dataset = sequences.map(split_input_target)
dataset = dataset.shuffle(10000).batch(64, drop_remainder=True)


# === 2. Build & Train Model ===

vocab_size = len(vocab)
embedding_dim = 256
rnn_units = 1024

def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    return tf.keras.Sequential([
        layers.Embedding(vocab_size, embedding_dim),
        layers.LSTM(rnn_units, return_sequences=True, stateful=True),
        layers.Dense(vocab_size)
    ])

model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=64)
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))
model.fit(dataset, epochs=3)


# === 3. Save Model in .keras format ===

os.makedirs('model', exist_ok=True)
model_path = 'model/shakespeare_model.keras'
model.save(model_path)


# === 4. Compress Model Directory ===

tar_path = 'shakespeare_model.tar.gz'
with tarfile.open(tar_path, mode='w:gz') as archive:
    archive.add('model', arcname='.')  # add model directory


# === 5. Upload to S3 ===

sagemaker_session = sagemaker.Session()
role = sagemaker.get_execution_role()

model_artifact = sagemaker_session.upload_data(path=tar_path, key_prefix='models/shakespeare')


# === 6. Deploy Model using TensorFlowModel ===

tf_model = TensorFlowModel(model_data=model_artifact,
                           role=role,
                           framework_version='2.11',
                           entry_point='inference.py')  # Make sure inference.py is in the same directory

predictor = tf_model.deploy(initial_instance_count=1, instance_type='ml.m5.large')
