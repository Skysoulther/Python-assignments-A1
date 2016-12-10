'''
Created on 3 Nov 2016

@author: DDL
'''
'''
The module for the client class, movie class and rental class
'''
import datetime

class Movie:
    '''
    Class for movie
    '''
    
    def __init__(self,movID,title,desc,genre):
        '''
        Creates a movie
        '''
        self.__movieID=movID
        self.__title=title
        self.__description=desc
        self.__genre=genre
        self.__available=True
        
    def __str__(self):
        '''
        Creates a string for a movie
        Output: movieString - movie as a string
        '''
        mov1=6-len(str(self.__movieID))
        mov2=52-len(str(self.__title))
        mov3=15-len(str(self.__genre))
        movieString=str(self.__movieID)+" "*mov1+str(self.__title)+" "*mov2+str(self.__genre)[:1].upper()+str(self.__genre)[1:]+" "*mov3
        return movieString
    
    def get_title(self):
        '''
        Get the title of the movie
        Output: self.__title - the title of the movie
        '''
        return self.__title
    
    def set_title(self,title):
        '''
        Set the tile of the movie
        Input: title - the new title of the movie
        '''
        self.__title=title
    
    def get_Id(self):
        '''
        Get the Id of the movie
        Output: self.__movieID - the Id of the movie
        '''
        return self.__movieID
    
    def set_Id(self,Id):
        '''
        Set the Id of the movie
        Input: Id - the Id of the new movie
        '''
        self.__movieID=Id
        
    def get_genre(self):
        '''
        Get the genre of the movie
        Output: self.__genre - the genre of the movie
        '''
        return self.__genre
    
    def set_genre(self,genre):
        '''
        Set the genre of the movie
        Input: genre - the new genre of the movie
        '''
        self.__genre=genre
    
    def get_description(self):
        '''
        Get the description of the movie
        Output: self.__description - the description of the movie
        '''
        return self.__description
    
    def set_description(self, desc):
        '''
        set the description of the movie
        Input: desc - the new description of the movie
        '''
        self.__description=desc
    
    def get_availability(self):
        '''
        Get True if the movie is available and False if it is not
        Output: self.__available - True or False
        '''
        return self.__available
    
    def set_availability(self,booly):
        '''
        Set the availability of the movie
        Input: booly - a boolean value
        '''
        self.__available=booly
        
        
#############################################################################################
    
class Client:
    '''
    Class for client
    '''
    def __init__(self,clientID,name):
        '''
        Creates a client
        '''
        self.__clientID=clientID
        self.__name=name
    
    def __str__(self):
        '''
        Writes the data for clients in a better way
        output: clientString - client as a string
        '''
        cli1=6-len(str(self.__clientID))
        cli2=25-len(str(self.__name))
        clientString=str(self.__clientID)+" "*cli1+str(self.__name)+" "*cli2
        return clientString
    
    def get_clientName(self):
        '''
        Get the name of the client
        Output: self.__name - the name of the client
        '''
        return self.__name
    
    def set_clientName(self,name):
        '''
        Set the name of the client
        Input: name - the new name of the client
        '''
        self.__name=name
        
    def get_clientID(self):
        '''
        Get the id of the client
        Output: self.__clientID - the Id of the client
        '''
        return self.__clientID
    
    def set_clientID(self, Id):
        '''
        Set the id of the client
        Input: Id - the new Id of the client
        '''
        self.__clientID=Id

###########################################################################################
        
class Rental:
    '''
    Class for rentals
    '''
    def __init__(self,rentID,movID,cliID,rentDate,dueDate):
        '''
        Creates a rental
        '''
        self.__rentalID=rentID
        self.__rmovieID=movID
        self.__rclientID=cliID
        self.__rentDate=rentDate
        self.__dueDate=dueDate
        self.__returnDate=None
    
    def __str__(self):
        '''
        Shows a rental as a string
        Output rentalString - rental as a string
        '''
        ren1=7-len(str(self.__rentalID))
        ren2=7-len(str(self.__rmovieID))
        ren3=7-len(str(self.__rclientID))
        ren4=12-len(str(self.__rentDate))
        ren5=12-len(str(self.__dueDate))
        rentalString=str(self.__rentalID)+" "*ren1+str(self.__rmovieID)+" "*ren2+str(self.__rclientID)+" "*ren3
        rentalString+=str(self.__rentDate)+" "*ren4+str(self.__dueDate)+" "*ren5+str(self.__returnDate)                 
        return rentalString
    
    def get_rentalId(self):
        '''
        Get the Id of the rental
        Output: self._rentalID - the Id of the rental
        '''
        return self.__rentalID
    
    def set_rentalId(self,Id):
        '''
        Set the Id of the rental
        Input: Id - the id we want to set for the rental
        '''
        self.__rentalID=Id
    
    def get_rmovieId(self):
        '''
        Get the Id of the rented movie
        Output: self._rmovieID - the id of the rented movie
        '''
        return self.__rmovieID
    
    def set_rmovieId(self, Id):
        '''
        Set the Id of the rented movie
        Input: Id - the id of the movie
        '''
        self.__rmovieID=Id
    
    def get_rclientId(self):
        '''
        Get the Id of the client who rented the movie
        Output: self._rclientID - the Id of a client in rental list
        '''
        return self.__rclientID
    
    def set_rclientId(self, Id):
        '''
        Set the Id of the client who rented the movie
        Input: Id - the new Id of a client in rental list
        '''
        self.__rclientID=Id
    
    def get_rentDate(self):
        '''
        Get the date when the movie was rented
        Output: self._rentDate - the date when the movie was rented
        '''
        return self.__rentDate
    
    def set_rentDate(self,day,month,year):
        '''
        Set the date when the movie was rented
        Input: day - a number representing a day in a month
               month - a number representing a month
               year - a number representing a year
        '''
        rDate=datetime.date(year=year,month=month,day=day)
        self.__rentDate=rDate
        
    def get_dueDate(self):
        '''
        Get the final date when the movie should be returned
        Output: self._dueDate - the duedate of the movie
        '''
        return self.__dueDate
    
    def set_dueDate(self, day, month, year):
        '''
        Set the date when the movie should be returned
        Input: day - a number representing a day in a month
               month - a number representing a month
               year - a number representing a year
        '''
        dDate=datetime.date(day=day,month=month,year=year)
        self.__dueDate=dDate
    
    def set_returnedDate(self, date):
        '''
        Set the date when the movie returned
        Input: day - a number representing a day in a month
               month - a number representing a month
               year - a number representing a year
        '''
        self.__returnDate=date
        
    def get_returnedDate(self):
        '''
        Get the date when the movie returned
        Output: self._returnDate - the date when the movie was returned
        '''
        return self.__returnDate
    
    def set_rentJSONDate(self,rDate):
        '''
        Set the date when the movie was rented
        Input: day - a number representing a day in a month
               month - a number representing a month
               year - a number representing a year
        '''
        self.__rentDate=rDate
    
    def set_dueJSONDate(self,dDate):
        '''
        Set the date when the movie was rented
        Input: day - a number representing a day in a month
               month - a number representing a month
               year - a number representing a year
        '''
        self.__dueDate=dDate
    