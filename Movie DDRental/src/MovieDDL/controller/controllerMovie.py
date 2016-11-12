'''
Created on 4 Nov 2016

@author: DDL
'''

class movieController:
    '''
    Contains functions which operates on movies
    '''
    def __init__(self,repoMovie):
        '''
        Creates a controller for movies
        '''
        self._repository=repoMovie
    
    def add_movie(self,movie):
        '''
        Add movie to the repository
        Input: movie -  a list which contains the values of the fields of a movie
        Output: -
        Exceptions: -
        '''
        newMovie=Movie(movie[0],movie[1],movie[3],movie[2])
        self._repository.add_movie(newMovie)
    
    def remove_movie(self, Id):
        '''
        Remove a movie from the repository if it exists
        Input: Id - a natural number
        Output: -
        Exceptions: -
        '''
        self._repository.remove_movie(Id)
    
    def get_allMovies(self):
        '''
        Returns the list of available movies
        '''
        return self._repository.get_all()
    
    def return_movie_Id(self,Id):
        '''
        Returns a movie with a certain Id
        '''
        return self._repository.return_movie_Id(Id)
   
    def search_movie(self, field, information):
        '''
        Searches all the movies with the mentioned field and information
        '''
        return self._repository.search_movie(field,information)