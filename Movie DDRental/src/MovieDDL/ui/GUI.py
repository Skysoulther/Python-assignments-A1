'''
Created on 3 Dec 2016

@author: DDL
'''
import datetime
from tkinter import *
from tkinter import messagebox

class MenuGUI:
    def __init__(self,movControl,cliControl,renControl):
        '''
        Creates a menu which uses controllers
        '''
        self._movieController=movControl
        self._clientController=cliControl
        self._rentalController=renControl
    
    def run(self):
        '''
        Starts the GUI
        '''
        self.main=Tk()
        
        self.main.title("MovieRental DDL")
        self.main.geometry("400x500+500+50")
        
        mainLabel=Label(self.main,text="Main Menu",fg="red")
        mainLabel.pack()
        
        mainFrame=Frame(self.main)
        mainFrame.pack()
        self.mainFrame=mainFrame
        
        self.menu1Title=Label(mainFrame,text="Available options")
        menuObservation=Label(self.main,text="NOTE: Press Ctrl+Z to undo and Ctrl+R to redo")
        menuObservation.pack(side=BOTTOM)
        
        
        self.movieBtn = Button(mainFrame, text="Manage movies", command=self.manageMovies)
        self.movieBtn.pack(side=TOP)
        
        self.clientBtn = Button(mainFrame, text="Manage clients", command=self.manageClients)
        self.clientBtn.pack(side=TOP)

        self.rentBtn = Button(mainFrame, text="Rent movies", command=self.rentMovie)
        self.rentBtn.pack(side=TOP)
        
        self.returnBtn = Button(mainFrame, text="Return a movie", command=self.returnMovie)
        self.returnBtn.pack(side=TOP)

        self.statisticsBtn = Button(mainFrame, text="Statistics", command=self.statisticsMenu)
        self.statisticsBtn.pack(side=TOP)

        self.quitBtn = Button(mainFrame, text="QUIT", fg="red", command=mainFrame.quit)
        self.quitBtn.pack(side=TOP)
        
        self.main.bind("<Control-z>", self.undo)
        self.main.bind("<Control-r>", self.redo)
        
        self.movies=None
        self.clients=None
        self.statistics=None
        self.rentFrame1=None
        self.rentFrame2=None
        self.rentframe3=None
        self.rentFrame4=None
        self.returnFrame1=None
        self.returnFrame2=None
        self.returnFrame3=None
        
        self.main.mainloop()
    
    ####################################################################################
        
        
    def manageMovies(self):
        '''
        The main menu for movies management
        '''
        if not self.movies:
            self.movies=Tk()
        
            self.movies.title("Movies Manager")
            self.movies.geometry("300x500+200+50")
        
            mainLabel=Label(self.movies,text="Manage Movies",fg="red")
            mainLabel.pack()
        
            movieFrame=Frame(self.movies)
            movieFrame.pack()
            self.movieFrame=movieFrame
        
            self.addMovieBtn = Button(movieFrame, text="Add movie", command=self.addMovie)
            self.addMovieBtn.pack(side=TOP)
        
            self.removeMovieBtn = Button(movieFrame, text="Remove movie", command=self.removeMovie)
            self.removeMovieBtn.pack(side=TOP)

            self.listMoviesBtn = Button(movieFrame, text="Show available movies", command=self.showAllMovies)
            self.listMoviesBtn.pack(side=TOP)
        
            self.editMovieBtn = Button(movieFrame, text="Edit the description of a movie", command=self.editMovie)
            self.editMovieBtn.pack(side=TOP)

            self.searchMovieBtn = Button(movieFrame, text="Search movie", command=self.searchMovies)
            self.searchMovieBtn.pack(side=TOP)

            self.closeBtn = Button(movieFrame, text="CLOSE", fg="red", command=self.closeMoviesWindow)
            self.closeBtn.pack(side=TOP)
            
            self.movies.bind("<Control-z>", self.undo)
            self.movies.bind("<Control-r>", self.redo)
            self.movies.protocol('WM_DELETE_WINDOW', self.closeMoviesWindow)
            
        ###################################################
        
            self.addFrame1=None
            self.addFrame2=None
            self.addFrame3=None
            self.addFrame4=None
            self.addFrame5=None
            self.removeFrame1=None
            self.removeFrame2=None
            self.editFrame1=None
            self.editFrame2=None
            self.editFrame3=None
            self.searchFrame1=None
            self.searchFrame2=None
            self.searchFrame3=None
    
    def closeMoviesWindow(self):
        '''
        Close Button function
        '''
        self.movies.destroy()
        self.movies=None
                
    def _readMovie(self):
        '''
       read movie's data
        Input: -
        Output: the movie's properties as a list
        Exceptions: -
        '''
        movie=[]
        movie.append(self.idMov.get())
        movie.append(self.titleMov.get())
        movie.append(self.genreMov.get())
        movie.append(self.descMov.get())
        return movie
        
    def addMovie(self):
        '''
        GUI to add a movie in the repository
        '''
        if not self.addFrame1:
            addFrame1=Frame(self.movies)
            addFrame1.pack()
            self.addFrame1=addFrame1;
        
            addFrame2=Frame(self.movies)
            addFrame2.pack()
            self.addFrame2=addFrame2;
            
            addFrame3=Frame(self.movies)
            addFrame3.pack()
            self.addFrame3=addFrame3;
            
            addFrame4=Frame(self.movies)
            addFrame4.pack()
            self.addFrame4=addFrame4;
            
            addFrame5=Frame(self.movies)
            addFrame5.pack()
            self.addFrame5=addFrame5;
            
            lbl = Label(self.addFrame1, text="ID:")
            lbl.pack(side=LEFT)

            self.idMov = Entry(self.addFrame1, {})
            self.idMov.pack(side=LEFT)

            lbl = Label(self.addFrame2, text="Title:")
            lbl.pack(side=LEFT)

            self.titleMov = Entry(self.addFrame2, {})
            self.titleMov.pack(side=LEFT)

            lbl = Label(self.addFrame3, text="Genre:")
            lbl.pack(side=LEFT)

            self.genreMov = Entry(self.addFrame3, {})
            self.genreMov.pack(side=LEFT)

            lbl = Label(self.addFrame4, text="Description:")
            lbl.pack(side=LEFT)

            self.descMov = Entry(self.addFrame4, {})
            self.descMov.pack(side=LEFT)
            
            addBtn = Button(self.addFrame5,text="Add",command=self.addMovie2)
            addBtn.pack()
        
        
    def addMovie2(self):
        '''
        add movie in the repository
        '''
        self.addFrame1.pack_forget()
        self.addFrame1=None
        self.addFrame2.pack_forget()
        self.addFrame2=None
        self.addFrame3.pack_forget()
        self.addFrame3=None
        self.addFrame4.pack_forget()
        self.addFrame4=None
        self.addFrame5.pack_forget()
        self.addFrame5=None
        try:
            movie=self._readMovie()
            self._movieController.add_movie(movie)
            messagebox.showinfo("Success", "Movie was added!")
        except Exception as ex:
            messagebox.showinfo(title="Error", message="Error adding movie: \n" + str(ex))
        
        
    def removeMovie(self):
        '''
        GUI to remove a movie from the repository
        '''
        if not self.removeFrame1:
            removeFrame1=Frame(self.movies)
            removeFrame1.pack()
            self.removeFrame1=removeFrame1;
            
            removeFrame2=Frame(self.movies)
            removeFrame2.pack()
            self.removeFrame2=removeFrame2;
            
            lbl = Label(self.removeFrame1, text="ID to remove:")
            lbl.pack(side=LEFT)

            self.ridMov = Entry(self.removeFrame1, {})
            self.ridMov.pack(side=LEFT)
            
            removeBtn = Button(self.removeFrame2,text="Remove",command=self.removeMovie2)
            removeBtn.pack()
        
               
    def removeMovie2(self):
        '''
            
        '''
        self.removeFrame1.pack_forget()
        self.removeFrame1=None
        self.removeFrame2.pack_forget()
        self.removeFrame2=None
        try:
            self._movieController.remove_movie(self.ridMov.get())
            messagebox.showinfo("Success","Movie was removed!")
        except Exception as ex:
            messagebox.showinfo(title="Error", message="Error removing movie: \n" + str(ex))
        
    def editMovie(self):
        '''
        GUI to edit the name of a movie
        '''
        if not self.editFrame1:
            editFrame1=Frame(self.movies)
            editFrame1.pack()
            self.editFrame1=editFrame1;
            
            editFrame2=Frame(self.movies)
            editFrame2.pack()
            self.editFrame2=editFrame2;
            
            editFrame3=Frame(self.movies)
            editFrame3.pack()
            self.editFrame3=editFrame3;
            
            lbl = Label(self.editFrame1, text="ID to edit:")
            lbl.pack(side=LEFT)

            self.nidMov = Entry(self.editFrame1, {})
            self.nidMov.pack(side=LEFT)
            
            lbl = Label(self.editFrame2, text="New Description:")
            lbl.pack(side=LEFT)

            self.ndescMov = Entry(self.editFrame2, {})
            self.ndescMov.pack(side=LEFT)
            
            editBtn = Button(self.editFrame3,text="Edit",command=self.editMovie2)
            editBtn.pack()
               
        
    def editMovie2(self):
        '''
        UI to edit the name of a movie
        '''
        self.editFrame1.pack_forget()
        self.editFrame1=None
        self.editFrame2.pack_forget()
        self.editFrame2=None
        self.editFrame3.pack_forget()
        self.editFrame3=None
        try:
            editId=self.nidMov.get()
            editDesc=self.ndescMov.get()
            self._movieController.edit_movie(editId,editDesc)
            messagebox.showinfo("Success","Movie was updated!")
        except Exception as ex:
            messagebox.showinfo(title="Error", message="Error changing description: \n" + str(ex))
         
    def printList1(self,lists):
        '''
        Print a list of movies
        '''
        self.listMovies=Tk()
            
        self.listMovies.geometry("500x500+200+100")
        self.listMovies.title("List of movies")
            
        scrollbar = Scrollbar(self.listMovies)
        scrollbar.pack( side = RIGHT, fill=Y )

        mylist = Listbox(self.listMovies, yscrollcommand = scrollbar.set )
        mylist.pack( side = LEFT, fill = BOTH,expand=True)
        scrollbar.config( command = mylist.yview )
            
        if len(lists)==0:
            fstring="There are no movies!\n"
            mylist.insert(END,fstring)
                
        else:
            for key in lists:
                mylist.insert(END, str(lists[key]))
                mylist.insert(END, "Description: "+str(lists[key].get_description()))
                    
    def showAllMovies(self):
        '''
        UI to show all the available movies
        '''
        try:
            movies=self._movieController.get_allMovies()
            self.printList1(movies)
        except Exception as ex:
            messagebox.showinfo(title="Error", message="Error showing the movies: \n" + str(ex))
                
    def searchMovie2(self):
        '''
        Searches the partial string in the repository of movies
        '''
        self.searchFrame1.pack_forget()
        self.searchFrame1=None
        self.searchFrame2.pack_forget()
        self.searchFrame2=None
        self.searchFrame3.pack_forget()
        self.searchFrame3=None
        try:
            self.field=self.x
            self.information=self.info.get()
            askedMovies=self._movieController.search_movie(self.field,self.information)
            self.printList1(askedMovies)
        except Exception as ex:
            messagebox.showinfo(title="Error", message="Error searching movie: \n" + str(ex))
        
    def searchMovies(self):
        '''
        the main menu for searching movies
        '''
        if not self.searchFrame1:
            searchFrame1=Frame(self.movies)
            searchFrame1.pack()
            self.searchFrame1=searchFrame1;
            
            searchFrame2=Frame(self.movies)
            searchFrame2.pack()
            self.searchFrame2=searchFrame2;
            
            searchFrame3=Frame(self.movies)
            searchFrame3.pack()
            self.searchFrame3=searchFrame3;
                
            self.x = "No field selected"
            R1 = Radiobutton(self.searchFrame1, text="ID", variable=self.x, value=1, command=self.selected1)
            R1.pack( side=LEFT )
            R2 = Radiobutton(self.searchFrame1, text="Title", variable=self.x, value=2, command=self.selected2)
            R2.pack( side=LEFT )
            R3 = Radiobutton(self.searchFrame1, text="Genre", variable=self.x, value=3, command=self.selected3)
            R3.pack( side=LEFT)
            R4 = Radiobutton(self.searchFrame1, text="Description", variable=self.x, value=4, command=self.selected4)
            R4.pack( side=LEFT)
            
            R1.deselect()
            R2.deselect()
            R3.deselect()
            R4.deselect()
            
            lbl = Label(self.searchFrame2, text="Search: ")
            lbl.pack(side=LEFT)

            self.info = Entry(self.searchFrame2, {})
            self.info.pack(side=LEFT)
            
            editBtn = Button(self.searchFrame3,text="Search",command=self.searchMovie2)
            editBtn.pack()
        
    def selected1(self):
        self.x=1
    def selected2(self):
        self.x=2
    def selected3(self):
        self.x=3   
    def selected4(self):
        self.x=4        
                
    ##############################################################################################################################
    
    def manageClients(self):
        '''
        The main menu for movies management
        '''
        if not self.clients:
            self.clients=Tk()
        
            self.clients.title("Clients Manager")
            self.clients.geometry("300x500+900+50")
        
            mainLabel=Label(self.clients,text="Manage Clients",fg="red")
            mainLabel.pack()
        
            clientFrame=Frame(self.clients)
            clientFrame.pack()
            self.clientFrame=clientFrame
        
            self.addClientBtn = Button(clientFrame, text="Add client", command=self.addClient)
            self.addClientBtn.pack(side=TOP)
        
            self.removeClientBtn = Button(clientFrame, text="Remove client", command=self.removeClient)
            self.removeClientBtn.pack(side=TOP)

            self.listClientBtn = Button(clientFrame, text="Show all clients", command=self.showAllClients)
            self.listClientBtn.pack(side=TOP)
        
            self.editClientBtn = Button(clientFrame, text="Edit the name of a client", command=self.editClient)
            self.editClientBtn.pack(side=TOP)

            self.searchClientBtn = Button(clientFrame, text="Search client", command=self.searchClients)
            self.searchClientBtn.pack(side=TOP)

            self.closeBtn2 = Button(clientFrame, text="CLOSE", fg="red", command=self.closeClientsWindow)
            self.closeBtn2.pack(side=TOP)
            
            self.clients.bind("<Control-z>", self.undo)
            self.clients.bind("<Control-r>", self.redo)
            self.clients.protocol('WM_DELETE_WINDOW', self.closeClientsWindow)
            
        ###################################################
        
            self.addFrame6=None
            self.addFrame7=None
            self.addFrame8=None
            self.removeFrame3=None
            self.removeFrame4=None
            self.editFrame4=None
            self.editFrame5=None
            self.editFrame6=None
            self.searchFrame4=None
            self.searchFrame5=None
            self.searchFrame6=None
    
    def closeClientsWindow(self):
        '''
        Close Button function
        '''
        self.clients.destroy()
        self.clients=None            
    
        
    def _readClient(self):
        '''
        read client's data
        Input: -
        Output: the client's properties as a list
        Exceptions: -
        '''
        client=[]
        client.append(self.idCli.get())
        client.append(self.nameCli.get())
        return client
        
    def addClient(self):
        '''
        GUI to add a client in the repository
        '''
        if not self.addFrame6:
            addFrame6=Frame(self.clients)
            addFrame6.pack()
            self.addFrame6=addFrame6;
        
            addFrame7=Frame(self.clients)
            addFrame7.pack()
            self.addFrame7=addFrame7;
            
            addFrame8=Frame(self.clients)
            addFrame8.pack()
            self.addFrame8=addFrame8;
            
            lbl = Label(self.addFrame6, text="ID:")
            lbl.pack(side=LEFT)

            self.idCli = Entry(self.addFrame6, {})
            self.idCli.pack(side=LEFT)

            lbl = Label(self.addFrame7, text="Name:")
            lbl.pack(side=LEFT)

            self.nameCli = Entry(self.addFrame7, {})
            self.nameCli.pack(side=LEFT)
            
            addBtn = Button(self.addFrame8,text="Add",command=self.addClient2)
            addBtn.pack()
        
        
    def addClient2(self):
        '''
        add client in the repository
        '''
        self.addFrame6.pack_forget()
        self.addFrame6=None
        self.addFrame7.pack_forget()
        self.addFrame7=None
        self.addFrame8.pack_forget()
        self.addFrame8=None
        try:
            client=self._readClient()
            self._clientController.add_client(client)
            messagebox.showinfo("Success", "Client was added!")
        except Exception as ex:
            messagebox.showinfo(title="Error", message="Error adding client: \n" + str(ex))
    
        
    def removeClient(self):
        '''
        GUI to remove a client from the repository
        '''
        if not self.removeFrame3:
            removeFrame3=Frame(self.clients)
            removeFrame3.pack()
            self.removeFrame3=removeFrame3;
            
            removeFrame4=Frame(self.clients)
            removeFrame4.pack()
            self.removeFrame4=removeFrame4;
            
            lbl = Label(self.removeFrame3, text="ID to remove:")
            lbl.pack(side=LEFT)

            self.ridCli = Entry(self.removeFrame3, {})
            self.ridCli.pack(side=LEFT)
            
            removeBtn = Button(self.removeFrame4,text="Remove",command=self.removeClient2)
            removeBtn.pack()
        
               
    def removeClient2(self):
        '''
            
        '''
        self.removeFrame3.pack_forget()
        self.removeFrame3=None
        self.removeFrame4.pack_forget()
        self.removeFrame4=None
        try:
            removeId=self.ridCli.get()
            client=self._clientController.remove_client(removeId)
            self._rentalController.remove_rentals(client)
            messagebox.showinfo("Success","Client was removed!")
        except Exception as ex:
            messagebox.showinfo(title="Error", message="Error removing client: \n" + str(ex))
        
            
    def editClient(self):
        '''
        GUI to edit the name of a client
        '''
        if not self.editFrame4:
            editFrame4=Frame(self.clients)
            editFrame4.pack()
            self.editFrame4=editFrame4;
            
            editFrame5=Frame(self.clients)
            editFrame5.pack()
            self.editFrame5=editFrame5;
            
            editFrame6=Frame(self.clients)
            editFrame6.pack()
            self.editFrame6=editFrame6;
            
            lbl = Label(self.editFrame4, text="ID to edit:")
            lbl.pack(side=LEFT)

            self.nidCli = Entry(self.editFrame4, {})
            self.nidCli.pack(side=LEFT)
            
            lbl = Label(self.editFrame5, text="New Name:")
            lbl.pack(side=LEFT)

            self.nnameCli = Entry(self.editFrame5, {})
            self.nnameCli.pack(side=LEFT)
            
            editBtn = Button(self.editFrame6,text="Edit",command=self.editClient2)
            editBtn.pack()
               
        
    def editClient2(self):
        '''
        UI to edit the name of a client
        '''
        self.editFrame4.pack_forget()
        self.editFrame4=None
        self.editFrame5.pack_forget()
        self.editFrame5=None
        self.editFrame6.pack_forget()
        self.editFrame6=None
        try:
            editId=self.nidCli.get()
            editName=self.nnameCli.get()
            self._clientController.edit_client(editId,editName)
            messagebox.showinfo("Success","Client was updated!")
        except Exception as ex:
            messagebox.showinfo(title="Error", message="Error changing name: \n" + str(ex))
         
    def printList2(self,lists):
        '''
        Print a list of clients
        '''
        self.listClients=Tk()
            
        self.listClients.geometry("500x500+200+100")
        self.listClients.title("List of clients")
            
        scrollbar = Scrollbar(self.listClients)
        scrollbar.pack( side = RIGHT, fill=Y )

        mylist = Listbox(self.listClients, yscrollcommand = scrollbar.set )
        mylist.pack( side = LEFT, fill = BOTH,expand=True)
        scrollbar.config( command = mylist.yview )
            
        if len(lists)==0:
            fstring="There are no clients!\n"
            mylist.insert(END,fstring)
                
        else:
            for key in lists:
                mylist.insert(END, str(lists[key]))
                    
    def showAllClients(self):
        '''
        UI to show all the available clients
        '''
        try:
            clients=self._clientController.get_allClients()
            self.printList2(clients)
        except Exception as ex:
            messagebox.showinfo(title="Error", message="Error showing the movies: \n" + str(ex))
                
    def searchClient2(self):
        '''
        Searches the partial string in the repository of movies
        '''
        self.searchFrame4.pack_forget()
        self.searchFrame4=None
        self.searchFrame5.pack_forget()
        self.searchFrame5=None
        self.searchFrame6.pack_forget()
        self.searchFrame6=None
        try:
            self.field2=self.y
            self.information2=self.info2.get()
            askedClients=self._clientController.search_client(self.field2,self.information2)
            self.printList2(askedClients)
        except Exception as ex:
            messagebox.showinfo(title="Error", message="Error searching client: \n" + str(ex))
        
    def searchClients(self):
        '''
        the main menu for searching movies
        '''
        if not self.searchFrame4:
            searchFrame4=Frame(self.clients)
            searchFrame4.pack()
            self.searchFrame4=searchFrame4;
            
            searchFrame5=Frame(self.clients)
            searchFrame5.pack()
            self.searchFrame5=searchFrame5;
            
            searchFrame6=Frame(self.clients)
            searchFrame6.pack()
            self.searchFrame6=searchFrame6;
                
            self.y = "No field selected"
            R1 = Radiobutton(self.searchFrame4, text="ID", variable=self.y, value=1, command=self.selected5)
            R1.pack( side=LEFT )
            R2 = Radiobutton(self.searchFrame4, text="Name", variable=self.y, value=2, command=self.selected6)
            R2.pack( side=LEFT )
            
            R1.deselect()
            R2.deselect()
            
            lbl = Label(self.searchFrame5, text="Search: ")
            lbl.pack( side=LEFT )

            self.info2 = Entry(self.searchFrame5, {})
            self.info2.pack(side=LEFT)
            
            editBtn = Button(self.searchFrame6,text="Search",command=self.searchClient2)
            editBtn.pack()
    
    def selected5(self):
        self.y=1
    def selected6(self):
        self.y=2
    
###########################################################################################################################################
    
    
    def returnMovie(self):
        '''
        GUI to return a movie
        '''
        if not self.returnFrame1:
            returnFrame1=Frame(self.main)
            returnFrame1.pack()
            self.returnFrame1=returnFrame1;
            
            returnFrame2=Frame(self.main)
            returnFrame2.pack()
            self.returnFrame2=returnFrame2;
            
            returnFrame3=Frame(self.main)
            returnFrame3.pack()
            self.returnFrame3=returnFrame3;
            
            lbl1 = Label(self.returnFrame1, text="ID of the client: ")
            lbl1.pack( side=LEFT )

            self.idReturnCli = Entry(self.returnFrame1, {})
            self.idReturnCli.pack(side=LEFT)
            
            lbl2 = Label(self.returnFrame2, text="ID of the movie to return: ")
            lbl2.pack( side=LEFT )
            
            self.idReturnMov = Entry(self.returnFrame2, {})
            self.idReturnMov.pack(side=LEFT)
            
            returnBtn = Button(self.returnFrame3,text="Return",command=self.returnMovie2)
            returnBtn.pack()
        
    def returnMovie2(self):
        '''
        UI to return a movie
        '''
        self.returnFrame1.pack_forget()
        self.returnFrame1=None
        self.returnFrame2.pack_forget()
        self.returnFrame2=None
        self.returnFrame3.pack_forget()
        self.returnFrame3=None
        try:
            clientId=self.idReturnCli.get()
            self._rentalController.checks_client(clientId)
            movieId=self.idReturnMov.get()
            self._rentalController.checks_movie2(movieId)
            self._rentalController.return_rental(clientId,movieId)
            messagebox.showinfo(title="Success", message="Movie was returned!")
        except Exception as ex:
            messagebox.showinfo(title="Error", message="Error returning movie: \n" + str(ex))
    
    def rentMovie(self):
        '''
        GUI to rent a movie
        '''
        if not self.rentFrame1:
            rentFrame1=Frame(self.main)
            rentFrame1.pack()
            self.rentFrame1=rentFrame1;
            
            rentFrame2=Frame(self.main)
            rentFrame2.pack()
            self.rentFrame2=rentFrame2;
            
            rentFrame3=Frame(self.main)
            rentFrame3.pack()
            self.rentFrame3=rentFrame3;
            
            rentFrame4=Frame(self.main)
            rentFrame4.pack()
            self.rentFrame4=rentFrame4;
            
            lbl1 = Label(self.rentFrame1, text="ID of the movie: ")
            lbl1.pack( side=LEFT )

            self.idRentMov = Entry(self.rentFrame1, {})
            self.idRentMov.pack(side=LEFT)
            
            lbl2 = Label(self.rentFrame2, text="ID of the client: ")
            lbl2.pack( side=LEFT )
            
            self.idRentCli = Entry(self.rentFrame2, {})
            self.idRentCli.pack(side=LEFT)
            
            self.z = "No option selected"
            R1 = Radiobutton(self.rentFrame3, text="3 days", variable=self.z, value=3, command=self.selected7)
            R1.pack( side=LEFT )
            R2 = Radiobutton(self.rentFrame3, text="5 days", variable=self.z, value=5, command=self.selected8)
            R2.pack( side=LEFT )
            R3 = Radiobutton(self.rentFrame3, text="1 week (7 days)", variable=self.z, value=7, command=self.selected9)
            R3.pack( side=LEFT )
            R4 = Radiobutton(self.rentFrame3, text="2 weeks (14days)", variable=self.z, value=14, command=self.selected10)
            R4.pack( side=LEFT )
            
            R1.deselect()
            R2.deselect()
            R3.deselect()
            R4.deselect()
            
            rentBtn = Button(self.rentFrame4,text="Rent",command=self.rentMovie2)
            rentBtn.pack()
        
    def rentMovie2(self):
        '''
        UI to rent a movie
        '''
        self.rentFrame1.pack_forget()
        self.rentFrame1=None
        self.rentFrame2.pack_forget()
        self.rentFrame2=None
        self.rentFrame3.pack_forget()
        self.rentFrame3=None
        self.rentFrame4.pack_forget()
        self.rentFrame4=None
        try:
            movieId=self.idRentMov.get()
            self._rentalController.checks_movie(movieId)
            clientId=self.idRentCli.get()
            self._rentalController.checks_client(clientId)
            today=datetime.date.today()
            rental=[int(movieId),int(clientId),today]
            if type(self.z) is str:
                raise Exception("Please select an option!")
            dueDate=rental[2]+datetime.timedelta(days=self.z)
            rental.append(dueDate)
            self._rentalController.rent_movie(rental)
            messagebox.showinfo("Success","The movie was rented! Return Date: "+str(dueDate.strftime ("%d.%m.%Y")))
        except Exception as ex:
            messagebox.showinfo(title="Error", message="Error renting movie: \n" + str(ex))
    
    def selected7(self):
        self.z=3
    def selected8(self):
        self.z=5
    def selected9(self):
        self.z=7
    def selected10(self):
        self.z=14
    
############################################################################################################    
            
    def statisticsMenu(self):
        '''
        The GUI menu for statistics
        '''
        if not self.statistics:
            self.statistics=Tk()
        
            self.statistics.title("Statistics")
            self.statistics.geometry("400x250+500+500")
        
            mainLabel=Label(self.statistics,text="Statistics",fg="red")
            mainLabel.pack()
        
            statisticsFrame=Frame(self.statistics)
            statisticsFrame.pack()
            self.statisticsFrame=statisticsFrame
        
            self.mostRentedBtn = Button(statisticsFrame, text="Most rented movies", command=self._mostRentedMovies)
            self.mostRentedBtn.pack(side=TOP)
        
            self.mostActiveBtn = Button(statisticsFrame, text="Most active clients", command=self._mostActiveClients)
            self.mostActiveBtn.pack(side=TOP)

            self.allRentalsBtn = Button(statisticsFrame, text="All rentals", command=self._allRentals)
            self.allRentalsBtn.pack(side=TOP)
        
            self.lateRentalsBtn = Button(statisticsFrame, text="Late rentals", command=self._lateRentals)
            self.lateRentalsBtn.pack(side=TOP)

            self.closeBtn3 = Button(statisticsFrame, text="CLOSE", fg="red", command=self.closeStatisticsWindow)
            self.closeBtn3.pack(side=TOP)
            
            self.statistics.bind("<Control-z>", self.undo)
            self.statistics.bind("<Control-r>", self.redo)
            self.statistics.protocol('WM_DELETE_WINDOW', self.closeStatisticsWindow)
    
    ############################################################
    
            self.rentedFrame=None
            
            
    def closeStatisticsWindow(self):
        '''
        Close Button function
        '''
        self.statistics.destroy()
        self.statistics=None
    
    def _mostRentedMovies(self):
        '''
        GUI for most rented movies
        '''
        if not self.rentedFrame:
            rentedFrame=Frame(self.statistics)
            rentedFrame.pack()
            self.rentedFrame=rentedFrame
        
            self.allRentalsBtn = Button(rentedFrame, text="Most rented by number of days", command=self._mostRentedMovies2)
            self.allRentalsBtn.pack(side=TOP)
        
            self.lateRentalsBtn = Button(rentedFrame, text="Most rented by number of times", command=self._mostRentedMovies3)
            self.lateRentalsBtn.pack(side=TOP)
            
    def _mostRentedMovies2(self):
        '''
        UI for most rented movies by days
        '''
        self.rentedFrame.pack_forget()
        self.rentedFrame=None
        mostRented=self._rentalController.most_rented(1)
        self._createList(mostRented,1)
    
    def _mostRentedMovies3(self):
        '''
        UI for most rented movies by times
        '''
        self.rentedFrame.pack_forget()
        self.rentedFrame=None
        mostRented=self._rentalController.most_rented(2)
        self._createList(mostRented,1)
            
    def _mostActiveClients(self):
        '''
        GUI for most active clients
        '''
        mostActive=self._rentalController.active_clients()
        self._createList(mostActive,2)
        
    def _allRentals(self):
        '''
        GUI for all rentals list
        '''
        rentals=self._rentalController.all_rentals()
        self._createList(rentals,1)
        
    def _lateRentals(self):
        '''
        GUI for late rentals
        '''
        lateRentals=self._rentalController.late_rentals()
        self._createList(lateRentals,1)
        
    def _createList(self, lists, typeL):
        '''
        Creates a window with a list
        Input: lists - a list of objects
        Output: -
        Exceptions: -
        '''
        self.listStatistics=Tk()
            
        self.listStatistics.geometry("500x500+200+100")
        if typeL==1:
            self.listStatistics.title("List of movies")
        elif typeL==2:
            self.listStatistics.title("List of clients")
            
        scrollbar = Scrollbar(self.listStatistics)
        scrollbar.pack( side = RIGHT, fill=Y )

        mylist = Listbox(self.listStatistics, yscrollcommand = scrollbar.set )
        mylist.pack( side = LEFT, fill = BOTH,expand=True)
        scrollbar.config( command = mylist.yview )
            
        if len(lists)==0:
            fstring="The list is empty!\n"
            mylist.insert(END,fstring)
        else:
            for i in range(len(lists)):
                mylist.insert(END, str(lists[i]))
    
    def undo(self,second):
        '''
        GUI for undo
        '''
        try:
            self._rentalController.undo()
            messagebox.showinfo("Success","Undo completed!!")
        except Exception as ex:
            messagebox.showinfo("Error","Error for undo: \n"+str(ex))
       
    def redo(self,second):
        '''
        GUI for undo
        '''
        try:
            self._rentalController.redo()
            messagebox.showinfo("Success","Redo completed!!")
        except Exception as ex:
            messagebox.showinfo("Error","Error for redo: \n"+str(ex))
            
