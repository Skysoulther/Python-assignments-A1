'''
Created on 4 Nov 2016

@author: DDL
'''

class movieRepository:
    '''
    repository for the movies
    '''
    def __init__(self,validator,movies):
        '''
        Creates repository for the movies
        '''
        self._movies=movies
        self._validator=validator
        
    def add_movie(self,movie):
        '''
        Adds a movie in the repository
        Input: movie - an object of the class Movie
        Output: -
        Exceptions: -
        '''
        self._validator.validateMovie(movie)
        Id=int(movie.get_Id())
        if not self.find_by_ID(Id):
            self._movies[Id]=movie
        else:
            raise ValueError("A movie with the same ID already in the list\n")
    
    def remove_movie(self, Id):
        '''
        Removes a movie from the repository
        Input: Id - a number
        Output: -
        Exceptions: -
        '''
        self._validator.validateID(Id)
        Id=int(Id)
        if self.find_by_ID(Id):
            self._movies.pop(Id)
        else:
            raise ValueError("There is no movie with the ID: "+str(Id)+"\n")
    
    def return_movie_Id(self,Id):
        '''
        Returns a movie with a certain Id
        '''
        self._validator.validateID(Id)
        Id=int(Id)
        if not self.find_by_ID(Id):
            raise ValueError("There is no movie with the ID: "+str(Id)+"\n")
        else:
            return self._movies[Id]
                
    def get_all(self):
        '''
        Gets the dictionary of movies
        '''
        return self._movies
    
    def find_by_ID(self,Id):
        '''
        Checks if the Id is in the list of movies
        Input: Id - a number
        Output: True if the Id exists, False otherwise
        Exceptions: -
        '''
        if Id in self._movies:
            return True
        else:
            return False
    
    def search_movie(self,field,information):
        '''
        Searches movies with certain properties in the repository in the repository
        '''
        askedMovies={}
        if field==1:
            for key in self._movies:
                movie=self._movies[key]
                stringer=str(movie.get_Id())
                result=stringer.find(information)
                if result!=-1:
                    askedMovies[movie.get_Id()]=movie
        elif field==2:
            for key in self._movies:
                movie=self._movies[key]
                stringer=str(movie.get_title()).lower()
                result=stringer.find(information.lower())
                if result!=-1:
                    askedMovies[movie.get_Id()]=movie
        elif field==3:
            for key in self._movies:
                movie=self._movies[key]
                stringer=str(movie.get_genre()).lower()
                result=stringer.find(information.lower())
                if result!=-1:
                    askedMovies[movie.get_Id()]=movie
        else:
            for key in self._movies:
                movie=self._movies[key]
                stringer=str(movie.get_description()).lower()
                result=stringer.find(information.lower())
                if result!=-1:
                    askedMovies[movie.get_Id()]=movie
        
        return askedMovies