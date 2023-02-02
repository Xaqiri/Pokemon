import difflib
import random

pokemon = {
	'bulbasaur': {
  	'feet': 4,
    'color1': 'blue-green',
    'color2': 'none',
    'type1': 'grass',
    'type2': 'poison'
  },
    'ivysaur': {
    'feet': 4,
    'color1': 'blue-green',
    'color2': 'red',
    'type1': 'grass',
    'type2': 'poison'
  },
    'venusaur': {
    'feet': 4,
    'color1': 'blue-green',
    'color2': 'pink',
    'type1': 'grass',
    'type2': 'poison'  
  },
    'charmander': {
    'feet': 2,
    'color1': 'orange',
    'color2': 'yellow',
    'type1': 'fire',
    'type2': 'none'  
  },
    'charmeleon': {
    'feet': 2,
    'color1': 'red',
    'color2': 'yellow',
    'type1': 'fire',
    'type2': 'none'  
  },
    'charizard': {
    'feet': 2,
    'color1': 'orange',
    'color2': 'yellow',
    'type1': 'fire',
    'type2': 'flying'  
  },
    'squirtle': {
    'feet': 2,
    'color1': 'blue',
    'color2': 'brown',
    'type1': 'water',
    'type2': 'none'  
  },
    'wartortle': {
    'feet': 2,
    'color1': 'purple',
    'color2': 'brown',
    'type1': 'water',
    'type2': 'none'  
  },
    'blastoise': {
    'feet': 2,
    'color1': 'blue',
    'color2': 'brown',
    'type1': 'water',
    'type2': 'none'  
  },
}

# Get random pokemon
randPokemonName = random.choice(list(pokemon.keys()))
randPokemon = pokemon[randPokemonName]
print(randPokemon)  
done = False
while (not done):
  player = input('Enter a pokemon: ').lower().rstrip()
  while player not in randPokemonName:
        print("incorrect")
        player = input ('Enter a pokemon? ').lower().rstrip()
  player == randPokemonName
  print('correct')
  player = input('Are you Done? Y/N? ')
  if player.lower() == 'y':
    done = True
  if player.lower() == 'n':
    (not done)
    randPokemonName = random.choice(list(pokemon.keys()))
    randPokemon = pokemon[randPokemonName]
    print(randPokemon)
      
# closest_match = difflib.get_close_matches(input , pokemon)
# print(closest_match)





