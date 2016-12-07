'''
Created on 6 Nov 2016

@author: DDL
'''
from MovieDDL.domain.Entities import Rental
from MovieDDL.controller.UndoController import Operation
from MovieDDL.controller.ControllerExceptions import ControllerException
import datetime

class rentalController:
    '''
    Contains functions which operates on rentals
    '''
    def __init__(self,repoMovie,repoClient,repoRental,validator,undo):
        '''
        Creates a controller for rentals
        '''
        self._undoControl=undo
        self._repositoryRental=repoRental
        self._repositoryMovie=repoMovie
        self._repositoryClient=repoClient
        self.__validator=validator
        self.__functions={"add_movie":self._repositoryMovie.add_movie,
                          "remove_movie":self._repositoryMovie.remove_movie,
                          "edit_movie":self._repositoryMovie.update_movie,
                          "add_client":self._repositoryClient.add_client,
                          "remove_client":self._repositoryClient.remove_client,
                          "edit_client":self._repositoryClient.update_client,
                          "remove_rentals":self._repositoryRental.remove_rentals,
                          "add_rentals":self._repositoryRental.add_rentals,
                          "rent_movie":self._repositoryRental.add_rental,
                          "unrent_movie":self._remove_rental,
                          "return_movie":self._return_rental,
                          "unreturn_movie":self._disable_return}
    
    def _generate_rentalID(self,Id):
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
        return True
    
    def remove_rentals(self,client):
        '''
        Remove some rentals from the repository if they exist
        Input: client - a client Object
        Output: -
        Exceptions: Controller Exception when Id is not valid
        '''
        Id=client.get_clientID()
        self.__validator.validateID(Id)
        removedRentals=self._repositoryRental.remove_rentals(Id)
        self._undoControl.store_undo([Operation("add_client",[client]),Operation("add_rentals",[removedRentals])])
        self._undoControl.store_redo([Operation("remove_client",[client.get_clientID()]),Operation("remove_rentals",[client.get_clientID()])])
    
    def add_rentals(self,rentals):
        '''
        Add some rentals in the repository if they exist
        Input: rentals - a list of rentals
        Output: -
        Exceptions: Controller Exception when Id is not valid
        '''
        self._repositoryRental.add_rentals(rentals)
    
    def _remove_rental(self,Id):
        '''
        Remove rental from the repository
        Input: Id - the ID of the rental
        Output: -
        Exceptions: Controller Exception when the Id of the rental is not valid
        '''
        rental=self._repositoryRental.remove_rental(Id)
        self._repositoryMovie.change_availability(rental.get_rmovieId(),True)
    
    
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
        return True
    
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
        return True
    
    def rent_movie(self,rental):
        '''
        Add a rental in the list of rentals
        Input: rental -  a list which contains the values of the fields of a rental
        Output: -
        Exceptions: StoreException if the data from rental is invalid
        '''
        rentalId=self._generate_rentalID(rental[1])
        rental.insert(0,rentalId)
        rental=Rental(rental[0],rental[1],rental[2],rental[3],rental[4])
        self.__validator.validateRental(rental)
        self._repositoryRental.add_rental(rental)
        self._repositoryMovie.change_availability(rental.get_rmovieId(),False)
        self._undoControl.store_undo([Operation("unrent_movie",[rental.get_rentalId()])])
        self._undoControl.store_redo([Operation("rent_movie",[rental])])
    
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
            raise ControllerException("The movie with the ID: "+str(Id)+" is not rented!\n")
        return True
    
    
    def return_rental(self,clientId,movieId):
        '''
        Return a rental from the list of rentals
        Input: clientId -  the Id of the client
               movieId - the Id of the movie
        Output: -
        Exceptions: -
        '''
        clientId=int(clientId)
        movieId=int(movieId)
        rental=self._repositoryRental.return_rental(clientId,movieId)
        self._repositoryMovie.change_availability(rental.get_rmovieId(),True)
        self._undoControl.store_undo([Operation("unreturn_movie",[clientId,movieId])])
        self._undoControl.store_redo([Operation("return_movie",[clientId,movieId])])
        
    def _return_rental(self,clientId,movieId):
        '''
        Return a rental from the list of rentals
        Input: clientId -  the Id of the client
               movieId - the Id of the movie
        Output: -
        Exceptions: -
        '''
        clientId=int(clientId)
        movieId=int(movieId)
        rental=self._repositoryRental.return_rental(clientId,movieId)
        self._repositoryMovie.change_availability(rental.get_rmovieId(),True)
        
    def _disable_return(self,clientId,movieId):
        '''
        Set as unreturned a rental from the list of rentals
        Input: clientId -  the Id of the client
               movieId - the Id of the movie
        Output: -
        Exceptions: -
        '''
        rental=self._repositoryRental.unreturn_rental(clientId,movieId)
        self._repositoryMovie.change_availability(rental.get_rmovieId(),False)
        
        
    def all_rentals(self):
        '''
        returns a list of rentals
        Input: -
        Output: rentedMovies -  the list of rentals
        Exceptions: -
        '''
        rentedMovies=[]
        allMovies=self._repositoryMovie.get_all()
        for key in allMovies:
            if not allMovies[key].get_availability():
                rentedMovies.append(allMovies[key])
        return rentedMovies
    
    def _calculate_lateDays(self,dueDate,returnDate):
        '''
        Calculates the late rental days of a rental
        Input: dueDate - duedate of the rental
               returnDate - returndate of the movie
        Output: delta.days - number of late rental days of a rental
        Exceptions: -
        '''
        today=datetime.date.today()
        delta=today-today
        if today>dueDate:
            if returnDate==None:
                delta=today-dueDate
            elif returnDate>dueDate:
                delta=returnDate-dueDate
        return delta.days
    
    def _calculate_days(self,rentDate,returnDate):
        '''
        Calculates the rental days of a rental
        Input: rentDate - rent date of the rental
               returnDate - returndate of the movie
        Output: delta.days - number of late rental days of a rental
        Exceptions: -
        '''
        today=datetime.date.today()
        if returnDate==None:
            delta=today-rentDate
        else:
            delta=returnDate-rentDate
        return delta.days
    
    def late_rentals(self):
        '''
        returns a list of rentals which are late with their returns
        Input: -
        Output: list2 - the list of late rentals
        Exceptions: -
        '''
        dtoList=[]
        list1=[]
        allMovies=self._repositoryMovie.get_all()
        rentals=self._repositoryRental.get_all()
        for key in rentals:
            dueDate=rentals[key].get_dueDate()
            returnDate=rentals[key].get_returnedDate()
            delta=self._calculate_lateDays(dueDate, returnDate)
            if delta>0:
                movieId=rentals[key].get_rmovieId()
                list1.append([movieId,delta])
        for element in list1:
            dtoList.append(objectRentalCount(allMovies[element[0]],element[1]))
        dtoList.sort(reverse=True)
        return dtoList
        
    def active_clients(self):
        '''
        returns a list of clients who rented movies pretty often
        Input: -
        Output: askedString - a string which represents the list of late rentals
        Exceptions: -
        '''
        list1={}
        dtoList=[]
        allClients=self._repositoryClient.get_all()
        for key in allClients:
            list1[key]=0
        rentals=self._repositoryRental.get_all()
        for key in rentals:
            rentDate=rentals[key].get_rentDate()
            returnDate=rentals[key].get_returnedDate()
            delta=self._calculate_days(rentDate, returnDate)
            clientId=rentals[key].get_rclientId()
            list1[clientId]+=delta
        for key in list1:
            dtoList.append(objectRentalCount(allClients[key],list1[key]))
        dtoList.sort(reverse=True)
        return dtoList
    
    def most_rented(self,option):
        '''
        Returns a list of movies which were rented the most
        Input: -
        Output: askedString - a string which represents the list of late rentals
        Exceptions: -
        '''
        dtoList=[]
        list1={}
        allMovies=self._repositoryMovie.get_all()
        for key in allMovies:
            list1[key]=[0,0]
        rentals=self._repositoryRental.get_all()
        for key in rentals:
            rentDate=rentals[key].get_rentDate()
            returnDate=rentals[key].get_returnedDate()
            delta=self._calculate_days(rentDate, returnDate)
            movieId=rentals[key].get_rmovieId()
            list1[movieId][0]+=delta
            list1[movieId][1]+=1
        if option==1:
            for key in list1:
                dtoList.append(objectRentalCount(allMovies[key],list1[key][0]))
        else:
            for key in list1:
                dtoList.append(objectRentalCount(allMovies[key],list1[key][1]))
        dtoList.sort(reverse=True)
        return dtoList
    
    def undo(self):
        '''
        Undo function
        '''
        operations=self._undoControl.load_undo()
        for operation in operations:
            params=operation.get_parameters()
            name=operation.get_name()
            self.__functions[name](*params)
        
    
    def redo(self):
        '''
        Redo function
        '''
        operations=self._undoControl.load_redo()
        for operation in operations:
            params=operation.get_parameters()
            name=operation.get_name()
            self.__functions[name](*params)
    
####################################################################################

class objectRentalCount:
    '''
    class for data transfer object
    '''
    def __init__(self,obiect,rentalCount):
        '''
        Constructor for this data transfer object
        object - The object
        rentalCount - The number of times/days the object was rented
        '''
        self.__object=obiect
        self.__count=rentalCount
    
    def get_count(self):
        '''
        Get the count
        '''
        return self.__count
    
    def get_movie(self):
        '''
        Get the movie
        '''
        return self.__object
    
    def __lt__(self, objectRental):
        '''
        '''
        return self.get_count()<objectRental.get_count()
    def __str__(self):
        '''
        '''
        return str(self.get_movie()).ljust(15)+str(self.get_count())

#################################################################################