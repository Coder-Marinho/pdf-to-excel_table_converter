import tabula


def extract_tables(pdf_file):
    tables = tabula.read_pdf(pdf_file, pages="all", multiple_tables=True)
    
    return tables

