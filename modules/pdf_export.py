from fpdf import FPDF

def export_pdf(content, output_file):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, content)

    pdf.output(output_file)
