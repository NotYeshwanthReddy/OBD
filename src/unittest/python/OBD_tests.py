# Python code to demonstrate working of unittest 
import sys
sys.path.insert(0, '../../main/python/')
import OBD
import unittest
import cv2
import numpy as np
from matplotlib import pyplot as plt


input_image_names = ['../resources/images/input/test.png',
					'../resources/images/input/Clear1.jpg',
					'../resources/images/input/GaussianNoise1.jpg',
					'../resources/images/input/saltNpepper1.jpg',]

class TestOBD(unittest.TestCase): 
      
    def setUp(self): 
        pass

    # Returns True if the string contains 4 a. 
    def test_color2gray(self):
    	global input_image_names
    	for input_image_name in input_image_names:
    		input_img = cv2.imread(input_image_name)
    		output = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    		out_height, out_width = output.shape[:2]
    		result = OBD.color2gray(input_img)
    		res_height, res_width= result.shape[:2]
    		self.assertEqual((res_height, res_width), (out_height, out_width))

    # Returns True if the string is in upper case. 
    def test_GaussianDenoise(self):
    	global input_image_names
    	for input_image_name in input_image_names:
    		input_img = cv2.imread(input_image_name)
    		gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    		output = cv2.GaussianBlur(gray,(3,3),0)
    		out_height, out_width = output.shape[:2]
    		result = OBD.GaussianDenoise(gray)
    		res_height, res_width= result.shape[:2]
    		self.assertEqual((res_height, res_width), (out_height, out_width))
  
    # Returns TRUE if the string is in uppercase 
    # else returns False. 
    # def test_Boundary(self):         
    #     self.assertEqual() 
    #     self.assertFalse('Foo'.isupper()) 

if __name__ == '__main__': 
    unittest.main() 