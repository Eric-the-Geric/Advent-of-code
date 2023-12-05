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
        elfs = [x.replace("\n", "") for x in elfs if x]
        for num in elfs:
            if num in winners:
                print(card, num)
                n+=1
        if n>0:
            points += 2**n
        elif n ==0:
            points+=1
        total+=points
print(total)
        