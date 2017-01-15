'''
Created on 4 Nov 2016

@author: DDL
'''
from MovieDDL.repository.RepositoryExceptions import RepositoryException
from MovieDDL.repository.Iterator import iterableData

class movieRepository():
    '''
    Repository for the movies
    '''
    def __init__(self):
        '''
        Creates repository for the movies
        '''
        self.__movies=iterableData()
        
    def add_movie(self,movie):
        '''
        Adds a movie in the repository
        Input: movie - an object of the class Movie
        Output: -
        Exceptions: RepositoryException from validator or if the ID is already used
        '''
        Id=movie.get_Id()
        if not self.find_by_ID(Id):
            self.__movies[Id]=movie
        else:
            raise RepositoryException("A movie with the same ID already in the list\n")
    
    def remove_movie(self, Id):
        '''
        Removes a movie from the repository
        Input: Id - a number
        Output: -
        Exceptions: RepositoryException from validator or if the ID is not in the list
        '''
        if self.find_by_ID(Id) and self.__movies[Id].get_availability():
            return self.__movies.pop(Id)
        else:
            raise RepositoryException("There is no movie with the ID: "+str(Id)+"\n")
    
    def return_movie_Id(self,Id):
        '''
        Returns a movie with a certain Id
        Input: Id - a number
        Output: self._movies[Id] - a movie having the ID Id
        Exceptions: RepositoryException if there is no movie with that Id
        '''
        if not self.find_by_ID(Id):
            raise RepositoryException("There is no movie with the ID: "+str(Id)+"\n")
        else:
            return self.__movies[Id]
        
    def update_movie(self,Id,Desc):
        '''
        Updates the movie with a new description
        '''
        self.__movies[Id].set_description(Desc)
            
    def get_all(self):
        '''
        Gets the dictionary of movies
        Output: self.__movies - the dictionary of movies
        '''
        return self.__movies
    
    def get_available(self):
        '''
        Gets the available list
        Output: availableMovies - a dictionary of availableMovies
        '''
        availableMovies={}
        for key in self.__movies:
            movie=self.__movies[key]
            if movie.get_availability():
                availableMovies[movie.get_Id()]=movie
        
        return availableMovies
    
    def change_availability(self,Id,booly):
        '''
        Changes the availability of a movie with ID Id in booly
        Input: Id - a number
               booly - True or False
        '''
        self.__movies[Id].set_availability(booly)
        
    
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
        Searches movies with certain properties in the repository
        Input: field - the field used for searching
               information - a partial string which is used for searching
        '''
        askedMovies={}
        
        for key in self.__movies:
            movie=self.__movies[key]
            fields={1:movie.get_Id,2:movie.get_title,3:movie.get_genre,4:movie.get_description}
            stringer=str(fields[field]()).lower()
            result=stringer.find(information.lower())
            if result!=-1 and movie.get_availability():
                askedMovies[movie.get_Id()]=movie
        
        return askedMovies

###########################################################################