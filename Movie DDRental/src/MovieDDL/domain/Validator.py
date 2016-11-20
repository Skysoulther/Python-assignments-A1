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
        genres=["horror","comedy","drama","action","adventure","biography","western","fantasy"]
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
    
    def validateID(self, Id):
        '''
        validates an id
        '''
        self._clearErrors()
        self._validateId(Id)
        if len(self._errors)>0:
            raise StoreException(self._errors)
    
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
        
    def validateID(self, Id):
        '''
        validates an id
        '''
        self._clearErrors()
        self._validateId(Id)
        if len(self._errors)>0:
            raise StoreException(self._errors)

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
        
    def validateID(self, Id):
        '''
        validates an id
        '''
        self._clearErrors()
        self._validateId(Id)
        if len(self._errors)>0:
            raise StoreException(self._errors)

#############################################################

#################################################################

def testMovieValidator():
    '''
    Test the validator for movies
    '''
    from MovieDDL.domain.Entities import Movie
    movValidator=MovieValidator()
    movie1=Movie(1,"Good Title","Description1","horror")
    movie2=Movie(10000,"Bad Title sssssssssssssssssssssssssssssssssssssss", "Description2","bad genre")
    try:
        movValidator.validateMovie(movie1)
        assert True
    except StoreException:
        assert False
    
    try:
        movValidator.validateMovie(movie2)
        assert False
    except StoreException:
        assert True
    
    try:
        movValidator.validateID(-2)
        assert False
    except StoreException:
        assert True
    
    try:
        movValidator.validateID(25)
        assert True
    except StoreException:
        assert False

def testClientValidator():
    '''
    Test the validator for clients
    '''
    from MovieDDL.domain.Entities import Client
    cliValidator=ClientValidator()
    client1=Client(1,"Good Client")
    client2=Client(10000,"Bad Client sssssssssssssssssssssssssssssssssssssss")
    try:
        cliValidator.validateClient(client1)
        assert True
    except StoreException:
        assert False
    
    try:
        cliValidator.validateClient(client2)
        assert False
    except StoreException:
        assert True
    
    try:
        cliValidator.validateID(-2)
        assert False
    except StoreException:
        assert True
    
    try:
        cliValidator.validateID(25)
        assert True
    except StoreException:
        assert False

def testRentalValidator():
    '''
    Test the validator for rentals
    '''
    from MovieDDL.domain.Entities import Movie,Client,Rental
    import datetime
    rentValidator=RentalValidator()
    rDate1=datetime.date(year=2016, month=10, day=30)
    dDate1=datetime.date(year=2016, month=11, day=7)
    dDate2=datetime.date(year=2015, month=10, day=10)
    movie1=Movie(13,"A beautiful Mind","A movie about the life of John Nash","Biography")
    client1=Client(47,"Sergiu Gherman")
    rental1=Rental(1,movie1,client1,rDate1,dDate1)
    rental2=Rental(2,movie1,client1,rDate1,dDate2)
    try:
        rentValidator.validateRental(rental1)
        assert True
    except StoreException:
        assert False
    
    try:
        rentValidator.validateRental(rental2)
        assert False
    except StoreException:
        assert True
    
    try:
        rentValidator.validateID(-2)
        assert False
    except StoreException:
        assert True
    
    try:
        rentValidator.validateID(25)
        assert True
    except StoreException:
        assert False
    
def testValidators():
    '''
    test all validators
    '''
    testMovieValidator()
    testClientValidator()
    testRentalValidator()
    print("Well done!")
    
#testValidators()
    
        
    
        