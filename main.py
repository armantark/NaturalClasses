from letters import letters

inputLetters = input("Enter list of letters, separated by commas:\n")
inputLetters = [x.strip() for x in inputLetters.split(',')]
intersection = letters[inputLetters[0]]
for x in inputLetters:
     intersection = intersection.intersection(letters[x])
intersection = [x.value for x in intersection]
print("The letters you input share the following natural classes:\n" + str(intersection))