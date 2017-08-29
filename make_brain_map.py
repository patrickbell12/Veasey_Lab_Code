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


i = 0

pic_width = 60
x_distance = 30
x_plus = x_distance + 65
y_distance = 37.4

tag_hold = ''

page_number = 1

while True:
	pic_name = pic_names.readline()
	
#	if i == 24:break

	if pic_name == '':break

	pic = pic_name.strip('\n')
	short_pic = pic.strip('.jpeg')
	pic_dets = pic.split('_')
	group = pic_dets[0]

	if group != sys.argv[1]:continue
	
	condition = pic_dets[1]
	tag = pic_dets[2]
	section = pic_dets[3]
	
	name = group + ' ' + condition + ' ' + tag

	if i%2 == 0: #triggers for L side (i=0 is first)
		
		if tag != tag_hold or y_distance > (6*35+37.4):
			tag_hold = tag
			
			pdf.add_page()
			page_number +=1
			y_distance = 37.4
			
			pdf.set_font('Arial', 'B', 16)
			pdf.cell(170,10.3,'Base and Tau KO amygdala map '+pic,1,2,'C')
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
		y_distance += 46
	i+=1


pic_names.close()
pdf.output(sys.argv[1]+'_brain_map.pdf','F')
