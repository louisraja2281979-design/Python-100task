from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Create PDF document
pdf = SimpleDocTemplate("output.pdf")

# Styles
styles = getSampleStyleSheet()

# Content
elements = []

title = Paragraph("PDF Generator Using Python", styles['Title'])
elements.append(title)

elements.append(Spacer(1, 12))

text = Paragraph(
    "This PDF file was generated using Python and ReportLab.",
    styles['BodyText']
)
elements.append(text)

elements.append(Spacer(1, 12))

text2 = Paragraph(
    "You can add headings, paragraphs, tables, images, and more.",
    styles['BodyText']
)
elements.append(text2)

# Build PDF
pdf.build(elements)

print("PDF created successfully: output.pdf")