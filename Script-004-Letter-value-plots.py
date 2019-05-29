#!/usr/bin/env python
# coding: utf-8

# In[46]:


import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-Bathy.csv")
dfM.head(5)
sb.set_style('darkgrid')
sb.catplot(data=dfM, kind="boxen",palette='Paired', 
          orient="v", legend=True, legend_out=True, margin_titles=True)
plt.xticks(rotation=45)
plt.title('Letter-value plots for the Mariana Trench bathymetry', fontsize=12, fontfamily='serif')
plt.subplots_adjust(bottom=0.15,top=0.85)
plt.show()
