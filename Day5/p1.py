import re

def main():
    path = "eg.txt"
    lines = parser(path)
    
    for line in lines:
        line = re.findall(r"\d+", line)
        print(line)




def parser(path):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    return lines



if __name__=="__main__":
    main()
