
red = 12; green = 13; blue = 14

with open("in_text.txt", "r") as f:
    possible_games = []
    lines = f.readlines()
    for line in lines:
        game_is_possible = True
        game_set = line.split(":")
        game_id, round = game_set[0],game_set[1]
        something, actual_id = game_id.split(" ")
        # print(game_id)
        sets = round.split(";")
        minimum_red = 0
        minimum_blue = 0
        minimum_green = 0
        for s in sets:
            colours = s.split(",")
    
            for col in colours:
                
                _, num, color = col.split(" ")
                num =int(num)
                # print("space", _)
                if color.__contains__("red"):
                    if num > minimum_red:
                        minimum_red = num
                        
                elif color.__contains__("green"):
                    if num > minimum_green:
                        minimum_green = num
                        
                elif color.__contains__("blue"):
                    if num > minimum_blue:
                        minimum_blue =num
                
                else:
                    raise KeyError
        power = minimum_red*minimum_green*minimum_blue
        possible_games.append(power)


    print(sum(possible_games))