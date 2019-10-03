#To analyse the data coming from the chatbot(application)
import tensorflow as tf

#node1 = tf.constant(3.09,tf.float64)
#node2 = tf.constant(4.0)

#print(node1,node2)
#print(sess.run([node1,node2]))
#with tf.Session() as sess:
#    output = sess.run([node1,node2])
 #   print(output)

#a = tf.constant(4.05)
#b = tf.constant(5.07)
#d = tf.constant(9.05)
#r = tf.constant(18.6)
#c = (((a * b) + d)*r)
#sess = tf.Session()
#File_Writer = tf.summary.FileWriter("C:\\Users\\Samarth\\PycharmProjects\\Learning\\graph",sess.graph)
#print(sess.run(c))
#sess.close()
A = tf.placeholder(tf.float32)
B = tf.placeholder(tf.float32)
C = A + B
sess = tf.Session()
print(sess.run(C,{A:[4,7],B:[5,6]}))
s = tf.Variable([0.3],tf.float32)                    #How this works
j = tf.Variable([-0.3],tf.float32)                     #for value :s = -1,x = 1 and j = 1
x = tf.placeholder(tf.float32)                        #s*x+j
#tf.gfile.DeleteRecursively("C:\\Users\\Samarth\\PycharmProjects\\Learning\\graph")                                                     #-1*1 +1=0
Linear_Model = s*x+j

y = tf.placeholder(tf.float32)
#Define loss function
squared_values = tf.square(Linear_Model-y)
loss = tf.reduce_sum(squared_values)
#optimize the model
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)


init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(1000):
    sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})
#print(sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]}))
print(sess.run([s,j]))

graph2 = tf.Graph()
#File_Writer = tf.summary.FileWriter("C:\\Users\\Samarth\\PycharmProjects\\Learning\\graph2",sess.graph)
#tf.gfile.DeleteRecursively("C:\\Users\\Samarth\\PycharmProjects\\Learning\\graph2")
with graph2.as_default():
    Scalar = tf.constant(2.0,tf.float32)
    Vector = tf.constant([5,6,3],tf.float32)
    Matrix = tf.constant([[4,3,2],[4,6,7],[9,8,4]])
    Tensor = tf.constant( [ [[4,5,7],[7,8,6],[2,3,8],[7,9,8]] ] )
with tf.Session(graph=graph2) as sess:
    result = sess.run(Scalar)
    print("Scalar(1entry) \n %s \n" % result)
    result = sess.run(Vector)
    print("Vector(3 entry) \n %s \n" % result)
    result = sess.run(Matrix)
    print("Matrix (3x3 entry) \n %s \n" % result)
    result = sess.run(Tensor)
    print ("Tensor (3x3x3 entry) \n %s \n" % result)
sess.close()
Scalar.shape
Vector.shape
Tensor.shape

graph3 = tf.Graph()
File_Writer = tf.summary.FileWriter("C:\\Users\\Samarth\\PycharmProjects\\Learning\\graph3",sess.graph)
#tf.gfile.DeleteRecursively("C:\\Users\\Samarth\\PycharmProjects\\Learning\\graph3")
with graph3.as_default():
    Matrix_1 = tf.constant([[3,6,7],[4,5,8],[4,7,0]])
    Matrix_2 = tf.constant([[9,8,6],[3,6,5],[8,9,7]])
add_operation = tf.add(Matrix_1,Matrix_2)
with tf.Session(graph = graph3) as sess:
    result = sess.run(add_operation)
    print("Result calculated by tensorflow")
    print(result)
sess.close()
graph4 = tf.Graph()
with graph4.as_default():
    Tensor_A = ([[3,4,5],[6,8,9],[9,0,8]])
    Tensor_B = ([[4,5,8],[9,8,1],[7,6,3]])
    mul_operation = tf.multiply(Tensor_A,Tensor_B)
with tf.Session(graph = graph4) as sess:
    result = sess.run(mul_operation)
    print("Result calculated by tensor")
    print(result)

v = tf.Variable(0)
update = tf.assign(v,v+1)
init_op = tf.global_variables_initializer()
with tf.Session() as session:
    session.run(init_op)
    print(session.run(v))
    for _ in range(30):
        session.run(update)
        print(session.run(v))

graph5 = tf.Graph()
with graph5.as_default():
    a = tf.constant(9)
    b = tf.constant(7)
    c = tf.add(a,b)
    d = tf.subtract(a,b)

with tf.Session(graph = graph5) as sess:
    result_1 = sess.run(c)
    print("addition by tensorflow")
    print(result_1)
    result_2 = sess.run(d)
    print("subtraction done by tensorflow")
    print(result_2)