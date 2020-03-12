import tensorflow as tf
import random

print(tf.__version__)

# Nodes as tf.Operation
# Edges as tf.Tensor

# Definition Phase: builds computational graph tf.Graph
# Execution Phase: feeding data and fetching results from the graph tf.Session

graph = tf.Graph()

# Definition phase
with graph.as_default():
    # Placeholder = will contain an input
    x = tf.placeholder(tf.float32, shape=[], name='x')
    # A variale, something that it's gonna be learned
    A = tf.get_variable('A', shape=[], dtype=tf.float32,
                        # Initializer defines value on the first run
                        initializer=tf.initializers.random_normal())
    # Constant (assigning value), will keep value between runs
    b = tf.random_normal(shape=[], dtype=tf.float32, name='b')
    y = A * x  # Liniar regressor (1/2)
    z = y + b  # Liniar regressor (2/2)

# Execution phase
with tf.Session(graph=graph) as session:
    session.run(tf.global_variables_initializer())
    result = session.run(z, feed_dict={x: random.random()})

print(result)
