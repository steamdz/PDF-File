from fpdf import FPDF

#save FDPF() class into Variable pdf

pdf = FPDF()

#add a page pdf

pdf.add_page()

#set style and size font

pdf.set_font("Arial",size=30)

#Creat Text

pdf.cell(200 , 20 ,txt="AYMEN DEV",
         align="C",ln=1)
pdf.cell(200 , 20 ,txt="WELCOME TO OUR YOUTUBE CHANNEL",
         align="C", ln=2)

#save our pdf

pdf.output("AYMENDEv.pdf")
