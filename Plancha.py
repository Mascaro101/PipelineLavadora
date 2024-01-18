#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import time
from datetime import datetime

##Guardamos el excel en una df
df = pd.read_excel('C:/Users/masca/JupyterTest/PipelineLavadora/RopaSeca2.xlsx')

##Creamos un for loop que lopeara por cada celula de la columna E
for cell in range(len(df['E'])):
    
    ##El countdown que cuenta atras desde un numero dado
    countdown = 5 
    while countdown != 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)
        
    print("Prenda Planchada")
    
    ##Printea el momento exacto donde se finalzia la tarea en una celula
    timestamp = datetime.now()
    print(timestamp)
    
    ##Se cambia el valor de la celula
    df.at[cell, 'E'] = 'TRUE'
    
##Output del fichero final
file_name = 'C:/Users/masca/JupyterTest/PipelineLavadora/RopaPlanchada.xlsx'       
df.to_excel(file_name, index=False)


# In[ ]:




