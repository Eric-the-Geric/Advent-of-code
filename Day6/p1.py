import re

with open("in.txt", "r") as f:
    lines = f.readlines()
    time_line, distance_line = lines[0].split(": "), lines[1].split(": ")

    # total amount of time(s) we have
    time = re.findall(r"\d+", time_line[1])

    # distance(s) we have to beat
    distance = re.findall(r"\d+", distance_line[1])


    
    totals = []
    for total_time, distance_to_beat in zip(time, distance):
        count=0
        total_t = int(total_time)
        for i in range(int(total_t)+1):
            if i*(total_t-i) > int(distance_to_beat):
                count+=1
        if count >0:
            totals.append(count)
    product = 1
    for t in totals:
        product*=t
    print(product)



