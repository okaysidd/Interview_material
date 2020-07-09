import os

path = r'C:\Users\siddhartha.s\Desktop\something\02. py_algo_ds\Interview_material\Extras\\'
files = os.listdir(path)
for file in files:
	if file.startswith('LC'):
		os.rename(path+file, path+file.split('-')[1])
		# break
	