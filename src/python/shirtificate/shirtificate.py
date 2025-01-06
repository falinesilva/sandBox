from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(text="Faline took CS50")
pdf.output("shirtificate.pdf")