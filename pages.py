from fpdf import FPDF

pdf = FPDF()

class Report:
	def __init__(self, title, pdf=pdf, WIDTH=210, HEIGHT=240):
		self.title = title
		self.pdf = pdf
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT

		self.pdf.set_margins(10, 10, -1)

	def save(self, filename='report.pdf'):
		if filename[-4:] == '.pdf':
			self.pdf.output(filename, 'F')
		else:
			self.pdf.output('{filename}.pdf', 'F')


	def cover_page(self):
		self.pdf.set_font('Helvetica', 'B', 32)

		self.pdf.add_page()
		self.pdf.cell(210, 50, "Supermarket Business Analysis", align='C')
		self.pdf.ln()
		self.pdf.image('images/market.png', self.WIDTH/4.5, 60, self.WIDTH/1.6, self.HEIGHT/3, 'png')
		self.pdf.set_font('Helvetica', '', 12)
		self.pdf.ln(120)
		self.pdf.cell(210, 10, "January 2019 - March 2019", align='C')
		self.pdf.set_font('Helvetica', '', 10)
		self.pdf.ln(10)
		self.pdf.cell(210, 10, "Analyzed and Reported by Yusuf Atolagbe", align='C')


class Topic:
	def __init__(self, title, report):
		self.title = title
		self.report = report

#	def add_page(self):
#		self.pdf.set_font('Helvetica', 'B', 28)
#		self.pdf.add_page()
#		self.pdf.cell(210, 20, self.title, align='C')


#   DEFAULT PAGEGROUP


class Page:
	def __init__(self, topic, title='Page Title', line=20):
		self.topic = topic
		self.title = title
		self.line=line

	def shift_line(self, space=10):
		pdf_ = self.topic.report.pdf
		pdf_.ln()
		self.line += space

	def refresh_line(self):
		self.line = 20

	def write(self):
		pdf_ = self.topic.report.pdf

		pdf_.add_page()
		pdf_.set_font('Helvetica', 'B', 26)
		pdf_.cell(210, self.line, self.topic.title, align='C')
		self.shift_line()


	def write_insight(self, insight):
		pdf_ = self.topic.report.pdf

		x, y, w, h = self.topic.report.WIDTH/4, self.line+self.topic.report.HEIGHT/6, self.topic.report.WIDTH/2,self.topic.report.HEIGHT/4

		for insight in insight.insights:

			self.refresh_line()
			self.write()

			pdf_.set_font('Helvetica', 'B', 18)
			

			pdf_.cell(210, self.line, insight['title'], align='C')
			self.shift_line()
			
			pdf_.set_font('Helvetica', '', 14)

			#	IMAGE

			pdf_.ln()
			pdf_.image(insight['image'], x, y, w, h, 'png')
			pdf_.ln()

			self.shift_line(h+30)
			pdf_.multi_cell(0, 10, insight['description'], align='C')
			# ADJUST IMAGE POSITION




class Insight:
	def __init__(self, insights=[{'title': ['Insight'], 'description': 'Description', 'image': 'images/daily_rating.png'}]):
		self.insights=insights

#	def write(self):	
#		self.page_group.pdf.cell(210, 10, self.title, align='C')
#		self.page_group.pdf.set_font('Helvetica', '', 14)
#		self.page_group.pdf.ln()
#		self.page_group.pdf.cell(210, 10, self.description, align='C')

