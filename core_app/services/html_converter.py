import pandas as pd


def tables_to_html(tables):
    
    html_tables = []

    for table in tables:
        html_tables.append(table.to_html(escape=True, index=False))

    return html_tables


def headings(tables):

    info = []

    for table in tables:
        rows, cols = table.shape
        info.append({
            "rows": rows,
            "cols": cols,
        })
    return info