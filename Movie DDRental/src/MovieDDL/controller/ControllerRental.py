'''
Created on 6 Nov 2016

@author: DDL
'''
from MovieDDL.controller.ControllerExceptions import ControllerException
import datetime

class rentalController:
    '''
    Contains functions which operates on rentals
    '''
    def __init__(self,repoMovie,repoClient,repoRental):
        '''
        Creates a controller for rentals
        '''
        self._repositoryRental=repoRental
        self._repositoryMovie=repoMovie
        self._repositoryClient=repoClient
    
    def _generateRentalID(self,Id):
            '''
            Generates a rental ID
            '''
            Rents=self._repositoryRental.get_all()
            for key in Rents:
                if Rents[key].get_rclientId()==Id and Rents[key].get_dueDate()<datetime.date.today():
                    client=self._repositoryClient.return_client_Id(Id)
                    movie=self._repositoryMovie.return_movie_Id(Rents[key].get_rmovieId())
                    if not movie.get_availability():
                        raise ControllerException("The client: '"+str(client.get_clientID())+" - "+str(client.get_clientName())+"' can't rent this movie!\nThe movie: '"+str(movie.get_Id())+" - "+str(movie.get_title())+"' passed the due date!\n")
            i=1
            while i in Rents:
                i+=1
            return i
    
    def _validateID(self,Id):
        '''
        Validates ID
        Exceptions: Controller Exception when ID is not a number
        '''
        try:
            Id=int(Id)
        except ValueError:
            raise ControllerException("The ID should be a number!\n")
    
    def get_allRentals(self):
        '''
        Returns the list of rentals
        '''
        return self._repositoryRental.get_all()
    
    def checks_movie(self,Id):
        '''
        Checks if a movie is in the list of availableMovies or not
        Input: Id - a number
        Output: -
        Exceptions: ControllerException from invalid Id or if the movie is not available
        '''
        self._validateID(Id)
        Id=int(Id)
        available=self._repositoryMovie.get_available()
        if not Id in available:
            raise ControllerException("The movie with the ID: "+str(Id)+" is not in the available list!\n")
        return
    
    def checks_client(self,Id):
        '''
        Checks if the client exists or not
        Input: Id - a number
        Output: -
        Exceptions: ControllerException from invalid Id or if the client can't be found
        '''
        self._validateID(Id)
        Id=int(Id)
        available=self._repositoryClient.get_all()
        if not Id in available:
            raise ControllerException("There is not client with the ID: "+str(Id)+"!\n")
        return
    
    def rent_movie(self,rental):
        '''
        Add a rental in the list of rentals
        Input: rental -  a list which contains the values of the fields of a rental
        Output: -
        Exceptions: -
        '''
        rentalId=self._generateRentalID(rental[1])
        rental.insert(0,rentalId)
        self._repositoryRental.add_rental(rental)
        self._repositoryMovie.change_availability(rental[1],False)
    
    def checks_movie2(self,Id):
        '''
        Checks if a movie is in the list of availableMovies or not
        Input: Id - a number
        Output: -
        Exceptions: ControllerException from invalid Id or if the movie is not available
        '''
        self._validateID(Id)
        Id=int(Id)
        alls=self._repositoryMovie.get_all()
        available=self._repositoryMovie.get_available()
        if not Id in alls:
            raise ControllerException("There is no movie with the ID: "+str(Id)+"!\n")
        if Id in available:
            raise ControllerException("The movie with the ID: "+str(Id)+" wasn't rented!\n")
        return
    
    
    def return_rental(self,clientId,movieId):
        '''
        Removes a rental from the list of rentals
        Input: rental -  a list which contains the values of the fields of a rental
        Output: -
        Exceptions: -
        '''
        clientId=int(clientId)
        movieId=int(movieId)
        rental=self._repositoryRental.return_rental(clientId,movieId)
        self._repositoryMovie.change_availability(rental.get_rmovieId(),True)
        
####################################################################################
#################################################################################