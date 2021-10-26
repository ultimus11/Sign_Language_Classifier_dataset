import numpy as np
import cv2
dataset = np.load("X.npy")
print("dataset shape:",dataset.shape)
# print("single_image",dataset[0].reshape(64,64))
# cv2.imwrite("first.jpg",dataset[0].reshape(64,64)*255)
for idx,data in enumerate(dataset):
	cv2.imwrite("images/"+str(idx)+".jpg",data.reshape(64,64)*255)