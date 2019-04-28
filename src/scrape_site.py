# BoxOfficeMojo Python WebScraper Master Script

if __name__ == '__main__':
    import sys
    import os
    import inspect
    import pandas as pd

    filename = inspect.getframeinfo(inspect.currentframe()).filename
    curpath = os.path.dirname(os.path.abspath(filename))
    sys.path.insert(0, curpath + '/utils')

    import utils

    HomeDirectory = 'https://www.boxofficemojo.com/yearly/'

    MasterURLs = utils.MasterURLsparser(HomeDirectory)

    df = pd.DataFrame()

    for url in MasterURLs:
        df = df.append(
            {
                'Title': utils.titleparser(url)
                , 'Distributor': utils.distributorparser(url)
                , 'Genre': utils.genreparser(url)
                , 'MPAARating': utils.mpaaratingparser(url)
                , 'ProductionBudget': utils.productionbudgetparser(url)
                , 'ReleaseDate': utils.releasedateparser(url)
                , 'Runtime': utils.runtimeparser(url)
                , 'DomesticGross': utils.domesticparser(url)
                , 'ForeignGross': utils.foreignparser(url)
                , 'WorldwideGross': utils.worldwideparser(url)
                , 'OpeningWeekendGross': utils.openingweekendgrossparser(url)
                , 'OpeningWeekendTheaters': utils.openingweekendtheatersparser(url)
                , 'WidestTheaters': utils.widestreleaseparser(url)
                # , 'Director': utils.directorparser(url)
                # , 'Writer': utils.writerparser(url)
                # , 'Actors': utils.actorparser(url)
                # , 'Producer': utils.producerparser(url)
                # , 'Composer': utils.composerparser(url)
                , 'Genres': utils.genresparser(url)
                , 'URL': str(url)
            }, ignore_index=True
        )
        
    df.to_csv(curpath + '/data/BoxOfficeMojoDataset.csv')
