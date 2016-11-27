'''
Created on 6 Nov 2016

@author: DDL
'''
from MovieDDL.controller.ControllerExceptions import ControllerException
from operator import itemgetter
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
        rentalId=self._generate_rentalID(rental[1])
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
    
        
    def all_rentals(self):
        '''
        returns a list of rentals
        Input: -
        Output: askedString - a string which represents the list of rentals
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
        Output: askedString - a string which represents the list of late rentals
        Exceptions: -
        '''
        list1=[]
        list2=[]
        allMovies=self._repositoryMovie.get_all()
        rentals=self._repositoryRental.get_all()
        for key in rentals:
            dueDate=rentals[key].get_dueDate()
            returnDate=rentals[key].get_returnedDate()
            delta=self._calculate_lateDays(dueDate, returnDate)
            if delta>0:
                movieId=rentals[key].get_rmovieId()
                list1.append([movieId,delta])
        list1=sorted(list1,key=itemgetter(1),reverse=True)
        for element in list1:
            list2.append(allMovies[element[0]])
        return list2
        
    def active_clients(self):
        '''
        returns a list of clients who rented movies pretty often
        Input: -
        Output: askedString - a string which represents the list of late rentals
        Exceptions: -
        '''
        list1={}
        list2=[]
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
            list2.append([key,list1[key]])
        list1=[]
        list2=sorted(list2,key=itemgetter(1),reverse=True)
        for element in list2:
            list1.append(allClients[element[0]])
        return list1
    
    def most_rented(self,option):
        '''
        Returns a list of movies which were rented the most
        Input: -
        Output: askedString - a string which represents the list of late rentals
        Exceptions: -
        '''
        list1={}
        list2=[]
        list3=[]
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
        for key in list1:
            list2.append([key,list1[key][0],list1[key][1]])
        list1=[]
        if option==1:
            list2=sorted(list2,key=itemgetter(1),reverse=True)
        else:
            list2=sorted(list2,key=itemgetter(2),reverse=True)
        for element in list2:
            list1.append(allMovies[element[0]])
        return list1
                    
####################################################################################
#################################################################################