import PyPDF2 

mergeFile = PyPDF2.PdfFileMerger()

mergeFile.append(PyPDF2.PdfFileReader('photo_2021-10-20_12-26-42.pdf', 'rb'))

mergeFile.append(PyPDF2.PdfFileReader('NewMergedFile1.pdf', 'rb'))


mergeFile.write("NewMergedFile2.pdf")
