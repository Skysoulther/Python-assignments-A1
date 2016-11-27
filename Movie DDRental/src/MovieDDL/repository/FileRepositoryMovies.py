'''
Created on 27 Nov 2016

@author: DDL
'''
from MovieDDL.repository.RepositoryExceptions import FileRepositoryException
from MovieDDL.domain.Entities import Movie

class movieFileRepository:
    def __init__(self, fileName="movies.txt"):
        self.__fName=fileName
        
    def _loadFromFile(self):
        movies={}
        try:
            f=open(self.__fName,"r")
            line=f.readline().strip()
            while line!="":
                attrs=line.split(";")
                movie=Movie(int(attrs[0]),attrs[1],attrs[3],attrs[2])
                movies[int(attrs[0])]=movie
                line=f.readline().strip()
        except IOError:
            raise FileRepositoryException()
        finally:
            f.close
            return movies
    
    def _storeToFile(self,movies):
        f=open(self.__fName, "w")
        for key in movies:
            strf=str(movies[key].get_Id())+";"+str(movies[key].get_title())+";"+str(movies[key].get_genre())+";"+str(movies[key].get_description())+"\n"
            f.write(strf)
        f.close