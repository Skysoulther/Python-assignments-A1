'''
Created on 5 Nov 2016

@author: DDL
'''
from MovieDDL.domain.ValidatorExceptions import StoreException

class MovieValidator():
    '''
    A class to validates fields of a movie
    '''
    def __init__(self):
        '''
        Creates a validator for movies
        '''
        self._errors=""
    
    def _clearErrors(self):
        '''
        clear the string
        '''
        self._errors=""
    
    def _validateId(self, Id):
        '''
        Validates the ID of a Movie
        '''
        if Id>9999:
            self._errors+="The ID can't be greater than 9999! :)\n"
        if Id<0:
            self._errors+="The ID can't be smaller than 0! :)\n"
    
    def _validateTitle(self, title):
        '''
        Validates the title of a Movie
        '''
        if len(title)>49:
            self._errors+="The title of the movie is too long!It should be shorter than 50 letters\n"
        
    def _validateGenre(self, genre):
        genre=genre.lower()
        genres=["sci-fi","crime","horror","comedy","drama","action","adventure","biography","western","fantasy","mystery","animation","war","thriller","romance"]
        if not genre in genres:
            self._errors+="The genre is not recognized by the app\n"
        if len(genre)>15:
            self._errors+="The genre should be shorter than 15 letters!\n"
    
    def validateMovie(self, movie):
        '''
        validates a movie
        '''
        self._clearErrors()
        self._validateId(movie.get_Id())
        self._validateTitle(movie.get_title())
        self._validateGenre(movie.get_genre())
        if len(self._errors)>0:
            raise StoreException(self._errors)
        return True
    
    def validateID(self, Id):
        '''
        validates an id
        '''
        self._clearErrors()
        self._validateId(Id)
        if len(self._errors)>0:
            raise StoreException(self._errors)
        return True
    
class ClientValidator():
    '''
    A class to validates fields of a client
    '''
    def __init__(self):
        '''
        Creates a validator for clients
        '''
        self._errors=""
    
    def _clearErrors(self):
        '''
        clear the string
        '''
        self._errors=""
    
    def _validateId(self, Id):
        '''
        Validates the ID of a Movie
        '''
        if Id>9999:
            self._errors+="The ID can't be greater than 9999! :)\n"
        if Id<0:
            self._errors+="The ID can't be smaller than 0! :)\n"
        
    def _validateName(self, name):
        '''
        Validates the name of a Client
        '''
        if len(name)>24:
            self._errors+="The name of the client is too long! It should be shorter than 25 letters!\n"
    
    def validateClient(self, client):
        '''
        validates a client
        '''
        self._clearErrors()
        self._validateId(client.get_clientID())
        self._validateName(client.get_clientName())
        if len(self._errors)>0:
            raise StoreException(self._errors)
        return True
        
    def validateID(self, Id):
        '''
        validates an id
        '''
        self._clearErrors()
        self._validateId(Id)
        if len(self._errors)>0:
            raise StoreException(self._errors)
        return True

class RentalValidator():
    '''
    A class to validates fields of a rented movie
    '''
    def __init__(self):
        '''
        Creates a validator for rented movies
        '''
        self._errors=""
        
    def _clearErrors(self):
        '''
        clear the string
        '''
        self._errors=""
    
    def _validateId(self, Id):
        '''
        Validates the ID of a Movie
        '''
        if Id>9999:
            self._errors+="The ID can't be greater than 9999! :)\n"
        if Id<0:
            self._errors+="The ID can't be smaller than 0! :)\n"
        
    def _validateDueDate(self,dueDate, rentedDate):
        '''
        Validates the DueDate of the movie
        '''
        if dueDate<rentedDate:
            self._errors+="The dueDate can't be smaller than the day of rental!\n"
        
    def _validateReturnedDate(self, returnDate, rentedDate):
        '''
        Validates the Duedate of the movie
        '''
        if returnDate:
            if returnDate<rentedDate:
                self._errors+="You can't return a movie before rental!\n"
        
    def validateRental(self,rental):
        '''
        Validates a Rental
        '''
        self._clearErrors()
        self._validateId(rental.get_rentalId())
        self._validateId(rental.get_rclientId())
        self._validateId(rental.get_rmovieId())
        self._validateDueDate(rental.get_dueDate(), rental.get_rentDate())
        self._validateReturnedDate(rental.get_returnedDate(), rental.get_rentDate())
        if len(self._errors)>0:
            raise StoreException(self._errors)
        return True
        
    def validateID(self, Id):
        '''
        validates an id
        '''
        self._clearErrors()
        self._validateId(Id)
        if len(self._errors)>0:
            raise StoreException(self._errors)
        return True

#############################################################
        