# BoxOfficeMojo Python WebScraper Utility Package


from bs4 import BeautifulSoup
import requests



def YearlyTop100sparser(url):
    '''
    Scrape a list of URLs for each Year listed in the home directory
    
    Parameters:
    url (string): home url associated to all Top 100 Yearly films
    
    Returns:
    YearlyTop100s (list): list of all urls associated to Top 100 Yearly films
    '''
    page = requests.get(url)
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'PageMissing' + ' ' + str(url)
        elif soup == 'TimeoutError':
            return 'TimeoutError' + ' ' + str(url)
        else:
            year = BeautifulSoup(page.content, 'lxml').find('div', id='body').find('table').find_next('table').find_next('table')
            li = []
            td = year.find_all('a')
            for i in td:
                li.append(i.get('href'))
            YearlyTop100s = []
            for i in range(0, len(li)-1):
                if 'chart' in li[i]:
                    YearlyTop100s.append(li[i])
            for i in range(0, len(YearlyTop100s)):
                YearlyTop100s[i] = 'https://www.boxofficemojo.com/yearly/'+ YearlyTop100s[i]
            return YearlyTop100s
    except AttributeError:
        return 'AttributeError'


def YearlyNonTop100sparser(url):
    '''
    Loop over YearlyTop100s and return another list of the footer URLs for each Year
    
    Parameters:
    url (string): home url associated to all non-Top 100 Yearly films
    
    Returns:
    YearlyNonTop100s (list): list of all urls associated to non-Top 100 Yearly films
    '''
    YearlyTop100s = YearlyTop100sparser(url)
    YearlyNonTop100s = []
    for x in YearlyTop100s:
        page = requests.get(x)
        soup = BeautifulSoup(page.content, 'lxml')
        footer = soup.find('center')
        try:
            footer_url_rows = footer.find_all('a')
            for i in footer_url_rows:
                YearlyNonTop100s.append(i.get('href'))
        except Exception:
            stopgap = 0
            while stopgap <= 8:
                try:
                    footer_url_rows = footer.find_all('a')
                    for i in footer_url_rows:
                        YearlyNonTop100s.append(i.get('href'))
                    stopgap += 1
                    continue
                except Exception:
                    stopgap += 1
                    continue
    for i in range(0, len(YearlyNonTop100s)):
        YearlyNonTop100s[i] = 'https://www.boxofficemojo.com'+ YearlyNonTop100s[i]
    return YearlyNonTop100s


def AllYearlyURLsparser(url):
    '''
    Merge these two lists together (YearlyTop100s & YearlyNonTop100s), by year
    
    Parameters:
    url (string): urls associated to all non-Top 100 Yearly films & Top 100 Yearly films
    
    Returns:
    AllYearlyURLs (list): List of all urls within YearlyTop100s & YearlyNonTop100s
    '''
    AllYearlyURLs = []
    YearlyTop100s = YearlyTop100sparser(url)
    YearlyNonTop100s = YearlyNonTop100sparser(url)
    for x in YearlyTop100s:
        AllYearlyURLs.append(x)
    for x in YearlyNonTop100s:
        AllYearlyURLs.append(x)
    return AllYearlyURLs


def MasterURLsparser(url):
    '''
    Loop over every AllYearlyURLs entry, to merge all years together.
    
    Parameters:
    url (string): Home Directory of BoxOfficeMojo film listings.
    
    Returns:
    MasterURLs (list): list of all urls associated to films on BoxOfficeMojo.
    '''
    MasterURLs = []
    AllYearlyURLs = AllYearlyURLsparser(url)
    for x in AllYearlyURLs:
        page = requests.get(x)
        soup = BeautifulSoup(page.content, 'lxml')
        body = soup.find('table', cellpadding='5')
        try:
            urls_rows_ffffff = body.find_all('tr', bgcolor='#ffffff')
            li = []
            for tr in urls_rows_ffffff:
                td = tr.find_all('a')
                for i in td:
                    li.append(i.get('href'))
            urls_rows_f4f4ff = body.find_all('tr', bgcolor='#f4f4ff')
            lis = []
            for tr in urls_rows_f4f4ff:
                td = tr.find_all('a')
                for i in td:
                    lis.append(i.get('href'))
            for i in range(0, len(li)-1):
                if 'movies' in li[i]:
                    MasterURLs.append(li[i])
            for i in range(0, len(lis)-1):
                if 'movies' in lis[i]:
                    MasterURLs.append(lis[i])
        except Exception:
            stopgap = 0
            while stopgap <= 8:
                try:
                    urls_rows_ffffff = body.find_all('tr', bgcolor='#ffffff')
                    li = []
                    for tr in urls_rows_ffffff:
                        td = tr.find_all('a')
                        for i in td:
                            li.append(i.get('href'))
                    urls_rows_f4f4ff = body.find_all('tr', bgcolor='#f4f4ff')
                    lis = []
                    for tr in urls_rows_f4f4ff:
                        td = tr.find_all('a')
                        for i in td:
                            lis.append(i.get('href'))
                    for i in range(0, len(li)-1):
                        if 'movies' in li[i]:
                            MasterURLs.append(li[i])
                    for i in range(0, len(lis)-1):
                        if 'movies' in lis[i]:
                            MasterURLs.append(lis[i])
                    stopgap += 1
                    continue
                except Exception:
                    stopgap += 1
                    continue
    for i in range(0, len(MasterURLs)):
        MasterURLs[i] = 'https://www.boxofficemojo.com'+ MasterURLs[i]
    return MasterURLs


def downloadhtml(url):
    '''
    Download the raw html of a given url on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    soup (string): html for a single film on BoxOfficeMojo.
    '''
    try:
        page = requests.get(url)
        if 'Sorry, we\'re not able to process your request.' in BeautifulSoup(page.content, 'lxml').find('div', id='main').find('p'):
            return None
        elif 'chart' in url:
            return None
        elif '..' in url:
            return None
        else:
            soup = BeautifulSoup(page.content, 'lxml')
            return soup
    except Exception as e:
        soup = e
        return 'ErrorCode' + ' ' + str(soup)


def uppertabledataparser(soup):
    '''
    Parse out the div/table at the top of each BoxOfficeMojo film page.
    
    Parameters:
    soup (string): html for a single film on BoxOfficeMojo.
    
    Returns:
    upper_table_data_rows (string): html for the div/table at the top of each BoxOfficeMojo film page.
    '''
    upper_table_data_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find('table', bgcolor='#dcdcdc').find_all('tr')
    return upper_table_data_rows


def totallifetimegrossestableparser(soup):
    '''
    Parse out the total lifetime gross of a film on BoxOfficeMojo.
    
    Parameters:
    soup (string): html for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): total lifetime gross of a film on BoxOfficeMojo.
    '''
    total_lifetime_grosses_table = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('table').find_all('td')
    return total_lifetime_grosses_table


def titleparser(url):
    '''
    Parse out the title of a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): title of a film on BoxOfficeMojo.
    '''
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'PageMissing' + ' ' + str(url)
        elif 'ErrorCode' in soup:
            return str(soup) + ' ' + str(url)
        else:
            try:
                title = soup.find('div', id='body').find('table', style='padding-top: 5px;').find('b').text
                return title
            except TypeError:
                return 'ErrorCode' + ' ' + str(soup)
    except AttributeError:
        while True:
            try:
                soup = downloadhtml(url)
                title = soup.find('div', id='body').find('table', style='padding-top: 5px;').find('b').text
                return title
            except AttributeError:
                continue


def distributorparser(url):
    '''
    Parse out the distributor of a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): distributor of a film on BoxOfficeMojo.
    '''
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'PageMissing' + ' ' + str(url)
        elif 'ErrorCode' in soup:
            return str(soup) + ' ' + str(url)
        else:
            try:
                upper_table_data_rows = uppertabledataparser(soup)
                li = []
                for tr in upper_table_data_rows:
                    td = tr.find_all('td')
                    for i in td:
                        li.append(i.text)
                upper_table_dict = {k:v for k,v in (x.split(':') for x in li[1:])}
                for i in upper_table_dict.keys():
                    upper_table_dict[i] = upper_table_dict[i].lstrip()
                return upper_table_dict['Distributor']
            except TypeError:
                return 'ErrorCode' + ' ' + str(soup)
    except AttributeError:
        stopgap = 0
        while stopgap <= 8:
            try:
                soup = downloadhtml(url)
                upper_table_data_rows = uppertabledataparser(soup)
                li = []
                for tr in upper_table_data_rows:
                    td = tr.find_all('td')
                    for i in td:
                        li.append(i.text)
                upper_table_dict = {k:v for k,v in (x.split(':') for x in li[1:])}
                for i in upper_table_dict.keys():
                    upper_table_dict[i] = upper_table_dict[i].lstrip()
                return upper_table_dict['Distributor']
            except AttributeError:
                if stopgap == 8:
                    return 'AttributeError' + ' ' + str(url)
                else:
                    stopgap += 1
                    continue


def genreparser(url):
    '''
    Parse out the genre of a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): genre of a film on BoxOfficeMojo.
    '''
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'NULL'
        else:
            try:
                upper_table_data_rows = uppertabledataparser(soup)
                li = []
                for tr in upper_table_data_rows:
                    td = tr.find_all('td')
                    for i in td:
                        li.append(i.text)
                upper_table_dict = {k:v for k,v in (x.split(':') for x in li[1:])}
                for i in upper_table_dict.keys():
                    upper_table_dict[i] = upper_table_dict[i].lstrip()
                return upper_table_dict['Genre']
            except TypeError:
                return 'ErrorCode' + ' ' + str(soup)
    except AttributeError:
        stopgap = 0
        while stopgap <= 8:
            try:
                soup = downloadhtml(url)
                if soup is None:
                    return 'NULL'
                else:
                    upper_table_data_rows = uppertabledataparser(soup)
                    li = []
                    for tr in upper_table_data_rows:
                        td = tr.find_all('td')
                        for i in td:
                            li.append(i.text)
                    upper_table_dict = {k:v for k,v in (x.split(':') for x in li[1:])}
                    for i in upper_table_dict.keys():
                        upper_table_dict[i] = upper_table_dict[i].lstrip()
                    return upper_table_dict['Genre']           
            except AttributeError:
                if stopgap ==8:
                    return 'AttributeError' + ' ' + str(url)
                else:
                    stopgap += 1
                    continue

    
def mpaaratingparser(url):
    '''
    Parse out the mpaa rating of a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): mpaa rating of a film on BoxOfficeMojo.
    '''
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'NULL'
        else:
            try:
                upper_table_data_rows = uppertabledataparser(soup)
                li = []
                for tr in upper_table_data_rows:
                    td = tr.find_all('td')
                    for i in td:
                        li.append(i.text)
                upper_table_dict = {k:v for k,v in (x.split(':') for x in li[1:])}
                for i in upper_table_dict.keys():
                    upper_table_dict[i] = upper_table_dict[i].lstrip()
                return upper_table_dict['MPAA Rating']
            except TypeError:
                return 'ErrorCode' + ' ' + str(soup)
    except AttributeError:
        stopgap = 0
        while stopgap <= 8:
            try:
                soup = downloadhtml(url)
                if soup is None:
                    return 'NULL'
                else:
                    upper_table_data_rows = uppertabledataparser(soup)
                    li = []
                    for tr in upper_table_data_rows:
                        td = tr.find_all('td')
                        for i in td:
                            li.append(i.text)
                    upper_table_dict = {k:v for k,v in (x.split(':') for x in li[1:])}
                    for i in upper_table_dict.keys():
                        upper_table_dict[i] = upper_table_dict[i].lstrip()
                    return upper_table_dict['MPAA Rating']
            except AttributeError:
                if stopgap == 8:
                    return 'AttributeError' + ' ' + str(url)
                else:
                    stopgap += 1
                    continue

            
def productionbudgetparser(url):
    '''
    Parse out the production budget of a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): production budget of a film on BoxOfficeMojo.
    '''
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'NULL'
        else:
            try:
                upper_table_data_rows = uppertabledataparser(soup)
                li = []
                for tr in upper_table_data_rows:
                    td = tr.find_all('td')
                    for i in td:
                        li.append(i.text)
                upper_table_dict = {k:v for k,v in (x.split(':') for x in li[1:])}
                for i in upper_table_dict.keys():
                    upper_table_dict[i] = upper_table_dict[i].lstrip()
                return upper_table_dict['Production Budget']
            except TypeError:
                return 'ErrorCode' + ' ' + str(soup)
    except AttributeError:
        stopgap = 8
        while stopgap <= 8:
            try:
                soup = downloadhtml(url)
                if soup is None:
                    return 'NULL'
                else:
                    upper_table_data_rows = uppertabledataparser(soup)
                    li = []
                    for tr in upper_table_data_rows:
                        td = tr.find_all('td')
                        for i in td:
                            li.append(i.text)
                    upper_table_dict = {k:v for k,v in (x.split(':') for x in li[1:])}
                    for i in upper_table_dict.keys():
                        upper_table_dict[i] = upper_table_dict[i].lstrip()
                    return upper_table_dict['Production Budget']
            except AttributeError:
                if stopgap == 8:
                    return 'AttributeError' + ' ' + str(url)
                else:
                    stopgap += 1
                    continue

    
def releasedateparser(url):
    '''
    Parse out the release date of a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): release date of a film on BoxOfficeMojo.
    '''
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'NULL'
        else:
            try:
                upper_table_data_rows = uppertabledataparser(soup)
                li = []
                for tr in upper_table_data_rows:
                    td = tr.find_all('td')
                    for i in td:
                        li.append(i.text)
                upper_table_dict = {k:v for k,v in (x.split(':') for x in li[1:])}
                for i in upper_table_dict.keys():
                    upper_table_dict[i] = upper_table_dict[i].lstrip()
                return upper_table_dict['Release Date']
            except TypeError:
                return 'ErrorCode' + ' ' + str(soup)
    except AttributeError:
        stopgap = 0
        while stopgap <= 8:
            try:
                soup = downloadhtml(url)
                if soup is None:
                    return 'NULL'
                else:
                    upper_table_data_rows = uppertabledataparser(soup)
                    li = []
                    for tr in upper_table_data_rows:
                        td = tr.find_all('td')
                        for i in td:
                            li.append(i.text)
                    upper_table_dict = {k:v for k,v in (x.split(':') for x in li[1:])}
                    for i in upper_table_dict.keys():
                        upper_table_dict[i] = upper_table_dict[i].lstrip()
                    return upper_table_dict['Release Date']
            except AttributeError:
                if stopgap == 8:
                    return 'AttributeError' + ' ' + str(url)
                else:
                    stopgap += 1
                    continue
    
    
def runtimeparser(url):
    '''
    Parse out the runtime of a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): runtime of a film on BoxOfficeMojo.
    '''
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'NULL'
        else:
            try:
                upper_table_data_rows = uppertabledataparser(soup)
                li = []
                for tr in upper_table_data_rows:
                    td = tr.find_all('td')
                    for i in td:
                        li.append(i.text)
                upper_table_dict = {k:v for k,v in (x.split(':') for x in li[1:])}
                for i in upper_table_dict.keys():
                    upper_table_dict[i] = upper_table_dict[i].lstrip()
                return upper_table_dict['Runtime']
            except TypeError:
                return 'ErrorCode' + ' ' + str(soup)
    except AttributeError:
        stopgap = 0
        while stopgap <= 8:
            try:
                soup = downloadhtml(url)
                if soup is None:
                    return 'NULL'
                else:
                    upper_table_data_rows = uppertabledataparser(soup)
                    li = []
                    for tr in upper_table_data_rows:
                        td = tr.find_all('td')
                        for i in td:
                            li.append(i.text)
                    upper_table_dict = {k:v for k,v in (x.split(':') for x in li[1:])}
                    for i in upper_table_dict.keys():
                        upper_table_dict[i] = upper_table_dict[i].lstrip()
                    return upper_table_dict['Runtime']
            except AttributeError:
                if stopgap == 8:
                    return 'AttributeError' + ' ' + str(url)
                else:
                    stopgap += 1
                    continue
    
    
# def domestictotalgrossparser(url):
#     soup = downloadhtml(url)
#     if soup is None:
#         return 'NULL'
#     else:
#         upper_table_data_rows = uppertabledataparser(soup)
#         li = []
#         for tr in upper_table_data_rows:
#             td = tr.find_all('td')
#             for i in td:
#                 li.append(i.text)
#         upper_table_dict = {k:v for k,v in (x.split(':') for x in li)}
#         for i in upper_table_dict.keys():
#             upper_table_dict[i] = upper_table_dict[i].lstrip()


def domesticparser(url):
    '''
    Parse out the domestic gross of the opening weekend release associated to a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): domestic gross of the opening weekend release associated to a film on BoxOfficeMojo.
    '''
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'NULL'
        else:
            try:
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
            except TypeError:
                return 'ErrorCode' + ' ' + str(soup)
    except AttributeError:
        stopgap = 0
        while stopgap <= 8:
            try:
                soup = downloadhtml(url)
                if soup is None:
                    return 'NULL'
                else:
                    try:
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
                    except TypeError:
                        return 'ErrorCode' + ' ' + str(soup)
            except AttributeError:
                if stopgap == 8:
                    return 'AttributeError' + ' ' + str(url)
                else:
                    stopgap += 1
                    continue


def foreignparser(url):
    '''
    Parse out the foreign gross of the opening weekend release associated to a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): foreign gross of the opening weekend release associated to a film on BoxOfficeMojo.
    '''
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'NULL'
        else:
            try:
                total_lifetime_grosses_table_rows = totallifetimegrossestableparser(soup)
                li = []
                for tr in total_lifetime_grosses_table_rows:
                    li.append(tr.text)
                if len(li) == 2:
                    return None
                else:
                    for x in range(0, len(li)):
                        li[x] = li[x].replace('\xa0', '')
                        li[x] = li[x].replace('+', '')
                        li[x] = li[x].replace('=', '')
                        li[x] = li[x].replace(':', '')
                    li = [x for x in li if x]
                    return li[4]
            except TypeError:
                return 'ErrorCode' + ' ' + str(soup)
    except AttributeError:
        stopgap = 0
        while stopgap <= 8:
            try:
                soup = downloadhtml(url)
                if soup is None:
                    return 'NULL'
                else:
                    try:
                        total_lifetime_grosses_table_rows = totallifetimegrossestableparser(soup)
                        li = []
                        for tr in total_lifetime_grosses_table_rows:
                            li.append(tr.text)
                        if len(li) == 2:
                            return None
                        else:
                            for x in range(0, len(li)):
                                li[x] = li[x].replace('\xa0', '')
                                li[x] = li[x].replace('+', '')
                                li[x] = li[x].replace('=', '')
                                li[x] = li[x].replace(':', '')
                            li = [x for x in li if x]
                            return li[4]
                    except TypeError:
                        return 'ErrorCode' + ' ' + str(soup)
            except AttributeError:
                if stopgap == 8:
                    return 'AttributeError' + ' ' + str(url)
                else:
                    stopgap += 1
                    continue


def worldwideparser(url):
    '''
    Parse out the worldwide gross of the opening weekend release associated to a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): worldwide gross of the opening weekend release associated to a film on BoxOfficeMojo.
    '''
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'NULL'
        else:
            try:
                if soup is None:
                    return 'NULL'
                else:
                    total_lifetime_grosses_table_rows = totallifetimegrossestableparser(soup)
                    li = []
                    for tr in total_lifetime_grosses_table_rows:
                        li.append(tr.text)
                    if len(li) == 2:
                        return None
                    else:
                        for x in range(0, len(li)):
                            li[x] = li[x].replace('\xa0', '')
                            li[x] = li[x].replace('+', '')
                            li[x] = li[x].replace('=', '')
                            li[x] = li[x].replace(':', '')
                        li = [x for x in li if x]
                        return li[7]
            except TypeError:
                return 'ErrorCode' + ' ' + str(soup)
    except AttributeError:
        stopgap = 0
        while stopgap <= 8:
            try:
                soup = downloadhtml(url)
                if soup is None:
                    return 'NULL'
                else:
                    try:
                        total_lifetime_grosses_table_rows = totallifetimegrossestableparser(soup)
                        li = []
                        for tr in total_lifetime_grosses_table_rows:
                            li.append(tr.text)
                        if len(li) == 2:
                            return None
                        else:
                            for x in range(0, len(li)):
                                li[x] = li[x].replace('\xa0', '')
                                li[x] = li[x].replace('+', '')
                                li[x] = li[x].replace('=', '')
                                li[x] = li[x].replace(':', '')
                            li = [x for x in li if x]
                            return li[7]
                    except TypeError:
                        return 'ErrorCode' + ' ' + str(soup)
            except AttributeError:
                if stopgap == 8:
                    return 'AttributeError' + ' ' + str(url)
                else:
                    stopgap += 1
                    continue


def openingweekendgrossparser(url):
    '''
    Parse out the gross of the opening weekend release associated to a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): gross of the opening weekend release associated to a film on BoxOfficeMojo.
    '''
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'NULL'
        else:
            try:
                domesticsummary_table_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('table').find_next('table').find_all('td')
                li = []
                for tr in domesticsummary_table_rows:
                    li.append(tr.text)
                for x in range(0, len(li)):
                    li[x] = li[x].replace('\xa0', '')
                    li[x] = li[x].replace('+', '')
                    li[x] = li[x].replace('=', '')
                    li[x] = li[x].replace(':', '')
                if len(li) == 2:
                    li = [None, None]
                try:
                    return li[1]
                except IndexError:
                    return 'NULL' + ' ' + str(soup)
            except TypeError:
                return 'ErrorCode' + ' ' + str(soup)
    except AttributeError:
        stopgap = 0
        while stopgap <= 8:
            try:
                soup = downloadhtml(url)
                if soup is None:
                    return 'NULL'
                else:
                    try:
                        domesticsummary_table_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('table').find_next('table').find_all('td')
                        li = []
                        for tr in domesticsummary_table_rows:
                            li.append(tr.text)
                        for x in range(0, len(li)):
                            li[x] = li[x].replace('\xa0', '')
                            li[x] = li[x].replace('+', '')
                            li[x] = li[x].replace('=', '')
                            li[x] = li[x].replace(':', '')
                        if len(li) == 2:
                            li = [None, None]
                        try:
                            return li[1]
                        except IndexError:
                            return 'NULL' + ' ' + str(soup)
                    except TypeError:
                        return 'ErrorCode' + ' ' + str(soup)
            except AttributeError:
                if stopgap == 8:
                    return 'AttributeError' + ' ' + str(url)
                else:
                    stopgap += 1
                    continue


def openingweekendtheatersparser(url):
    '''
    Parse out the theaters in the opening weekend release associated to a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): theaters in the opening weekend release associated to a film on BoxOfficeMojo.
    '''
    try:
        soup = downloadhtml(url)
        if soup is None:
            return 'NULL'
        else:
            try:
                domesticsummary_table_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('table').find_next('table').find_all('td')
                li = []
                for tr in domesticsummary_table_rows:
                    li.append(tr.text)
                for x in range(0, len(li)):
                    li[x] = li[x].replace('\xa0', '')
                    li[x] = li[x].replace('+', '')
                    li[x] = li[x].replace('=', '')
                    li[x] = li[x].replace(':', '')
                if len(li) == 2:
                    k = [None, None]
                else:
                    try:
                        k = li[2].split(', ')
                    except IndexError:
                        return 'NULL' + ' ' + str(url)
                try:
                    return k[1]
                except IndexError:
                    return 'NULL' + ' ' + str(url)
            except TypeError:
                return 'ErrorCode' + ' ' + str(soup)
    except AttributeError:
        stopgap = 0
        while stopgap <= 8:
            try:
                soup = downloadhtml(url)
                if soup is None:
                    return 'NULL'
                else:
                    try:
                        domesticsummary_table_rows = soup.find('div', id='body').find('table', style='padding-top: 5px;').find_next_sibling('table').find('table', width='100%').find('table', width='100%').find('table').find_next('table').find_all('td')
                        li = []
                        for tr in domesticsummary_table_rows:
                            li.append(tr.text)
                        for x in range(0, len(li)):
                            li[x] = li[x].replace('\xa0', '')
                            li[x] = li[x].replace('+', '')
                            li[x] = li[x].replace('=', '')
                            li[x] = li[x].replace(':', '')
                        if len(li) == 2:
                            k = [None, None]
                        else:
                            try:
                                k = li[2].split(', ')
                            except IndexError:
                                return 'NULL' + ' ' + str(url)
                        try:
                            return k[1]
                        except IndexError:
                            return 'NULL' + ' ' + str(url)
                    except TypeError:
                        return 'ErrorCode' + ' ' + str(soup)
            except AttributeError:
                if stopgap == 8:
                    return 'AttributeError' + ' ' + str(url)
                else:
                    stopgap += 1
                    continue


def widestreleaseparser(url):
    '''
    Parse out the theaters in the widest weekend release associated to a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): theaters in the widest weekend release associated to a film on BoxOfficeMojo.
    '''
    soup = downloadhtml(url)
    if soup is None:
        return 'NULL'
    else:
        try:
            soup = downloadhtml(url)
            if soup is None:
                return 'NULL'
            else:
                try:
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
                    try:
                        return li[1]
                    except IndexError:
                        return 'NULL' + ' ' + str(url)
                except TypeError:
                    return 'ErrorCode' + ' ' + str(soup)
        except AttributeError:
            stopgap = 0
            while stopgap <= 8:
                try:
                    soup = downloadhtml(url)
                    if soup is None:
                        return 'NULL'
                    else:
                        try:
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
                            try:
                                return li[1]
                            except IndexError:
                                return 'NULL' + ' ' + str(url)
                        except TypeError:
                            return 'ErrorCode' + ' ' + str(soup)
                except AttributeError:
                    if stopgap == 8:
                        return 'AttributeError' + ' ' + str(url)
                    else:
                        stopgap += 1
                        continue


def directorparser(url):
    '''
    Parse out the list of directors associated to a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): list of directors associated to a film on BoxOfficeMojo.
    '''
    soup = downloadhtml(url)
    if soup is None:
        return 'NULL'
    else:
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
        try:
            director_index
        except NameError:
            director_index = None

        try:
            writer_index
        except NameError:
            writer_index = None

        if director_index is None:
            director_data = None
        elif writer_index is None:
            director_data = li[1]
        elif len(li[director_index+1:writer_index]) == 1:
            director_data = li[director_index+1]
        else:
            director_data = li[director_index+1:writer_index]

        return str(director_data)


def writerparser(url):
    '''
    Parse out the list of writers associated to a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): list of writers associated to a film on BoxOfficeMojo.
    '''
    soup = downloadhtml(url)
    if soup is None:
        return 'NULL'
    else:
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

        try:
            writer_index
        except NameError:
            writer_index = None

        try:
            actor_index
        except NameError:
            actor_index = None

        if writer_index is None:
            writer_data = None
        elif actor_index is None:
            writer_data = li[4]
        elif len(li[writer_index+1:actor_index]) == 1:
            writer_data = li[writer_index+1]
        else:
            writer_data = li[writer_index+1:actor_index]
        return str(writer_data)


def actorparser(url):
    '''
    Parse out the list of actors associated to a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): list of actors associated to a film on BoxOfficeMojo.
    '''
    soup = downloadhtml(url)
    if soup is None:
        return 'NULL'
    else:
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
    '''
    Parse out the list of producer associated to a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): list of producer associated to a film on BoxOfficeMojo.
    '''
    soup = downloadhtml(url)
    if soup is None:
        return 'NULL'
    else:
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
    '''
    Parse out the list of composer associated to a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): list of composer associated to a film on BoxOfficeMojo.
    '''
    soup = downloadhtml(url)
    if soup is None:
        return 'NULL'
    else:
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
    '''
    Parse out the list of genres associated to a film on BoxOfficeMojo.
    
    Parameters:
    url (string): url for a single film on BoxOfficeMojo.
    
    Returns:
    li (string): list of genres associated to a film on BoxOfficeMojo.
    '''
    soup = downloadhtml(url)
    if soup is None:
        return 'NULL'
    else:
        try:
            soup = downloadhtml(url)
            if soup is None:
                return 'NULL'
            else:
                try:
                    genres_table_rows = soup.find(
                        'div', id='body').find(
                        'table', style='padding-top: 5px;').find_next_sibling(
                        'table').find(
                        'table', width='100%').find(
                        'table', width='100%').find_next_sibling(
                        'div').find_all(
                        'a')
                    li = []
                    for tr in genres_table_rows:
                        td = tr.find_all('b')
                        for i in td:
                            li.append(i.text)
                    return str(li)
                except TypeError:
                    return 'ErrorCode' + ' ' + str(soup)
        except AttributeError:
            stopgap = 0
            while stopgap <= 8:
                try:
                    soup = downloadhtml(url)
                    if soup is None:
                        return 'NULL'
                    else:
                        try:
                            genres_table_rows = soup.find(
                                'div', id='body').find(
                                'table', style='padding-top: 5px;').find_next_sibling(
                                'table').find(
                                'table', width='100%').find(
                                'table', width='100%').find_next_sibling(
                                'div').find_all(
                                'a')
                            li = []
                            for tr in genres_table_rows:
                                td = tr.find_all('b')
                                for i in td:
                                    li.append(i.text)
                            return str(li)
                        except TypeError:
                            return 'ErrorCode' + ' ' + str(soup)
                except AttributeError:
                    if stopgap == 8:
                        return 'AttributeError' + ' ' + str(url)
                    else:
                        stopgap += 1
                        continue

