'''
Created on 9 Dec 2016

@author: DDL
'''
from datetime import datetime
from MovieDDL.repository.RepositoryExceptions import FileRepositoryException
from MovieDDL.repository.RepositoryRentals import rentalRepository
import pickle

class rentalPickleRepository(rentalRepository):
    '''
    Hit all the walls in front of you in order to know how to avoid them the next time
    '''
    def __init__(self, repoMovie,fileName="rentals.pickle"):
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
        f=open(self.__fName,"rb")
        try:
            rentals=pickle.load(f)
            for key in rentals:
                rentalRepository.add_rental(self, rentals[key])
        except EOFError:
            rentalRepository.__movies={}
        except Exception as e:
            raise FileRepositoryException(e)
        finally:
            f.close()
    
    def __storeToFile(self):
        f=open(self.__fName, "wb")
        self.__rentals=rentalRepository.get_all(self)
        pickle.dump(self.__rentals, f)
        f.close