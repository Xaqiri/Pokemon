from bs4 import BeautifulSoup as bs
import requests
import re
import os.path

def main():
    # Get data from webpage
    html = requests.get('https://en.wikipedia.org/wiki/List_of_generation_I_Pokémon').text
    # Get the data as a nested data structure
    content = bs(html, 'html.parser')
    # Data I'm looking for is in the second table
    pokeTable = content.find_all('table')[1]
    # Each row is a different pokemon, so get them all
    pokeTableRows = pokeTable.find_all('tr')

    # Open the file, or create it if it doesn't exist
    pokeFile = open('poke_bs.txt', 'w')
    # The first row contains the main headers
    headers = pokeTableRows[0].text.strip().split('\n\n')
    # The second row contains a few more headers
    sub_headers = pokeTableRows[1].text.strip().split('\n\n')
    # Shortening 'National Pokedex Number' to just 'Number'
    headers[1] = 'Number'
    # Combining all the headers into one variable
    headers = sub_headers[0:2] + headers[1:2] + sub_headers[2:] + headers[3:]
    # Putting thos headers at the top of the file
    pokeFile.writelines(';'.join(headers) + '\n')
    # Loop through every row that contains pokemon data
    for i in range(2, len(pokeTable.find_all('tr'))):
        # Convert each row from html to text, strip off any white space, and split it into a list
        row = pokeTableRows[i].text.strip().split('\n\n')
        # Making sure there's data in each row. This would probably be better to do in Excel
        if 'No evolution' in row:
            row.insert(5, 'No evolution') 
        if len(row) < len(headers):
            row.insert(4, 'None')
            row.append('No notes')
        # Joining the list of pokemon data into a string, with each index delineated by a semicolon.
        # The notes contain commas, so I didn't want to use them since it would interfere with importing the data to Excel
        row = ';'.join(row)
        # The raw html contains footnotes and citation links, so this gets rid of them all
        row = re.sub(r'\[[nb\s\d]+\]', '', row)
        # Write the pokemon data to the file
        pokeFile.writelines(row + '\n')
    # Close the file to get it out of memory
    pokeFile.close()

if os.path.isfile('poke_bs.txt'):
    print('File already exists')
else:
    main()