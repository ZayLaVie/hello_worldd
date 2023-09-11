#function for getting unique elements from a list
def get_unique_list(some_list):
    #initialize unique elements
    unique_element=set()

    #for each elememt in the list, adds unique element to the list
    for element in some_list:
        unique_element.add(element)

    #initialize new list 
    new_list = list(unique_element)

    return new_list

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)