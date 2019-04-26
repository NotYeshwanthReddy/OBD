"""Developer: Yeshwanth Reddy	"""
"""Enroll no: U101116FCS155		"""

"""
Reference: 
https://gist.github.com/rahit/c078cabc0a48f2570028bff397a9e154
"""


"""
Description: 
Works best on salt and pepper noise
"""

"""The following problem is of three marks.
Download five images affected by Gaussian noise and five images affected by
Salt and Pepper noise. Perform edge detection of these noisy images using
Sobel, Prewitt, and Canny edge detection methods. Denoise these original
images using Gaussian filtering and then again perform edge detection using
the above edge detection methods. Observe and compare the edge detection
in noisy images and images after denoising. You are allowed to use standard
functions available in Python/Matlab for edge detection and filtering."""


import cv2
import numpy as np
from matplotlib import pyplot as plt


def color2gray(input_img):
	return cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)

def GaussianDenoise(gray):
	return cv2.GaussianBlur(gray,(3,3),0)

def Boundary(input_img, input_image_name):
	output_name = "../resources/images/output/" + input_image_name.split("/")[-1][:-4] + "_Original.jpg"
	output_canny_name = "../resources/images/output/" + input_image_name.split("/")[-1][:-4] + "_Canny.jpg"
	output_sobel_name = "../resources/images/output/" + input_image_name.split("/")[-1][:-4] + "_Sobel.jpg"
	output_prewitt_name = "../resources/images/output/" + input_image_name.split("/")[-1][:-4] + "_Prewitt.jpg"
	output_laplacian_name = "../resources/images/output/" + input_image_name.split("/")[-1][:-4] + "_Laplacian.jpg"


	# Canny
	output_canny_img = cv2.Canny(input_img,100,200)
	# Sobel
	sobelx = cv2.Sobel(input_img,cv2.CV_64F,1,0,ksize=5)
	sobely = cv2.Sobel(input_img,cv2.CV_64F,0,1,ksize=5)
	sobel = sobelx+sobely
	# Prewitt
	kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
	kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
	prewittx = cv2.filter2D(input_img, -1, kernelx)
	prewitty = cv2.filter2D(input_img, -1, kernely)
	prewitt = prewittx + prewitty
	# Laplacian
	laplacian = cv2.Laplacian(input_img,cv2.CV_64F)


	cv2.imwrite(output_name, input_img)
	cv2.imwrite(output_canny_name, output_canny_img)
	cv2.imwrite(output_sobel_name, sobel)
	cv2.imwrite(output_prewitt_name, prewitt)
	cv2.imwrite(output_laplacian_name, laplacian)
	return True


def main():
	input_image_name = '../resources/images/input/test.png'
	gaussian_denoise_name = "../resources/images/output/" + input_image_name.split("/")[-1][:-4] + "_Gaussian_Denoised.jpg"
	median_denoised_name = "../resources/images/output/" + input_image_name.split("/")[-1][:-4] + "_Median_Denoised.jpg"


	# # Original without Denoising 
	input_img = cv2.imread(input_image_name)
	# Boundary(input_img, input_image_name)

	# Gaussina Deoising 
	gray = color2gray(input_img)
	gaussian_denoise_img = GaussianDenoise(gray)
	Success = Boundary(gaussian_denoise_img, gaussian_denoise_name)
	if(Success):
		print("Finished Succesfully")


	# # Median Denoising
	# median_denoised_img = cv2.medianBlur(input_img,5)
	# Boundary(median_denoised_img, median_denoised_name)
# main()

import math
import numpy as np
import mahotas as mh

# Define functions
def cart2pol(x, y):
     theta = np.arctan2(y, x)
     rho = np.hypot(x, y)
     return (theta, rho)    
def PST(I,LPF,Phase_strength,Warp_strength, Threshold_min, Threshold_max, Morph_flag):
     L=0.5
     x = np.linspace(-L, L, I.shape[0])
     y = np.linspace(-L, L, I.shape[1])
     [X1, Y1] =(np.meshgrid(x, y))
     X=X1.T
     Y=Y1.T
     [THETA,RHO] = cart2pol(X,Y)
 
     # Apply localization kernel to the original image to reduce noise
     Image_orig_f=((np.fft.fft2(I)))  
     expo = np.fft.fftshift(np.exp(-np.power((np.divide(RHO, math.sqrt((LPF**2)/np.log(2)))),2)))
     Image_orig_filtered=np.real(np.fft.ifft2((np.multiply(Image_orig_f,expo))))
     # Constructing the PST Kernel
     PST_Kernel_1=np.multiply(np.dot(RHO,Warp_strength), np.arctan(np.dot(RHO,Warp_strength)))-0.5*np.log(1+np.power(np.dot(RHO,Warp_strength),2))
     PST_Kernel=PST_Kernel_1/np.max(PST_Kernel_1)*Phase_strength
     # Apply the PST Kernel
     temp=np.multiply(np.fft.fftshift(np.exp(-1j*PST_Kernel)),np.fft.fft2(Image_orig_filtered))
     Image_orig_filtered_PST=np.fft.ifft2(temp)

     # Calculate phase of the transformed image
     PHI_features=np.angle(Image_orig_filtered_PST)
     
     if Morph_flag ==0:
         out=PHI_features
     else:
         #   find image sharp transitions by thresholding the phase
         features = np.zeros((PHI_features.shape[0],PHI_features.shape[1]))
         features[PHI_features> Threshold_max] = 1 # Bi-threshold decision
         features[PHI_features< Threshold_min] = 1 # as the output phase has both positive and negative values
         features[I<(np.amax(I)/20)]=0 # Removing edges in the very dark areas of the image (noise)
   
         # apply binary morphological operations to clean the transformed image 
         out = features
         out = mh.thin(out, 1)
         out = mh.bwperim(out, 4)
         out = mh.thin(out, 1)
         out = mh.erode(out, np.ones((1, 1))); 
   
     return (out, PST_Kernel)