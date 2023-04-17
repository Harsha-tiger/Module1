# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:09:19 2023

@author: harsha.srinivasa
"""
import pandas as pd
import random
import os
import numpy as np
import collections
import copy
import matplotlib.pyplot as plt

###Define the writer



df=pd.read_excel("python_plots_values.xlsx")
df=df[df.columns[2:]]

df.sort_index(axis=1,inplace=True)

coeff_cols=list(df.columns)

x=df.index

import matplotlib.backends.backend_pdf
pdf = matplotlib.backends.backend_pdf.PdfPages("output_1k.pdf")
for coeff in coeff_cols: ## will open an empty extra figure :(
    
    print(coeff_cols.index(coeff))    
    fig=plt.figure()
    y=df[coeff]
    plt.plot(x,y)
    plt.xlabel("Iteration")
    plt.title(coeff)
    pdf.savefig( fig )
pdf.close()
