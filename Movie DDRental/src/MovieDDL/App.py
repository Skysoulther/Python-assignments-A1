'''
Created on 5 Nov 2016

@author: DDL
'''
from MovieDDL.domain import Validator
from MovieDDL.controller import ControllerMovie
from MovieDDL.controller import ControllerClient
from MovieDDL.controller import ControllerRental
from MovieDDL.ui import MenuUI
from MovieDDL.repository import RepositoryMovies
from MovieDDL.repository import RepositoryClients
from MovieDDL.repository import RepositoryRentals

class Application():
    def __init__(self):
        '''
        Creates the application
        ''' 
        movieValid=Validator.MovieValidator()
        clientValid=Validator.ClientValidator()
        rentalValid=Validator.RentalValidator()
        movieRepo=RepositoryMovies.movieRepository(movieValid,"movies.txt")
        clientRepo=RepositoryClients.clientRepository(clientValid,"clients.txt")
        rentalRepo=RepositoryRentals.rentalRepository(rentalValid,"rentals.txt",movieRepo)
        movieControl=ControllerMovie.movieController(movieRepo)
        clientControl=ControllerClient.clientController(clientRepo)
        rentalControl=ControllerRental.rentalController(movieRepo,clientRepo,rentalRepo)
        self._mainMenu=MenuUI.Menu(movieControl,clientControl,rentalControl)
    
    def run(self):
        '''
        run the application
        '''
        self._mainMenu.run()
    
app=Application()
app.run()