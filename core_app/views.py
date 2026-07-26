import string

from django.shortcuts import redirect, render

from .forms import uploadPDFForm
from .services.extractor import extract_tables
from .services.html_converter import tables_to_html, headings



def my_view(request):
    form = uploadPDFForm()
    tables = None
    matrix = [], []

    # Handle file upload
    if request.method == "POST":
        form = uploadPDFForm(request.POST, request.FILES)

        if form.is_valid():
            pdf_file = request.FILES["docfile"]
            tables = extract_tables(pdf_file)       #tables recebe o valor do dataframe das tabelas do pdf
            html_tables = tables_to_html(tables)    #html_tables recebe o valor de tables convertido para html
            tables_number = len(tables)             #informa a quantidade de tabelas
            headers = headings(tables)
            letters = list(string.ascii_uppercase)
            columns = letters
        
        else:
            print("FORMULÁRIO INVÁLIDO")

   

    # Render list page with the documents and the form
    context = {'form':form, 'tables':html_tables, "number":tables_number, "headers":headers,}
    return render(request, 'list.html', context)
