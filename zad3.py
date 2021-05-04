import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

a = pd.read_excel('imiona.xlsx', sheet_name='Arkusz1')
b = a[(a['Rok'] >= 2012)]
grupa = b.groupby(["Plec"]).agg({'Liczba': ['sum']})
wykres = grupa.plot.pie(subplots=True,autopct='%.2f %%', fontsize=15, figsize=(6,6), legend=(0, 0))
plt.legend(loc='lower right')
plt.show()