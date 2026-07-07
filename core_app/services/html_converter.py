import pandas as pd

from .extractor import extract_tables

def tables_to_html(tables):
    
    html_tables = []

    for table in tables:
        html_tables.append(table.to_html(escape=True, index=False))

    return html_tables