'''
Created on 27 Nov 2016

@author: DDL
'''
from datetime import datetime
from MovieDDL.repository.RepositoryExceptions import FileRepositoryException
from MovieDDL.domain.Entities import Rental

class rentalFileRepository:
    def __init__(self, fileName="rentals.txt"):
        self.__fName=fileName
        
    def _loadFromFile(self):
        rentals={}
        try:
            f=open(self.__fName,"r")
            line=f.readline().strip()
            while line!="":
                attrs=line.split(";")
                attrs[3]=datetime.strptime(attrs[3],"%d-%m-%Y").date()
                attrs[4]=datetime.strptime(attrs[4],"%d-%m-%Y").date()
                rental=Rental(int(attrs[0]),int(attrs[1]),int(attrs[2]),attrs[3],attrs[4])
                rentals[int(attrs[0])]=rental
                line=f.readline().strip()
        except IOError:
            raise FileRepositoryException()
        finally:
            f.close
            return rentals
    
    def _storeToFile(self,rentals):
        f=open(self.__fName, "w")
        for key in rentals:
            rentDate=rentals[key].get_rentDate()
            rentDate=rentDate.strftime("%d-%m-%Y")
            dueDate=rentals[key].get_dueDate()
            dueDate=dueDate.strftime("%d-%m-%Y")
            strf=str(rentals[key].get_rentalId())+";"+str(rentals[key].get_rmovieId())+";"+str(rentals[key].get_rclientId())+";"+str(rentDate)+";"+str(dueDate)+"\n"
            f.write(strf)
        f.close