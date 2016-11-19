'''
Created on 5 Nov 2016

@author: DDL
'''
import datetime
from MovieDDL.domain import Entities, Validator
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
        movies={1:Entities.Movie(1,"The Shawshank Redemption","Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.","Drama"),
                2:Entities.Movie(2,"The Godfather","The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.","Drama"),
                3:Entities.Movie(3,"The Godfather: Part II","The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on his crime syndicate stretching from Lake Tahoe, Nevada to pre-revolution 1958 Cuba.","Drama"),
                4:Entities.Movie(4,"The Dark Knight","When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice","Action"),
                5:Entities.Movie(5,"Schindler's List","In German-occupied Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazi Germans.","Biography"),
                6:Entities.Movie(6,"The Lord of the Rings: The Return of the King","Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.","Adventure"),
                7:Entities.Movie(7,"The Good, the Bad and the Ugly","A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.","Western"),
                8:Entities.Movie(8,"Fight Club","An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.","Drama"),
                9:Entities.Movie(9,"The Lord of the Rings: The Fellowship of the Ring","A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle Earth from the Dark Lord Sauron.","Adventure"),
                10:Entities.Movie(10,"Monty Python and the Holy Grail","King Arthur and his knights embark on a low-budget search for the Grail, encountering many, very silly obstacles.","Comedy"),
                11:Entities.Movie(11,"Doctor Strange","A former neurosurgeon embarks on a journey of healing only to be drawn into the world of the mystic arts.","Fantasy"),
                12:Entities.Movie(12,"Hacksaw Ridge","WWII American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, refuses to kill people and becomes the first Conscientious Objector in American history to be awarded the Medal of Honor.","Biography"),
                13:Entities.Movie(13,"Suicide Squad","A secret government agency recruits some of the most dangerous incarcerated super-villains to form a defensive task force. Their first mission: save the world from the apocalypse.","Action"),
                14:Entities.Movie(14,"Doctor Strange","A former neurosurgeon embarks on a journey of healing only to be drawn into the world of the mystic arts.","Fantasy"),
                15:Entities.Movie(15,"Mr. Nobody","A boy stands on a station platform as a train is about to leave. Should he go with his mother or stay with his father? Infinite possibilities arise from this decision. As long as he doesn't choose, anything is possible.","Fantasy"),
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
        for i in range(11,16):
            movies[i].set_availability(False)
        rentals={1:Entities.Rental(1,13,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=13,month=11,year=2016)),
                 2:Entities.Rental(2,14,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=26,month=11,year=2016)),
                 3:Entities.Rental(3,12,1,datetime.date(day=1,month=11,year=2016),datetime.date(day=8,month=11,year=2016)),
                 4:Entities.Rental(4,15,10,datetime.date(day=10,month=11,year=2016),datetime.date(day=13,month=11,year=2017)),
                 5:Entities.Rental(5,11,1,datetime.date(day=7,month=11,year=2016),datetime.date(day=14,month=11,year=2016))
                 }
        '''
                 6:Entities.Rental(6,8,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=13,month=11,year=2016)),
                 7:Entities.Rental(7,8,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=13,month=11,year=2016)),
                 8:Entities.Rental(8,8,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=13,month=11,year=2016)),
                 9:Entities.Rental(9,8,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=13,month=11,year=2016)),
                 10:Entities.Rental(10,8,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=13,month=11,year=2016))
                 }
        '''
        movieValid=Validator.MovieValidator()
        clientValid=Validator.ClientValidator()
        rentalValid=Validator.RentalValidator()
        movieRepo=RepositoryMovies.movieRepository(movieValid,movies)
        clientRepo=RepositoryClients.clientRepository(clientValid,clients)
        rentalRepo=RepositoryRentals.rentalRepository(rentalValid,rentals)
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