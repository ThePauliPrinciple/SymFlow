
import tensorflow as tf
from symflow import SymLayer,AddLayer



add=AddLayer()

x=tf.keras.layers.Input(1)
y=tf.keras.layers.Input(1)

Model=tf.keras.models.Model(inputs=[x,y],outputs=add([x,y]))
print(Model([[3],[3]]))


print(add([2,2]))


