import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import ipywidgets as widgets
from ipywidgets import interactive, interact
import folium
import os
from zipfile import ZipFile
import shutil 


def load_data (self):
        with ZipFile(self, 'r') as zip:
            zip.printdir()
            zip.extractall()
        files = ["MMM_EcoCompt_X2H19070220_Archive2020.json", 
        "MMM_EcoCompt_X2H20042632_Archive2020.json", "MMM_EcoCompt_X2H20042633_Archive2020.json", 
        "MMM_EcoCompt_X2H20042634_Archive2020.json", "MMM_EcoCompt_X2H20042635_Archive2020.json", 
        "MMM_EcoCompt_X2H20063161_Archive2020.json", "MMM_EcoCompt_X2H20063162_Archive2020.json", 
        "MMM_EcoCompt_X2H20063163_Archive2020.json", "MMM_EcoCompt_X2H20063164_Archive2020.json", 
        "MMM_EcoCompt_XTH19101158_Archive2020.json"]
        for file in files:
                shutil.move(file, "Visualization/data")    


load_data("Visualization/data/MMM_EcoCompt_Archives.zip") 

loc1 = pd.read_json("Visualization/data/MMM_EcoCompt_X2H20042633_Archive2020.json", lines=True)
loc2 = pd.read_json("Visualization/data/MMM_EcoCompt_X2H20042632_Archive2020.json", lines=True) 
loc3 = pd.read_json("Visualization/data/MMM_EcoCompt_X2H19070220_Archive2020.json", lines=True) 
loc4 = pd.read_json("Visualization/data/MMM_EcoCompt_X2H20042635_Archive2020.json", lines=True)
loc5 = pd.read_json("Visualization/data/MMM_EcoCompt_X2H20042634_Archive2020.json", lines=True)
loc6 = pd.read_json("Visualization/data/MMM_EcoCompt_X2H20063161_Archive2020.json", lines=True) 
loc7 = pd.read_json("Visualization/data/MMM_EcoCompt_X2H20063162_Archive2020.json", lines=True)
loc8 = pd.read_json("Visualization/data/MMM_EcoCompt_XTH19101158_Archive2020.json", lines=True)
loc9 = pd.read_json("Visualization/data/MMM_EcoCompt_X2H20063163_Archive2020.json", lines=True)
loc10 = pd.read_json("Visualization/data/MMM_EcoCompt_X2H20063164_Archive2020.json", lines=True) 

##The maximum of bike intensity for each location:
maxloc1 = loc1['intensity'].max()
maxloc2 = loc2['intensity'].max()
maxloc3 = loc3['intensity'].max()
maxloc4 = loc4['intensity'].max()
maxloc5 = loc5['intensity'].max()
maxloc6 = loc6['intensity'].max()
maxloc7 = loc7['intensity'].max()
maxloc8 = loc8['intensity'].max()
maxloc9 = loc9['intensity'].max()
maxloc10 = loc10['intensity'].max()

##Map of the max intensity of bikes in Montpellier:
mtp_map = folium.Map(location = [43.6162094554924, 3.87440800666809], zoom_start = 12)
folium.CircleMarker([43.61465, 3.8336], popup="loc1 <br> max=1002 ", color='red', fill_color='red', radius=50).add_to(mtp_map)
folium.CircleMarker([43.5907, 3.81324], popup="loc2 <br> max=679", color='red', fill_color='red', radius=30).add_to(mtp_map)
folium.CircleMarker([43.60969924926758, 3.896939992904663], popup="loc3 <br> max=3245", color='red', fill_color='red', radius=50).add_to(mtp_map)
folium.CircleMarker([43.57883, 3.93324], popup="loc4 <br> max=1023", color='red', fill_color='red', radius=50).add_to(mtp_map)
folium.CircleMarker([43.57926, 3.93327], popup="loc5 <br> max=300", color='red', fill_color='red', radius=20).add_to(mtp_map)
folium.CircleMarker([43.6157418, 3.9096322], popup="loc6 <br> max=492 ", color='red', fill_color='red', radius=30).add_to(mtp_map)
folium.CircleMarker([43.6138841, 3.8684671], popup="loc7 <br> max=1884", color='red', fill_color='red', radius=50).add_to(mtp_map)
folium.CircleMarker([43.61620945549243, 3.874408006668091], popup="loc8 <br> max=3515", color='red', fill_color='red', radius=50).add_to(mtp_map)
folium.CircleMarker([43.6266977, 3.8956288], popup="loc9 <br> max=1089", color='red', fill_color='red', radius=50).add_to(mtp_map)
folium.CircleMarker([43.6266977, 3.8956288], popup="loc10 <br> max=235", color='red', fill_color='red', radius=30).add_to(mtp_map)
mtp_map

##HTML
mtp_map.save('Bike_intensity.html')
