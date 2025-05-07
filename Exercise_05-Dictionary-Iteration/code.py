#prg to reverse dictionary mapping i.e key-value pair to value-key pair.
ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
inverse_dict={}
for key,value in ascii_dict.items():
    inverse_dict[value]=key
print("Initial dictionary: ",ascii_dict)
print("Inversed dictionary: ",inverse_dict)