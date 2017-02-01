def function_names(file_Open):
    '''(io.TextIOWrapper) -> list of str
    takes as a parameter a file open for reading, and returns a list
    of all of the function names in that file.

    REQ: file_Open actually exists and is within the same directory
         as this file
    REQ: Mode == "r"

    >>> function_names(open("ex4.py","r"))
    ['insert', 'up_to_first', 'cut_list']

    '''
    # Opening a given file
    my_file = file_Open
    # Creating a list
    functions = []
    test_string = ""

    # loop through using a custom for loop created for file handles
    for next_line in my_file:
        # takes a line from the file
        test_list = (next_line.split())
        # checks if the line contains def
        if ('def' in test_list):
            # Changes the list into a string for manipulation
            test_string = test_list[1]
            # Takes the string from beginning to the (
            funcName = test_string[:test_string.find("(")]
            # adds the string to the functions
            functions.append(funcName)

    return functions


def justified(fileOpen):
    '''io.TextIOWrapper) -> bool
    takes as a parameter a file open for reading, and returns a boolean
    which is true if and only if every line in that file is
    left-justified (the first character is something other than
    a space). If any lines start with a space,
    the program should return False

    REQ: file_Open actually exists and is within the same directory
         as this file
    REQ: Mode == "r"

    >>> justified(open("ex4.py","r"))
        False

    '''
    isjustified = True
    my_file = fileOpen
    # loop through using a custom for loop created for file handles
    for next_line in my_file:
        if (next_line.startswith(' ') == True):
            isjustified = False
    my_file.close()
    return isjustified
