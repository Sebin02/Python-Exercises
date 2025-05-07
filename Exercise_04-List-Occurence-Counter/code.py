sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
tmp_list=[]
duplicate_list=[]
for item in sample_list:
    if item not in tmp_list:
        tmp_list.append(item)
    else:
        duplicate_list.append(item)
print("Duplicate items in the list: ", duplicate_list)