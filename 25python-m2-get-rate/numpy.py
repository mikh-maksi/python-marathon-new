# Python Program illustrating 
# numpy.quantile() method 
import numpy


# 1D array 
arr = [20, 2, 7, 1, 34] 

print("arr : ", arr) 
print("Q2 quantile of arr : ", numpy.quantile(arr, .50)) 
print("Q1 quantile of arr : ", numpy.quantile(arr, .25)) 
print("Q3 quantile of arr : ", numpy.quantile(arr, .75)) 
print("100th quantile of arr : ", numpy.quantile(arr, .1)) 
	
