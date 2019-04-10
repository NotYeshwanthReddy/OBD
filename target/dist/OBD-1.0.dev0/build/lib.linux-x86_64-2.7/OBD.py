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


def main(out):
	input_image_name = '../resources/images/input/test.png'
	gaussian_denoise_name = "../resources/images/output/" + input_image_name.split("/")[-1][:-4] + "_Gaussian_Denoised.jpg"
	median_denoised_name = "../resources/images/output/" + input_image_name.split("/")[-1][:-4] + "_Median_Denoised.jpg"


	# # Original without Denoising 
	input_img = cv2.imread(input_image_name)
	out.write("Input Succesfull")
	# Boundary(input_img, input_image_name)

	# Gaussina Deoising 
	gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
	out.write("Converted to gray")
	gaussian_denoise_img = cv2.GaussianBlur(gray,(3,3),0)
	out.write("Denoising image")
	Boundary(gaussian_denoise_img, gaussian_denoise_name)
	out.write("Getting Boundaries")


	# # Median Denoising
	# median_denoised_img = cv2.medianBlur(input_img,5)
	# Boundary(median_denoised_img, median_denoised_name)

