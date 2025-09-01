import re


def read_txt(filepath):
    with open(filepath,"r") as f:
        return f.read()

def get_options_dict(options_lines):
    options = {}
    for line in options_lines:
        frm, to = re.match("([A-Za-z]+) ", line).group(1), re.search(" ([A-Za-z]+)", line).group(1)
        if frm in options.keys():
            options[frm].append(to)
        else: options[frm] = [to]
    return options

def get_combinations(options, molecule):
    combinations = set()
    if "e" in molecule:
        for option in options["e"]:
            combinations.add(option)
        return combinations
    for match in re.finditer("[A-Z]{1}[a-z]*", molecule):
        if match.group(0) in options.keys():
            for option in options[match.group(0)]:
                combinations.add(molecule[:match.start()] + option + molecule[match.end():])
    return combinations

def get_fewest_steps(start_molecule, options, end_molecule, steps):
    steps+=1
    combinations = set()
    for molecule in start_molecule:
        for match in re.finditer("[A-Z]{1}[a-z]*", end_molecule):
            if match.group(0) in options.keys():
                for option in options[match.group(0)]:
                    new_molecule = molecule[:match.start()] + option + molecule[match.end():]
                    if new_molecule == end_molecule:
                        print(steps)
                        exit()
                    elif len(new_molecule) >= len(end_molecule):
                        pass
                    else:
                        combinations.add(new_molecule)
        get_fewest_steps(combinations, options, end_molecule, steps)


def main():
    molecule = read_txt("2015-19.txt")
    options_lines = read_txt("2015-19_options.txt").splitlines()
    options = get_options_dict(options_lines)
    combinations = get_combinations(options, molecule)
    print(len(combinations))

    test_options= {
        "e": ["H", "O"],
        "H": ["HO", "OH"],
        "O": ["HH"]
    }

    part2_input = set(["e"])
    steps = 1
    while True:
        print(steps)
        #print(part2_input)
        all_new_combinations = set()
        for combination in part2_input:
            new_combinations = get_combinations(options, combination)
            print(new_combinations)
            all_new_combinations.update(new_combinations)
            if molecule in all_new_combinations:
                print(steps)
                exit()
            #print(all_new_combinations)
        part2_input = set([i for i in all_new_combinations if len(i)<=len(molecule)])
        #print(part2_input)
        print(part2_input)
        steps += 1
        #if steps > 7:
        #    exit()



main()

"""
Andere Idee

steps = 1
combinations = set(["e"])
while True:
    loop über alle elemente des sets
        alle kombinationen erhalten und hinzufügen mit der funktion und mit .append()
        dann das ursprüngliche item löschen
        dann checken ob das richtige item in der liste ist -> wenn ja, steps ausgeben


"""

"""
Rekursion

neue iteration

neue leere liste mit den neuen iterationen
alle kombinationen durchmachen und gucken
    - ob die länge > len(molecule) (dann nichts tun)
    - ob das erstellte = molecule (dann anzahl der schritte ausgeben, anwendung beenden)
    - ansonsten: kombination zur neuen leeren liste hinzufügen
am ende mit allen items in der liste eine neue iteration beginnen

kein return-value, das ergebnis wird geprinted

"""