import random

from pokedex import pokemon 

done = False

# Get random pokemon
randPokemonName = random.choice(list(pokemon.keys()))
randPokemon = randPokemonName

while (not done):
  print(randPokemon) 
  player = input('Enter a pokemon: ').lower().rstrip()
  # Player choice has to be an exact match
  if player == randPokemonName:
    print(randPokemonName.upper())
    print('correct!'.upper())
    player = input('Are you Done? Y/N? ')
    if player.lower() == 'y':
      done = True
    #Get a new random pokemon only if the player is correct AND they still want to play
    randPokemonName = random.choice(list(pokemon.keys()))
    randPokemon = pokemon[randPokemonName]
  #If the player choice isn't a match, but is contained in the correct answer 
  if player in randPokemonName:
    print('almost, try again')
  else:
    print('incorrect')
      





