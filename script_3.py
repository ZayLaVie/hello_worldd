user_input= input("Enter a string: ")

def get_lowerCase(dict_1):
    unique_dict={}

    dict_1 = dict_1.lower()

    for key in dict_1:
        if key.isalpha():
            if key in unique_dict:
                unique_dict[key] +=1
            else:
               unique_dict[key] =1

    return unique_dict

result = get_lowerCase(user_input)
print(result)
