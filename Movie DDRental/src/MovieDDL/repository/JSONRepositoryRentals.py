'''
Created on 10 Dec 2016

@author: DDL
'''
from datetime import datetime
from MovieDDL.repository.RepositoryExceptions import FileRepositoryException
from MovieDDL.repository.RepositoryRentals import rentalRepository
from MovieDDL.domain.Entities import Rental
import json

class rentalJSONRepository(rentalRepository):
    '''
    Hit all the walls in front of you in order to know how to avoid them the next time
    '''
    def __init__(self, repoMovie,fileName="rentals.json"):
        '''
        Constructor for file repository
        Input: fileName - the name of the file
        Output: -
        '''
        rentalRepository.__init__(self, repoMovie)
        self.__fName=fileName
        self.__loadFromFile()
        self.setAvailability()
    
    def remove_rentals(self, Id):
        '''
        Method to remove a rental
        Input: Id - the id of the client
        Output: -
        '''
        removedRentals=rentalRepository.remove_rentals(self, Id)
        self.__storeToFile()
        return removedRentals
    
    def add_rentals(self, rentals):
        '''
        Method to add rentals
        Input: rentals - a list with the rentals that should be added
        Output: -
        '''
        rentalRepository.add_rentals(self, rentals)
        self.__storeToFile()
    
    def add_rental(self, rental):
        '''
        Method to add a new rental
        Input: rental - object of Class rental
        Output: -
        '''
        rentalRepository.add_rental(self, rental)
        self.__storeToFile()
    
    def remove_rental(self, Id):
        '''
        Method to remove an existing rental
        Input: Id - a natural number
        Output: -
        '''
        removedRental=rentalRepository.remove_rental(self, Id)
        self.__storeToFile()
        return removedRental
    
    def return_rental(self, clientId, movieId):
        '''
        Method to return a rental
        Input: clientId - the ID of the client
               movieId - the ID of the movie
        Output: -
        '''
        rental=rentalRepository.return_rental(self, clientId, movieId)
        self.__storeToFile()
        return rental
    
    def unreturn_rental(self, clientId, movieId):
        '''
        Method to unreturn a rental
        Input: clientId - the ID of the client
               movieId - the ID of the movie
        Output: -
        '''
        rental= rentalRepository.unreturn_rental(self, clientId, movieId)
        self.__storeToFile()
        return rental
        
    def __loadFromFile(self):
        f=open(self.__fName,"r")
        try:
            rentals=json.load(f)
            for key in rentals:
                rental=self._JSONtoRental(rentals[key])
                rentalRepository.add_rental(self, rental)
        except EOFError:
            rentalRepository.__rentals={}
        except Exception as e:
            raise FileRepositoryException(e)
        finally:
            f.close()
    
    def __storeToFile(self):
        f=open(self.__fName, "w")
        rentals={}
        self.__rentals=rentalRepository.get_all(self)
        for key in self.__rentals:
            rentDate=self.__rentals[key].get_rentDate()
            rentDate2=rentDate.strftime("%d-%m-%Y")
            self.__rentals[key].set_rentJSONDate(rentDate2)
            dueDate=self.__rentals[key].get_dueDate()
            dueDate2=dueDate.strftime("%d-%m-%Y")
            self.__rentals[key].set_dueJSONDate(dueDate2)
            returnedDate=self.__rentals[key].get_returnedDate()
            if returnedDate!=None:
                returnedDate2=returnedDate.strftime("%d-%m-%Y")
                self.__rentals[key].set_returnedDate(returnedDate2)
            rentals[key]=json.dumps(self.__rentals[key].__dict__)
            self.__rentals[key].set_rentDate(rentDate.day,rentDate.month,rentDate.year)
            self.__rentals[key].set_dueDate(dueDate.day,dueDate.month,dueDate.year)
            self.__rentals[key].set_returnedDate(returnedDate)
        json.dump(rentals, f)
        f.close
    
    def _JSONtoRental(self,object):
        '''
        Convert JSON object to Movie
        '''
        object=json.loads(object)
        rmovieId=object["_Rental__rmovieID"]
        rclientId=object["_Rental__rclientID"]
        id=object["_Rental__rentalID"]
        rentDate=object["_Rental__rentDate"]
        rentDate=datetime.strptime(rentDate, "%d-%m-%Y").date()
        dueDate=object["_Rental__dueDate"]
        dueDate=datetime.strptime(dueDate, "%d-%m-%Y").date()
        returnedDate=object["_Rental__returnDate"]
        rental=Rental(id,rmovieId,rclientId,rentDate,dueDate)
        if returnedDate!=None:
            returnedDate=datetime.strptime(returnedDate, "%d-%m-%Y").date()
            rental.set_returnedDate(returnedDate)
        return rental