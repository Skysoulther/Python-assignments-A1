'''
Created on 27 Nov 2016

@author: DDL
'''
from MovieDDL.repository.RepositoryExceptions import FileRepositoryException
from MovieDDL.repository.RepositoryMovies import movieRepository
from MovieDDL.domain.Entities import Movie

class movieFileRepository(movieRepository):
    '''
    Hit all the walls in front of you in order to know how to avoid them the next time
    '''
    def __init__(self, fileName="movies.txt"):
        '''
        Constructor for file repository
        Input: fileName - the name of the file
        Output: -
        '''
        movieRepository.__init__(self)
        self.__fName=fileName
        self.__loadFromFile()
        
    def add_movie(self, movie):
        '''
        Method to add a new movie
        Input: movie - object of Class movie
        Output: -
        '''
        movieRepository.add_movie(self, movie)
        self.__storeToFile()
    
    def remove_movie(self, Id):
        '''
        Method to remove a movie
        Input: Id - Id of the movie to remove
        Output: -
        '''
        movie=movieRepository.remove_movie(self, Id)
        self.__storeToFile()
        return movie
    
    def update_movie(self, Id, Desc):
        '''
        Method to edit the description of a movie
        Input: Id - id of the movie to edit
               Desc - The new description of the movie
        output: -
        '''
        movieRepository.update_movie(self, Id, Desc)
        self.__storeToFile()
    
    def __loadFromFile(self):
        try:
            f=open(self.__fName,"r")
            line=f.readline().strip()
            while line!="":
                attrs=line.split(";")
                movie=Movie(int(attrs[0]),attrs[1],attrs[3],attrs[2])
                movieRepository.add_movie(self, movie)
                line=f.readline().strip()
        except IOError:
            raise FileRepositoryException()
        finally:
            f.close
    
    def __storeToFile(self):
        f=open(self.__fName, "w")
        movies=movieRepository.get_all(self)
        for key in movies:
            strf=str(movies[key].get_Id())+";"+str(movies[key].get_title())+";"+str(movies[key].get_genre())+";"+str(movies[key].get_description())+"\n"
            f.write(strf)
        f.close