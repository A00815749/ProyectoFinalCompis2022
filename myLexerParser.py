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

#The Operation number that will be stored inside the quads product indicating which type of operation the quads is

##### PYTHON LISTS, MUTABLE, ORDER OF ELEMENTS INHERENT IN THEIR APPLICATION, CAN FUNCTION AS STACKS #############


######### MY STACKS, USING THE PYTHON LISTS AND POP() TO SIMULATE THE STACK BEHAVIOR


###### SENSORS, CHECKING THE SCOPE (CONTEXT) OF THE VARIABLES, & COUNTERS ############

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

#### SEMANTIC CUBE CLASS OBJECT, A SENSOR THAR CHECKS OPERATIONS BETWEEN THE SIMPLE DATATYPES #############
semantics = Semanticcube()

########################################################################################################################################

#---------------------------------------------------NEURALGIC FUNCTIONS AUX ------------------------------------------------------------
#---------------------------------------------------NEURALGIC FUNCTIONS AUX ------------------------------------------------------------
#---------------------------------------------------NEURALGIC FUNCTIONS AUX ------------------------------------------------------------
#---------------------------------------------------NEURALGIC FUNCTIONS AUX ------------------------------------------------------------
#---------------------------------------------------NEURALGIC FUNCTIONS AUX ------------------------------------------------------------

########### GLOBAL AUXILIAR METHODS FOR NEURALGIC POINTS MANIPULATIONS ############



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
    program : PROGRAM ID SEMICOLON varsgl modules MAIN LEFTPAR RIGHTPAR LEFTBR statutes RIGHTBR
    '''
    print ('Llego al final de la gramatica, aceptado \n')



####### VARIABLES DECLARATION HANDLING ##########

def p_VARSGL(p):
    '''
    varsgl : VARS vars
            | empty
    '''

def p_VARS(p):
    '''
    vars : typing COLON ID varsarr varsmul vars
            | empty
    '''

def p_VARSARR(p):
    '''
    varsarr : LEFTSQR CTEINT RIGHTSQR
        | empty
    '''

def p_VARSMUL(p):
    '''
    varsmul : COMMA ID varsarr varsmul
            | SEMICOLON
    '''


####### MODULES HABDLING ##########

def p_MODULES(p):
    '''
    modules : FUNCTION functype ID funcparam
            | empty
    '''

def p_FUNCTYPE(p):
    '''
    functype : VOID
            | typing
    '''

def p_FUNCPARAM(p):
    '''
    funcparam : LEFTPAR parameters RIGHTPAR SEMICOLON varsgl LEFTBR statutes RIGHTBR modules
    '''

def p_TYPING(p):
    '''
    typing : INT
            | FLOAT
            | CHAR
    '''

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



#def p_FUNCTYPE(p):
#    '''
#    specialfuncs : empty
#            | empty
#    '''



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
    elsing : ELSE LEFTBR STATUTES RIGHTBR
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
    boolexp : arithexp arithexp1
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
    print (p)
    sys.exit()


##ALTERNATIVE FILEHANDLER
#
#import ply.yacc as yacc
#parser = yacc.yacc()
#f = open("./"+arch , "r")
#input = f.read()
#parser.parse(input, debug=0)
#output = open("Quads.mir", "w")
#for x in QUADSlist:
#    output.write(str(x.QUADcounter)+ "~" + str(x.operator) + "~" + str(x.LeftOperand)+ "~" + str(x.RightOperand) + "~" + str(x.result) + "\n")
#output.close()
#