# BoxOfficeMojo Python WebScraper Master Script

if __name__ == '__main__':
    import sys
    import os
    import pymysql
    import inspect
    import pandas as pd
    import sqlalchemy as sql

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
                'id': len(df)
                , 'Title': utils.titleparser(url)
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
        
    df.to_csv(curpath + '/data/BoxOfficeMojoDataset.csv',index=False)

    # Create connection variables
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    DB_HOST = 'localhost'
    DB_PORT = 3306
    DATABASE = 'movies'

    # Connect to the database for pymysql connection
    connection = pymysql.connect(host=DB_HOST,
                                 user=os.environ.get('DB_USER'),
                                 password=os.environ.get('DB_PASS'),
                                 db=DATABASE,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    # Create connection string for sqlalchemy
    connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)

    # To setup the persistent connection, you do the following:
    sql_engine = sql.create_engine(connect_string)
    
    # Ensue the features are in the appropriate order to be inserted into the database
    df[['id', 'Title', 'Distributor', 'Genre', 'MPAARating', 'ProductionBudget', 'ReleaseDate', 'Runtime', 'DomesticGross', 'ForeignGross', 'WorldwideGross', 'OpeningWeekendGross', 'OpeningWeekendTheaters', 'WidestTheaters', 'Genres', 'URL']]

    for i in range(len(df)):
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `BoxOfficeMojo` (`id`, `Title`, `Distributor`, `Genre`, `MPAARating`, `ProductionBudget`, `ReleaseDate`, `Runtime`, `DomesticGross`, `ForeignGross`, `WorldwideGross`, `OpeningWeekendGross`, `OpeningWeekendTheaters`, `WidestTheaters`, `Genres`, `URL`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (str(df.iloc[i][0]), str(df.iloc[i][1]), str(df.iloc[i][2]), str(df.iloc[i][3]), str(df.iloc[i][4]), str(df.iloc[i][5]), str(df.iloc[i][6]), str(df.iloc[i][7]), str(df.iloc[i][8]), str(df.iloc[i][9]), str(df.iloc[i][10]), str(df.iloc[i][11]), str(df.iloc[i][12]), str(df.iloc[i][13]), str(df.iloc[i][14]), str(df.iloc[i][15])))
    # connection is not autocommit by default. So you must commit to save your changes.
    connection.commit()