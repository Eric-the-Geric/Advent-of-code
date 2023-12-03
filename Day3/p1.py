import sys
schematic_array = []

with open("in.txt", "r") as f:
    lines = f.readlines()
    
    for line in lines:
        row = []
        line = line.removesuffix("\n")
        for c in line:
            row.append(c)
        schematic_array.append(row)


indexes = {}
for idx, row in enumerate(schematic_array):
    for idy, value in enumerate(row):
        indexes[(idx, idy)] = []
        if value != "." and not value.isdigit():
            for i in range(-1, 2):
                digits = ""
                for j in range(-1,2):
                    index_x = idx+i
                    index_y = idy+j
                    if index_x <0 or index_x >= len(row):
                        continue
                    elif index_y <0 or index_y >= len(schematic_array):
                        continue
                    else:
                        if schematic_array[index_x][index_y].isdigit():
                             indexes[(idx, idy)].append((index_x, index_y))

                                    

real_indices = {index[0]: index[1] for index in indexes.items() if len(indexes[index[0]])}
# print(real_indices)
totals = []
for key in real_indices.keys():
    
    list_indexs = real_indices[key]
    # if len(list_indexs) == 1:
    #     print("only 1 index")
    last_index = None
    last_digit=""
    for index in list_indexs:
        if last_index != None:
            if abs(last_index[0] - index[0])==0 and (abs(last_index[1] - index[1]) < 2):
                continue

        digits=""

        for i in range(len(schematic_array[0])):
            if i == 0:
                if schematic_array[index[0]][index[1]].isdigit():
                    digits +=schematic_array[index[0]][index[1]]
            elif index[1] - i >= 0:
                if schematic_array[index[0]][index[1]-i].isdigit():
                    digits = schematic_array[index[0]][index[1]-i] + digits
                else:
                    break
            else:
                break
        for i in range(1, len(schematic_array[0])):
            if i == 0 and len(digits) == 0:
                if schematic_array[index[0]][index[1]].isdigit():
                    digits +=schematic_array[index[0]][index[1]]
                    # print(digits)
            elif index[1] + i < len(schematic_array[0]):
                if schematic_array[index[0]][index[1]+i].isdigit() and i >0:
                    digits =  digits  + schematic_array[index[0]][index[1]+i]
                else:
                    break
            else:
                break
        last_index = index
        if last_digit:
            if last_digit == digits:
                continue
        last_digit = digits

        totals.append(int(digits))
print(sum(totals))
                
            







        

                
