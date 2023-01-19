#Lexer by Andres Carlos Barrera Basilio A00815749
#Lexer using PLY
#Parser by Andres Carlos Barrera Basilio A00815749
#Parser using the above LExer and PLY

################## THE MIR LEXER AND PARSER #############################


#Librerias para importar en el Lexer-Parser
from re import split
import os
import sys
from typing import Hashable
import PIL
import ply.yacc as yacc
from Semanticcube import Semanticcube
from time import sleep

#Entrada de archivo de programacion para compilar con el input
arch = input("Nombre del archivo para compilar : ")


###################----------------GLOBAL VARIABLES AND METHODS------------------###################
###### PYTHON SETS, MUTABLE, ORDER OF ELEMENTS NOT IMPORTANT############

Tableof_functions = {} # The table set where we store the functions name and other things
GlobalVar_set = {} # Storing the variables in a global context
LocalVar_set = {} # Local context
ConstantVar_set = {} # Direct values of variables that don't change in the running process

# The Operation number that will be stored inside the quads product indicating which type of operation the quads is
HASHofoperatorsinquads = {
    '+' : 1,
    '-' : 2,
    '*' : 3,
    '/' : 4,
    '>' : 5,
    '>=' : 6,
    '<' : 7,
    '<=' : 8,
    '==' : 9,
    '<>' : 10,
    '=' : 11,
    'READ' : 12,
    'WRITE' : 13,
    'and' : 14,
    'OR' : 15,
    'GOTO' : 16,
    'GOTOF' : 17,
    'GOTOV' : 18,
    'ERA' : 19,
    'VER' : 20,
    'ENDPROC' : 21,
    'PARAM' : 22,
    'GOSUB' : 23,
    'MEDIA' : 24,
    'MEDIANA' : 25,
    'MODA' : 26,
    'STDEV' : 27,
    'VARIANZA' : 28,
    'PLOTXY' : 29,
    'RETURN' : 30,
    '' : -1
}

##### PYTHON LISTS, MUTABLE, ORDER OF ELEMENTS INHERENT IN THEIR APPLICATION, CAN FUNCTION AS STACKS #############
QUADSlist = []
GLOBALnames = [] # Storing names in global scope, using lists for ease of search, used as backup for the idnames in the sets used above
LOCALnames = [] # As above but in local scope
PARAMETERSvarlist = [] # QUEUE
PARAMETERStypelist = [] # TABLE
COUNTERparameter = [] 

######### MY STACKS, USING THE PYTHON LISTS AND POP() TO SIMULATE THE STACK BEHAVIOR
PilaO = []
Ptypes = []
POper = []
Pjumps = []
PDim = []
###### SENSORS, CHECKING THE SCOPE (CONTEXT) OF THE VARIABLES, & COUNTERS ############
Scopesensor = 'g' # G for global or l for local
currenttyping = '' # Stores the typing, being either int float or char
currentfunctionname = ''
TEMPORALScounter = 0 # Sensor for counting the temporals used, stored in the table of functions
INITIALvalinFOR = 0 # Global value to store the counter in the for logic section
FINALvalinFOR = 0 # Global value to store the final value in the counter for the for logic section
Dim = 0
################ MEMORY MAP FOR VARIABLE, CONSTANT, FUNCTION, TEMPORAL, PARAMETERS AND POINTERS STORAGE ###########
#When a memory block is used, it adds 1 to the counter.
GLOBALINTcounter = 1000 - 1  # BLOCK of 2000 spaces 
GLOBALFLOATcounter = 3000 - 1
GLOBALCHARcounter = 5000 - 1
LOCALINTcounter = 7000 - 1
LOCALFLOATcounter = 9000 - 1
LOCALCHARcounter = 11000 - 1
TEMPINTcounter = 13000 - 1
TEMPFLOATcounter = 15000 - 1
TEMPCHARcounter = 17000 - 1
TEMPBOOLcounter = 19000 - 1
CONSTINTcounter = 21000 - 1
CONSTFLOATcounter = 23000 - 1
CONSTCHARcounter = 25000 - 1
FUNCTIONVIRADDRcounter = 27000 - 1 # BLOCK of 3000 spaces 
PARAMSINTcounter = 30000 - 1
PARAMSFLOATcounter = 33000 - 1
PARAMSCHARcounter = 36000 - 1 # BLOCK of 4000 spaces 
POINTERScounter = 40000 - 1 # LAST BLOCK


############### QUADRUPLE CLASS FOR STORING THE COMPILER OPERATIONS ############

class Quadruple :
    def __init__(self, operator,LeftOperand,RightOperand,result):
        global QUADSlist
        self.QUADcounter = len(QUADSlist) + 1 # The number of the quadruple, so that we can have GOTO and derived functions
        self.operator = operator
        self.LeftOperand = LeftOperand
        self.RightOperand = RightOperand
        self.result = result

#### SEMANTIC CUBE CLASS OBJECT, A SENSOR THAR CHECKS OPERATIONS BETWEEN THE SIMPLE DATATYPES IN VARIABLES #############
semanticchecker = Semanticcube()

########################################################################################################################################

#---------------------------------------------------THE LEXER -------------------------------------------------------------------------- 
#---------------------------------------------------THE LEXER -------------------------------------------------------------------------- 
#---------------------------------------------------THE LEXER -------------------------------------------------------------------------- 
#---------------------------------------------------THE LEXER -------------------------------------------------------------------------- 
#---------------------------------------------------THE LEXER -------------------------------------------------------------------------- 
#---------------------------------------------------THE LEXER -------------------------------------------------------------------------- 

reserved = {
    'Program' : 'PROGRAM', # program reserved word
    'main' : 'MAIN', # main reserved word
    'function' : 'FUNCTION', # function reserved word 
    'VARS' : 'VARS', # VARS reserved word
    'int' : 'INT', # int reserved word
    'float' : 'FLOAT', # flot reserved word
    'char' : 'CHAR', # char reserved word
    'str' : 'STR', # STR reserved word
    'return' : 'RETURN', # return reserved word
    'read' : 'READ', # read reserved word
    'write' : 'WRITE', # write reserved word
    'and' : 'AND', # and reserved word
    'or' : 'OR', # or reserved word
    'if' : 'IF', # if reserved word
    'then' : 'THEN', # then reserved word
    'else' : 'ELSE',  # else reserved word
    'while' : 'WHILE', # while reserved word
    'do' : 'DO', # do reserved word
    'for' : 'FOR', # for reserved word
    'to' : 'TO', # to reserved word
    'void' : 'VOID', # void reserved word
    'true' : 'TRUE', # TRUE reserved word
    'false' : 'FALSE', # FALSE reserved word
    'media' : 'MEDIA', # special function average
    'mediana': 'MEDIANA', # special function median
    'moda' : 'MODA', # special function mode
    'varianza' : 'VARIANZA', # special function variance
    'stdev' : 'STDEV', # special function simple regression
    'plotxy' : 'PLOTXY', # special function plot two data columns
    } #dont put the previous reserved words as ID types, this handles that


##### THE LIST OF TOKENS IN MIR LANGUAGE
tokens = [
    'STRING', # String token
    'ID', # ID token
    'PLUS', # + symbol
    'REST', # - symbol
    'TIMES', # * symbol
    'DIVIDE', # / symbol
    'GREATER', # > symbol
    'GREATERAND', # >= symbol
    'LESSER', # < symbol
    'LESSERAND', # <= symbol
    'SAME', # == symbol
    'NOTSAME', # <> symbol
    'NOT', # ! symbol
    'EQUAL', # = symbol
    'LEFTBR', # { symbol
    'RIGHTBR', # } symbol
    'LEFTPAR', # ( symbol
    'RIGHTPAR', # ) symbol
    'LEFTSQR', # [ symbol
    'RIGHTSQR', # ] symbol
    'COLON', # : symbol
    'SEMICOLON', # ; symbol
    'COMMA', # , symbol
    'CTEINT', # constant int
    'CTEFLOAT', # constant float
    'CTECHAR', # constant char
] + list(reserved.values())

##### THE DEFINITION OF THE TOKENS
#---SYMBOLS

t_ignore = ' \t'
t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_COMMA = r'\,'
t_EQUAL = r'\='
t_SAME = r'\=\='
t_LEFTPAR = r'\('
t_RIGHTPAR = r'\)'
t_LEFTBR = r'\{'
t_RIGHTBR = r'\}'
t_LEFTSQR = r'\['
t_RIGHTSQR = r'\]'
t_STRING = r'\".*\"'
t_PLUS  = r'\+'
t_REST = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_GREATER = r'\>'
t_GREATERAND = r'\>\='
t_LESSER = r'\<'
t_LESSERAND = r'\<\='
t_NOTSAME = r'\<\>'
t_NOT = r'\!'
t_CTECHAR =r"\'.\'"

#----COMPLEX DEFINITIONS

def t_CTEFLOAT(t):
    r'-?\d+\.\d+' # able to accept sign symbols, and .97 (numbers without the integer part)
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_CTEINT(t):
    r'-?\d+' # taking account if sign symbol is present
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID') 
    return t


# every symbol that doesn't match with almost one of the previous tokens is considered an error
# modification so that all errors can be processed and debugged with the error catcher below

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("ERROR with illegal character (lexer) at: '%s'" % t.value[0])
    t.lexer.skip(1)

###################### BUILDING THE LEXER #########################
import ply.lex as lex
lexer = lex.lex()


########################################################################################################################################

#---------------------------------------------------NEURALGIC FUNCTIONS AUX ------------------------------------------------------------
#---------------------------------------------------NEURALGIC FUNCTIONS AUX ------------------------------------------------------------
#---------------------------------------------------NEURALGIC FUNCTIONS AUX ------------------------------------------------------------
#---------------------------------------------------NEURALGIC FUNCTIONS AUX ------------------------------------------------------------
#---------------------------------------------------NEURALGIC FUNCTIONS AUX ------------------------------------------------------------

########### GLOBAL AUXILIAR METHODS FOR NEURALGIC POINTS MANIPULATIONS ############

def getsetvirtualaddrFUNC():
    global FUNCTIONVIRADDRcounter
    FUNCTIONVIRADDRcounter+= 1
    return FUNCTIONVIRADDRcounter

def addtotableoffunctions(idname, type, scopecontext, variables):
    if (idname in Tableof_functions):
        errorhandler(1)
    elif (idname in GLOBALnames):
        errorhandler(2)
    else:
        Tableof_functions[idname] = {'type': type, 'scopecontext' : scopecontext, 'variables' : variables }
        GLOBALnames.append(idname)

def insertinVARStables(id,virtualaddr,type):
    if (virtualaddr < 7000):
        if (id in GLOBALnames):
            errorhandler(3, str(id + " " + type))
        if (id in GlobalVar_set):
            errorhandler(4,id)
        GlobalVar_set[id]= {'virtualaddress': virtualaddr, 'type' : type }
        GLOBALnames.append(id)
    else:
        if id in LOCALnames:
            errorhandler(3, str(id + " " + type))
        if id in LocalVar_set:
            errorhandler("varrepetida",id)
        LocalVar_set[id] = {'virtualaddress': virtualaddr,'type' : type}
        LOCALnames.append(id)

def endandresetfunction(): # RESET THE MEMORY SPACES
    global Scopesensor, LocalVar_set,LOCALnames
    global LOCALCHARcounter,LOCALFLOATcounter,LOCALINTcounter
    global TEMPINTcounter, TEMPFLOATcounter, TEMPCHARcounter, TEMPBOOLcounter, POINTERScounter
    global PARAMSINTcounter, PARAMSFLOATcounter, PARAMSCHARcounter
    LOCALINTcounter = 7000 - 1
    LOCALFLOATcounter = 9000 - 1
    LOCALCHARcounter = 11000 - 1
    TEMPINTcounter = 13000 - 1
    TEMPFLOATcounter = 15000 - 1
    TEMPCHARcounter = 17000 - 1
    TEMPBOOLcounter = 19000 - 1
    PARAMSINTcounter = 30000 - 1
    PARAMSFLOATcounter = 33000 - 1
    PARAMSCHARcounter = 36000 - 1 
    POINTERScounter = 40000 - 1 
    Scopesensor = 'g' # RETURN TO THE GLOBAL SCOPE TILL NEXT LOCAL CHANGE
    LocalVar_set = {} # EMPTY THE LOCAL VARIABLES
    LOCALnames = [] # EMPTY THE ORDERED USED NAMES

def setAVAILvirtualtempaddress(type): # GETTING THE TEMPORAL
    global TEMPINTcounter, TEMPFLOATcounter, TEMPCHARcounter, TEMPBOOLcounter
    global TEMPORALScounter, POINTERScounter
    TEMPORALScounter += 1
    if type == 'int':
        TEMPINTcounter += 1
        return TEMPINTcounter
    elif type == 'float':
        TEMPFLOATcounter += 1
        return TEMPFLOATcounter
    elif type == 'char':
        TEMPCHARcounter += 1
        return TEMPCHARcounter
    elif type == 'bool':
        TEMPBOOLcounter += 1
        return TEMPBOOLcounter
    elif type == 'pointer':
        POINTERScounter += 1
        return POINTERScounter

def setAVAILvirtualCTEaddress(value):
    global CONSTINTcounter,CONSTFLOATcounter,CONSTCHARcounter
    constanttype = type(value)
    if constanttype == int:
        CONSTINTcounter += 1
        return CONSTINTcounter
    elif constanttype == float:
        CONSTFLOATcounter += 1
        return CONSTFLOATcounter
    elif constanttype == str:
        CONSTCHARcounter += 1
        return CONSTCHARcounter
    else: 
        errorhandler(6, str(value)) # SEND THE VALUE THAT WE TRIED TO MAKE CONSTANT

def virtualaddrfetch(value):
    global GlobalVar_set, LocalVar_set, ConstantVar_set, Tableof_functions
    if value in LocalVar_set: # GET ME THE VIRTUAL ADDRESS IF LOCAL OR GLOBAL OR CONSTANT
        return LocalVar_set[value]['virtualaddress']
    elif value in GlobalVar_set:
        return GlobalVar_set[value]['virtualaddress']
    else:
        if type(value) == int:
            return ConstantVar_set[int(value)]
        if type(value) == float:
            return ConstantVar_set[float(value)]
        if type(value) == str:
            return ConstantVar_set[str(value)]

def getsetvirtualaddrVARS(type,scope):
    global GLOBALINTcounter,GLOBALFLOATcounter,GLOBALCHARcounter
    global LOCALINTcounter,LOCALFLOATcounter,LOCALCHARcounter
    if scope == 'g':
        if type == 'int':
            GLOBALINTcounter+= 1
            return GLOBALINTcounter + 1
        elif type == 'float':
            GLOBALFLOATcounter+= 1
            return GLOBALFLOATcounter + 1
        elif type == 'char':
            GLOBALCHARcounter+= 1
            return GLOBALCHARcounter + 1
    else:
        if type == 'int':
            LOCALINTcounter+= 1
            return LOCALINTcounter 
        elif type == 'float':
            LOCALFLOATcounter+= 1
            return LOCALFLOATcounter 
        elif type == 'char':
            LOCALCHARcounter+= 1
            return LOCALCHARcounter 

def getVALtype(value): # RETURN THE TYPE OF THE VARIABLE OR FUNCTION ID BEING CALLED
    if value in LocalVar_set:
        return LocalVar_set[value]['type']
    if value in GlobalVar_set:
        return GlobalVar_set[value]['type']
    if value in Tableof_functions:
        return Tableof_functions[value]['type']
    if type(value)== int:
        return 'int'
    if type(value)== float:
        return 'float'
    if type(value)== str:
        return 'char'

def setarraysize(id,context,size): # METHOD ADDING THE SIZE VALUE TO THE VARIABLE THAT IS AN ARRAY
    global GlobalVar_set,LocalVar_set
    if context == 'g':
        GlobalVar_set[id]['size'] = size
    elif context == 'l':
        LocalVar_set[id]['size'] = size

def setvirtualaddrarray(context,type,size): # METHOD USED IN DIMENSION MANAGEMENT OF VECTORS
    global GLOBALINTcounter, GLOBALFLOATcounter, GLOBALCHARcounter
    global LOCALINTcounter, LOCALCHARcounter, LOCALFLOATcounter
    if context == 'g':
        if type == 'int':
            GLOBALINTcounter += size
        elif type == 'float':
            GLOBALFLOATcounter += size
        elif type == 'char':
            GLOBALCHARcounter += size
    elif context == 'l':
        if type == 'int':
            LOCALINTcounter += size
        elif type == 'float':
            LOCALFLOATcounter += size
        elif type == 'char':
            LOCALCHARcounter += size

def fetchvirtualaddr(id): # GET THE INITIAL VIRTUAL ADDRESS ONLY FOR VECTORS
    global GlobalVar_set, LocalVar_set
    try:
        return LocalVar_set[id]['virtualaddress']
    except:
        return GlobalVar_set[id]['virtualaddress']

def getlimits(id):
    global GlobalVar_set,LocalVar_set
    try:
        return LocalVar_set[id]['size']
    except:
        return GlobalVar_set[id]['size']


#### ERROR HABDLER IN AUXILIAR METHODS

#LIST OF ERRORS
# 1 = Function name is duplicated in the table of functions
# 2 = Backup simple set name indicates that the name called is duplicate, check the table of functions status
# 3 = Name trying to be used as variable name is used as a function name
# 4 = Duplicated variable name
# 5 = Mismatch of variable types in the semantic cube, the operationg between the two variables gives an ERROR in the cube
# 6 = Error while trying to add a constant variable value in the virtual memory blocks, is neither int, float or char/string
# 7 = Error trying to parse a non-boolean value in the if neuralif handling
# 8 = Error in for variable expression being evaluated to other than int (neuralfor1)
# 9 = Error in for variable expression being evaluated to other than int (neuralfor2)
# 10 = Error in for variable expression being evaluated to other than int (neuralfor3)
# 11 = Error in a function call with an invalid number of parameters (neuralpar)
# 12 =  Error in a function call with a mismatch of parameters (neuralpar2)
# 13 = Error in a function call where the stored number of types in a function does not match with the actual number of types in the list of that function (neuralpar2)
# 14 = Error in a NULL check where the function id does not exist (neuralexist at CTEEXP)
# 15 = Error in checking if an id actually corresponds to an array in the variables sets (initarray)

def errorhandler(errortype, location = ""):
    errormessage = ""
    if (errortype == 1):
        errormessage = "Function name is duplicated in the table of functions"
    elif (errortype == 2):
        errormessage = "Backup simple set name indicates that the name called is duplicate, check the table of functions status"
    elif (errortype == 3):
        errormessage = "Name trying to be used as variable name is used as a function name"
    elif (errortype == 4):
        errormessage = "Duplicated variable name"
    elif (errortype == 5):
        errormessage = "Mismatch of variable types in the semantic cube, the operationg between the two variables gives an ERROR in the cube"
    elif (errortype == 6):
        errormessage = "Error while trying to add a constant variable value in the virtual memory blocks, is neither int, float or char/string"
    elif (errortype == 7):
        errormessage = "Error trying to parse a non-boolean value in the if neuralif handling"
    elif (errortype == 8):
        errormessage = "Error in for variable expression being evaluated to other than int (neuralfor1)"
    elif (errortype == 9):
        errormessage = "Error in for variable expression being evaluated to other than int (neuralfor2)"
    elif (errortype == 10):
        errormessage = "Error in for variable expression being evaluated to other than int (neuralfor3)"
    elif (errortype == 11):
        errormessage = "Error in a function call with an invalid number of parameters (neuralpar)"
    elif (errortype == 12):
        errormessage = "Error in a function call with a mismatch of parameters (neuralpar2)"
    elif (errortype == 13):
        errormessage = "Error in a function call where the stored number of types in a function does not match with the actual number of types in the list of that function (neuralpar2)"
    elif (errortype == 14):
        errormessage = "Error in a NULL check where the function id does not exist (neuralexist at CTEEXP)"
    elif (errortype == 15):
        errormessage = "Error in checking if an id actually corresponds to an array in the variables sets (initarray)"
    print("ERROR " + errormessage + "\n at ===> " + str(location))
    sys.exit()


########################################################################################################################################

#---------------------------------------------------THE GRAMMAR ------------------------------------------------------------------------
#---------------------------------------------------THE GRAMMAR ------------------------------------------------------------------------
#---------------------------------------------------THE GRAMMAR ------------------------------------------------------------------------
#---------------------------------------------------THE GRAMMAR ------------------------------------------------------------------------
#---------------------------------------------------THE GRAMMAR ------------------------------------------------------------------------
#---------------------------------------------------THE GRAMMAR ------------------------------------------------------------------------ 



#-----------------------------------OUTER INITIAL SHELL---------------------------------------------#
#functions = modules

def p_PROGRAM(p): #PROGRAM SHELL LOGIC
    '''
    program : PROGRAM neuraltablefunctions SEMICOLON varsgl modules MAIN LEFTPAR RIGHTPAR LEFTBR neuralmainjump statutes RIGHTBR
    '''
    print ('Llego al final de la gramatica, aceptado \n')
    global GLOBALINTcounter,GLOBALFLOATcounter,GLOBALCHARcounter
    global TEMPINTcounter,TEMPFLOATcounter,TEMPCHARcounter,TEMPBOOLcounter
    global CONSTINTcounter,CONSTFLOATcounter,CONSTCHARcounter,POINTERScounter
    actualname = p[2] # NAME OF THE PROGRAM
    Tableof_functions[actualname]['Intnumbers'] = (GLOBALINTcounter-(1000-1)) + (TEMPINTcounter - (13000-1))
    Tableof_functions[actualname]['Floatnumbers'] = (GLOBALFLOATcounter - (3000 - 1)) + (TEMPFLOATcounter - (15000-1))
    Tableof_functions[actualname]['Charnumbers'] = (GLOBALCHARcounter-(5000-1)) + (TEMPCHARcounter - (17000-1))
    Tableof_functions[actualname]['Boolnumbers'] = (TEMPBOOLcounter-(19000-1))
    Tableof_functions[actualname]['Pointernumbers'] = (POINTERScounter-(40000-1))
    #STORING THE VARIABLE NUMBERS BY SUBSTRACTING THE INITIAL MEMORY ALLOCATIONS TO THE FINAL VARIABLES COUNTERS
    #WHEN ENDING THE PROGRAM DELETE THE TABLE OF FUNCTIONS AND GLOBAL VAR TABLE
    #PROBABLY NOT TILL VIRTUAL MACHINE IS COMPLETE
    #print(Tableof_functions)


def p_NEURALTABLEFUNCTIONS(p):
    '''
    neuraltablefunctions : ID
    '''
    #print (p[1]) #THE VALUE STORED IN ID
    p[0] = p[1]  # STORING THE TOKEN VALUE IN THE YACC STACK 'p'
    addtotableoffunctions(p[1],'VOID',Scopesensor, GlobalVar_set)
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['GOTO'],-1,-1,-999))
    Pjumps.append(len(QUADSlist))
    ConstantVar_set[0] = setAVAILvirtualCTEaddress(0)
    ConstantVar_set[1] = setAVAILvirtualCTEaddress(1) # SETTING THE CONSTANTS 0 AND 1 for FOR LOGIC HANDLING 

def p_NEURALMAINJUMP(p):
    '''
    neuralmainjump :
    '''
    global QUADSlist, Pjumps
    if Pjumps:
        endoffunctions = Pjumps.pop()
        newQuad = QUADSlist[endoffunctions-1]
        newQuad.result = len(QUADSlist) + 1 # GO TO THE PART WHERE THE MAIN ACTUALLY STARTS


####### VARIABLES DECLARATION HANDLING ##########

def p_VARSGL(p):
    '''
    varsgl : VARS vars
            | empty
    '''

def p_VARS(p):
    '''
    vars : typing COLON neuralinsertvar varsarr varsmul vars
            | empty
    '''

def p_NEURALINSERTVAR(p):
    '''
    neuralinsertvar : ID
    '''
    global Scopesensor,currenttyping
    p[0] = p[1] # TOKEN STORING IN THE IN THE YACC STACK 'p'
    newaddr = getsetvirtualaddrVARS(currenttyping,Scopesensor) # GET THE VIRTUAL BLOCK ADDRESS DEPENDING ON THE TYPE OF VARIABLE AND THE SCOPE OF THE ENVIRONMENT
    insertinVARStables(p[1],newaddr,currenttyping) # STORE THE VARIABLE DATA
    
def p_VARSMUL(p): # MULTIPLE VARIABLE LOGIC
    '''
    varsmul : COMMA neuralinsertvar varsarr varsmul
            | SEMICOLON
    '''

###### VECTORS DECLARATION HANDLING #################


def p_VARSARR(p):
    '''
    varsarr : initdim CTEINT enddim
        | empty
    '''

def p_INITDIM(p): # SET THE VARIABLE isArray SENSOR AS TRUE
    '''
    initdim : LEFTSQR
    '''
    global LocalVar_set,GlobalVar_set,Scopesensor
    id = p[-1] # STORE THE VARIABLE ID
    if Scopesensor == 'g':
        GlobalVar_set[id]['isArray'] = True
    else:
        LocalVar_set[id]['isArray'] = True

def p_ENDDIM(p):
    '''
    enddim : RIGHTSQR
    '''
    global Scopesensor,currenttyping,ConstantVar_set
    LsDim = int(p[-1]) # STORE THE PREVIOUS TOKEN AS THE UPPER LIMIT, IN THIS LANGUAGE THIS INDICATES THE VECTOR/ARRAY SIZE, FROM 1 TO N
    id = p[-3]
    if not p[-1] in ConstantVar_set: # STORE THAT CONSTANT VALUE WITH ITS ACTUAL VIRTUAL ADDRESS
        ConstantVar_set[LsDim] = setAVAILvirtualCTEaddress(LsDim)
    setarraysize(id,Scopesensor,LsDim) # STORE THE SIZE OF THE ARRAY
    setvirtualaddrarray(Scopesensor,currenttyping,LsDim) # MODIFY THE VIRTUAL MEMORY BLOCK WITH THE SPACE NEEDED FOR THE VECTOR



##### VARIABLES VECTORS CALLS HANDLING #####

def p_IDARRAY(p):
    '''
    idarray : initarray exp verify RIGHTSQR
            | empty
    '''
    global PilaO,Ptypes,POper,QUADSlist,HASHofoperatorsinquads,GlobalVar_set,ConstantVar_set,Dim
    #### WHEREAS aux IS THE VALUE OF THE INTERNAL EXPRESSION, BEING IT A CONSTANT OR AN EXPRESSION, AND WHEREAS baseaddr IS OUR BASEADDRESS (dirBase)
    if len(p) > 2: # IF WE ARENT DEALING WITH AN EMPTY 
        if PilaO and POper: # CHECK THE STACKS FOR THE INTERNAL EXPRESSION, AND THAT WE HAVE A FAKE BOTTOM
            aux = PilaO.pop()
            baseaddr = fetchvirtualaddr(p[-1]) # GET THE VIRTUAL ADDRESS OF THE VARIABLE ARRAY WE ARE LOOKING (ITS STARTING POINT)
            pointer = setAVAILvirtualtempaddress('pointer') # GET THE POINTER VIRTUAL MEMORY DEALT WITH
            QUADSlist.append(Quadruple(HASHofoperatorsinquads['+'],aux,baseaddr,pointer)) # GET THE VERIFYING QUADRUPLE 
            PilaO.append(pointer)
            POper.pop() # ELIMINATING FAKE BOTTOM
            Dim = 0

def p_INITARRAY(p):
    '''
    initarray : LEFTSQR
    '''
    global POper,Ptypes,PilaO,Dim
    ### WE DEALT WITH THE NEED TO ASSIGN ARRAY SENSORS IN ANOTHER SECTION IN THE LOGIC, WE DONT NEED TO ADD THE ID TO THE PilaO HERE
    nameid = p[-1]
    # CHECK IF THE VAR WE HAVE ITS ACTUALLY AN ARRAY IN BOTH GLOBAL AND LOCAL VAR SETS
    if GlobalVar_set[nameid]['isArray']: 
        Dim += 1
        PDim.append((nameid,Dim))
        POper.append("~~~") # ADD FAKE BOTTOM
    elif LocalVar_set[nameid]['isArray']:
        Dim += 1
        PDim.append((nameid,Dim))
        POper.append("~~~") # ADD FAKE BOTTOM
    else:
        errorhandler(15)

def p_VERIFY(p):
    '''
    verify : 
    '''
    global PilaO,QUADSlist,HASHofoperatorsinquads,ConstantVar_set
    value = PilaO[-1]
    id = p[-3]
    limit = getlimits(id)
    LsDim = virtualaddrfetch(limit)
    LiDim = virtualaddrfetch(0)
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['VER'],value,LiDim,LsDim)) # GET THE VER QUADRUPLE

###### VARIABLE TYPING HANDLING #########
def p_TYPING(p):
    '''
    typing : INT
            | FLOAT
            | CHAR
    '''
    global currenttyping
    currenttyping = p[1] # STORE THE INT, FLOAT OR CHAR TOKEN FOR THE VARIABLE TYPE
    p[0] = p[1]  # STORING THE TOKEN IN THE YACC STACK 'p'

####### MODULES HANDLING ##########

def p_MODULES(p):
    '''
    modules : FUNCTION functype neuralinsertfuncname funcparam
            | empty
    '''

def p_NEURALINSERTFUNCNAME(p):
    '''
    neuralinsertfuncname : ID
    '''
    global Scopesensor, currentfunctionname,LocalVar_set,GlobalVar_set,currenttyping
    p[0] = p[1]
    Scopesensor = 'l'
    funcaddr = getsetvirtualaddrFUNC() # GET A FUNCTION ADDRESS IN MEMORY
    currentfunctionname = p[1]
    GlobalVar_set[currentfunctionname]={'virtualaddress': funcaddr,'type': currenttyping}  # SAVE THE FUNCTION NAME AS GLOBAL VARIABLE
    addtotableoffunctions(currentfunctionname,currenttyping,Scopesensor,LocalVar_set) # SAVE THE DATA TO TABLE OF FUNCTIONS

def p_FUNCTYPE(p):
    '''
    functype : VOID
            | typing
    '''
  
def p_FUNCPARAM(p):
    '''
    funcparam : LEFTPAR parameters RIGHTPAR SEMICOLON varsgl LEFTBR startfunc statutes RIGHTBR funcsize neuralendfuncs modules
    '''
    global Scopesensor
    Scopesensor = 'l' # CHANGING THE CONTEXT

def p_NEURALENDFUNCS(p):
    '''
    neuralendfuncs : 
    '''
    global Tableof_functions,QUADSlist,HASHofoperatorsinquads,currentfunctionname,TEMPORALScounter
    id = currentfunctionname
    Tableof_functions[id]["Tempsnumber"]= TEMPORALScounter # SAVE THE NUMBER OF TEMPORALS IN THE FUNCTION
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['ENDPROC'],-1,-1,-1)) # UPLOAD THE QUAD
    endandresetfunction() # CLEAN THE LOCAL TABLES, RESET CONTEXT TO GLOBAL

def p_FUNCSIZE(p): # SAVE THE MEMORY SIZE NEEDED FOR THE VARS IN THE FUNCTION INVOLVED
    '''
    funcsize :
    '''
    global Tableof_functions,LocalVar_set,QUADSlist,currentfunctionname
    global LOCALINTcounter,LOCALFLOATcounter, LOCALCHARcounter, TEMPINTcounter, TEMPFLOATcounter, TEMPCHARcounter, TEMPBOOLcounter, POINTERScounter
    functionname = currentfunctionname
    Tableof_functions[functionname]['Paramnumbers'] = len(LocalVar_set)
    Tableof_functions[functionname]['Intnumbers'] = (LOCALINTcounter-(7000-1)) + (TEMPINTcounter - (13000-1))
    Tableof_functions[functionname]['Floatnumbers'] = (LOCALFLOATcounter - (9000 - 1)) + (TEMPFLOATcounter - (15000-1))
    Tableof_functions[functionname]['Charnumbers'] = (LOCALCHARcounter-(11000-1)) + (TEMPCHARcounter - (17000-1))
    Tableof_functions[functionname]['Boolnumbers'] = (TEMPBOOLcounter-(19000-1))
    Tableof_functions[functionname]['Pointernumbers'] = (POINTERScounter-(40000-1))

def p_STARTFUNC(p):
    '''
    startfunc :
    '''
    global currentfunctionname,QUADSlist,Tableof_functions
    functionname = currentfunctionname
    Tableof_functions[functionname]['Initialfuncpoint']= len(QUADSlist) + 1


####### PARAMETER VARIABLE HANDLING IN FUNCTION DEFINITION ############

def p_PARAMETERS(p):
    '''
    parameters : typing COLON neuralinsertid idarray mulparams
            | empty
    '''

def p_NEURALINSERTID(p):
    '''
    neuralinsertid : ID
    '''
    global Scopesensor, currenttyping, PARAMETERSvarlist, PARAMETERStypelist
    Scopesensor = 'l'
    virtualaddress = getsetvirtualaddrVARS(currenttyping,Scopesensor)
    insertinVARStables(p[1],virtualaddress,currenttyping)
    PARAMETERSvarlist.append(virtualaddress)
    PARAMETERStypelist.append(currenttyping)


def p_MULPARAMS(p):
    '''
    mulparams : COMMA parameters
            | empty
    '''

# RETURNING SPECIAL QUADRUPLE LOGIC

def p_RETURNING(p):
    '''
    returning : RETURN LEFTPAR exp RIGHTPAR SEMICOLON
    '''
    global PilaO,QUADSlist,HASHofoperatorsinquads,GlobalVar_set
    valuetoreturn = PilaO.pop() ## CHECK THE STATUS OF PILAO AND PTYPES
    Ptypes.pop()
    functionvirtualaddr = GlobalVar_set[currentfunctionname]['virtualaddress'] # GET THE ADDRESS OF THE SPECIAL FUNCTION ADDRESS TO BE USED AS TEMPORAL CONTAINER
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['RETURN'],valuetoreturn,-1,functionvirtualaddr))


#########PARAMETERS HANDLING IN FUNCTION CALLS #########

def p_PARAMSEXP(p):
    '''
    paramsexp : LEFTPAR neuralera paramsexp2 neuralpar
                | idarray
    '''

def p_PARAMSEXP2(p):
    '''
    paramsexp2 : exp neuralpar2 auxparamsexp2
            | empty
    '''

def p_AUXPARAMSEXP2(p):
    '''
    auxparamsexp2 : COMMA exp neuralpar2 auxparamsexp2
            | empty
    '''

def p_NEURALERA(p):
    '''
    neuralera :
    '''
    global QUADSlist,HASHofoperatorsinquads,POper,COUNTERparameter
    POper.append("~~~")
    id = p[-3] # FUNCTION ID
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['ERA'],-1,-1,id))
    COUNTERparameter.append(0)

def p_NEURALPAR(p):
    '''
    neuralpar : RIGHTPAR
    '''
    global QUADSlist,HASHofoperatorsinquads,Tableof_functions,GlobalVar_set
    global POper,PilaO,Ptypes,COUNTERparameter,PARAMETERStypelist,currentfunctionname
    POper.pop() ## GET RID OF THE FALSE BOTTOM
    id = p[-4] #FUNCTION NAME BEING 4 TOKENS BACK
    counter = COUNTERparameter.pop()
    if len(PARAMETERStypelist) != counter:
        errorhandler(11)
    startaddress = Tableof_functions[id]['Initialfuncpoint']
    fucntionvirtualaddress = GlobalVar_set[id]['virtualaddress']
    functiontype = GlobalVar_set[id]['type']
    temporal = setAVAILvirtualtempaddress(functiontype)
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['GOSUB'],id,-1,startaddress))
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['='],fucntionvirtualaddress,-1,temporal))
    PilaO.append(temporal)
    Ptypes.append(functiontype)

def p_NEURALPAR2(p):
    '''
    neuralpar2 :
    '''
    global PARAMSINTcounter,PARAMSFLOATcounter,PARAMSCHARcounter,PARAMETERStypelist
    global PilaO,Ptypes,QUADSlist,HASHofoperatorsinquads,PARAMETERSvarlist,COUNTERparameter
    if PilaO and Ptypes and PARAMETERStypelist:
        argument = PilaO.pop()
        argumenttype = Ptypes.pop()
        counter = COUNTERparameter.pop()
        if argumenttype != PARAMETERStypelist[counter]:
            errorhandler(12)
        if argumenttype == 'int':
            PARAMSINTcounter += 1
            QUADSlist.append(Quadruple(HASHofoperatorsinquads['PARAM'],argument,-1,PARAMETERSvarlist[counter]))
        elif argumenttype == 'float':
            PARAMSFLOATcounter += 1
            QUADSlist.append(Quadruple(HASHofoperatorsinquads['PARAM'],argument,-1,PARAMETERSvarlist[counter]))
        elif argumenttype == 'char':
            PARAMSCHARcounter += 1
            QUADSlist.append(Quadruple(HASHofoperatorsinquads['PARAM'],argument,-1,PARAMETERSvarlist[counter]))
        COUNTERparameter.append(counter+1)
    else:
        if len(PARAMETERStypelist)!= COUNTERparameter:
            errorhandler(13,p[-1])


#### STATUTES HANDLING #####

def p_STATUTES(p):
    '''
    statutes : assign statutesaux
            | reading statutesaux
            | writing statutesaux
            | returning statutesaux
            | ifing statutesaux
            | whiling statutesaux
            | foring statutesaux
            | exp statutesaux
            | specialfunc statutesaux
    '''

def p_STATUTESAUX(p): # Repeat of statutes
    '''
    statutesaux : statutes 
                | empty
    '''

def p_SPECIALFUNC(p):
    '''
    specialfunc : empty
    '''


#### ASSIGNING IDs TO VARIABLES LOGIC SECTION############

def p_ASSIGN(p):
    '''
    assign : neuralassign1 idarray neuralassign2 assignexp SEMICOLON 
    '''
    global PilaO,Ptypes,HASHofoperatorsinquads,POper,QUADSlist
    if PilaO and Ptypes:
        asigned = PilaO.pop()
        righttype = Ptypes.pop()
        leftoperand = PilaO.pop()
        lefttype = Ptypes.pop()
        operator = POper.pop()
        resulttype =semanticchecker.getType(lefttype,righttype,operator)
        if resulttype == 'ERROR':
                errorhandler(5)
        QUADSlist.append(Quadruple(HASHofoperatorsinquads['='],asigned,-1,leftoperand))

def p_NEURALASSIGN1(p):
    '''
    neuralassign1 : ID
    '''
    global Ptypes,PilaO
    p[0] = p[1]
    virtualaddr = virtualaddrfetch(p[1])
    PilaO.append(virtualaddr)
    Ptypes.append(getVALtype(p[1]))

def p_NEURALASSIGN2(p):
    '''
    neuralassign2 : EQUAL
    '''
    global POper
    POper.append(p[1]) # STORING THE EQUAL TOKEN

def p_ASSIGNEXP(p):
    '''
    assignexp : exp
    '''
    p[0] = p[1] # STORE THAT EXP FOR FUTURE USE


###### WRITING LOGIC SECTION ############

def p_WRITING(p):
    '''
    writing : WRITE LEFTPAR auxwrite mulwrite RIGHTPAR SEMICOLON
    '''

def p_AUXWRITE(p):
    '''
    auxwrite : writetyping
            | exp
    '''
    global PilaO,QUADSlist,HASHofoperatorsinquads
    result = PilaO.pop() # GET THE OPERAND THAT WILL BE WRITTEN
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['WRITE'],-1,-1,result))

def p_WRITETYPING(p):
    '''
    writetyping : STRING
            | CTECHAR
    '''
    global PilaO
    PilaO.append(p[1]) # STORE THAT OPERAND THAT IS A CTECHAR OR A STRING

def p_MULWRITE(p): # MULTIPLE VARS TO WRITE
    '''
    mulwrite : COMMA auxwrite mulwrite
            | empty
    '''

###### READING LOGIC SECTION #######

def p_READING(p):
    '''
    reading : READ LEFTPAR neuralread idarray mulread RIGHTPAR SEMICOLON
    '''

def p_NEURALREAD(p):
    '''
    neuralread : ID
    '''
    global QUADSlist,HASHofoperatorsinquads
    readedvar = virtualaddrfetch(p[1]) #VAR TO BE READ AND ASSIGNED VIRTUAL ADDRESS VALUE
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['READ'],-1,-1,readedvar))

def p_MULREAD(p):
    '''
    mulread : COMMA neuralread idarray mulread
            | empty
    '''

########### CYCLES AND DECISIONS #############

# IFING

def p_IFING(p):
    '''
    ifing : IF LEFTPAR exp neuralif THEN LEFTBR statutes RIGHTBR elsing
    '''
    global Pjumps, QUADSlist
    if Pjumps: #IF there are pending jumps
        endofjump = Pjumps.pop() # GET THE ADDRESS FOR THE START OF THE ELSE SECTION
        modQuad = QUADSlist[endofjump-1] # USE THE PREVIOUS ADDRESS TO GET TO THE GOTO QUAD
        modQuad.result = len(QUADSlist)+ 1 # MODIFY THAT GOTO QUAD

def p_NEURALIF(p):
    '''
    neuralif : RIGHTPAR
    '''
    global Pjumps,Ptypes, PilaO, QUADSlist,HASHofoperatorsinquads
    if Ptypes and PilaO:
        VARStype = Ptypes.pop()
        if VARStype == 'bool': # CHECK THAT THE IF STATEMENT GIVES A BOOL VALUE
            result = PilaO.pop()
            QUADSlist.append(Quadruple(HASHofoperatorsinquads['GOTOF'],result,-1,-99)) # THE PENDING QUADRUPLE TO BE MODIFIED LATER 
            Pjumps.append(len(QUADSlist))
        else:
            errorhandler(7)

def p_ELSING(p):
    '''
    elsing : neuralelse LEFTBR statutes RIGHTBR
            | empty
    '''

def p_NEURALELSE(p):
    '''
    neuralelse : ELSE
    '''
    global QUADSlist,Pjumps,HASHofoperatorsinquads
    if Pjumps:
        QUADSlist.append(Quadruple(HASHofoperatorsinquads['GOTO'],-1,-1,-99))
        elseendofjump = Pjumps.pop() # GET THE ADDRESS FOR THE START OF THE IF SECTION
        Pjumps.append(len(QUADSlist)) # ADD THE QUADRUPLE COUNTER FOR THE START OF THE ELSE SECTION
        modQuad = QUADSlist[elseendofjump-1] # USE THE ADDRESS FOR THE START OF THE IF SECTION TO GET THE GOTOF QUAD
        modQuad.result = len(QUADSlist) + 1 # MODIFY THE QUAD WITH CURRENT QUADCOUNTER 





######### WHILE CYCLE LOGIG SECTION ###########

def p_WHILING(p):
    '''
    whiling : neuralwhile1 LEFTPAR exp neuralwhile2 DO LEFTBR statutes RIGHTBR
    '''
    global Pjumps,QUADSlist,HASHofoperatorsinquads
    if Pjumps:
        endofwhile = Pjumps.pop() # THE GOTOF QUADCOUNTER
        startofwhile = Pjumps.pop() # THE BOOLEAN EVALUATION QUADCOUNTER
        QUADSlist.append(Quadruple(HASHofoperatorsinquads['GOTO'],-1,-1,startofwhile+1)) # SET THE GOTO QUAD WHITH THE OFFSET QUADCOUNTER
        modQuad = QUADSlist[endofwhile - 1]
        modQuad.result = len(QUADSlist) + 1 # MODIFY THE GOTOF QUADRUPLE


def p_NEURALWHILE1(p):
    '''
    neuralwhile1 : WHILE
    '''
    global Pjumps, QUADSlist
    Pjumps.append(len(QUADSlist)) # GET THE QUADCOUNTER SAVED FOR THE BOOLEAN EVALUATION AND START OF WHILE SECTION

def p_NEURALWHILE2(p):
    '''
    neuralwhile2 : RIGHTPAR
    '''
    global Ptypes,PilaO,QUADSlist,Pjumps,HASHofoperatorsinquads
    if Ptypes and PilaO:
        exptype = Ptypes.pop()
        if exptype == 'bool':
            result = PilaO.pop()
            QUADSlist.append(Quadruple(HASHofoperatorsinquads['GOTOF'],result,-1,-999)) 
            Pjumps.append(len(QUADSlist)) # THE GOTOF QUADCOUNTER STORED IN PJUMPS



###### FOR LOGIC SECTION #####################

def p_FORING(p):
    '''
    foring : FOR neuralfor1 idarray EQUAL exp neuralfor2 exp neuralfor3 LEFTBR statutes RIGHTBR
    '''
    global INITIALvalinFOR,Pjumps,QUADSlist,HASHofoperatorsinquads,Ptypes,PilaO
    temporalint = setAVAILvirtualtempaddress('int')
    constant1addr = virtualaddrfetch(1)
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['+'],INITIALvalinFOR,constant1addr,temporalint)) # THE ITERATION
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['='],temporalint,-1,INITIALvalinFOR)) #CONTINUING ITERATION
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['='],temporalint,-1,PilaO[-1])) #THE QUADRUPLE GETTING THE OPERATOR STACK MODIFIED
    endoffor = Pjumps.pop() #GET THE COUNTER FOR THE GOTOF
    startoffor = Pjumps.pop() # GET THE COUNTER FOR THE EXPRESSION EVALUATION
    QUADSlist.append(Quadruple(HASHofoperatorsinquads['GOTO'],-1,-1,startoffor)) # VALIDATE THE CONDITION
    QUADSlist[endoffor - 1].result =  len(QUADSlist) + 1 # GET THAT PENDING QUADRUPLE WITH THE QUAD COUNTER
    PilaO.pop()
    Ptypes.pop()

def p_NEURALFOR1(p):
    '''
    neuralfor1 : ID
    '''
    global PilaO, Ptypes
    virtualaddr = virtualaddrfetch(p[1]) # THE VIRTUAL ADDRESS OF THE VARIABLE(ID) WE ARE LOOKING FOR
    type = getVALtype(p[1])
    PilaO.append(virtualaddr) # ADD THE VARIABLE TO THE STACK
    if type == 'int':
        Ptypes.append(type)
    else:
        errorhandler(8)


def p_NEURALFOR2(p):
    '''
    neuralfor2 : TO
    '''
    global Ptypes,PilaO,QUADSlist,HASHofoperatorsinquads,INITIALvalinFOR
    type = Ptypes.pop()
    if type == 'int':
        if PilaO:
            exp = PilaO.pop()
            INITIALvalinFOR = PilaO[-1] # STORE THE LAST OPERAND, MUST BE THE ONE IN NEURALFOR1
            QUADSlist.append(Quadruple(HASHofoperatorsinquads['='],exp,-1,INITIALvalinFOR))
    else:
        errorhandler(9)


def p_NEURALFOR3(p):
    '''
    neuralfor3 : DO
    '''
    global Ptypes,PilaO,INITIALvalinFOR,FINALvalinFOR,Pjumps,QUADSlist,HASHofoperatorsinquads
    if Ptypes and PilaO:
        type = Ptypes.pop()
        if type == 'int':
            exp = PilaO.pop()
            FINALvalinFOR = setAVAILvirtualtempaddress('int') # GET THE VIRTUAL ADDRESS
            QUADSlist.append(Quadruple(HASHofoperatorsinquads['='],exp,-1,FINALvalinFOR))
            temporalbool = setAVAILvirtualtempaddress('bool') # GET THE VIRTUAL ADDRESS
            QUADSlist.append(Quadruple(HASHofoperatorsinquads['<'],INITIALvalinFOR,FINALvalinFOR,temporalbool))
            Pjumps.append(len(QUADSlist)) # THE EXPRESSION EVALUATION QUADCOUNTER
            QUADSlist.append(Quadruple(HASHofoperatorsinquads['GOTOF'],temporalbool,-1,-99))
            Pjumps.append(len(QUADSlist)) # THE GOTOF QUADCOUNTER
        else:
            errorhandler(10)




########################################################## EXPRESSION LOGIC START POINT ######################################

def p_EXP(p):
    '''
    exp : andexp exp1
    '''
    p[0]= p[1] # STORE THAT EXP TOKEN 

def p_EXP1(p):
    '''
    exp1 : OR exp
        | empty
    '''

def p_ANDEXP(p):
    '''
    andexp : boolexp andexp1
    '''
    p[0] = p[1] # STORE THAT ANDEXP TOKEN

def p_ANDEXP1(p):
    '''
    andexp1 : neuraland andexp
        | empty
    '''

def p_NEURALAND(p):
    '''
    neuraland : AND
    '''
    global POper
    # CAN CHANGE THE 'and' TO & IN THE FUTURE
    POper.append(p[1]) #STORING 'and' OPERATOR TOKEN




###### BOOLEANS AND THE AND QUADS GENERATOR ################

def p_BOOLEXP(p):
    '''
    boolexp : arithexp boolexp1
    '''
    #HERE YOU EXIT THE BOOLEAN EXPRESSION, WHICH IS INSIDE THE SINTAX DIAGRAM OF THE AND EXPRESSION, SO YOU MUST RESOLVE
    #THE QUADS FOR THE ANDs, AS SEEN IN CLASS
    global POper,PilaO,Ptypes,HASHofoperatorsinquads,QUADSlist
    if len(POper) > 0:
        if POper[-1] == 'and':
            rightOperand = PilaO.pop()
            righttype = Ptypes.pop()
            leftOperand = PilaO.pop()
            lefttype = Ptypes.pop()
            operator = POper.pop()
            resulttype = semanticchecker.getType(lefttype,righttype,operator)
            if resulttype == 'ERROR':
                errorhandler(5)
            # AVAIL SPACE, IN THE FUTURE IS A VIRTUAL TEMPORAL ADDRESS
            resultaddress = setAVAILvirtualtempaddress(resulttype)
            QUADSlist.append(Quadruple(HASHofoperatorsinquads[operator],leftOperand,rightOperand,resultaddress))
            PilaO.append(resultaddress)
            Ptypes.append(resulttype)
    p[0] = p[1] # STORE THAT BOOLEXP


def p_BOOLEXP1(p):
    '''
    boolexp1 : neuralbool arithexp
        | empty
    '''

def p_NEURALBOOL(p):
    '''
    neuralbool : GREATER 
        | GREATERAND 
        | LESSER 
        | LESSERAND 
        | SAME 
        | NOTSAME 
        | NOT 
    '''
    global POper
    POper.append(p[1]) # STORE THE BOOLEAN TOKEN



###### ARITHMETIC TOKENS AND BOOLEAN QUADS GENERATOR ##############



def p_ARITHEXP(p):
    '''
    arithexp : geoexp arithexp1
    '''
    global POper,Ptypes,PilaO,QUADSlist,HASHofoperatorsinquads
    booltokens = ['>','>=', '<','<=','==','<>']
    if len(POper) > 0:
        if POper[-1] in booltokens: # GENERATING THE BOOL OPERATORS QUADS
            rightOperand = PilaO.pop()
            righttype = Ptypes.pop()
            leftOperand = PilaO.pop()
            lefttype = Ptypes.pop()
            operator = POper.pop()
            resulttype = semanticchecker.getType(lefttype,righttype,operator)
            if resulttype == 'ERROR':
                errorhandler(5)
            # AVAIL SPACE, IN THE FUTURE IS A VIRTUAL TEMPORAL ADDRESS
            resultaddress = setAVAILvirtualtempaddress(resulttype)
            QUADSlist.append(Quadruple(HASHofoperatorsinquads[operator],leftOperand,rightOperand,resultaddress))
            PilaO.append(resultaddress)
            Ptypes.append(resulttype)
    p[0] = p[1] # STORE THAT ARITHEXP

def p_ARITHEXP1(p):
    '''
    arithexp1 : neuralarith arithexp
        | empty
    '''

def p_NEURALARITH(p):
    '''
    neuralarith : PLUS
                | REST
    '''
    global POper
    POper.append(p[1])


###### GEOMETRIC TOKENS AND ARITHMETIC QUADS GENERATOR #####################################


def p_GEOEXP(p):
    '''
    geoexp : finexp geoexp1
    '''
    global POper,Ptypes,PilaO,QUADSlist,HASHofoperatorsinquads
    if len(POper) > 0:
        if POper[-1] == '+' or POper[-1] == '-': # GENERATING THE ARITHMETIC OPERATORS QUADS
            rightOperand = PilaO.pop()
            righttype = Ptypes.pop()
            leftOperand = PilaO.pop()
            lefttype = Ptypes.pop()
            operator = POper.pop()
            resulttype = semanticchecker.getType(lefttype,righttype,operator)
            if resulttype == 'ERROR':
                errorhandler(5)
            # AVAIL SPACE, IN THE FUTURE IS A VIRTUAL TEMPORAL ADDRESS
            resultaddress = setAVAILvirtualtempaddress(resulttype)
            QUADSlist.append(Quadruple(HASHofoperatorsinquads[operator],leftOperand,rightOperand,resultaddress))
            PilaO.append(resultaddress)
            Ptypes.append(resulttype)
    p[0] = p[1] #STORE THAT GEOEXP

def p_GEOEXP1(p):
    '''
    geoexp1 : neuralgeo geoexp
        | empty
    '''

def p_NEURALGEO(p):
    '''
    neuralgeo : TIMES
            | DIVIDE
    '''
    global POper
    POper.append(p[1]) # ADD THE GEOMETRIC TOKENS BEING * OR /


###### PARENTHESIS LOGIC, FALSE BOTTOMS AND VECTORS(ARRAYS), GEOMETRIC QUADS GENERATOR ######################

def p_ADDPARENTH(p):
    '''
    addparenth : LEFTPAR
    '''
    global POper
    POper.append('~~~') # ADD A FALSE BOTTOM


def p_POPPARENTH(p):
    '''
    popparenth : RIGHTPAR
    '''
    global POper
    POper.pop() #GET RID OF FALSE BOTTOM

def p_FINEXP(p):
    '''
    finexp : addparenth exp popparenth
            | cteexp
    '''
    global PilaO,POper,Ptypes,QUADSlist,HASHofoperatorsinquads,ConstantVar_set
    # PARENTHESES HANDLING, VECTORS HANDLING SECTION AND CTEEXP HANDLING
    if len(p) == 2:
        virtualaddr = virtualaddrfetch(p[1])
        isArraysensor = False
        try:
            if GlobalVar_set[p[1]]['isArray'] :
                isArraysensor = True
        except:
            try:
                if LocalVar_set[p[1]]['isArray'] :
                    isArraysensor = True
            except:
                    isArraysensor =  False    
        if not virtualaddr >= 27000 and virtualaddr < 30000 : # IF NOT A FUNCTION CALL ID
            if not isArraysensor:
                PilaO.append(virtualaddr)
                Ptypes.append(getVALtype(p[1]))
        p[0] = p[1] # STORE THAT CONSTANT EXP
    if len(p) == 3: # FUNCTION CALL HANDLING HERE
        newvirtualaddr = virtualaddrfetch(p[1])
        PilaO.append(newvirtualaddr)
        Ptypes.append(getVALtype(p[1]))
        p[0] = p[1] # STORE THAT FUNCTION CALL TOKEN
    if len(POper) > 0:
        if POper[-1] =='*' or POper[-1]=='/': # GENERATING THE GEOMETRIC QUADS
            rightOperand = PilaO.pop()
            righttype = Ptypes.pop()
            leftOperand = PilaO.pop()
            lefttype = Ptypes.pop()
            operator = POper.pop()
            resulttype = semanticchecker.getType(lefttype,righttype,operator)
            if resulttype == 'ERROR':
                errorhandler(5)
            # AVAIL SPACE, IN THE FUTURE IS A VIRTUAL TEMPORAL ADDRESS
            resultaddress = setAVAILvirtualtempaddress(resulttype)
            QUADSlist.append(Quadruple(HASHofoperatorsinquads[operator],leftOperand,rightOperand,resultaddress))
            PilaO.append(resultaddress)
            Ptypes.append(resulttype)




###### CONSTANT TOKENS AND EXPRESSIONS HANDLING ############

def p_CTEEXP(p):
    '''
    cteexp : CTEINT
            | CTEFLOAT
            | CTECHAR
            | ID neuralexist paramsexp
    '''
    global ConstantVar_set
    if len(p) == 2:
        if not p[1] in ConstantVar_set: #IF THE CONSTANT IS NOT ALREADY SAVED, SAVE IT NOW
            ConstantVar_set[p[1]] = setAVAILvirtualCTEaddress(p[1])
    p[0] = p[1] # STORE THAT CONSTANT EXP

def p_NEURALEXIST(p):
    '''
    neuralexist :
    '''
    global LocalVar_set,GlobalVar_set,ConstantVar_set,Tableof_functions
    if p[-1] not in ConstantVar_set and p[-1] not in GlobalVar_set and p[-1] not in LocalVar_set and p[-1] not in Tableof_functions:
        errorhandler(14,p[-1])
    p[0] = p[-1] # STORE THAT ID BEFORE FUNCTION CALLS

####EXCEPTIONS HANDLING#####

def p_empty(p):
    '''
    empty : 
    '''     
    pass  

def p_error(p):
    print ("Syntax Error in '%s'" % p.value)
    print ("The token is ")
    print (p)
    sys.exit()

def p_DEBUG(p): # Manual Debugger 
    '''
    debug : empty
    '''
    print ("Llego aqui")



##ALTERNATIVE FILEHANDLER

import ply.yacc as yacc
parser = yacc.yacc()
f = open("./"+arch , "r")
input = f.read()
parser.parse(input, debug=0)
output = open("Quads.mir", "w")
for x in QUADSlist:
    output.write(str(x.QUADcounter)+ "~" + str(x.operator) + "~" + str(x.LeftOperand)+ "~" + str(x.RightOperand) + "~" + str(x.result) + "\n")
output.close()
