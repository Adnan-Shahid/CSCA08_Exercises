def insert(listA, listB, placement):
    '''(string/list, string/list, int) -> string/list

    Takes 3 parameters, it then takes listB and places it within
    the index of the listA. The index is designated by placement.
    The new string or list is then returned

    >>> insert([1, 2, 3], ['a', 'b', 'c'], 2)
    [1, 2, 'a', 'b', 'c', 3]
    >>> insert("123","abc",2)
    '12abc3'
    '''
    # makes a new string or list with the beginning part of list
    # until placement, and adds listB into it, then continues on with
    # listA
    newlist = (listA[0:placement] + listB + listA[placement:len(listA)])
    return newlist


def up_to_first(listA, value):
    '''(str/list, ANY) -> str/list
    takes two parameters, a list (or string) and an object, and returns
    a copy of the list up to (but not including) the first occurrence
    of that object, or all of the elements if that object is not in the list

    >>> up_to_first([1, 2, 3, 4], 3)
    [1, 2]
    >>> up_to_first([1, 2, 3, 4], 9)
    [1, 2, 3, 4]

    '''
    # variable for checking if it contains the value

    # If listA is a string
    if (type(listA) == str):
        # placeholder value for the output
        Output = ""
        # finds where in the string the target value is
        value_location = listA.find(value)
        # if The value is in the string, Output is the all of listA
        # until the first occurrence of value
        if (value_location != -1):
            Output = listA[0:value_location]
        else:
            # if value_location returns -1
            # it means that value isn't in the string
            # as a result, Output would be all of listA
            Output = listA

    # If listA is a list
    elif (type(listA) == list):
        # placeholder value for Output
        Output = []
        # Checks if value is actually within listA
        if (value in listA):
            # finds the index of value
            value_location = listA.index(value)
            # creates a new list output from the beginning of listA to
            # the index of value
            Output = listA[0:value_location]
        else:
            # if value isn't in listA, then all of listA is outputted
            Output = listA

    return Output


def cut_list(listA, cut):
    '''(list/string, int) -> list/string
    given a list/string and a cut value, returns a copy of the
    list or string, but with the items before and after the cut swapped.

    >>> cut_list([0,1,2,3,4,5,6,7,8,9], 3)
    [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]
    >>> cut_list("ABCDEFGX1234",7)
    '1234XABCDEFG'

    '''
    # If listA is a string
    if (type(listA) == str):
        newList = (listA[cut+1:(len(listA))] + listA[cut] + listA[0:cut])

    # If listA is a list
    elif (type(listA) == list):
        newList = listA[cut+1:(len(listA))] + [listA[cut]] + listA[0:cut]

    return newList