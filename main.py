from fpdf import FPDF

#create pdf object
my_pdf = FPDF()

#create a pdf page
my_pdf.add_page()

#set the font and sixe of pdf text
my_pdf.set_font("Arial", size=16)

#create a title cell
my_pdf.cell(200, 10, txt="PDF Generator", ln=1, align="C")

#create a content cell
text = "Write your own text, to generato it into pdf format"

my_pdf.cell(200, 10, txt=text, ln=2, align="C")

my_pdf.output("myPDF.pdf")