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
        self._movieID=movID
        self._title=title
        self._description=desc
        self._genre=genre
        
    def __str__(self):
        mov1=6-len(str(self._movieID))
        mov2=52-len(str(self._title))
        mov3=15-len(str(self._genre))
        movieString=str(self._movieID)+" "*mov1+str(self._title)+" "*mov2+str(self._genre)[:1].upper()+str(self._genre)[1:]+" "*mov3
        return movieString
    
    def get_title(self):
        '''
        Get the title of the movie
        '''
        return self._title
    
    def set_title(self,title):
        '''
        Set the tile of the movie
        '''
        self._title=title
    
    def get_Id(self):
        '''
        Get the Id of the movie
        '''
        return self._movieID
    def set_Id(self,Id):
        '''
        Set the Id of the movie
        '''
        self._movieID=Id
    def get_genre(self):
        '''
        Get the genre of the movie
        '''
        return self._genre
    def set_genre(self,genre):
        '''
        Set the genre of the movie
        '''
        self._genre=genre
    def get_description(self):
        '''
        Get the description of the movie
        '''
        return self._description
    def set_descriprion(self, desc):
        '''
        set the description of the movie
        '''
        self._description=desc
        
#############################################################################################
    
class Client:
    '''
    Class for client
    '''
    def __init__(self,clientID,name):
        '''
        Creates a client
        '''
        self._clientID=clientID
        self._name=name
        self._rentedDays=0
    
    def __str__(self):
        '''
        Writes the data for clients in a better way
        '''
        cli1=5-len(str(self._clientID))
        cli2=25-len(str(self._name))
        clientString=str(self._clientID)+" "*cli1+str(self._name)+" "*cli2
        return clientString
    
    def get_clientName(self):
        '''
        Get the name of the client
        '''
        return self._name
    
    def set_clientName(self,name):
        '''
        Set the name of the client
        '''
        self._name=name
    def get_clientID(self):
        '''
        Get the id of the client
        '''
        return self._clientID
    
    def set_clientID(self, Id):
        '''
        Set the id of the client
        '''
        self._clientID=Id

###########################################################################################
        
class Rental:
    '''
    Class for rented movie
    '''
    def __init__(self,rentID,movID,clientID,rentDate,dueDate):
        '''
        Creates a rented movie
        '''
        self._rentalID=rentID
        self._rmovieID=movID
        self._rclientID=clientID
        self._rentDate=rentDate
        self._dueDate=dueDate
    
    def get_rentalId(self):
        '''
        Get the Id of the rental
        '''
        return self._rentalID
    
    def set_rentalId(self,Id):
        '''
        Set the Id of the rental
        '''
        self._rentalID=Id
    
    def get_rmovieId(self):
        '''
        Get the Id of the rented movie
        '''
        return self._rmovieID
    def set_rmovieId(self, Id):
        '''
        Set the Id of the rented movie
        '''
        self._rmovieID=Id
    
    def get_rclientId(self):
        '''
        Get the Id of the client who rented the movie
        '''
        return self._rclientID
    
    def set_rclientId(self, Id):
        '''
        Set the Id of the client who rented the movie
        '''
        self._rclientID=Id
    
    def get_rentDate(self):
        '''
        Get the date when the movie was rented
        '''
        return self._rentDate
    
    def set_rentDate(self,day,month,year):
        '''
        Set the date when the movie was rented
        '''
        rDate=datetime.date(year=year,month=month,day=day)
        self._rentDate=rDate
        
    def get_dueDate(self):
        '''
        Get the date when the movie should be returned
        '''
        return self._dueDate
    
    def set_dueDate(self, day, month, year):
        '''
        Set the date when the movie should be returned
        '''
        dDate=datetime.date(day=day,month=month,year=year)
        self._dueDate=dDate
    
    def set_returnedDate(self, day, month, year):
        '''
        Set the date when the movie returned
        '''
        self._returnDate=datetime.date(year=year, month=month,day=day)
        
    def get_returnedDate(self):
        '''
        Get the date when the movie returned
        '''
        return self._returnDate
    

def testMovieClass():
    '''
    Test the Movie class
    '''
    movie1=Movie(13,"A beautiful Mind","A movie about the life of John Nash","Biography")
    assert movie1.get_Id()==13
    assert movie1.get_title()=="A beautiful Mind"
    assert movie1.get_genre()=="Biography"
    assert movie1.get_descrption()=="A movie about the life of John Nash"
    movie1.set_Id(18)
    assert movie1.get_Id()==18
    assert movie1.get_title()=="A beautiful Mind"
    movie1.set_title("The last day of summer")
    assert movie1.get_title()=="The last day of summer"
    movie1.set_descriprion("A movie about summer")
    assert movie1.get_descrption()=="A movie about summer"
    movie1.set_genre("Comedy")
    assert movie1.get_genre()=="Comedy"

def testClientClass():
    '''
    Test the Client class
    '''
    client1=Client(47,"Sergiu Gherman")
    assert client1.get_clientID()==47
    assert client1.get_clientName()=="Sergiu Gherman"
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
    rental1=Rental(1,17,20,rDate,dDate)
    assert rental1.get_rentalId()==1
    assert rental1.get_rmovieId()==17
    assert rental1.get_rclientId()==20
    assert rental1.get_rentDate()==datetime.date(year=2016,month=10,day=30)
    assert rental1.get_dueDate().year==2016
    assert rental1.get_dueDate().month==11
    assert rental1.get_dueDate().day==7
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
       
def runAllTests():
    testMovieClass()
    testClientClass()
    testRentalClass()
    print("well done!")
    
#runAllTests()