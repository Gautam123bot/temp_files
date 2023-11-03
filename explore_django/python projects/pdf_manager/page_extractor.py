from PyPDF2 import PdfReader, PdfWriter

pdf_file_path = 'dsa practical file1.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')

pdf = PdfReader(pdf_file_path)

pages = []
pdfWriter = PdfWriter()

# pages = [2, 4, 5, 10]
# pages = [(1, 3), (2, 6)]      # number of ways are there to print and extract the pages either in sequence or put up random pages
# for page_num in pages:
#     pdfWriter.add_page(pdf.pages[page_num])

start=3
end=7
for i in range(start-1, end):
    pdfWriter.add_page(pdf.pages[i])

with open('{0}_subset.pdf'.format(file_base_name), 'wb') as f:
    pdfWriter.write(f)
    f.close()