import re


# class mapping:
#     def __init__(self, name, raw_mapping):
#         self.name = name
#         self.raw_mapping = raw_mapping




def main():
    path = "eg.txt"
    lines = parser(path)

    mappings = {
        "seeds": [],
        "seed-to-soil map:":[],
        "soil-to-fertilizer map:":[],
        "fertilizer-to-water map:":[],
        "water-to-light map:":[],
        "light-to-temperature map:":[],
        "temperature-to-humidity map:":[],
        "humidity-to-location map:":[],
                }
    for line in lines:
        name = ""
        items = []
        if line =="\n":
            continue
        clean_line = re.findall(r".+", line)[0]
        print(clean_line)
        if clean_line[0] == "seeds":
            mappings["seeds"] = re.findall(r"\d+")
    print(mappings)
            

        
        # print(line)



def parser(path):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    return lines



if __name__=="__main__":
    main()
