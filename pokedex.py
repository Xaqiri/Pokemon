cleanFile = open('cleaned_pokedex.txt', 'r')

cats = []
dex = {}
for i in cleanFile.readline().strip().split(','):
    cats.append(i)

pokeDict = {}
for line in cleanFile.readlines():
    line = line.strip().split(',')
    x = 0
    for i in line:
        if x == 0:
            pokeDict = {i: {}}
            
        else:
            pokeDict[line[0]][cats[x]] = i
        x += 1
    dex.update(pokeDict)
        
cleanFile.close()

pokemon = dex