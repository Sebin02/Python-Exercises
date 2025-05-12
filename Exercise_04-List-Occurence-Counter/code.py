#to show duplicate items from given list
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
tmp_list=[]
duplicate_list=[]
for item in sample_list:
    if item not in tmp_list:    #if item is not in tmp_list, append it to tmp_list
        tmp_list.append(item)
    else:                       #if item is already in tmp_list then it is a duplicate
        duplicate_list.append(item)
print("Duplicate items in the list: ", duplicate_list)