import os

path = r'C:\Users\siddhartha.s\Desktop\something\02. py_algo_ds\Leetcode questions\June_challenge\\'
files = os.listdir(path)
for file in files:
	if file.startswith('day'):
		os.rename(path+file, path+file.split('-')[1])
		# break
	