#prg tp filters a list of numbers to include only those that are less than 50.
# It then prints the filtered list.
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("The id of number list before change: ",id(number_list))
i=0
while i < len(number_list):
    if number_list[i]>50:
       number_list.pop(i)
    else:
        i+=1
print("The number list: ",number_list)
print("The id of number list after change: ",id(number_list))
