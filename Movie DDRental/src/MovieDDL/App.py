'''
Created on 5 Nov 2016

@author: DDL
'''
from MovieDDL.domain import Validator
from MovieDDL.controller import ControllerMovie
from MovieDDL.controller import ControllerClient
from MovieDDL.controller import ControllerRental
from MovieDDL.controller import UndoController
from MovieDDL.ui import MenuUI
from MovieDDL.ui import GUI
from MovieDDL.repository import FileRepositoryMovies
from MovieDDL.repository import FileRepositoryClients
from MovieDDL.repository import FileRepositoryRentals
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
        movieRepo=FileRepositoryMovies.movieFileRepository("movies.txt")
        clientRepo=FileRepositoryClients.clientFileRepository("clients.txt")
        rentalRepo=FileRepositoryRentals.rentalFileRepository(movieRepo,"rentals.txt")
        undoController=UndoController.undoController()
        movieControl=ControllerMovie.movieController(movieRepo,movieValid,undoController)
        clientControl=ControllerClient.clientController(clientRepo,clientValid,undoController)
        rentalControl=ControllerRental.rentalController(movieRepo,clientRepo,rentalRepo,rentalValid,undoController)
        self._mainMenu=MenuUI.Menu(movieControl,clientControl,rentalControl)
        self._GUI=GUI.MenuGUI(movieControl,clientControl,rentalControl)
    
    def run1(self):
        '''
        run the application
        '''
        self._mainMenu.run()
    
    def run2(self):
        '''
        run the application
        '''
        self._GUI.run()
    
app=Application()
app.run2()
#app.run1()