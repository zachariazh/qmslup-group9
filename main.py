# Import necessary modules
import pandas as pd
import geopandas as gpd
from geocode import geocode
from filefinder import filefinder
from tablejoiner import tablejoiner

# Filepaths for the address .csv, the YKR Grid, and the outputs
    # Addresses .csv file path
addr_fp = r"C:\...\addresses.txt"
    # YKR Grid file path
ykr_fp = r"C:\...\MetropAccess_YKR_grid\MetropAccess_YKR_grid_EurefFIN.shp"
    # Travel Time Matrix *folder* path
ttm_fp = r"C:\...\HelsinkiTravelTimeMatrix2018"
    # Output folder path
out_fp = r"C:\...\qmslup-group9\data"

# Read the data
data = pd.read_csv(addr_fp, sep=';')
ykr = gpd.read_file(ykr_fp)

# Geocode the addresses to points using geocode.py
points = geocode(addr_fp)

# Reproject the library points to match the YKR Grid projection
geo = points.to_crs("EPSG:3067")

squares = gpd.sjoin(ykr, geo, how="inner", op='contains')

# Select the YKR Grid squares that contain the points
# and create a list of those squares' IDs
join_ids = []
for ykr_id in squares['YKR_ID']:
    join_ids.append(ykr_id)

# Use filefinder.py to find filepaths to each grid square
files = filefinder(ttm_fp, out_fp, join_ids)

# Create the Travel Time Matrix -joined YKR Grid shapefiles for each location
# using tablejoiner.py
for fp in files:
    tablejoiner(fp, ykr_fp, out_fp)


    