from django.shortcuts import redirect, render

from .models import File
from .forms import uploadPDFForm
from .services.extractor import extract_tables
from .services.html_converter import tables_to_html



def my_view(request):
    form = uploadPDFForm()
    tables = None

    # Handle file upload
    if request.method == "POST":
        form = uploadPDFForm(request.POST, request.FILES)

        if form.is_valid():
            pdf_file = request.FILES["docfile"]
            tables = extract_tables(pdf_file)
            tables = tables_to_html(tables)
            tables_number = len(tables)
        
        else:
            print("FORMULÁRIO INVÁLIDO")

   

    # Render list page with the documents and the form
    context = {'form': form, 'tables':tables, "number":tables_number}
    return render(request, 'list.html', context)


    