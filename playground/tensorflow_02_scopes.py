import tensorflow as tf

# To be used as a reference!
# Don't run this because it will do nothing

with tf.variable_scope('MyModel'):
    # Full name will e 'MyModel/v'
    foo = tf.get_variable('v', shape=[], initializer=1)
    # will be 'MyModel/bar'
    bar = tf.add(foo, 5, name='bar')
