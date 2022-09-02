from flask_testing import LiveServerTestCase
from urllib.request import urlopen
from flask import url_for

# this is testing 3
from app import app,musicDBConnection

class TestBase(LiveServerTestCase):
    TEST_PORT=5050 #test port,does not need to be open


def musicDBConnection():  
    app.config.update(
        SQLALCHEMY_DATABASE_URI="sqlite:///",
        LIVESERVER_PORT=Self.TEST_PORT,            
        DEBUG=True,
        TESTING=True
    )
    return app
def setUp(self):
    from app import c7Music
    musicDBConnection.app() 

   