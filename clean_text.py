# Pokemon data from https://pokemondb.net/tools/text-list

# Clean the data

file = open('pokedex.txt', 'r')
cleanFile = open('cleaned_pokedex.txt', 'a')
for line in file.readlines():
    l = line.strip().split(',')
    if l[-1] == '':
        l = l[:-1]
    cleanFile.writelines(','.join(l))
    cleanFile.writelines('\n')

file.close()
cleanFile.close()
