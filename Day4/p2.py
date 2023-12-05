total = 0
with open("in.txt", "r") as f:
    lines = f.readlines()
    cards = {i+1: 1 for i in range(len(lines))}
    for line in lines:
        points = 0
        n = -1
        card, numbers = line.split(": ")
        card_line = [x for x in card.split(" ") if x == "Card" or x.isdigit()]
        _, card_num = card_line
        winners, elfs = numbers.split(" | ")
        winners = winners.split(" ")
        winners = [x for x in winners if x.isdigit()]
        elfs = elfs.split(" ")

        elfs = [x.replace("\n", "") for x in elfs if x]
        
        for num in elfs:
            if num in winners:
                points+= 1
        
        for copy in range(cards[int(card_num)]):
            if points:
                for i in range(int(card_num)+1, int(card_num)+points+1):

                    cards[i] += 1
        
sum = 0
for key, value in cards.items():
    sum+=value

print(sum)

