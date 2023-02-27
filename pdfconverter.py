import pdfkit

print('Start')
config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

options = {
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}

pdfkit.from_file('book.html', 'out.pdf', configuration=config)
z = input('stop')
