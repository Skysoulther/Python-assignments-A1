'''
Created on 4 Nov 2016

@author: DDL
'''
from MovieDDL.domain.Entities import Movie
from MovieDDL.controller.UndoController import Operation
from MovieDDL.controller.ControllerExceptions import ControllerException

class movieController:
    '''
    Contains functions which operates on movies
    '''
    def __init__(self,repoMovie,validator,undo):
        '''
        Creates a controller for movies
        '''
        self._undoControl=undo
        self.__validator=validator
        self._repository=repoMovie
    
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
        
    def add_movie(self,movie):
        '''
        Add movie to the repository
        Input: movie -  a list which contains the values of the fields of a movie
        Output: -
        Exceptions: Controller Exception when the Id of the movie is not valid
        '''
        self._validateID(movie[0])
        movie=Movie(int(movie[0]),movie[1],movie[3],movie[2])
        self.__validator.validateMovie(movie)
        self._repository.add_movie(movie)
        self._undoControl.store_undo([Operation("remove_movie",[movie.get_Id()])])
        self._undoControl.store_redo([Operation("add_movie",[movie])])
    
    def remove_movie(self, Id):
        '''
        Remove a movie from the repository if it exists
        Input: Id - a natural number
        Output: -
        Exceptions: Controller Exception when Id is not valid
        '''
        self._validateID(Id)
        Id=int(Id)
        self.__validator.validateID(Id)
        movie=self._repository.remove_movie(Id)
        self._undoControl.store_undo([Operation("add_movie",[movie])])
        self._undoControl.store_redo([Operation("remove_movie",[Id])])
    
    def get_allMovies(self):
        '''
        Returns the list of available movies
        '''
        return self._repository.get_available()
    
    def edit_movie(self,Id,Desc):
        '''
        Edits the description of the movie with a certain ID
        '''
        self._validateID(Id)
        Id=int(Id)
        if self._repository.find_by_ID(Id):
            movie=self._repository.return_movie_Id(Id)
            self._undoControl.store_undo([Operation("edit_movie",[Id,movie.get_description()])])
            self._repository.update_movie(Id,Desc)
            self._undoControl.store_redo([Operation("edit_movie",[Id,Desc])])
            
        else:
            raise ControllerException("The movie you want to edit can't be found!\n")
        
    def return_movie_Id(self,Id):
        '''
        Returns a movie with a certain Id
        '''
        self._validateID(Id)
        Id=int(Id)
        self.__validator.validateID(Id)
        movie=self._repository.return_movie_Id(Id)
        if not movie.get_availability():
            raise ControllerException("The movie is not available!\n")
        else:
            return movie
   
    def search_movie(self, field, information):
        '''
        Searches all the movies with the mentioned field and information
        '''
        return self._repository.search_movie(field,information)
    
################################################################################

#################################################################################