
# I forgot to add a new file for p1 and p2 so this is actualy only part 2 :P
def main():
   
    digs = ["1","2","3","4","5","6","7","8","9", "0"]
    word_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
    characters_dict = {x:x+i+x for x, i in zip(word_digits, digs)}
    # print(characters_dict)

    with open("in_text.txt", "r") as f:
        count = 0
        for line in f.readlines():
            for word in word_digits:
                if word in line:
                    line = line.replace(word, characters_dict[word])
            line = line.lower()
            digit_list = []
            

            for char in line:
                if char in digs:
                    digit_list.append(char)
  
            count += int(digit_list[0]+digit_list[-1])
        print(count)

       
            

if __name__=="__main__":
    main()