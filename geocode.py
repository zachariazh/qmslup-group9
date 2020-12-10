# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:33:56 2020

@author: Saku
"""
def geocode(fp):
    # Import necessary modules
    import pandas as pd

    # Read the data
    data = pd.read_csv(fp, sep=';')
    
    # Import the geocoding tool
    from geopandas.tools import geocode
    
    # Geocode addresses using Nominatim. Remember to provide a custom
    # "application name" in the user_agent parameter!
    geo = geocode(data['addr'], provider='nominatim'
                  , user_agent='qmslup_ss', timeout=4)
    
    join = geo.join(data)

    return join