from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def create_invoice(file_name, dates, total, your_name, client_name, invoice_date, invoice_number, balance_due):
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Invoice Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 50, "INVOICE")

    # Your Name and Details
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 100, your_name)
    # You can add sort code and account number here

    # Client Name
    c.drawString(30, height - 150, "To: " + client_name)

    # Lesson Dates
    c.drawString(30, height - 200, "Lesson Date")
    y_position = height - 220
    for date in dates:
        c.drawString(50, y_position, date)
        y_position -= 20

    # Total
    c.drawString(400, height - 200, "Total")
    c.drawString(450, height - 200, total)

    # Footer with Invoice Date, Number, and Balance Due
    c.drawString(30, 100, "Date: " + invoice_date)
    c.drawString(30, 80, "Invoice #: " + invoice_number)
    c.drawString(30, 60, "Balance Due: " + balance_due)

    c.drawString(30, 40, "Thank you!")

    c.save()

# Example Usage
dates = ["02/11/2023", "08/11/2023", "12/11/2023"]  # Replace with actual dates
create_invoice("new_invoice.pdf", dates, "301", "Reem", "Mr ", "30/11/2023", "301", "43")
