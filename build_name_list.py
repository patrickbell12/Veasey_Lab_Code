import os

midfile=open('Pic_names.txt', 'w')

directory = 'tif_files'

if not os.path.exists(directory):
	os.makedirs(directory)

for root, dirs, files in os.walk('/Users/patrickbell/Desktop/Veasey_Lab/Pat_ayg-folder'):
	for file in files:
		if file.endswith('.tif'):
			if not os.path.exists(file):
				print ".tif Files no longer exist"
				break
			
			print file
			
			name = file
			name = name.split('.')[0]
			
			command = 'convert %s.tif %s.jpeg'%(name,name)

			os.system(command)

			command = 'mv %s.tif tif_files'%name

			os.system(command)

			print command
#			raw_input()
			midfile.write(name)
			midfile.write('.jpeg')
			midfile.write('\n')
			
for root, dirs, files in os.walk('/Users/patrickbell/Desktop/Veasey_Lab/Pat_ayg-folder'):
	for file in files:
		if file.endswith('.jpeg'):
			midfile.write(file)
			midfile.write('\n')

midfile.close()
