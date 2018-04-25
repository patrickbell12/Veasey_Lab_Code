import os
#not intended for the same animal over different conditions, NO REPEATING ANIMALS

#make list of all animals in study and convert all to jpeg, move TIFF's

#get tag number for each animal

animals = []

old_number = ''

pic_list = 'Pic_names.txt'

if os.path.exists(pic_list):
	name_file=open(pic_list,'r')
else:
	command = 'python build_name_list.py'
	os.system(command)
	name_file = open(pic_list,'r')


while True:
	pic_name = name_file.readline()
#	print pic_name

	if pic_name == '':break

	number = pic_name.split('_')[0]

#	print number

	if number != old_number:
		old_number = number
		animals.append(number)

name_file.close()

#make map for each animal
for i in range(len(animals)):
	print i
	print animals[i]
	command = 'python make_brain_map.py %s' %(animals[i])
	print command
	os.system(command)

