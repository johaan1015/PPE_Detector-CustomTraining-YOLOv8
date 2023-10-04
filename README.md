# PPE_Detector-CustomTraining-YOLOv8
###Dataset
* The dataset used for custom training need to be in a particular format. The directory needs to contain -train -test -valid folders which has images folder containg images and labels folder which contain text file for each image which has the class id and coordinates for every detections in the image.
* The directory also needs to contain a data,yaml file which connects all these folders, which contains information regarding the number of classes and a list containing the class names.

###Training
* The training is done using YOLOv8 where we use transfer learning to tune our weights on our new dataset.
* After training we download the best.pt file which has the best weights for the model.
* This is then used for detection in our ppe videos.
