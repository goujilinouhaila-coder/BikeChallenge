import pandas as pd
import numpy as np 
import os 
import Prediction 

# Bokeh libraries
from bokeh.io import output_notebook
from bokeh.plotting import figure, show

__file__ = 'script.py'
url='https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv'
target_bike = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Prediction","data", "bike.csv")
 
bike= Prediction.Load_data(url, target_bike).save_as_df(target_bike)
bike.columns=['Date','Heure','Grandtotal','Todaystotal', 'Unnamed','Remark']
bike.drop(0,0,inplace=True)
bike.drop(1,0,inplace=True)
bike['Date'] = pd.to_datetime(bike['Date'])

bike['Heure'].fillna(0, inplace = True) 

# Create a figure with a datetime type x-axis
fig = figure(title='The number of TodaysTotal by date',
             plot_height=400, plot_width=700,
             x_axis_label='Day ', y_axis_label='Todaystotal',
             x_minor_ticks=2, y_range=(0, 6000),
             toolbar_location=None)

# The daily words will be represented as vertical bars (columns)
fig.vbar(x=bike['Date'], bottom=0, top=bike['Todaystotal'], 
         color='blue', width=0.75, 
         legend='Daily')


# Put the legend in the upper left corner
fig.legend.location = 'top_left'

# Let's check it out
show(fig)