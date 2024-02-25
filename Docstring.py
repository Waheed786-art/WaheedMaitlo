def square(n):
    '''Takes a number n, returns the square of n'''   # docstring only work in the first line of function definition used by print(square.__doc__)
    a = f"{n*4}" # f-string
    print(a)
    print(n**2)
    
square(5)
print(square.__doc__)


from PyPDF2 import PdfMerger

pdfs = ['one.pdf' , 'two.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)


merger.write("merged.pdf")    
merger.close()