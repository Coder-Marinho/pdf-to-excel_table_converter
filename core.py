import os
import pandas as pd
import tabula


os.system("clear")

def pdfDataframe(file):

    table = tabula.read_pdf(file, pages="all")
    print(table)

file = str(input("Digite o nome do arquivo: "))

pdfDataframe(file)