
red = 12; green = 13; blue = 14

with open("in_text.txt", "r") as f:
    possible_games = []
    lines = f.readlines()
    for line in lines:
        game_is_possible = True
        game_set = line.split(":")
        game_id, round = game_set[0],game_set[1]
        something, actual_id = game_id.split(" ")
        print(game_id)
        sets = round.split(";")
        for s in sets:
            colours = s.split(",")
            # print(colours)
            
            for col in colours:
                
                _, num, color = col.split(" ")
                # print("space", _)
                if color.__contains__("red"):
                    if int(num) > red:
                        game_is_possible = False
                        break
                elif color.__contains__("green"):
                    if int(num) > green:
                        game_is_possible = False
                        break
                elif color.__contains__("blue"):
                    if int(num) > blue:
                        game_is_possible = False
                        break

                else:
                    raise KeyError
        if game_is_possible:
            possible_games.append(int(actual_id))

    print(sum(possible_games))

                        

        
        
        

# for line in open("eg.txt", "r").readlines():
#     print(line.split(":"))