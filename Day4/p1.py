
total = 0
with open("eg.txt", "r") as f:
    lines = f.readlines()
    
    for line in lines:
        points = 0
        n = -1
        card, numbers = line.split(": ")
        winners, elfs = numbers.split(" | ")
        winners = winners.split(" ")
        winners = [x for x in winners if x.isdigit()]
        elfs = elfs.split(" ")
        # print(card)
        # print(repr(elfs))
        elfs = [x.replace("\n", "") for x in elfs if x]
        print(elfs)
        print(winners)
        for num in elfs:
            if num in winners:
                print(card, num)
                n+=1
                # print(n)
        if n>0:
            points += 2**n
        elif n ==0:
            points+=1
        print(points)
        total+=points
print(total)
        