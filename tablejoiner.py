import pandas as pd
import geopandas as gpd
import os

def tablejoiner(ttm_input_fp, ykr_input_fp, output_fp):
    
    """
    The TableJoiner tool creates a new spatial layer file by joining
    a specified Travel Time Matrix table to the YKR grid.
    The join is made by spatially joining corresponding YKR IDs.
    
    Args:
        ttm_input_fp (string): filepath of the Travel Time Matrix file
        ykr_input_fp (string): filepath of the YKR grid shapefile
        output_fp (string): filepath of the data output folder
        
    Returns:
        None
    """
    
    output_file = output_fp + "/" + ttm_input_fp[-11:-4]
    print("\n\nCreating shapefile:", output_file + "/" + ttm_input_fp[-11:-4] + ".shp")
    
    # Read inputs
    travel_matrix = pd.read_csv(ttm_input_fp, sep = ";", na_values = [-1])
    ykr = gpd.read_file(ykr_input_fp)
    
    print(ykr.head())
    
    # Join data
    merge = ykr.merge(travel_matrix, left_on = "YKR_ID", right_on = "from_id")
    
    # Output shapefile
    if os.path.exists(output_file):
        print("\nWarning: A file with the same name already exists, do you want to overwrite? (y/n)")
        overwrite = input()
        if overwrite == "y" or overwrite == "Y":
            merge.to_file(output_file)
            print("\nNew shapefile created:", output_file)
        else:
            print("\nOverwriting file cancelled.")
    else:
        merge.to_file(output_file)
        print("\nNew shapefile created:", output_file + "/" + ttm_input_fp[-11:-4] + ".shp")
    
    
    
tablejoiner(r"C:\Users\Saku\Desktop\Temp_GIS\QMSLUP\library_accessibility\HelsinkiTravelTimeMatrix2018\5931xxx\travel_times_to_ 5931307.txt"
            , r"C:\Users\Saku\Desktop\Temp_GIS\QMSLUP\library_accessibility\MetropAccess_YKR_grid\MetropAccess_YKR_grid_EurefFIN.shp"
            , r"C:\Users\Saku\Desktop\Temp_GIS\QMSLUP\library_accessibility\qmslup-group9\data")