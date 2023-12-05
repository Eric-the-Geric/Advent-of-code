

def main():
    path = "eg.txt"
    lines = parser(path)
    print(lines)




def parser(path):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    return lines



if __name__=="__main__":
    main()