'''
Created on 5 Nov 2016

@author: DDL
'''
from MovieDDL.domain import Entities, Validator
from MovieDDL.controller import controllerMovie
from MovieDDL.controller import controllerClient
from MovieDDL.controller import controllerRental
from MovieDDL.ui import menuUI
from MovieDDL.repository import repositoryMovies
from MovieDDL.repository import repositoryClients
from MovieDDL.repository import repositoryRentals

class Application():
    def __init__(self):
        '''
        Creates the application
        '''
        movies={1:Entities.Movie(1,"The Shawshank Redemption","Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.","Drama"),
                2:Entities.Movie(2,"The Godfather","The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.","Drama"),
                3:Entities.Movie(3,"The Godfather: Part II","The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on his crime syndicate stretching from Lake Tahoe, Nevada to pre-revolution 1958 Cuba.","Drama"),
                4:Entities.Movie(4,"The Dark Knight","When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice","Action"),
                5:Entities.Movie(5,"Schindler's List","In German-occupied Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazi Germans.","Biography"),
                6:Entities.Movie(6,"The Lord of the Rings: The Return of the King","Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.","Adventure"),
                7:Entities.Movie(7,"The Good, the Bad and the Ugly","A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.","Western"),
                8:Entities.Movie(8,"Fight Club","An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.","Drama"),
                9:Entities.Movie(9,"The Lord of the Rings: The Fellowship of the Ring","A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle Earth from the Dark Lord Sauron.","Adventure"),
                10:Entities.Movie(10,"Monty Python and the Holy Grail","King Arthur and his knights embark on a low-budget search for the Grail, encountering many, very silly obstacles.","Comedy")
                }
        clients={1:Entities.Client(1,"Popescu Ion"),
                 2:Entities.Client(2,"Martinescu Martin"),
                 3:Entities.Client(3,"Lucescu Luca"),
                 4:Entities.Client(4,"Mark Manson"),
                 5:Entities.Client(5,"Cinci Bob"),
                 6:Entities.Client(6,"Grasu George"),
                 7:Entities.Client(7,"Monkey Gabriel"),
                 8:Entities.Client(8,"Octopus"),
                 9:Entities.Client(9,"5QY7 Bot"),
                 10:Entities.Client(10,"Mr Nobody")
                 }
        rentals={}
        movieValid=Validator.MovieValidator()
        clientValid=Validator.ClientValidator()
        rentalValid=Validator.RentalValidator()
        movieRepo=repositoryMovies.movieRepository(movieValid,movies)
        clientRepo=repositoryClients.clientRepository(clientValid,clients)
        rentalRepo=repositoryRentals.rentalRepository(rentalValid,rentals)
        movieControl=controllerMovie.movieController(movieRepo)
        clientControl=controllerClient.clientController(clientRepo)
        rentalControl=controllerRental.rentalController(rentalRepo)
        self._mainMenu=menuUI.Menu(movieControl,clientControl,rentalControl)
    
    def run(self):
        '''
        run the application
        '''
        self._mainMenu.run()
    
app=Application()
app.run()