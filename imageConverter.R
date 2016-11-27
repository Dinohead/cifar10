library(OpenImageR)
setwd("~/Downloads")
#train and test directories with proper folder strucutre should already
#be created and empty in the woring directory, also the sample image
#should be present

#read in data
#train <- read.csv("train.csv")
test <- read.csv("test.csv")

#a = NULL
#b = NULL

#sample image to setup dataframe
b <- readImage("sample.png")

#loop write pictures one at a time
#there might be more R-like vector way to do this... but his works
#can use on train and test with proper commenting
###########beginning of loop######################
for(i in 1:5000){

  cat(i, "\r")

# drop image into dataframe and convert values to 0..1  
# a = train[i,-1,drop=FALSE]
  a = test[i,]  
  a = a/255

# drop image into the properly formatted dataframe
  b[,,1]<- as.matrix(a[1,(1:1024)])
  b[,,2]<- as.matrix(a[1,(1:1024)+1024])
  b[,,3]<- as.matrix(a[1,(1:1024)+2048])

#for some reason images are sideways, rotate them back
  b <- rotateFixed(b,90)
  
#comment out switch statment if running on test
# writeImage(b, paste( "train/",
  writeImage(b, paste( "test/",        
                       
#                        switch(train$y[i],"airplane", "automobile", "bird", 
#                              "cat", "deer", "dog", "frog", 
#                              "horse", "ship", "truck"), "/", 

                        toString(i),".png",sep = "" ))
}
###########end of loop############################
