import PyPDF2, os

pdfFile=open('automate.pdf', 'rb')

reader=PyPDF2.PdfFileReader(pdfFile) # returns new pdf reader object for this file

print(reader.numPages) # prints pages in pdfFile

page=reader.getPage(0) # return a page object
print(page.extractText()) # prints string in page object

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText()) # prints whole pdf

# pdfFile.addPage(pageNum) # adds page to pdfFile
# pdfFile.write(newFile) # writes newFile at the end of pdfFile
