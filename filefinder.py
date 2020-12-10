import glob

def filefinder(input_fp, output_fp, id_list):
    
    """
    The FileFinder tool finds a list of travel time matrix files
    based on a list of YKR ID values
    from a specified input data folder.
    
    Args:
        input_fp (string): filepath of the travel time matrix data
        id_list (list): list of YKR IDs as strings or integers
        
    Returns:
        filepaths (list): list of found requested filepaths
    """
    
    filepaths = []
    
    for id in id_list:
        # Check if ID is int or str, and warn the user about excluding invalid IDs
        if isinstance(id, int):
            id_fp = 'travel_times_to_ ' + str(id) + '.txt'
        elif isinstance(id, str):
            id_fp = 'travel_times_to_ ' + id + '.txt'
        else:
            print('Warning: YKR IDs should be strings or integers, '
                  + 'ID "{}" is not a string or an integer!\n'.format(id)
                  + 'This ID will not be used.\n')
            continue
        
        print('Searching for file "{}", Progress: {}/{}\n'
              .format(id_fp, id_list.index(id) + 1, len(id_list)))
        
        found_files = glob.glob(input_fp + '/**/' + id_fp, recursive=True)
        
        if len(found_files) != 0:
            for fp in found_files:
                filepaths.append(fp)
        else:
            print('Warning: No matching file found for YKR ID "{}"\n'.format(id))
        
    print('--------------------\n')    
    print('Found {}/{} requested files:\n'.format(len(filepaths), len(id_list)))
    
    return filepaths