import re

def get_textlines():
    with open("2015-16.txt", "r", encoding="utf-8") as f:
        textlines = f.readlines()
    return textlines

def extract_data(textlines):
    aunts = {}
    for line in textlines:
        number = re.match("Sue ([0-9]+)", line).group(1)
        aunts[number] = {}
        properties = ["children", "cats","samoyeds","pomeranians","akitas","vizslas","goldfish","trees","cars","perfumes"]
        for property in properties:
            try:
                aunts[number][property] = re.search(rf'{property}: ([0-9]+)', line).group(1)
            except:
                aunts[number][property] = None
    return aunts

def find_sue(aunts:dict, correct_properties:dict) -> list:
    sues = []
    for aunt in aunts.keys():
        possible = True
        for property in aunts[aunt].keys():
            if property == "cats" or property == "cats":
                if aunts[aunt][property] != None and int(aunts[aunt][property]) <= correct_properties[property]:
                    possible = False
                    break
            elif property == "pomeranians" or property == "goldfish":
                if aunts[aunt][property] != None and int(aunts[aunt][property]) >= correct_properties[property]:
                    possible = False
                    break
            elif aunts[aunt][property] != None and int(aunts[aunt][property]) != correct_properties[property]:
                possible = False
                break
        if not possible:
            continue
        sues.append(aunt)
    return sues

def main():
    data = get_textlines()
    data = extract_data(data)
    correct_properties = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    sue = find_sue(data, correct_properties)
    print(sue)

main()