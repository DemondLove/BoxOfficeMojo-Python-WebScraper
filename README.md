# BoxOfficeMojo.com Python WebScraper

Web Scraping Package created to archive a BoxOfficeMojo database.

Key Information to Scrape for Each Film:
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

Using https://www.boxofficemojo.com/yearly/ as a Home Directory, the general approach is:
1. Scrape a list of URLs for each Year listed, called YearlyTop100s.
2. Loop over YearlyTop100s and return another list the Footer URLs for each Year, called YearlyNonTop100s.
3. Merge these two lists together (YearlyTop100s & YearlyNonTop100s), called AllYearlyURLs.
4. Loop over every AllYearlyURLs entry, to pull another list called MasterURLs.
5. Loop over this MasterURLs list and append data onto a master DataFrame, which will make up a BoxOfficeMojo database.
