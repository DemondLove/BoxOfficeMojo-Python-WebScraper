# Read-Only RESTful API (only including GET requests)
import cherrypy
import pandas as pd
import pymysql
import socket
import os

# Create database connection variables
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = 'localhost' # replace with AWS RDS host
DB_PORT = 3306 # replace with AWS RDS port   
DATABASE = 'movies'

# Connect to the database for pymysql connection
conn = pymysql.connect(host=DB_HOST,
                       port=DB_PORT,
                       user=os.environ.get('DB_USER'),
                       password=os.environ.get('DB_PASS'))


# Create RESTful API
@cherrypy.expose
class restfulAPI(object):
    
    @cherrypy.tools.json_out()
    def GET(self, title):
    '''
    Retrieve an existing film from BoxOfficeMojo database.
    
    Parameters:
    title (string): title for a single film on BoxOfficeMojo.
    
    Returns:
    query (json): Title, Distributor, Genre, MPAARating, ProductionBudget, ReleaseDate, Runtime, DomesticGross, ForeignGross, WorldwideGross, OpeningWeekendGross, OpeningWeekendTheaters, WidestTheaters associated to the film.
    '''
        try:
            query = pd.read_sql('''SELECT Title
                                , Distributor
                                , Genre
                                , MPAARating
                                , ProductionBudget
                                , ReleaseDate
                                , Runtime
                                , DomesticGross
                                , ForeignGross
                                , WorldwideGross
                                , OpeningWeekendGross
                                , OpeningWeekendTheaters
                                , WidestTheaters
                                FROM movies.BoxOfficeMojo
                                WHERE Title = %s'''
                                , params=[title]
                                , con=conn).to_dict('records')[0]
            return query
        
        except Exception as e:
            print(e)
    
# Configure the URI to be the current pc's IP Address (Need to update with AWS VPC info)
cherrypy.config.update({
    'server.socket_host': socket.gethostbyname(socket.gethostname()), # Enter current pc's IP Address
    'server.socket_port': 8888})

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }
    }
    cherrypy.quickstart(restfulAPI(), '/', conf)
