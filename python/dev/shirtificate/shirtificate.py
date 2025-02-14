from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", size=25)
pdf.image("shirtificate.png", w=180, x=15, y=58.5)
text = f"{name} took CS50"
pdf.set_xy(0, 110)
pdf.set_text_color(255, 255, 255)
pdf.cell(pdf.w, 10, text, align="C")

pdf.output("shirtificate.pdf")
