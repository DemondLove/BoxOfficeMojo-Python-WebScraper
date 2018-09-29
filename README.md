# BoxOfficeMojo.com Python WebScraper

Web Scraping Package created to archive a BoxOfficeMojo database.

## Using https://www.boxofficemojo.com/yearly/ as a Home Directory, the general approach is:
1. Scrape a list of URLs for each Year listed in the home directory, called YearlyTop100s.
2. Loop over YearlyTop100s and return another list of the footer URLs for each Year, called YearlyNonTop100s.
3. Merge these two lists together (YearlyTop100s & YearlyNonTop100s), by year, called AllYearlyURLs.
4. Loop over every AllYearlyURLs entry, to merge all years together, which will create the final list called MasterURLs.
5. Loop over this MasterURLs list and append data onto a DataFrame, which will be exported to make up a BoxOfficeMojo database.

## Key Information to Scrape for each film:
- Title
- Distributor
- Genre
- MPAA Rating
- Production Budget
- Release Date
- Runtime
- Domestic
- Foreign
- Worldwide
- Opening Weekend Gross
- Opening Weekend Theaters
- Widest Theaters
- Director
- Writer
- Actors
- Producer
- Composer
- Genres
