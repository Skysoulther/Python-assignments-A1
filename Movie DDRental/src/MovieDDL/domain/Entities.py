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
        self.__rentedDays=0
    
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
        rentalString+=str(self.__rentDate)+" "*ren4+str(self.__dueDate)+" "*ren5                 
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
    
    def set_returnedDate(self, day, month, year):
        '''
        Set the date when the movie returned
        Input: day - a number representing a day in a month
               month - a number representing a month
               year - a number representing a year
        '''
        self.__returnDate=datetime.date(year=year, month=month,day=day)
        
    def get_returnedDate(self):
        '''
        Get the date when the movie returned
        Output: self._returnDate - the date when the movie was returned
        '''
        return self.__returnDate
    

def testMovieClass():
    '''
    Test the Movie class
    '''
    movie1=Movie(13,"A beautiful Mind","A movie about the life of John Nash","Biography")
    assert movie1.get_Id()==13
    assert movie1.get_title()=="A beautiful Mind"
    assert movie1.get_genre()=="Biography"
    assert movie1.get_description()=="A movie about the life of John Nash"
    assert str(movie1)=="13    "+"A beautiful Mind"+" "*(52-len(movie1.get_title()))+"Biography"+" "*6
    movie1.set_Id(18)
    assert movie1.get_Id()==18
    assert movie1.get_title()=="A beautiful Mind"
    movie1.set_title("The last day of summer")
    assert movie1.get_title()=="The last day of summer"
    movie1.set_description("A movie about summer")
    assert movie1.get_description()=="A movie about summer"
    movie1.set_genre("Comedy")
    assert movie1.get_genre()=="Comedy"

def testClientClass():
    '''
    Test the Client class
    '''
    client1=Client(47,"Sergiu Gherman")
    assert client1.get_clientID()==47
    assert client1.get_clientName()=="Sergiu Gherman"
    assert str(client1)=="47    "+"Sergiu Gherman"+" "*11
    client1.set_clientID(48)
    assert client1.get_clientID()==48
    client1.set_clientName("Bobby")
    assert client1.get_clientName()=="Bobby"

def testRentalClass():
    '''
    Test the Rental class
    '''
    rDate=datetime.date(year=2016, month=10, day=30)
    dDate=datetime.date(year=2016, month=11, day=7)
    movie1=Movie(13,"A beautiful Mind","A movie about the life of John Nash","Biography")
    client1=Client(47,"Sergiu Gherman")
    rental1=Rental(1,movie1,client1,rDate,dDate)
    assert rental1.get_rentalId()==1
    assert rental1.get_rmovieId()==13
    assert rental1.get_rclientId()==47
    assert rental1.get_rentDate()==datetime.date(year=2016,month=10,day=30)
    assert rental1.get_dueDate().year==2016
    assert rental1.get_dueDate().month==11
    assert rental1.get_dueDate().day==7
    assert str(rental1)=="1"+" "*6+"13"+" "*5+"47"+" "*5+str(rental1.get_rentDate())+"  "+str(rental1.get_dueDate())+"  "
    rental1.set_rentalId(2)
    assert rental1.get_rentalId()==2
    rental1.set_rmovieId(18)
    assert rental1.get_rmovieId()==18
    rental1.set_rclientId(21)
    assert rental1.get_rclientId()==21
    rental1.set_rentDate(15, 10, 2016)
    assert rental1.get_rentDate()==datetime.date(year=2016,month=10,day=15)
    rental1.set_dueDate(14, 11, 2016)
    assert rental1.get_dueDate().day==14
    rental1.set_returnedDate(15, 11, 2017)
    assert rental1.get_returnedDate()==datetime.date(day=15,month=11,year=2017)
       
def runEntitiesTests():
    '''
    Runs all the tests in this module
    '''
    testMovieClass()
    testClientClass()
    testRentalClass()
    print("well done!")
    
#runEntitiesTests()