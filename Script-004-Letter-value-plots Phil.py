#!/usr/bin/env python
# coding: utf-8

# In[46]:


import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-PhilBathy.csv")
dfM.head(5)
sb.set_style('darkgrid')

sb.catplot(data=dfM, kind="boxen",palette='tab20c', scale = "exponential", outlier_prop = 0.007,
           orient="v", legend=True, legend_out=True, margin_titles=True)
plt.xticks(rotation=45)
plt.ylabel('Elevation, m')
plt.title('Letter-value plot for the topography of the 25 profiles cross secting \nPhilippine Trench and the Philippine archipelago', fontsize=12, fontfamily='serif')
txt="Graphics: Python, Matplotlib & Seaborn libraries"
plt.figtext(0.80, 0.005, txt, wrap=True, horizontalalignment='center', fontsize=10)
plt.subplots_adjust(bottom=0.15,top=0.85)
plt.show()

