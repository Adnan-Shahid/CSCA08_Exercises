def copy_me(listA):
    '''(list) -> list
    takes as input a list, and returns a copy of the list
    with the following changes
    Strings have all their letters converted to upper-case
    Integers and floats have their value increased by 1
    booleans are negated (False becomes True, True becomes False)
    Lists are replaced with the word ”List”

    REQ: listA has elements

    >>>copy_me(["asd",False,2,[1,2,3]])
    ['ASD', True, 3, 'List']

    >>>copy_me(["sAs",True,2,[1,2,3]])
    ['SAS', False, 3, 'List']

    >>>copy_me(["sAs",True,2.5,[1,2,3]])
    ['SAS', False, 3.5, 'List']

    '''
    # making a copy of the given list
    listCopy = listA[:]
    count = 0

    while (count < (len(listCopy))):
        if (type(listCopy[count]) == str):
            # make everything uppercase
            listCopy[count] = listCopy[count].upper()
        elif (type(listCopy[count]) == int):
            # increase all integer values by 1
            listCopy[count] += 1
        elif (type(listCopy[count]) == float):
            # increase all float values by 1
            listCopy[count] += 1
        elif (type(listCopy[count]) == bool):
            # reverse the boolean statement
            listCopy[count] = not listCopy[count]
        elif (type(listCopy[count]) == list):
            # Change any list to the word 'List'
            listCopy[count] = 'List'
        # Increase the iterator
        count += 1
    return listCopy


def mutate_me(ListA):
    '''(list) -> list
    takes as input a list, and returns a copy of the list
    with the following changes
    Strings have all their letters converted to upper-case
    Integers and floats have their value increased by 1
    booleans are negated (False becomes True, True becomes False)
    Lists are replaced with the word ”List”

    REQ: ListA has elements

    >>>mutate_me(["asd",False,2,[1,2,3]])
    None
    ListA == ['ASD', True, 3, 'List']

    >>>mutate_me(["sAs",True,2,[1,2,3]])
    None
    ListA == ['SAS', False, 3, 'List']

    >>>mutate_me(["sAs",True,2.5,[1,2,3]])
    None
    ListA == ['SAS', False, 3.5, 'List']

    '''
    # creating a counter to allow for the loop to happen
    count = 0
    while (count < (len(ListA))):
        if (type(ListA[count]) == str):
            # make everything uppercase
            ListA[count] = ListA[count].upper()
        elif (type(ListA[count]) == int):
            # increase all integer values by 1
            ListA[count] += 1
        elif (type(ListA[count]) == float):
            # increase all float values by 1
            ListA[count] += 1
        elif (type(ListA[count]) == bool):
            # reverse the boolean statement
            ListA[count] = not ListA[count]
        elif (type(ListA[count]) == list):
            # Change any list to the word 'List'
            ListA[count] = 'List'
        # Increase the iterator
        count += 1
