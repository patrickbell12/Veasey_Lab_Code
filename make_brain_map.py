#Dimentions are currently optomized for MUT project

from fpdf import FPDF
import sys

def word_space(x):
	for i in range(x) :
		pdf.ln()


pic_names = open('Pic_names.txt', 'r')
page_height = 279.4
page_width = 215.9
pdf = FPDF('p','mm',(page_width,page_height))
pdf.set_margins(25.4,25.4,-25.4)

pic_width = 60
x_distance = 30
x_plus = x_distance + 65
y_distance = 37.4

page_number = 1

i = 0

animal_hold = ''

while True:
	#cycle through all names on the list and pick out the one we are working on as 
        #stated by sys.argv[1] in command line
        
        pic_name = pic_names.readline()

	if pic_name == '':break

	pic = pic_name.strip('\n')
	short_pic = pic.strip('.jpeg')
        pic_dets = short_pic.split('_')

        #animal number
        animal = pic_dets[0]

        #find animal in question
	if animal != sys.argv[1]:continue
	

        #condition ie MUT, NLSEQ etc.
	condition = pic_dets[1]
	
	name = animal + ' ' + condition

	if i%2 == 0: #triggers for L side (i=0 is first)
		#reset to top of new page when starting an animal or when lower limit of page is reached	
		if animal != animal_hold or y_distance > (6*35+37.4):
			
			animal_hold = animal

			pdf.add_page()
			page_number +=1
			y_distance = 37.4
			
			pdf.set_font('Arial', 'B', 16)
			pdf.cell(170,10.3,pic,1,2,'C')
			pdf.set_font('Arial', '', 12)
			
			if i!=0:
				pdf.set_xy(x_distance, (page_number*page_height+y_distance))



		pdf.image(pic,(x_distance),y_distance, pic_width)
		pdf.set_xy(x_distance,y_distance)
		pdf.cell(35,5,(name),1)

	else: #triggers fror R side
		pdf.image(pic,(x_plus),y_distance, pic_width)
		pdf.set_xy(x_plus,y_distance)
		pdf.cell(35,5,(name),1)
		y_distance += 65 #This is specificly for these MUT pics which are longer in the y direction than most images. Normally should by 36 pixels.
	i+=1


pic_names.close()
pdf.output(sys.argv[1]+'_brain_map.pdf','F')
