import os

midfile=open('Pic_names.txt', 'w')

directory = 'tif_files'

if not os.path.exists(directory):
	os.makedirs(directory)


#the following path name needs to be updated for whichever directory you are working in
for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
	files.sort()
	for file in files:
		if file.endswith('.tif'):
			if not os.path.exists(file):
				print ".tif Files no longer exist"
				break
			
			print file
			
			name = file
			name = name.split('.')[0]
			
			os.system('convert %s.tif %s.jpeg'%(name,name))

			os.system('mv %s.tif tif_files'%name)

#			raw_input()
			midfile.write(name)
			midfile.write('.jpeg')
			midfile.write('\n')
			

midfile.close()
