def create_dict(file):
    '''(io.TextIOWrapper) -> dict of {str: [str, str, str, int, str]}
    read a file with each line having a username, first name, last name,
    age, gender (either M or F) and an e-mail address, all separated by
    whitespace. The function will insert each person’s information
    into a dictionary with their username as the key, and the
    value being a list of [last name, first name, e-mail, age, gender].
    When the entire file has been processed, it will then
    return the dictionary

    REQ: The file is formatted properly
    REQ: The file is opened to read

    '''
    # Takes in the file
    data = file.readlines()
    # Create an empty dictionary
    dictData = {}
    # Add items from the file into the dictionary
    for i in data:
        # Remove all whitespace by seperating elements into a list
        user = i.split()
        # Takes in each element within their respective data types
        for i in range(len(user)):
            dictData[user[0]] = [user[2], user[1],
                                 user[5], int(user[3]), user[4]]
    return(dictData)


def update_field(dictData, name, field, value):
    '''(str,str,str,str) -> Nonetype
    Takes in 4 values and accepts a new value to replace
    the appropriate field as indicated by the field variable
    The new value is indicated by the "value" variable

    REQ: file is formatted properly
    REQ: the field is one of the pre given values

    >>> my_dict = {'sclause':['Clause', 'Santa',
        'santa@christmas.np', 450, 'M']}
    >>> update_field(my_dict, 'sclause', 'AGE', 999)
    >>> my_dict == {'sclause': ['Clause', 'Santa',
        'santa@christmas.np', 999, 'M']}
    True
    '''
    # Creates a temporary dictionary to mutate
    temp_data = dictData[name]
    # If the required change is the "LAST" component, change it
    if (field == "LAST"):
        temp_data[0] = value
    # If the required change is the "FIRST" component, change it
    elif (field == "FIRST"):
        temp_data[1] = value
    # If the required change is the "E-MAIL" component, change it
    elif (field == "E-MAIL"):
        temp_data[2] = value
    # If the required change is the "AGE" component, change it
    elif (field == "AGE"):
        temp_data[3] = int(value)
    # Mutates the old list with the new list to update it
    dictData[name] = temp_data
