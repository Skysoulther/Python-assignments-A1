'''
Created on 27 Nov 2016

@author: DDL
'''
from datetime import datetime
from MovieDDL.repository.RepositoryExceptions import FileRepositoryException
from MovieDDL.repository.RepositoryRentals import rentalRepository
from MovieDDL.domain.Entities import Rental

class rentalFileRepository(rentalRepository):
    '''
    Hit all the walls in front of you in order to know how to avoid them the next time
    '''
    def __init__(self, repoMovie,fileName="rentals.txt"):
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
        try:
            f=open(self.__fName,"r")
            line=f.readline().strip()
            while line!="":
                attrs=line.split(";")
                attrs[3]=datetime.strptime(attrs[3],"%d-%m-%Y").date()
                attrs[4]=datetime.strptime(attrs[4],"%d-%m-%Y").date()
                rental=Rental(int(attrs[0]),int(attrs[1]),int(attrs[2]),attrs[3],attrs[4])
                if len(attrs)==6:
                    attrs[5]=datetime.strptime(attrs[5],"%d-%m-%Y").date()
                    rental.set_returnedDate(attrs[5])
                rentalRepository.add_rental(self, rental)
                line=f.readline().strip()
        except IOError:
            raise FileRepositoryException()
        finally:
            f.close
    
    def __storeToFile(self):
        f=open(self.__fName, "w")
        rentals=rentalRepository.get_all(self)
        for key in rentals:
            rentDate=rentals[key].get_rentDate()
            rentDate=rentDate.strftime("%d-%m-%Y")
            dueDate=rentals[key].get_dueDate()
            dueDate=dueDate.strftime("%d-%m-%Y")
            strf=str(rentals[key].get_rentalId())+";"+str(rentals[key].get_rmovieId())+";"+str(rentals[key].get_rclientId())+";"+str(rentDate)+";"+str(dueDate)
            returnedDate=rentals[key].get_returnedDate()
            if returnedDate!=None:
                returnedDate=returnedDate.strftime("%d-%m-%Y")
                strf+=";"+str(returnedDate)
            strf+="\n"
            f.write(strf)
        f.close