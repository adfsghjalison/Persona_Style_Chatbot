import tensorflow as tf
import os

tf.app.flags.DEFINE_string('mode', 'train', 'train / test / val')
tf.app.flags.DEFINE_string('model_dir', 'model', 'output model weight dir')
tf.app.flags.DEFINE_string('data_dir', 'data', 'data dir')
tf.app.flags.DEFINE_string('data_name', 'BG', 'data name')
tf.app.flags.DEFINE_string('load', '', 'loaded model name')
tf.app.flags.DEFINE_string('output', 'output', 'output name')
tf.app.flags.DEFINE_float('scale', 1.0, 'style score')
tf.app.flags.DEFINE_integer('batch_size', 50, 'batch size')
tf.app.flags.DEFINE_integer('latent_dim', 256, 'latent size')
tf.app.flags.DEFINE_integer('sequence_length', 10, 'sentence length')

"""
tf.app.flags.DEFINE_integer('printing_step', 1, 'printing step')
tf.app.flags.DEFINE_integer('saving_step', 2, 'saving step')
tf.app.flags.DEFINE_integer('num_step', 4, 'number of steps')
"""
tf.app.flags.DEFINE_integer('printing_step', 1000, 'printing step')
tf.app.flags.DEFINE_integer('saving_step', 10000, 'saving step')
tf.app.flags.DEFINE_integer('num_step', 100000, 'number of steps')

FLAGS = tf.app.flags.FLAGS

FLAGS.data_dir = os.path.join(FLAGS.data_dir, 'data_{}'.format(FLAGS.data_name))
FLAGS.model_dir = os.path.join(FLAGS.model_dir, 'model_{}_{}'.format(FLAGS.data_name, FLAGS.latent_dim))
if FLAGS.output == 'output':
  FLAGS.output = os.path.join(FLAGS.output, 'output_{}_Persona_{}_{}'.format(FLAGS.data_name, FLAGS.latent_dim, FLAGS.scale))

if not os.path.exists(FLAGS.model_dir):
  os.mkdir(FLAGS.model_dir)
  print ('Create model dir : {}'.format(FLAGS.model_dir))

