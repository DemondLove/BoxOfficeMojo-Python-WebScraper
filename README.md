# BoxOfficeMojo.com Python WebScraper

***NOTE: NOT IN USE DUE TO BOXOFFICEMOJO'S CONDITIONS OF USE AND "BOXOFFICEMOJO.COM BY IMDbPro" REFRESH***

Web Scraping Package created to archive a BoxOfficeMojo database.

## Using https://www.boxofficemojo.com/yearly/ as a Home Directory, the general approach is:
1. Scrape a list of URLs for each Year listed in the home directory, called YearlyTop100s.
2. Loop over YearlyTop100s and return another list of the footer URLs for each Year, called YearlyNonTop100s.
3. Merge these two lists together (YearlyTop100s & YearlyNonTop100s), by year, called AllYearlyURLs.
4. Loop over every AllYearlyURLs entry, to merge all years together, which will create the final list called MasterURLs.
5. Loop over this MasterURLs list and append data onto a DataFrame, which will be exported to make up a BoxOfficeMojo database.
6. Expose the results as a private RESTful API

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

Next Steps:
1. Refactor code base to properly pull from the new structure.
2. Refactor code base to be object-oriented
3. Restructure MySQL database to initially store data in a document-based approach, then as a relational approach.
4. Consider utilizing MongoDB if I can do relational queries with each.
5. Consider implementing into AWS w/ SQS, auto-scaling EC2s, Lambda, Airflow, RDS, and S3 for logs.
