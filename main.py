from letters import letters

inputLetters = input("Enter list of letters, separated by commas:\n")
inputLetters = [x.strip() for x in inputLetters.split(',')]
try:
    intersection = letters[inputLetters[0]]
except KeyError:
    print("Unidentifiable letter:", inputLetters[0])
    intersection = set([])
for x in inputLetters:
    if x != inputLetters[0]:
        try:
            intersection = intersection.intersection(letters[x])
        except KeyError:
            print("Unidentifiable letter:", x)
            intersection = set([])
intersection = [x.value for x in intersection]
print("The letters you input share the following natural classes:\n" + str(intersection))