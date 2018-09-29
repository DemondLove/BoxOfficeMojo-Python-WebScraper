from bs4 import BeautifulSoup

import requests

import pandas as pd

def YearlyTop100sparser(url):
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
    YearlyTop100s = YearlyTop100sparser(url)
    YearlyNonTop100s = []
    for x in YearlyTop100s:
        page = requests.get(x)
        soup = BeautifulSoup(page.content, 'lxml')
        footer = soup.find('center')
        footer_url_rows = footer.find_all('a')
        for i in footer_url_rows:
            YearlyNonTop100s.append(i.get('href'))
    for i in range(0, len(YearlyNonTop100s)):
        YearlyNonTop100s[i] = 'https://www.boxofficemojo.com'+ YearlyNonTop100s[i]
    return YearlyNonTop100s


def AllYearlyURLsparser(url):
    AllYearlyURLs = []
    YearlyTop100s = YearlyTop100sparser(url)
    YearlyNonTop100s = YearlyNonTop100sparser(url)
    for x in YearlyTop100s:
        AllYearlyURLs.append(x)
    for x in YearlyNonTop100s:
        AllYearlyURLs.append(x)
    return AllYearlyURLs


def MasterURLsparser(url):
    MasterURLs = []
    AllYearlyURLs = AllYearlyURLsparser(url)
    for x in AllYearlyURLs:
        page = requests.get(x)
        soup = BeautifulSoup(page.content, 'lxml')
        body = soup.find('table', cellpadding='5')
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
    for i in range(0, len(MasterURLs)):
        MasterURLs[i] = 'https://www.boxofficemojo.com'+ MasterURLs[i]
    return MasterURLs

	def downloadhtml(url):
	    try:
	        page = requests.get(url)
	        if 'Sorry, we\'re not able to process your request.' in BeautifulSoup(page.content, 'lxml').find('div', id='main').find('p'):
	            return None
	        else:
	            soup = BeautifulSoup(page.content, 'lxml')
	            return soup
	    except Exception as e:
	        soup = e
	        return 'ErrorCode' + ' ' + str(soup)

	def titleparser(url):
	    try:
	        soup = downloadhtml(url)
	        if soup is None:
	            return 'PageMissing' + ' ' + str(url)
	        elif 'ErrorCode' in soup:
	            return str(soup) + ' ' + str(url)
	        else:
	            title = soup.find('div', id='body').find('table', style='padding-top: 5px;').find('b').text
	            return title
	    except AttributeError:
	        while True:
	            try:    
	                soup = downloadhtml(url)
	                title = soup.find('div', id='body').find('table', style='padding-top: 5px;').find('b').text
	                return title
	            except AttributeError:
	                    continue
	#         return 'AttributeError' + ' ' + str(url)

	# url = 'https://www.boxofficemojo.com/yearly/'

	# MasterURLs = MasterURLsparser(url)
	
	MasterURL = MasterURLs[:1400]

	# MasterURL[152

	# downloadhtml('https://www.boxofficemojo.com/movies/?id=spiderman2017.htm')
	
	dfTitleDataset = pd.DataFrame()

	for url in MasterURLs:
	    dfTitleDataset = dfTitleDataset.append(
	        {

	            'Title': titleparser(url)
	            , 'URL': str(url)

	        }, ignore_index=True
	    )
	    print(str(dfTitleDataset.index.values[-1]) + ' ' + str(url))
	
		# dfTitleError = df[df['Title'] == 'AttributeError']

		for x in dfTitle['Title']:
		    if 'AttributeError' in x:
		        dfTitleError = dfTitleError.append(x)
		#     elif 'ErrorCode' in x:
		#         dfTitleError = dfTitleError.append(x)
		    else:
		        continue

		len(dfTitleError)
