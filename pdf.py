from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def write_list_to_pdf(input_file, output_pdf):
    # Read integers from the file
    with open(input_file, 'r') as file:
        numbers = file.read().splitlines()

    # Create a PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter

    # Set up initial position
    x = 72
    y = height - 72
    line_height = 14

    # Write integers to PDF
    for number in numbers:
        c.drawString(x, y, number)
        y -= line_height
        if y < 72:
            c.showPage()
            y = height - 72

    c.save()

# Usage
input_file = 'Untitled.txt'  # Path to your text file with integers
output_pdf = 'output.pdf'  # Desired output PDF file name
write_list_to_pdf(input_file, output_pdf)
