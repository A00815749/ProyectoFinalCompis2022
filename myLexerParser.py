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




#The Operation number that will be stored inside the quads product indicating which type of operation the quads is

##### PYTHON LISTS, MUTABLE, ORDER OF ELEMENTS INHERENT IN THEIR APPLICATION, CAN FUNCTION AS STACKS #############
QUADSlist = []
GLOBALnames = [] # Storing names in global scope, using lists for ease of search, used as backup for the idnames in the sets used above
LOCALnames = [] # As above but in local scope


######### MY STACKS, USING THE PYTHON LISTS AND POP() TO SIMULATE THE STACK BEHAVIOR


###### SENSORS, CHECKING THE SCOPE (CONTEXT) OF THE VARIABLES, & COUNTERS ############
Scopesensor = 'g' # G for global or l for local
currenttyping = '' # Stores the typing, being either int float or char
currentfunctionname = ''


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
semantics = Semanticcube()

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


def addtotableoffunctions(idname, type, scopecontext, variables):
    if (idname in Tableof_functions):
        errorhandler(1)
    elif (idname in GLOBALnames):
        errorhandler(2)
    else:
        Tableof_functions[idname] = {'type': type, 'scopecontext' : scopecontext, 'variables' : variables }
        GLOBALnames.append(idname)

def insertinVARStables(id,type):
    if (Scopesensor == 'g'):
        if (id in GLOBALnames):
            errorhandler(3, str(id + " " + type))
        if (id in GlobalVar_set):
            errorhandler(4,id)
        GlobalVar_set[id]= {'type' : type }
        GLOBALnames.append(id)
    else:
        if id in LOCALnames:
            errorhandler(3, str(id + " " + type))
        if id in LocalVar_set:
            errorhandler("varrepetida",id)
        LocalVar_set[id] = {'type' : type}
        LOCALnames.append(id)

def endandresetfunction():
    global Scopesensor, LocalVar_set,LOCALnames
    Scopesensor = 'g' # RETURN TO THE GLOBAL SCOPE TILL NEXT LOCAL CHANGE
    LocalVar_set = {} # EMPTY THE LOCAL VARIABLES
    LOCALnames = [] # EMPTY THE ORDERED USED NAMES






#### ERROR HABDLER IN AUXILIAR METHODS

#LIST OF ERRORS
# 1 = Function name is duplicated in the table of functions
# 2 = Backup simple set name indicates that the name called is duplicate, check the table of functions status
# 3 = Name trying to be used as variable name is used as a function name
# 4 = Duplicated variable name
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

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
    program : PROGRAM neuraltablefunctions SEMICOLON varsgl modules MAIN LEFTPAR RIGHTPAR LEFTBR statutes RIGHTBR
    '''
    print ('Llego al final de la gramatica, aceptado \n')
    #WHEN ENDING THE PROGRAM DELETE THE TABLE OF FUNCTIONS AND GLOBAL VAR TABLE
    #PROBABLY NOT TILL VIRTUAL MACHINE IS COMPLETE
    print(Tableof_functions)


def p_NEURALTABLEFUNCTIONS(p):
    '''
    neuraltablefunctions : ID
    '''
    #print (p[1]) #THE VALUE STORED IN ID
    addtotableoffunctions(p[1],'VOID',Scopesensor, GlobalVar_set)



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
    insertinVARStables(p[1],currenttyping)
    

def p_VARSARR(p):
    '''
    varsarr : LEFTSQR CTEINT RIGHTSQR
        | empty
    '''

def p_VARSMUL(p):
    '''
    varsmul : COMMA neuralinsertvar varsarr varsmul
            | SEMICOLON
    '''


####### MODULES HABDLING ##########

def p_MODULES(p):
    '''
    modules : FUNCTION functype neuralinsertfuncname funcparam
            | empty
    '''

def p_NEURALINSERTFUNCNAME(p):
    '''
    neuralinsertfuncname : ID
    '''
    global Scopesensor, currentfunctionname
    Scopesensor = 'l'
    currentfunctionname = p[1]
    GlobalVar_set[currentfunctionname]= {'type', currenttyping}
    addtotableoffunctions(currentfunctionname,currenttyping,Scopesensor,LocalVar_set)

def p_FUNCTYPE(p):
    '''
    functype : VOID
            | typing
    '''
    global currenttyping
    print(p[1])
    currenttyping = p[1]

def p_FUNCPARAM(p):
    '''
    funcparam : LEFTPAR parameters RIGHTPAR SEMICOLON varsgl LEFTBR statutes RIGHTBR neuralendfuncs modules
    '''

def p_NEURALENDFUNCS(p):
    '''
    neuralendfuncs : 
    '''
    endandresetfunction()

def p_TYPING(p):
    '''
    typing : INT
            | FLOAT
            | CHAR
    '''
    global currenttyping
    currenttyping = p[1] # STORE THE INT, FLOAT OR CHAR TOKEN FOR THE VARIABLE TYPE

def p_PARAMETERS(p):
    '''
    parameters : typing COLON ID idarray mulparams
            | empty
    '''

def p_MULPARAMS(p):
    '''
    mulparams : COMMA parameters
            | empty
    '''

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



def p_ASSIGN(p):
    '''
    assign : ID idarray EQUAL exp SEMICOLON 
    '''



# WRITING

def p_WRITING(p):
    '''
    writing : WRITE LEFTPAR auxwrite mulwrite RIGHTPAR SEMICOLON
    '''

def p_AUXWRITE(p):
    '''
    auxwrite : writetyping
            | exp
    '''

def p_WRITETYPING(p):
    '''
    writetyping : STRING
            | CTECHAR
    '''

def p_MULWRITE(p):
    '''
    mulwrite : COMMA auxwrite mulwrite
            | empty
    '''

# READING

def p_READING(p):
    '''
    reading : READ LEFTPAR ID idarray mulread RIGHTPAR SEMICOLON
    '''

def p_MULREAD(p):
    '''
    mulread : COMMA ID idarray mulread
            | empty
    '''

# RETURNING

def p_RETURNING(p):
    '''
    returning : RETURN LEFTPAR exp RIGHTPAR SEMICOLON
    '''


########### CYCLES AND DECISIONGS #############

# IFING

def p_IFING(p):
    '''
    ifing : IF LEFTPAR exp RIGHTPAR THEN LEFTBR statutes RIGHTBR elsing
    '''

def p_ELSING(p):
    '''
    elsing : ELSE LEFTBR statutes RIGHTBR
            | empty
    '''


# WHILING

def p_WHILING(p):
    '''
    whiling : WHILE LEFTPAR exp RIGHTPAR DO LEFTBR statutes RIGHTBR
    '''

# FORING

def p_FORING(p):
    '''
    foring : FOR ID idarray EQUAL exp TO exp DO LEFTBR statutes RIGHTBR
    '''



##### VARIABLES AND EXPRESSIONS HANDLING #####

def p_IDARRAY(p):
    '''
    idarray : LEFTSQR exp RIGHTSQR
            | empty
    '''


def p_EXP(p):
    '''
    exp : andexp exp1
    '''

def p_EXP1(p):
    '''
    exp1 : OR exp
        | empty
    '''

def p_ANDEXP(p):
    '''
    andexp : boolexp andexp1
    '''

def p_ANDEXP1(p):
    '''
    andexp1 : AND andexp
        | empty
    '''

def p_BOOLEXP(p):
    '''
    boolexp : arithexp boolexp1
    '''

def p_BOOLEXP1(p):
    '''
    boolexp1 : GREATER arithexp
        | GREATERAND arithexp
        | LESSER arithexp
        | LESSERAND arithexp
        | SAME arithexp
        | NOTSAME arithexp
        | NOT arithexp
        | empty
    '''

def p_ARITHEXP(p):
    '''
    arithexp : geoexp arithexp1
    '''

def p_ARITHEXP1(p):
    '''
    arithexp1 : PLUS arithexp
        | REST arithexp
        | empty
    '''

def p_GEOEXP(p):
    '''
    geoexp : finexp geoexp1
    '''

def p_GEOEXP1(p):
    '''
    geoexp1 : TIMES geoexp
        | DIVIDE geoexp
        | empty
    '''

def p_FINEXP(p):
    '''
    finexp : LEFTPAR exp RIGHTPAR
            | cteexp
    '''

def p_CTEEXP(p):
    '''
    cteexp : CTEINT
            | CTEFLOAT
            | CTECHAR
            | ID paramsexp
    '''


#FUNCTIONS WITH PARAMETERS CALL OR ARRAY CALL HANDLING 

def p_PARAMSEXP(p):
    '''
    paramsexp : LEFTPAR paramsexp2 RIGHTPAR
                | idarray
    '''

def p_PARAMSEXP2(p):
    '''
    paramsexp2 : exp auxparamsexp2
            | empty
    '''

def p_AUXPARAMSEXP2(p):
    '''
    auxparamsexp2 : COMMA exp auxparamsexp2
            | empty
    '''
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
#output = open("Quads.mir", "w")
#for x in QUADSlist:
#    output.write(str(x.QUADcounter)+ "~" + str(x.operator) + "~" + str(x.LeftOperand)+ "~" + str(x.RightOperand) + "~" + str(x.result) + "\n")
#output.close()
#