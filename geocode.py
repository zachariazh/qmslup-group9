# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:33:56 2020

@author: Saku
"""

# Import necessary modules
import pandas as pd
from shapely.geometry import Point

# Filepath
fp = r"C:/Users/Saku/Desktop/Temp_GIS/QMSLUP/library_accessibility/qmslup-group9/data/libraries.txt"

# Read the data
data = pd.read_csv(fp, sep=';')

# Import the geocoding tool
from geopandas.tools import geocode

# Geocode addresses using Nominatim. Remember to provide a custom
# "application name" in the user_agent parameter!
geo = geocode(data['addr'], provider='nominatim'
              , user_agent='qmslup_ss', timeout=4)

join = geo.join(data)
join.head()

# Output file path
outfp = r"C:/Users/Saku/Desktop/Temp_GIS/QMSLUP/library_accessibility/qmslup-group9/data/addresses.shp"

# Save to Shapefile
join.to_file(outfp)