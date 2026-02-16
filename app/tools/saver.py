def save(data: str, path: str):
    """
    Saves given data into given file
    
    :param data: data to save
    :type data: str
    :param path: file path where to save
    :type path: str
    """

    with open(path, 'w+') as file:
        try:
            file.write(data)
            print(f"Data succesfully saved in {path}")
        except:
            print("Error: Impossible to write file!")