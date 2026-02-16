import os

def save(data: str, path: str):
    """
    Saves given data into given file
    
    :param data: data to save
    :type data: str
    :param path: file path where to save
    :type path: str
    """
    try:
        # get direcotry of the given path
        dir = os.path.dirname(path)
        # if the path actually contains a dir (and not only the filename), and the path doesn't exist
        if dir and not os.path.exists(dir):
            # create the given directory
            os.makedirs(dir)
        
        with open(path, 'w') as file:
            # write data to file in filepath
            file.write(data)
            print(f"✅ Data succesfully saved in {path}")

    except Exception:
        # write out error if there are problems while creating/writing the file
        print("❌ Error: Impossible to write file!")