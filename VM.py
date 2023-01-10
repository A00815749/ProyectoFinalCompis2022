import sys
from os import truncate
from myLexerParser import QUADSlist,Tableof_functions,ConstantVar_set
import statistics,matplotlib.pyplot as plt 

# READING QUADRUPLES
file = open("Quads.mir","r")
Quads = file.read()
Quads = Quads.split("\n") # Only the separated lines enter
Quads = Quads[:-1] # Erasing the last char

############ DATA STRUCTURES VARIABLES, MEMORY CLASS #########
STACKofexecs = []
PROCList = []
PROCCOUNTER = 0
Scopesensorglobal = True

class Memorysimulacra:
    def __init__(self):
        self.simmemory = {} 

##### AUXILIAR METHODS FOR THE VIRTUAL MACHINE ####################

#### ERROR HANDLER #######
def ERROR(type,location = ""):
    print("ERROR: ", type , " at ===>", location)
    sys.exit()

for x in Tableof_functions.keys(): # GET THE THE NAME OF THE MAIN PROGRAM FUNCTION
    if Tableof_functions[x]['context'] == 'g':
        programname = x

GLOBALmemory= Memorysimulacra()
localmemory = None