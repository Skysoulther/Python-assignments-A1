'''
Created on 7 Dec 2016

@author: DDL
'''
import unittest
from MovieDDL.controller.ControllerExceptions import ControllerException
from MovieDDL.controller.UndoController import *

class UndoControllerTest(unittest.TestCase):
    '''
    class to test Undo Controller
    '''
    def setUp(self):
        '''
        the setUp of data
        '''
        self.undoControl=undoController()
        self.Operation1=Operation("name1",["parameter1"])
        self.Operation2=Operation("name2",["parameter1","parameter2"])
        self.Operation3=Operation("name3",["parameter1","parameter2","parameter3"])
        
    def testUndoController(self):
        '''
        Test the undo Controller
        '''
        self.undoControl.store_undo([self.Operation1])
        self.undoControl.store_undo([self.Operation1,self.Operation2])
        self.undoControl.store_undo([self.Operation1,self.Operation2,self.Operation3])
        self.undoControl.store_redo([self.Operation1])
        self.undoControl.store_redo([self.Operation2])
        self.undoControl.store_redo([self.Operation3])
        self.assertEqual(len(self.undoControl.load_undo()),3)
        undo2=self.undoControl.load_undo()
        self.assertEqual(len(undo2),2)
        self.assertEqual(undo2[0].get_name(),"name1")
        self.assertEqual(undo2[0].get_parameters(),["parameter1"])
        self.assertEqual(undo2[1].get_name(),"name2")
        self.assertEqual(undo2[1].get_parameters(),["parameter1","parameter2"])
        self.assertEqual(len(self.undoControl.load_undo()),1)
        redo3=self.undoControl.load_redo()
        self.assertEqual(len(redo3),1)
        self.assertEqual(redo3[0].get_name(),"name1")
        self.assertEqual(redo3[0].get_parameters(),["parameter1"])
        