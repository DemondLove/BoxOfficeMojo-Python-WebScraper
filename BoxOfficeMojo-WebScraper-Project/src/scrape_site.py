
# BoxOfficeMojo Python WebScraper Utility Package

if __name__ == '__main__':
    import sys

    import pandas as pd

    sys.path.append('/Users/Love/Documents/Projects/BoxOfficeMojo-Python-WebScraper/BoxOfficeMojo-WebScraper-Project/src/utils')

    import utils

    df = pd.DataFrame()

    li = ['https://www.boxofficemojo.com/movies/?id=scream.htm', 'https://www.boxofficemojo.com/movies/?id=girldragontattoo11.htm']

    for url in li:
        df = df.append(
            {
                'Title': utils.titleparser(url)
                , 'Distributor': utils.distributorparser(url)
                , 'Genre': utils.genreparser(url)
                , 'MPAA Rating': utils.mpaaratingparser(url)
                , 'Production Budget': utils.productionbudgetparser(url)
                , 'Release Date': utils.releasedateparser(url)
                , 'Runtime': utils.domesticparser(url)
                , 'Domestic': utils.domesticparser(url)
                , 'Foreign': utils.foreignparser(url)
                , 'Worldwide': utils.worldwideparser(url)
                , 'Opening Weekend Gross': utils.openingweekendgrossparser(url)
                , 'Opening Weekend Theaters': utils.openingweekendtheatersparser(url)
                , 'Widest Theaters': utils.widestreleaseparser(url)
                , 'Director': utils.directorparser(url)
                , 'Writer': utils.writerparser(url)
                , 'Actors': utils.actorparser(url)
                , 'Producer': utils.producerparser(url)
                , 'Composer': utils.composerparser(url)
                , 'Genres': utils.genresparser(url)
            }, ignore_index=True
        )

    print(df)
