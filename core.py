import os
import pandas as pd
import tabula


os.system("clear")


def pdfDataframe(file):
    tables = tabula.read_pdf(file, pages="all")
    numTables = len(tables)
    print(tables)
    saveTable(tables, numTables)
    return tables, numTables


def fileName():
    file = str(input("Digite o nome do arquivo: "))
    return file


def saveTable(tables, numTables):
    if numTables > 1:
        print("fForam encontradas {numTables} em seu arquivo pdf")
        print("Digite 1 para salvá-las em apenas uma planilha.")
        print("Digite 2 para salvá-las em duas planilhas.")
        print("Digite 3 para salvá-las em apenas uma planilha sendo uma aba da planilha para cada tabela.")
        
        choice = input("Escolha: ")

        match choice:

            case "1":
                df = pd.concat(tables, ignore_index=True)
                df.to_excel("tabela.xlsx", index=False)          

            case "2":
                 for i, df in enumerate(tables):
                    df.to_excel(f"tabela_{i+1}.xlsx", index=False)

            case "3":
                with pd.ExcelWriter("tabela.xlsx") as writer:
                    for i, df in enumerate(tables):
                        df.to_excel(writer, sheet_name=f"Tabela_{i+1}", index=False)
            
            case _:
                print("Opção inválida") 
            
    else:
        df.to_excel("tabela.xlsx", index=False)



pdfDataframe(fileName())