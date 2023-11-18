from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
class Report:
    def __init__(self, name, objects, attributes) -> None:
        self.name = name
        self.objects = objects
        self.attributes = attributes
    
    def print_pdf_report(self):
        pdf_filename = self.name+ '.pdf'
        c = canvas.Canvas(pdf_filename, pagesize=letter)
         # Add content to the PDF
        c.drawString(100, 750, self.name)
        c.line(100, 740, 500, 740)

        data = [
            self.attributes,
        ]
        for obj in self.objects:
            data.append([obj[attr] for attr in self.attributes])

        # Define table styles
        table_style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]

        # Draw the table
        from reportlab.platypus import Table, TableStyle
        table = Table(data)
        table.setStyle(TableStyle(table_style))
        table.wrapOn(c, 0, 0)
        table.drawOn(c, 72, 650)

        # Save the PDF file
        c.save()