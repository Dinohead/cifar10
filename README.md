This document breifly decribes how to utilize the included scripts, instructions, and code to build TensorFlow
on a fresh install of Ubuntu Server 16.04, compile the Inception v3 model, retrain the final layer to a 
specific set of imagaes, and use the model to create predictions for a test set of images.

The author does not claim credit for all of this code. Inception and TensorFlow are open source and information can
be found here:

https://github.com/tensorflow/models/tree/master/inception
https://www.tensorflow.org/
https://www.tensorflow.org/versions/r0.9/how_tos/image_retraining/index.html#bottlenecks

The tensorTest.py is modified version of a python script found here:

https://github.com/eldor4do/Tensorflow-Examples/blob/master/retraining-example.py

imageAugmentor.py is modified version of a python script found here:

https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html


Step 1: Install TensorFlow on Ubuntu Server 16.04

Use the "Install TensorFlow.txt" file as a guide to build TensorFlow on a new or exsiting image of Ubuntu 16.04.
This method has been tested on a new install of Ubuntu Server 16.04 (no GUI) but it should work on any Ubuntu 16.04
distribution or an exsiting install.





Step 2: Put train and test images on the Ubuntu machine

Images for training the inception model must be in .jpg format and sorted into directories named with the image label.
The images should be labeled sequentially from 1..n with no numbers repeated. Each number should be unique regardless
of the directory that it is in.

Here is an example of the required folder structure for the first 15 imagaes from CIFAR-10 dataset.

-Train
	-airplane

	
		8.jpg
		
		11.jpg
		
		14.jpg
		
		.......

	-automobile

		2.jpg

		6.jpg

		.......

	-bird

		3.jpg

		15.jpg

		.......

	-cat

		7.jpg

		9.jpg

		.......

	-deer

		13.jpg

		.......

	-dog

		10.jpg

		12.jpg

		.......

	-frog

		.......

	-horse

		5.jpg

		.......

	-ship

		1.jpg

		.......

	-truck

		4.jpg
		
Notice that all numbers from 1..15 are included and none are repeated. If the images are not sorted and labeled
correctly it will likely break the included scripts.

For the test image directory, all images should be placed in a single direcotry and labled from 1..n with no missing
values.





Step 2.5: This is specific to my Contest 2 submission

The images for the contest were provided as a csv of pixel values. The images had to be converted back to jpg format and sorted 
into directories. The "imageConverter.R" script was used to convert the train.csv file to a training direcotry with all images
sorted and in the proper format.

The images were then moved to the ubuntu machine by mounting a cifs volume. SCP could also be used. Actually moving the images over
could be accomplished in a variety of ways and is left up to the user.




Step 3: Build the Inception v3 Model and train the final layer

During step one TensorFlow was installed and it's source code was downloaded. The Inception v3 model is built
from the TensorFlow source code. The installed version of TensorFlow is then used to train, run, and utilize the
model.

Use "build inception model.txt" as a guide to build and train the final layer of the Inception model. All pictures
should be present on the Ubuntu machine and in the proper format and directories at this point.




Step 4: Start Predicting!

I am assuming the bash script, tensorTest, and Test directory are all in the same directory. Teaching linux
command line is not within the scope of this so hopefully you can follow along...



Edit the imagePath variable in the "tensor Test.py" script to to point to the directory containing the test images.
the "%s.jpg' % (sys.argv[1])" part should be left as is. This is what takes an argument from the system when the 
script is called.

Edit the output file to point to where the results file is. This file should be created if it doesn't already exist. 
Use the command:

touch filename

to create the file if necassary.

Now your ready to start predicting. This can be done in two ways. One at a time by calling the tensorTest.py script
or as batch to predict on multiple images.

To predict on a single image (image 35.jpg), use the command:

python tensorTest.py 35

The "35" tells the script which image to predict and any number can be presented to the script. The script will output
the the image number and it's prediction to the console. It will also append the prediction to the output file defined 
above.

To predict a batch of images start by editing the tensorBash script with the range of images you would like to predict.
The first time you use the tensorBash script you will have the give it permission to run with:

sudo chmod 755 tensorBash

You will also probably want to clear your output file:

rm filename && touch filename

The bash script can then be run with:

./tensorBash

The bash script will then start calling the tensorTest.py script over and over to predict your images.

After completion your output file should be a csv with all of your predictions

Note: It should be noted that a more elegant solution would be to do this entirely in python. I tried that. I
attempted to loop inside the python script but no matter how I coded it I always had a memory leak. Eventually 
the script would eat up all of the system memory and then crash. It would be good to figure that out and write
a proper python script to predict over a range of images. I assume that would be a much faster implementation.



Step 5: Convert the output file to a properly formated .csv for whatever

Use the "createCSV.R" script to read in the outputfile and format it as a proper csv. This file also converts
the labels to the corrisponding label number.

