from random import randint, choice
import string
from itertools import chain


dict_list = [] # empty list to store dictionaries
# formation of the list with random number of dictionaries inside
for i in range(randint(2, 10)):
    rand_letters = []
    rand_numbers = []
    for z in range(randint(0, 26)): # random number of letters(keys) inside each dictionary
        rand_letters.append(choice(string.ascii_lowercase)) # appending a random letter inside the list
        rand_numbers.append(randint(0, 100)) # appending a random number inside the list
    alphabet = dict(zip(rand_letters, rand_numbers)) # formation of the dictionary from keys and values
    dict_list.append(alphabet) # formation of the list with dictionaries inside
print(dict_list)

k = []
v = []
def lists_of_keys_values(dictionary):
    for z in range(len(dictionary)):
        k.append(list((dictionary[z].keys()))) # keys of each dictionary are now in the one list
        v.append(list((dictionary[z].values()))) # values of each dictionary are now in the one list
    return k, v
lists_of_keys_values(dict_list)

k_unnested = list(chain.from_iterable(k)) # one list of all keys (without nested lists)
v_unnested = list(chain.from_iterable(v)) # one list of all values (without nested lists)

seen = set() # set for all letters from all dictionaries without duplication
dupes = set() # set for duplicated letters
# with this cycle we make the list of duplicates and elements that are not duplicated
def unnested_list_of_keys(initial_keys):
    for i in initial_keys:
        if i in seen:
            dupes.add(i)
        else:
            seen.add(i)
    return seen, dupes
unnested_list_of_keys(k_unnested)

def final_lists():
    print(values)
    max_val = max(values)  # maximum value from the list of values for duplicated keys
    print(max_val)
    index_val = values.index(max_val)  # finding the index of the maximum value
    index_dict = indexes[index_val]  # finding from which dictionary the maximum value for each duplicated key is
    added_element = str(keys) + "_" + str(index_dict + 1)  # here we form the element for final dict (f. e. 'k_1')
    print(added_element)
    final_list_keys.append(added_element)
    final_list_values.append(max_val)

# creation the final dictionary in the case of existing duplicates
def final_final_dict(list_without_duplicates, unnested_keyslist, unnested_valuelist, list_keys, list_values):
    for i in list_without_duplicates: # creation of the list of values for the keys that are not duplicated
        index_val = unnested_keyslist.index(i)
        val.append(unnested_valuelist[index_val])
    final_final_list_keys = list_keys + list(saw) # merge the list of keys that are duplicated in dictionaries and not
    print(final_final_list_keys)
    final_final_list_values = list_values + val # merge the list of values that are duplicated in dictionaries and not
    print(final_final_list_values)
    final_dict = dict(zip(final_final_list_keys, final_final_list_values)) # final dictionary!
    print(final_dict)

if not dupes:
    print("the duplication list is empty")
    final_dict = dict(zip(k_unnested, v_unnested)) # if there are no duplicates the final dictionary is made here
    print(final_dict)
else:
    print("the duplication list is not empty")
    saw = seen.difference(dupes) # difference between all keys and duplicates
    print(seen)
    print(saw)
    print(list(dupes))
    final_list_keys = []
    final_list_values = []
    for keys in list(dupes):
        values = []
        indexes = []
        for inside_dict in dict_list: # for each key in duplicates we go inside each dictionary from the list of dictionaries
            # the check if the last dictionary from the list doesn`t have duplicate key, which we search in this cycle
            if not inside_dict.get(keys) and (dict_list.index(inside_dict) == len(dict_list)-1):
                final_lists()
            elif not inside_dict.get(keys):
                continue
            # the check if the last dictionary from the list has duplicate key, which we search in this cycle
            elif (dict_list.index(inside_dict) == len(dict_list) - 1) and inside_dict.get(keys):
                values.append(inside_dict[keys]) # appending the values from each dictionary for duplicated key
                indexes.append(dict_list.index(inside_dict)) # appeending the index of dictionary? from which the value for duplicated key was taken
                final_lists()
            # here we populate values from each dictionary for the key that we search in this cycle
            # and the respective index of the dictionary, from which this value was taken
            else:
                values.append(inside_dict[keys])
                indexes.append(dict_list.index(inside_dict))
    print(final_list_keys)
    print(final_list_values)
    val = []
    final_final_dict(saw, k_unnested, v_unnested, final_list_keys, final_list_values)