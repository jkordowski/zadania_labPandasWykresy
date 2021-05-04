import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

a = pd.read_excel('imiona.xlsx', sheet_name='Arkusz1')
grupa = a.groupby(["Rok"]).agg({'Liczba':['sum']})

wykres = grupa.cumsum()
print(wykres)
wykres.plot()
plt.show()