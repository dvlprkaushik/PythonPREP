def remWord(name, list):
    n = []
    for item in list:
        if item != name:
            n.append(item.strip(name))
    return n


names = ["Anna", "Nina", "Lana", "Jane", "Megan"]

print(remWord("a", names))
