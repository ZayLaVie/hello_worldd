def get_combined_dict(dict_1, dict_2):
    #initialize a common key 
    unique_dict ={}

     #if common elements
        #sum values
    #else 
       # do nothing

    #returns dic
    for key in dict_1:
        if key in dict_2:
            unique_dict[key]=dict_1[key] + dict_2[key]

    return unique_dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
   
