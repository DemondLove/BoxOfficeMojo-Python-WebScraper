
# BoxOfficeMojo Python WebScraper

from bs4 import BeautifulSoup

import requests

import pandas as pd

# Testing with Scream page on BoxOfficeMojo.com

# Ideal output would be these fields in a DataFrame, in the given order, as well a csv file for  backup.

# Pull URL request from the above page:

page = requests.get('https://www.boxofficemojo.com/movies/?id=scream.htm')
# page = requests.get('https://www.boxofficemojo.com/movies/?id=girldragontattoo11.htm')
# ^ The Girl with the Dragon Tattoo secondary test case to ensure html parsing is consistent

soup = BeautifulSoup(page.content, 'lxml')


# Move to Body of the html as a checkpoint:

body = soup.find('div', id='body')


# Move to table containing the film title. Identified by the style of the table:


upper_table = body.find('table', style='padding-top: 5px;')


# Parse out and Previewing the text of the title using 'b' tag:


title = upper_table.find('b').text


# Move to table containing the upper table of the page. Identified by the bgcolor of the table:


upper_table_data = upper_table.find('table', bgcolor='#dcdcdc')


# Parse out and Previewing the text of the upper table using 'tr' & 'td' tags yo add table data to a list:



upper_table_data_rows = upper_table_data.find_all('tr')


li = []
for tr in upper_table_data_rows:
    td = tr.find_all('td')
    for i in td:
        li.append(i.text)


# Convert Preview the upper table data from a list to a dictionary:

upper_table_dict = {k:v for k,v in (x.split(':') for x in li) }



# Strip the leading whitespace from the dictionary values:



for i in upper_table_dict.keys():
    upper_table_dict[i] = upper_table_dict[i].lstrip()


# Convert upper table dictionary data to a DataFrame:


resultset_df = pd.DataFrame(upper_table_dict, index=[0])


# Add the Title data to the DataFrame:

resultset_df['Title'] = title


# Reformat and Preview the DataFrame to display data in the correct order.



resultset_df = resultset_df.reindex(['Title','Distributor','Genre','MPAA Rating','Release Date','Runtime','Production Budget'], axis=1)


# Move to table containing the lower table of the page. Identified as the next sibling table of the upper_table:


lower_table = upper_table.find_next_sibling('table')


# Move to middle table, as a checkpoint I can use to get to the Genres table later:


middle_table = upper_table.find_next_sibling('table').find('table', width='100%').find('table', width='100%')


# Move down to the Total Lifetime Grosses Table. This table holds the Domestic, Foreign, and Worldwide data.

total_lifetime_grosses_table = middle_table.find('table')


# After reviewing the table structure, I can see that the Domestic and Worldwide data are within 'b' tags, but the foreign data is in 'a' tags. Parse out all three:


total_lifetime_grosses_table_rows = total_lifetime_grosses_table.find_all('td')

li = []
for tr in total_lifetime_grosses_table_rows:
    li.append(tr.text)

# Clean up output my removing unwanted characters and empty strings from the list:


for x in range(0, len(li)):
    li[x] = li[x].replace('\xa0', '')
    li[x] = li[x].replace('+', '')
    li[x] = li[x].replace('=', '')
    li[x] = li[x].replace(':', '')
li = [x for x in li if x]

# Adding Domestic, Foreign, and Worldwide to my resultset


resultset_df['Domestic'] = li[1]
resultset_df['Foreign'] = li[4]
resultset_df['Worldwide'] = li[7]
# Move to table containing the Domestic Summary table. This will contain the Opening Weekend Gross and Opening Weekend Theaters data.


domesticsummary_table = total_lifetime_grosses_table.find_next('table')


# Parse out Opening Weekend Gross and Opening Weekend Theaters data:

domesticsummary_table_rows = domesticsummary_table.find_all('td')


li = []
for tr in domesticsummary_table_rows:
    li.append(tr.text)


# Clean up output my removing unwanted characters and empty strings from the list:


for x in range(0, len(li)):
    li[x] = li[x].replace('\xa0', '')
    li[x] = li[x].replace('+', '')
    li[x] = li[x].replace('=', '')
    li[x] = li[x].replace(':', '')


# Parse out Opening Weekend Theaters data:

k = li[2].split(', ')


# Adding Opening Weekend Gross and Opening Weekend Theaters data to my resultset


resultset_df['Opening Weekend Gross'] = li[1]
resultset_df['Opening Weekend Theaters'] = k[1]
# Move to table containing the Domestic Summary footer information. This will contain the Widest Theater count data.


widest_release_table = domesticsummary_table.find_next('table')


# Parse out Widest Theaters data

widest_release_table_rows = widest_release_table.find_all('tr')


li = []
for tr in widest_release_table_rows:
    td = tr.find_all('td')
    for i in td:
        li.append(i.text)


# Clean up output my removing unwanted characters:

for x in range(0, len(li)):
    li[x] = li[x].replace('\xa0', ' ')
    li[x] = li[x].lstrip()
    li[x] = li[x].replace(':', '')


# Adding Widest Theaters data to my resultset:


resultset_df['Widest Theaters'] = li[1]

# Move to The Players Table:

the_players = middle_table.find('td', style='padding-left: 10px;').find('table')


# Reviewing the html for the_players table, BoxOfficeMojo actually uses 'a' tags around the most important actors, and simply uses 'td' tags around the rest. This is important, because I don't need to track all actors in all movies, but instead I only need to track those that are able to be searched on BoxOfficeMojo's People chart, which is the reason they are added in a 'tags' - to support a link to their People chart.

# Parse out Players data


the_players_rows = the_players.find_all('tr')


li = []
for tr in the_players_rows:
    td = tr.find_all('a')
    for i in td:
        li.append(i.text)


# BoxOfficeMojo denotes actors with minor roles with an * next to their name. So, we can remove these actors from the list of actors.


for i in range(0, len(li)-1):
    if '*' in li[i]:
        del li[i]


# Parse out Players data into Director, Writer, Actors, Producer, and Composer strings/lists.


for i in range(0, len(li)-1):
    if 'Director' in li[i]:
        director_index = i
    elif 'Writer' in li[i]:
        writer_index = i
    elif 'Actors' in li[i]:
        actor_index = i
    elif 'Producer' in li[i]:
        producer_index = i
    elif 'Composer' in li[i]:
        composer_index = i

director_data = li[director_index+1:writer_index]
writer_data = li[writer_index+1:actor_index]
actors_data = li[actor_index+1:producer_index]
producer_data = li[producer_index+1:composer_index]
composer_data = li[composer_index+1:]


if len(li[director_index+1:writer_index]) == 1:
    director_data = li[director_index+1]
if len(writer_data) == 1:
    writer_data = li[writer_index+1]
if len(actors_data) == 1:
    actors_data = li[actor_index+1]
if len(producer_data) == 1:
    producer_data = li[producer_index+1]
if len(composer_data) == 1:
    composer_data = li[composer_index+1]


# Adding Players data to resultset:


resultset_df['Director'] = str(director_data)
resultset_df['Writer'] = str(writer_data)
resultset_df['Actors'] = str(actors_data)
resultset_df['Producer'] = str(producer_data)
resultset_df['Composer'] = str(composer_data)

# Move to Genres table:

genres_table = upper_table.find_next_sibling('table').find('table', width='100%').find('table', width='100%').find_next_sibling('div')


# Parse out Genres

genres_table_rows = genres_table.find_all('a')



li = []
for tr in genres_table_rows:
    td = tr.find_all('b')
    for i in td:
        li.append(i.text)


# Adding Genres data to resultset:

resultset_df['Genres'] = str(li)

