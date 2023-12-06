import re

with open("in.txt", "r") as f:
    lines = f.readlines()
    time_line, distance_line = lines[0].split(": "), lines[1].split(": ")

    # total amount of time(s) we have
    real_time = ""
    time = re.findall(r"\d+", time_line[1])
    for tim in time:
        real_time+=tim
    real_time = int(real_time)

    # distance(s) we have to beat
    real_distance = ""
    distance = re.findall(r"\d+", distance_line[1])
    for dis in distance:
        real_distance+=dis
    real_distance = int(real_distance)

    
    count=0
    for i in range(real_time):
        if i*(real_time-i) > real_distance:
            count+=1
    print(count)