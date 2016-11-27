#Use this script to generate batches of augmented images.
#Images should be in a single directory labeled sequentially
#Set the source directory, target directory, first image number, last image number
#the numberAugs variable controls how many images are generated

#this script was modified from the script found here:

#https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

sourceDirectory = 'train1/truck'
targetDirectory = 'train2/truck'
firstInputImage = 4502
lastInputImage = 5000
numberAugs = 10

for loopVal in xrange(firstInputImage, lastInputImage + 1):

	datagen = ImageDataGenerator(
        	rotation_range=40,
	        width_shift_range=0.2,
	        height_shift_range=0.2,
	        shear_range=0.2,
	        zoom_range=0.2,
	        horizontal_flip=True,
	        fill_mode='nearest')

	loadImage = sourceDirectory + '/' + str(loopVal) + '.jpg'

	img = load_img(loadImage) # this is a PIL image
	x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
	x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

#	print('%s' % (loopVal))

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
	i = 0
	for batch in datagen.flow(x, batch_size=1,
                          save_to_dir=targetDirectory, save_prefix=loopVal, save_format='jpg'):
	    i += 1
	    print('i = %s, loopVal = %s' % (i,loopVal))
	    if i > numberAugs - 1:
	        break  # otherwise the generator would loop indefinitely
