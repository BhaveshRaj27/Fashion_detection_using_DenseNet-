# Fashion_detection_using_DenseNet

The Problem here consist of two parts image classification and object detection. Our problem is to detect the clothes present and than detecting the clothes which are present. We start with what is the difference in the image classification and object detection?

**Image Classification** - It is the process of recognizing the objects present in the image. Further it is divided into two parts which are binary classifcation or      multilabel classification. A image may contain a single object or multiple object based on that above two variation were done. Priority in image classification is to get if the object is present in the image but it donot bother with location of the object in the image.

**Object Detection** -  It is the process in which we try to recognize the object as well as try to locate it. It look like it can do work of classification but it is expensive and require more time than classification model to train.

The project is to allow a organization, which can be big fashion industry, or a retail shop, to get the trends which people like to wear in particular season, events or even in a country, which help them to stock clothes based on customer requirement. We are classifying the cloths and counting the particular type of clothes in images that can give us the statistics of the clothes worn by the people more frequently. I also **create DenseNet from The scratch which allow change the size and number of blocks in our model. Further the dataset are in code-words see image in results therfore I have to use object detection to count various clothes in the dataset.**

# DATASET
The consist of 15000 train images, 3000 validation images and 7000 test images. Images contain people wearing clothes or clothes hanging by there own.

![](https://github.com/BhaveshRaj27/Fashion_detection_using_DenseNet-/blob/main/Images/2.jpg)
![](https://github.com/BhaveshRaj27/Fashion_detection_using_DenseNet-/blob/main/Images/3.jpg)
![](https://github.com/BhaveshRaj27/Fashion_detection_using_DenseNet-/blob/main/Images/4.jpg)
![](https://github.com/BhaveshRaj27/Fashion_detection_using_DenseNet-/blob/main/Images/5.jpg)

# Step to follow
**Part A (Classification)**
1. The main task here is to load the images. I used google colab so I extract zip file direct in it. You can choose your own method.
2. Load the images using dataloader function. Give path of images, path of labels and image size required for model.
3. Creating DenseNet from scratch but built Keras DenseNet model (visit the link https://keras.io/api/applications/densenet/)  can also be used. Bulit-in model is trained weights which is easy to train if have low computation power but the DenseNet created in the code provide flexibility to  change the size of input image and denseNet Blocks as per requirement parameter total_iteration in the code allow you to change the size and number of blocks in our model.
4. Create Instance of DenseNet class and use insatnce.Run() which will create the DenseNet Model.
5. Load training and validation image using Data_loader and convert labels into categorical labels using MultiLabelBinarization an dfit data into it. 
6. Train the model using appropriate hyper-parameters. 
7. 7. Further you can save resukt into CSV using pandas.

**Part B (Object Detction)**
In this part, I used pre-trained model for detection of the object and feed the images to the model and get the count of particular type of cloth. For detail explanation object detection see (https://github.com/BhaveshRaj27/Object_Detection-using-YoloV3).

# Result
The Part A contain the imageId and lables.
![](https://github.com/BhaveshRaj27/Fashion_detection_using_DenseNet-/blob/main/Images/Screenshot%20(172).png)

The part B contain top 10 clothes in the market.
![](https://github.com/BhaveshRaj27/Fashion_detection_using_DenseNet-/blob/main/Images/Screenshot%20(173).png)
