#tensorTest.py is modified version of a python script found here:

#https://github.com/eldor4do/Tensorflow-Examples/blob/master/retraining-example.py


#this script takes an argument when called. The argument should be
#the number of the image you would like to predict

#The variable imagePath is used to set the location of the test image folder
#The variable outputFile is used to set the location of the outputFile


import numpy as np
import tensorflow as tf
import gc
import sys

imagePath = '/home/drock/contest02/test/%s.jpg' % (sys.argv[1])
modelFullPath = '/tmp/output_graph.pb'
labelsFullPath = '/tmp/output_labels.txt'
outputFile = 'results'


def create_graph():
    """Creates a graph from saved GraphDef file and returns a saver."""
    # Creates graph from saved graph_def.pb.
    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')


def run_inference_on_image():

    answer = None

    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('File does not exist %s', imagePath)
        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    # Creates graph from saved GraphDef.
    create_graph()

    with tf.Session() as sess:

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-5:][::-1]  # Getting top 5 predictions
        f = open(labelsFullPath, 'rb')
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]


        print('%s %s' % (sys.argv[1], labels[top_k[0]]))
        answer = labels[top_k[0]]

	with open(outputFile, "a") as myfile:
           myfile.write("%s, %s\n" % (sys.argv[1],labels[top_k[0]]))

        return answer


if __name__ == '__main__':
	run_inference_on_image()
