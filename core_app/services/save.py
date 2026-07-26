import pandas as pd
from .extractor import extract_tables

def save_excel(tables, filename):
    dataframe = pd.concat(tables, ignore_index=True)
    dataframe.to_excel("tabela.xlsx", index="false")