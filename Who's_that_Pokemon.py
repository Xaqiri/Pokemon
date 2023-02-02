import difflib
import random
from pokemoninfo import pokemon
pokemon = (pokemoninfo)
# Get random pokemon
randPokemonName = random.choice(list(pokemon.keys()))
randPokemon = pokemon[randPokemonName]
print(randPokemon) 
done = False
while (not done):
  player = input('Enter a pokemon: ').lower().rstrip()
  while player not in randPokemonName:
        print("incorrect")
        player = input ('Enter a pokemon: ').lower().rstrip()
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





