'''
Created on 4 Nov 2016

@author: DDL
'''
from MovieDDL.domain.Entities import Movie
from MovieDDL.domain.Validator import MovieValidator

class movieRepository:
    '''
    Repository for the movies
    '''
    def __init__(self,validator,movies):
        '''
        Creates repository for the movies
        '''
        self.__movies=movies
        self.__validator=validator
        
    def add_movie(self,movie):
        '''
        Adds a movie in the repository
        Input: movie - an object of the class Movie
        Output: -
        Exceptions: ValueError from validator or if the ID is already used
        '''
        self.__validator.validateMovie(movie)
        Id=int(movie.get_Id())
        if not self.find_by_ID(Id):
            self.__movies[Id]=movie
        else:
            raise ValueError("A movie with the same ID already in the list\n")
    
    def remove_movie(self, Id):
        '''
        Removes a movie from the repository
        Input: Id - a number
        Output: -
        Exceptions: ValueError from validator or if the ID is not in the list
        '''
        self.__validator.validateID(Id)
        Id=int(Id)
        if self.find_by_ID(Id):
            self.__movies.pop(Id)
        else:
            raise ValueError("There is no movie with the ID: "+str(Id)+"\n")
    
    def return_movie_Id(self,Id):
        '''
        Returns a movie with a certain Id
        Input: Id - a number
        Output: self._movies[Id] - a movie having the ID Id
        Exceptions: ValueError if there is no movie with that Id
        '''
        self.__validator.validateID(Id)
        Id=int(Id)
        if not self.find_by_ID(Id):
            raise ValueError("There is no movie with the ID: "+str(Id)+"\n")
        else:
            return self.__movies[Id]
                
    def get_all(self):
        '''
        Gets the dictionary of movies
        Output: self.__movies - the dictionary of movies
        '''
        return self.__movies
    
    def find_by_ID(self,Id):
        '''
        Checks if the Id is in the list of movies
        Input: Id - a number
        Output: True if the Id exists, False otherwise
        Exceptions: -
        '''
        if Id in self.__movies:
            return True
        else:
            return False
    
    def search_movie(self,field,information):
        '''
        Searches movies with certain properties in the repository in the repository
        Input: field - the field used for searching
               information - a partial string which is used for searching
        '''
        askedMovies={}
        if field==1:
            for key in self.__movies:
                movie=self.__movies[key]
                stringer=str(movie.get_Id())
                result=stringer.find(information)
                if result!=-1:
                    askedMovies[movie.get_Id()]=movie
                
        elif field==2:
            for key in self.__movies:
                movie=self.__movies[key]
                stringer=str(movie.get_title()).lower()
                result=stringer.find(information.lower())
                if result!=-1:
                    askedMovies[movie.get_Id()]=movie
                
        elif field==3:
            for key in self.__movies:
                movie=self.__movies[key]
                stringer=str(movie.get_genre()).lower()
                result=stringer.find(information.lower())
                if result!=-1:
                    askedMovies[movie.get_Id()]=movie
                
        else:
            for key in self.__movies:
                movie=self.__movies[key]
                stringer=str(movie.get_description()).lower()
                result=stringer.find(information.lower())
                if result!=-1:
                    askedMovies[movie.get_Id()]=movie
        
        return askedMovies
    

def testRepositoryMovies():
    '''
    Test this repository
    '''
    repoList={1:Movie(1,"Test1","Description1","comedy"),
              2:Movie(2,"Test2","Description2","horror"),
              3:Movie(3,"Test3","Description3","action")}
    movie1=Movie(17,"Test17","Description17","western")
    movie2=Movie(2,"Test56","Description56","horror")
    validator1=MovieValidator()
    repoTest=movieRepository(validator1,repoList)
    repoTest.add_movie(movie1)
    try:
        repoTest.add_movie(movie2)
        assert False
    except ValueError:
        assert True
    try:
        repoTest.remove_movie(4)
        assert False
    except ValueError:
        assert True
    repoTest.remove_movie(3)
    try:
        repoTest.return_movie_Id(3)
        assert False
    except ValueError:
        assert True
    assert repoTest.return_movie_Id(17).get_title()=="Test17"
    assert repoTest.find_by_ID(2)
    assert repoTest.find_by_ID(3)==False
    assert repoTest.search_movie(1, "5")=={}

#testRepositoryMovies()