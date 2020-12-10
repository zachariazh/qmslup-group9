import pandas as pd

def geocode(fp):
    
    """
    The geocode takes a .csv file of addresses, and geocodes the text in the column
    named 'addr' into point features
    
    Args:
        fp (string): filepath of the address .csv file
        
    Returns:
        points (geodataframe): geodataframe of the locations as point features
    """
    
    from geopandas.tools import geocode
    
    # Read the data
    data = pd.read_csv(fp, sep=';')
    

    # Geocode addresses using the provider Nominatim.
    # A custom "application name" is needed as the user_agent parameter!
    geo = geocode(data['addr'], provider='nominatim'
                  , user_agent='qmslup_group9', timeout=4)
    
    points = geo.join(data)

    return points