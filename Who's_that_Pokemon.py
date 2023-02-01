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
    'color2': 'red',
    'type1': 'grass',
    'type2': ''  
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
comp = random.choice(pokemon)
print(randPokemon)
input = input('Enter a pokemon: ')
  if input == comp
  print(correct)
  if 
# closest_match = difflib.get_close_matches(input , pokemon)
# print(closest_match)





