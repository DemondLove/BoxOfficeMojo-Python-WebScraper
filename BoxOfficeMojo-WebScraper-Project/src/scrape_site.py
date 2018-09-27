
# BoxOfficeMojo Python WebScraper Utility Package

if __name__ == '__main__':
    import sys

    import pandas as pd

    sys.path.append('/Users/Love/Documents/Projects/BoxOfficeMojo-Python-WebScraper/BoxOfficeMojo-WebScraper-Project/src/utils')

    import utils

    url = 'https://www.boxofficemojo.com/yearly/'

    MasterURLs = utils.MasterURLsparser(url)

    df = pd.DataFrame()

    for url in MasterURLs:
        df = df.append(
            {
                'Title': utils.titleparser(url)
                , 'Distributor': utils.distributorparser(url)
                , 'Genre': utils.genreparser(url)
                , 'MPAA Rating': utils.mpaaratingparser(url)
                , 'Production Budget': utils.productionbudgetparser(url)
                , 'Release Date': utils.releasedateparser(url)
                , 'Runtime': utils.runtimeparser(url)
                , 'Domestic': utils.domesticparser(url)
                , 'Foreign': utils.foreignparser(url)
                , 'Worldwide': utils.worldwideparser(url)
                , 'Opening Weekend Gross': utils.openingweekendgrossparser(url)
                , 'Opening Weekend Theaters': utils.openingweekendtheatersparser(url)
                , 'Widest Theaters': utils.widestreleaseparser(url)
                # , 'Director': directorparser(url)
                # , 'Writer': writerparser(url)
                # , 'Actors': actorparser(url)
                # , 'Producer': producerparser(url)
                # , 'Composer': composerparser(url)
                # , 'Genres': utils.genresparser(url)
            }, ignore_index=True
        )
        print(url)
