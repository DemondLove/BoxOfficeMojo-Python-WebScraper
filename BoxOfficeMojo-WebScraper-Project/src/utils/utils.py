
# BoxOfficeMojo Python WebScraper Utility Package

from bs4 import BeautifulSoup

import requests


def downloadhtml(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    return soup


def uppertabledataparser(soup):
    upper_table_data_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find('table', bgcolor='#dcdcdc').find_all('tr')
    return upper_table_data_rows


def totallifetimegrossestableparser(soup):
    total_lifetime_grosses_table = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('table').find_all('td')
    return total_lifetime_grosses_table


def titleparser(url):
    soup = downloadhtml(url)
    title = soup.find('div', id='body').find('table', style='padding-top: 5px;').find('b').text
    return title


def distributorparser(url):
    soup = downloadhtml(url)
    upper_table_data_rows = uppertabledataparser(soup)
    li = []
    for tr in upper_table_data_rows:
        td = tr.find_all('td')
        for i in td:
            li.append(i.text)
    upper_table_dict = {k:v for k,v in (x.split(':') for x in li)}
    for i in upper_table_dict.keys():
        upper_table_dict[i] = upper_table_dict[i].lstrip()
    return upper_table_dict['Distributor']


def domestictotalgrossparser(url):
    soup = downloadhtml(url)
    upper_table_data_rows = uppertabledataparser(soup)
    li = []
    for tr in upper_table_data_rows:
        td = tr.find_all('td')
        for i in td:
            li.append(i.text)
    upper_table_dict = {k:v for k,v in (x.split(':') for x in li)}
    for i in upper_table_dict.keys():
        upper_table_dict[i] = upper_table_dict[i].lstrip()
    return upper_table_dict['Domestic Total Gross']


def genreparser(url):
    soup = downloadhtml(url)
    upper_table_data_rows = uppertabledataparser(soup)
    li = []
    for tr in upper_table_data_rows:
        td = tr.find_all('td')
        for i in td:
            li.append(i.text)
    upper_table_dict = {k:v for k,v in (x.split(':') for x in li)}
    for i in upper_table_dict.keys():
        upper_table_dict[i] = upper_table_dict[i].lstrip()
    return upper_table_dict['Genre']


def mpaaratingparser(url):
    soup = downloadhtml(url)
    upper_table_data_rows = uppertabledataparser(soup)
    li = []
    for tr in upper_table_data_rows:
        td = tr.find_all('td')
        for i in td:
            li.append(i.text)
    upper_table_dict = {k:v for k,v in (x.split(':') for x in li)}
    for i in upper_table_dict.keys():
        upper_table_dict[i] = upper_table_dict[i].lstrip()
    return upper_table_dict['MPAA Rating']


def productionbudgetparser(url):
    soup = downloadhtml(url)
    upper_table_data_rows = uppertabledataparser(soup)
    li = []
    for tr in upper_table_data_rows:
        td = tr.find_all('td')
        for i in td:
            li.append(i.text)
    upper_table_dict = {k:v for k,v in (x.split(':') for x in li)}
    for i in upper_table_dict.keys():
        upper_table_dict[i] = upper_table_dict[i].lstrip()
    return upper_table_dict['Production Budget']


def releasedateparser(url):
    soup = downloadhtml(url)
    upper_table_data_rows = uppertabledataparser(soup)
    li = []
    for tr in upper_table_data_rows:
        td = tr.find_all('td')
        for i in td:
            li.append(i.text)
    upper_table_dict = {k:v for k,v in (x.split(':') for x in li)}
    for i in upper_table_dict.keys():
        upper_table_dict[i] = upper_table_dict[i].lstrip()
    return upper_table_dict['Release Date']


def runtimeparser(url):
    soup = downloadhtml(url)
    upper_table_data_rows = uppertabledataparser(soup)
    li = []
    for tr in upper_table_data_rows:
        td = tr.find_all('td')
        for i in td:
            li.append(i.text)
    upper_table_dict = {k:v for k,v in (x.split(':') for x in li)}
    for i in upper_table_dict.keys():
        upper_table_dict[i] = upper_table_dict[i].lstrip()
    return upper_table_dict['Runtime']


def domesticparser(url):
    soup = downloadhtml(url)
    total_lifetime_grosses_table_rows = totallifetimegrossestableparser(soup)
    li = []
    for tr in total_lifetime_grosses_table_rows:
        li.append(tr.text)
    for x in range(0, len(li)):
        li[x] = li[x].replace('\xa0', '')
        li[x] = li[x].replace('+', '')
        li[x] = li[x].replace('=', '')
        li[x] = li[x].replace(':', '')
    li = [x for x in li if x]
    return li[1]


def foreignparser(url):
    soup = downloadhtml(url)
    total_lifetime_grosses_table_rows = totallifetimegrossestableparser(soup)
    li = []
    for tr in total_lifetime_grosses_table_rows:
        li.append(tr.text)
    for x in range(0, len(li)):
        li[x] = li[x].replace('\xa0', '')
        li[x] = li[x].replace('+', '')
        li[x] = li[x].replace('=', '')
        li[x] = li[x].replace(':', '')
    li = [x for x in li if x]
    return li[4]


def worldwideparser(url):
    soup = downloadhtml(url)
    total_lifetime_grosses_table_rows = totallifetimegrossestableparser(soup)
    li = []
    for tr in total_lifetime_grosses_table_rows:
        li.append(tr.text)
    for x in range(0, len(li)):
        li[x] = li[x].replace('\xa0', '')
        li[x] = li[x].replace('+', '')
        li[x] = li[x].replace('=', '')
        li[x] = li[x].replace(':', '')
    li = [x for x in li if x]
    return li[7]


def openingweekendgrossparser(url):
    soup = downloadhtml(url)
    domesticsummary_table_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('table').find_next('table').find_all('td')
    li = []
    for tr in domesticsummary_table_rows:
        li.append(tr.text)
    for x in range(0, len(li)):
        li[x] = li[x].replace('\xa0', '')
        li[x] = li[x].replace('+', '')
        li[x] = li[x].replace('=', '')
        li[x] = li[x].replace(':', '')
    return li[1]


def openingweekendtheatersparser(url):
    soup = downloadhtml(url)
    domesticsummary_table_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('table').find_next('table').find_all('td')
    li = []
    for tr in domesticsummary_table_rows:
        li.append(tr.text)
    for x in range(0, len(li)):
        li[x] = li[x].replace('\xa0', '')
        li[x] = li[x].replace('+', '')
        li[x] = li[x].replace('=', '')
        li[x] = li[x].replace(':', '')
    k = li[2].split(', ')
    return k[1]


def widestreleaseparser(url):
    soup = downloadhtml(url)
    widest_release_table_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('table').find_next('table').find_next('table').find_all('tr')
    li = []
    for tr in widest_release_table_rows:
        td = tr.find_all('td')
        for i in td:
            li.append(i.text)
    for x in range(0, len(li)):
        li[x] = li[x].replace('\xa0', ' ')
        li[x] = li[x].lstrip()
        li[x] = li[x].replace(':', '')
    return li[1]


def directorparser(url):
    soup = downloadhtml(url)
    the_players_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('td', style='padding-left: 10px;').find('table').find_all('tr')
    li = []
    for tr in the_players_rows:
        td = tr.find_all('a')
        for i in td:
            li.append(i.text)
    for i in range(0, len(li)-1):
        if '*' in li[i]:
            del li[i]
    for i in range(0, len(li)-1):
        if 'Director' in li[i]:
            director_index = i
        elif 'Writer' in li[i]:
            writer_index = i
    director_data = li[director_index+1:writer_index]
    if len(li[director_index+1:writer_index]) == 1:
        director_data = li[director_index+1]
    return str(director_data)


def writerparser(url):
    soup = downloadhtml(url)
    the_players_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('td', style='padding-left: 10px;').find('table').find_all('tr')
    li = []
    for tr in the_players_rows:
        td = tr.find_all('a')
        for i in td:
            li.append(i.text)
    for i in range(0, len(li)-1):
        if '*' in li[i]:
            del li[i]
    for i in range(0, len(li)-1):
        if 'Writer' in li[i]:
            writer_index = i
        elif 'Actors' in li[i]:
            actor_index = i
    writer_data = li[writer_index+1:actor_index]
    if len(li[writer_index+1:actor_index]) == 1:
        writer_data = li[writer_index+1]
    return str(writer_data)


def actorparser(url):
    soup = downloadhtml(url)
    the_players_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('td', style='padding-left: 10px;').find('table').find_all('tr')
    li = []
    for tr in the_players_rows:
        td = tr.find_all('a')
        for i in td:
            li.append(i.text)
    for i in range(0, len(li)-1):
        if '*' in li[i]:
            del li[i]
    for i in range(0, len(li)-1):
        if 'Actors' in li[i]:
            actor_index = i
        elif 'Producer' in li[i]:
            producer_index = i
    actors_data = li[actor_index+1:producer_index]
    if len(li[actor_index+1:producer_index]) == 1:
        actors_data = li[actor_index+1]
    return str(actors_data)


def producerparser(url):
    soup = downloadhtml(url)
    the_players_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('td', style='padding-left: 10px;').find('table').find_all('tr')
    li = []
    for tr in the_players_rows:
        td = tr.find_all('a')
        for i in td:
            li.append(i.text)
    for i in range(0, len(li)-1):
        if '*' in li[i]:
            del li[i]
    for i in range(0, len(li)-1):
        if 'Producer' in li[i]:
            producer_index = i
        elif 'Composer' in li[i]:
            composer_index = i
    producer_data = li[producer_index+1:composer_index]
    if len(li[producer_index+1:composer_index]) == 1:
        producer_data = li[producer_index+1]
    return str(producer_data)


def composerparser(url):
    soup = downloadhtml(url)
    the_players_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('td', style='padding-left: 10px;').find('table').find_all('tr')
    li = []
    for tr in the_players_rows:
        td = tr.find_all('a')
        for i in td:
            li.append(i.text)
    for i in range(0, len(li)-1):
        if '*' in li[i]:
            del li[i]
    for i in range(0, len(li)-1):
        if 'Composer' in li[i]:
            composer_index = i
    composer_data = li[composer_index+1:]
    if len(composer_data) == 1:
        composer_data = li[composer_index+1]
    return str(composer_data)


def genresparser(url):
    soup = downloadhtml(url)
    genres_table_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find_next_sibling('div').find_all('a')
    li = []
    for tr in genres_table_rows:
        td = tr.find_all('b')
        for i in td:
            li.append(i.text)
    return str(li)
