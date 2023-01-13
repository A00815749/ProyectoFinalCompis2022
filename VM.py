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

def loadlocalmemory(processname):
    for elem in Tableof_functions[processname]['variables']:
        virtualaddr = Tableof_functions[processname]['variables'][elem]['virtualaddress']
        localmemory.simmemory[virtualaddr] = None # LOAD THE KEYS

def localsensor(value): # AS DEFINED
    try:
        localmemory.simmemory[value]
        return True
    except:
        return False

def globalsensor(value):
    try:
        GLOBALmemory.simmemory[value]
        return True
    except:
        ERROR("NO INSTANCE FOR THIS VALUE AT GLOBAL SCOPE ", str(value))


def isReadable(Variable, value):# CHECK IF IT CAN BE READ AS VARIABLE
    global Scopesensorglobal
    if Scopesensorglobal:
        if Variable < 3000 and Variable >= 1000:
            try:
                value = int(value)
            except:
                ERROR("TYPE MISMATCH WITH VARIABLE BLOCK ", value)
        elif Variable < 5000 and Variable >= 3000:
            try:
                value = float(value)
            except: 
                ERROR("TYPE MISMATCH WITH VARIABLE BLOCK ", value)
        elif Variable < 7000 and Variable >= 5000:
            if len(value) > 1:
                ERROR("NOT A CHAR WITH VARIABLE BLOCK ", value)
            value = str(value)
        else:
            ERROR("TYPE MISMATCH WITH VARIABLE BLOCK ", value)


def changeofcontextnext(value): # METHOD TO CHECK IF IT IS THE LAST LOCAL VARIABLE BEFORE CONTEXT CHANGE
    global STACKofexecs
    try:
        STACKofexecs[-1].simmemory[value]
        return True
    except:
        return False


for x in Tableof_functions.keys(): # GET THE THE NAME OF THE MAIN PROGRAM FUNCTION
    if Tableof_functions[x]['scopecontext'] == 'g':
        programname = x

GLOBALmemory = Memorysimulacra()
localmemory = Memorysimulacra()

for elem in Tableof_functions[programname]['variables']: ## READ THE GLOBAL MEMORY
    vmaddress = Tableof_functions[programname]['variables'][elem]['virtualaddress'] # GET THE REPRESENTATIVE BLOCKS IN THE TABLE OF FUNCTIONS OF THE COMPILER
    GLOBALmemory.simmemory[vmaddress] = None # SAVE THE KEYS, CURRENTLY EMPTY

for elem2 in ConstantVar_set: # LOAD THE DIRECT CONSTANT VALUES TO THE MEMORY
    virtualaddr = ConstantVar_set[elem2]
    if virtualaddr < 23000:
        GLOBALmemory.simmemory[virtualaddr]=int(elem2)
    elif virtualaddr < 25000:
        GLOBALmemory.simmemory[virtualaddr]=float(elem2)
    elif virtualaddr < 27000:
        GLOBALmemory.simmemory[virtualaddr]=str(elem2) 


while PROCCOUNTER <= len(Quads):
    #PARSE THE INTERMEDIATE CODE DOCUMENT INTO ELEMENTS
    (Qcounter,operator,leftoperand,rightoperand,result) = Quads[PROCCOUNTER].split("~")
    
    
    #DEBUG TOOL
    #print(PROCCOUNTER+1, "<=== QUADRUPLE WE ARE GOING TO WORK WITH")




    ####################### VIRTUAL MACHINE CONSOLE APPLICATION LOGIC STARTS HERE #######################
    # OPERATOR BEING "  EQUAL   =  "
    if int(operator) == 11:
        if Scopesensorglobal: # GLOBAL VARIABLE OR VALUES ASSIGNED TO GLOBAL VARIABLE
            if (GLOBALmemory.simmemory[int(leftoperand)] != None): # IS THERE SOMETHING TO ASSIGN?
                GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)]
            else:
                ERROR("LEFT OPERAND IS NULL/EMPTY","ASSIGN = OPERATOR QUAD")
        else:
            try: # LOCAL VARIABLE OR VALUE TO LOCAL VARIABLE
                if(localmemory.simmemory[int(leftoperand) ] != None):
                    localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)]
                else:
                    ERROR("LEFT OPERAND IS NULL/EMPTY","ASSIGN = OPERATOR QUAD")
            except: # GLOBAL VARIABLE TO LOCAL
                if(GLOBALmemory.simmemory[int(leftoperand)]!= None):
                    localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)]
                else:
                    ERROR("LEFT OPERAND IS NULL/EMPTY","ASSIGN = OPERATOR QUAD")


    # OPERATOR BEING "  SUM   +  "
    elif int(operator) == 1:
        if Scopesensorglobal:
            if(GLOBALmemory.simmemory[int(leftoperand)] != None and GLOBALmemory.simmemory[int(rightoperand)] != None): # CHECK IF BOTH ACTUALLY HAVE VALUES
                GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] + GLOBALmemory.simmemory[int(rightoperand)]
            else:
                ERROR("EITHER OPERAND IS NULL/EMPTY","SUM OPERATOR QUAD")
        else:
            if localsensor(int(leftoperand)) and localsensor (int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] + localmemory.simmemory[int(rightoperand)]
            elif localsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] + GLOBALmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] + localmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] + GLOBALmemory.simmemory[int(rightoperand)] # ACCOUNT FOR CONTEXT CHANGES
            else:
                ERROR("NULL VALUES IN THE SUM QUADS")
    
    # OPERATOR BEING "  TIMES   *  "
    elif int(operator) == 3:
        if Scopesensorglobal:
            if(GLOBALmemory.simmemory[int(leftoperand)] != None and GLOBALmemory.simmemory[int(rightoperand)] != None): # CHECK IF BOTH ACTUALLY HAVE VALUES
                GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] * GLOBALmemory.simmemory[int(rightoperand)]
            else:
                ERROR("EITHER OPERAND IS NULL/EMPTY","TIMES OPERATOR QUAD")
        else:
            if localsensor(int(leftoperand)) and localsensor (int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] * localmemory.simmemory[int(rightoperand)]
            elif localsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] * GLOBALmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] * localmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] * GLOBALmemory.simmemory[int(rightoperand)] # ACCOUNT FOR CONTEXT CHANGES
            else:
                ERROR("NULL VALUES THE TIMES QUADS")


    # OPERATOR BEING "  REST   -  "
    elif int(operator) == 2:
        if Scopesensorglobal:
            if(GLOBALmemory.simmemory[int(leftoperand)] != None and GLOBALmemory.simmemory[int(rightoperand)] != None): # CHECK IF BOTH ACTUALLY HAVE VALUES
                GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] - GLOBALmemory.simmemory[int(rightoperand)]
            else:
                ERROR("EITHER OPERAND IS NULL/EMPTY","REST OPERATOR QUAD")
        else:
            if len(STACKofexecs) > 0:
                if changeofcontextnext(int(leftoperand)) and changeofcontextnext(int(rightoperand)):
                    STACKofexecs[-1].simmemory[int(result)] = STACKofexecs[-1].simmemory[int(leftoperand)] - STACKofexecs[-1].simmemory[int(rightoperand)]
                elif changeofcontextnext(int(leftoperand)) and globalsensor(int(rightoperand)):
                    STACKofexecs[-1].simmemory[int(result)] = STACKofexecs[-1].simmemory[int(leftoperand)] - GLOBALmemory.simmemory[int(rightoperand)]
                elif globalsensor(int(leftoperand)) and changeofcontextnext(int(rightoperand)):
                    STACKofexecs[-1].simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] - STACKofexecs[-1].simmemory[int(rightoperand)]
                elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                    STACKofexecs[-1].simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] - GLOBALmemory.simmemory[int(rightoperand)] # ACCOUNT FOR CONTEXT CHANGES
                else:
                    ERROR("NULL VALUES IN THE REST QUADS")
            else:
                if localsensor(int(leftoperand)) and localsensor (int(rightoperand)):
                    localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] - localmemory.simmemory[int(rightoperand)]
                elif localsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                    localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] - GLOBALmemory.simmemory[int(rightoperand)]
                elif globalsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                    localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] - localmemory.simmemory[int(rightoperand)]
                elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                    localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] - GLOBALmemory.simmemory[int(rightoperand)] # ACCOUNT FOR CONTEXT CHANGES
                else:
                    ERROR("NULL VALUES IN THE REST QUADS")

    # OPERATOR BEING "  DIVIDE   /  "
    elif int(operator) == 4:
        if Scopesensorglobal:
            if(GLOBALmemory.simmemory[int(leftoperand)] != None and GLOBALmemory.simmemory[int(rightoperand)] != None): # CHECK IF BOTH ACTUALLY HAVE VALUES
                if type(GLOBALmemory.simmemory[int(leftoperand)]) == int and type(GLOBALmemory.simmemory[int(rightoperand)]) == int: # CHECK IF WE ARE DEALING WITH INT VARIABLES OR FLOAT VARIABLES
                    GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] // GLOBALmemory.simmemory[int(rightoperand)] #FLOOR DIVISION
                else:
                    GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] / GLOBALmemory.simmemory[int(rightoperand)] #NORMAL DIVISION
            else:
                ERROR("EITHER OPERAND IS NULL/EMPTY","DIVIDE OPERATOR QUAD")
        else: 
            if localsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                if type(localmemory.simmemory[int(leftoperand)]) == int and type(localmemory.simmemory[int(rightoperand)]) == int:
                    localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] // localmemory.simmemory[int(rightoperand)]
                else:
                    localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] / localmemory.simmemory[int(rightoperand)]
            elif localsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                if type(localmemory.simmemory[int(leftoperand)]) == int and type(GLOBALmemory.simmemory[int(rightoperand)]) == int:
                    localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] // GLOBALmemory.simmemory[int(rightoperand)]
                else:
                    localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] / GLOBALmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                if type(GLOBALmemory.simmemory[int(leftoperand)]) == int and type(localmemory.simmemory[int(rightoperand)]) == int:
                    localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] // localmemory.simmemory[int(rightoperand)]
                else:
                    localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] / localmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                if type(GLOBALmemory.simmemory[int(leftoperand)]) == int and type(GLOBALmemory.simmemory[int(rightoperand)]) == int:
                    localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] // GLOBALmemory.simmemory[int(rightoperand)]
                else:
                    localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] / GLOBALmemory.simmemory[int(rightoperand)]
            else:
                ERROR("NULL VALUES IN THE DIVIDE QUADS")

    # OPERATOR BEING "  READ  "
    elif int(operator)==12:
        if Scopesensorglobal:
            value = input() # READ FROM THE USER
            isReadable(int(result),value)
            GLOBALmemory.simmemory[int(result)] = value # SAVE IT IN MEMORY
        else:
            value = input() # READ FROM THE USER
            isReadable(int(result),value)
            if localsensor(int(result)):
                localmemory.simmemory[int(result)] = value
            elif globalsensor(int(result)):
                GLOBALmemory.simmemory[int(result)] = value # SAVE IT IN MEMORY


    # OPERATOR BEING "  WRITE  "
    elif int(operator) == 13:
        if result[0] == '"':
            print(result[1:-1]) # PRINT THE ENTIRE COMMENT IN ONE GO
        elif Scopesensorglobal:
            print(GLOBALmemory.simmemory[int(result)])
        else:
            try:
                print(localmemory.simmemory[int(result)])
            except:
                print(GLOBALmemory.simmemory[int(result)])
    

    # OPERATOR BEING "  GREATER    >  "

    elif int(operator) == 5 :
        if Scopesensorglobal:
            if GLOBALmemory.simmemory(int(leftoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","GREATER OPERATOR QUAD")
            if GLOBALmemory.simmemory(int(rightoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","GREATER OPERATOR QUAD")
            GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] > GLOBALmemory.simmemory[int(rightoperand)]
        else:
            if localsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] > localmemory.simmemory[int(rightoperand)]
            elif localsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] > GLOBALmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] > localmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] > GLOBALmemory.simmemory[int(rightoperand)] # ACCOUNT FOR CONTEXT CHANGES
            else:
                ERROR("NULL VALUES IN THE > QUADS")


    # OPERATOR BEING "  GREATERAND    >=  "

    elif int(operator) == 6 :
        if Scopesensorglobal:
            if GLOBALmemory.simmemory(int(leftoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","GREATERAND OPERATOR QUAD")
            if GLOBALmemory.simmemory(int(rightoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","GREATERAND OPERATOR QUAD")
            GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] >= GLOBALmemory.simmemory[int(rightoperand)]
        else:
            if localsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] >= localmemory.simmemory[int(rightoperand)]
            elif localsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] >= GLOBALmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] >= localmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] >= GLOBALmemory.simmemory[int(rightoperand)] # ACCOUNT FOR CONTEXT CHANGES
            else:
                ERROR("NULL VALUES IN THE >= QUADS")


    # OPERATOR BEING "  LESSER    <  "
    
    elif int(operator) == 7 :
        if Scopesensorglobal:
            if GLOBALmemory.simmemory(int(leftoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","LESSER OPERATOR QUAD")
            if GLOBALmemory.simmemory(int(rightoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","LESSER OPERATOR QUAD")
            GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] < GLOBALmemory.simmemory[int(rightoperand)]
        else:
            if localsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] < localmemory.simmemory[int(rightoperand)]
            elif localsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] < GLOBALmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] < localmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] < GLOBALmemory.simmemory[int(rightoperand)] # ACCOUNT FOR CONTEXT CHANGES
            else:
                ERROR("NULL VALUES IN THE < QUADS")


    # OPERATOR BEING "  LESSERAND    <=  "
    
    elif int(operator) == 8 :
        if Scopesensorglobal:
            if GLOBALmemory.simmemory(int(leftoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","LESSERAND OPERATOR QUAD")
            if GLOBALmemory.simmemory(int(rightoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","LESSERAND OPERATOR QUAD")
            GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] <= GLOBALmemory.simmemory[int(rightoperand)]
        else:
            if localsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] <= localmemory.simmemory[int(rightoperand)]
            elif localsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] <= GLOBALmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] <= localmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] <= GLOBALmemory.simmemory[int(rightoperand)] # ACCOUNT FOR CONTEXT CHANGES
            else:
                ERROR("NULL VALUES IN THE <= QUADS")


    # OPERATOR BEING "  SAME    ==  "
    
    elif int(operator) == 9 :
        if Scopesensorglobal:
            if GLOBALmemory.simmemory(int(leftoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","SAME OPERATOR QUAD")
            if GLOBALmemory.simmemory(int(rightoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","SAME OPERATOR QUAD")
            GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] == GLOBALmemory.simmemory[int(rightoperand)]
        else:
            if localsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] == localmemory.simmemory[int(rightoperand)]
            elif localsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] == GLOBALmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] == localmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] == GLOBALmemory.simmemory[int(rightoperand)] # ACCOUNT FOR CONTEXT CHANGES
            else:
                ERROR("NULL VALUES IN THE == QUADS")


    # OPERATOR BEING "  NOTSAME    <>  "
    
    elif int(operator) == 10 :
        if Scopesensorglobal:
            if GLOBALmemory.simmemory(int(leftoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","NOTSAME OPERATOR QUAD")
            if GLOBALmemory.simmemory(int(rightoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","NOTSAME OPERATOR QUAD")
            GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] != GLOBALmemory.simmemory[int(rightoperand)]
        else:
            if localsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] != localmemory.simmemory[int(rightoperand)]
            elif localsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] != GLOBALmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] != localmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] != GLOBALmemory.simmemory[int(rightoperand)] # ACCOUNT FOR CONTEXT CHANGES
            else:
                ERROR("NULL VALUES IN THE <> QUADS")

    
    # OPERATOR BEING "  AND  "
    
    elif int(operator) == 14 :
        if Scopesensorglobal:
            if GLOBALmemory.simmemory(int(leftoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","AND OPERATOR QUAD")
            if GLOBALmemory.simmemory(int(rightoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","AND OPERATOR QUAD")
            GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] and GLOBALmemory.simmemory[int(rightoperand)]
        else:
            if localsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] and localmemory.simmemory[int(rightoperand)]
            elif localsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] and GLOBALmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] and localmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] and GLOBALmemory.simmemory[int(rightoperand)] # ACCOUNT FOR CONTEXT CHANGES
            else:
                ERROR("NULL VALUES IN THE AND QUADS")

    
    # OPERATOR BEING "  OR  "

    elif int(operator) == 15 :
        if Scopesensorglobal:
            if GLOBALmemory.simmemory(int(leftoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","AND OPERATOR QUAD")
            if GLOBALmemory.simmemory(int(rightoperand)) == None:
                ERROR("NULL VALUE IN OPERAND","AND OPERATOR QUAD")
            GLOBALmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] or GLOBALmemory.simmemory[int(rightoperand)]
        else:
            if localsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] or localmemory.simmemory[int(rightoperand)]
            elif localsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = localmemory.simmemory[int(leftoperand)] or GLOBALmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and localsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] or localmemory.simmemory[int(rightoperand)]
            elif globalsensor(int(leftoperand)) and globalsensor(int(rightoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)] or GLOBALmemory.simmemory[int(rightoperand)] # ACCOUNT FOR CONTEXT CHANGES
            else:
                ERROR("NULL VALUES IN THE OR QUADS")

    # OPERATOR BEING "  GOTO  "
    elif int(operator) == 16:
        PROCCOUNTER = int(result) - 2 # LOAD THE JUMP, ADJUSTING WITH THE OFFSET


    # OPERATOR BEING "  GOTOF  "
    elif int(operator) == 17:
        if Scopesensorglobal:
            if GLOBALmemory.simmemory[int(leftoperand)] == None:
                ERROR("NULL VALUE IN OPERAND","GOTOF OPERATOR QUAD")
            if not GLOBALmemory.simmemory[int(leftoperand)]:
                PROCCOUNTER=int(result) - 2 # DO THE JUMP ONLY IF THE LEFTOPERAND BOOLEAN IS FALSE
        else:
            if localsensor(int(leftoperand)):
                if localmemory.simmemory[int(leftoperand)] == None:
                    ERROR("NULL VALUE IN OPERAND","GOTOF OPERATOR QUAD")
                if not localmemory.simmemory[int(leftoperand)]:
                    PROCCOUNTER=int(result)- 2 # DO THE JUMP ONLY IF THE LEFTOPERAND BOOLEAN IS FALSE
            elif globalsensor(int(leftoperand)):
                if GLOBALmemory.simmemory[int(leftoperand)] == None:
                    ERROR("NULL VALUE IN OPERAND","GOTOF OPERATOR QUAD")
                if not GLOBALmemory.simmemory[int(leftoperand)]:
                    PROCCOUNTER=int(result)- 2 # DO THE JUMP ONLY IF THE LEFTOPERAND BOOLEAN IS FALSE


    # OPERATOR BEING "  GOTOV  "
    elif int(operator) == 18:
        if Scopesensorglobal:
            if GLOBALmemory.simmemory[int(leftoperand)] == None:
                ERROR("NULL VALUE IN OPERAND","GOTOV OPERATOR QUAD")
            if GLOBALmemory.simmemory[int(leftoperand)]:
                PROCCOUNTER=int(result) - 2 # DO THE JUMP ONLY IF THE LEFTOPERAND BOOLEAN IS TRUE
        else:
            if localsensor(int(leftoperand)):
                if localmemory.simmemory[int(leftoperand)] == None:
                    ERROR("NULL VALUE IN OPERAND","GOTOV OPERATOR QUAD")
                if localmemory.simmemory[int(leftoperand)]:
                    PROCCOUNTER=int(result)- 2 # DO THE JUMP ONLY IF THE LEFTOPERAND BOOLEAN IS TRUE
            elif globalsensor(int(leftoperand)):
                if GLOBALmemory.simmemory[int(leftoperand)] == None:
                    ERROR("NULL VALUE IN OPERAND","GOTOV OPERATOR QUAD")
                if GLOBALmemory.simmemory[int(leftoperand)]:
                    PROCCOUNTER=int(result)- 2 # DO THE JUMP ONLY IF THE LEFTOPERAND BOOLEAN IS TRUE


    # OPERATOR BEING "  ERA  "
    elif int(operator)== 19:
        if localmemory is not None: # IS IT NOT EMPTY?
            STACKofexecs.append(localmemory)
            localmemory = Memorysimulacra()
            loadlocalmemory(result) # START THE FUNCTION NAME
        else:
            localmemory = Memorysimulacra()
            loadlocalmemory(result)

    # OPERATOR BEING "  VER  "
    elif int(operator)==20:
        if Scopesensorglobal:
            if GLOBALmemory.simmemory[int(leftoperand)]>= GLOBALmemory.simmemory[int(result)] or GLOBALmemory.simmemory[int(leftoperand)] < 0:
                ERROR ("VECTOR INDEX OUT OF BOUNDS ",leftoperand)
        else:
            if localsensor(int(leftoperand)):
                if localmemory.simmemory[int(leftoperand)]>= GLOBALmemory.simmemory[int(result)] or GLOBALmemory.simmemory[int(rightoperand)] < 0:
                    ERROR ("VECTOR INDEX OUT OF BOUNDS ",leftoperand)
            elif globalsensor(int(leftoperand)):
                if GLOBALmemory.simmemory[int(leftoperand)]>= GLOBALmemory.simmemory(int(result)) or GLOBALmemory.simmemory[int(rightoperand)]< 0:
                    ERROR ("VECTOR INDEX OUT OF BOUNDS ",leftoperand)

    # OPERATOR BEING "  ENDPROC  "
    elif int(operator) == 21:
        if STACKofexecs:
            localmemory=STACKofexecs.pop() # POP THE STACK OF EXECUTIONS
        else:
            Scopesensorglobal = True # CHANGE THE CONTEZT
        PROCCOUNTER = PROCList.pop()
    
    # OPERATOR BEING "  PARAMS  "
    elif int(operator)==22:
        if Scopesensorglobal:
            localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)]
        else:
            if changeofcontextnext(int(leftoperand)):
                localmemory.simmemory[int(result)] = STACKofexecs[-1].simmemory[int(leftoperand)]
            elif globalsensor(int(leftoperand)):
                localmemory.simmemory[int(result)] = GLOBALmemory.simmemory[int(leftoperand)]

    # OPERATOR BEING "  GOSUB  "
    elif int(operator)==23:
        Scopesensorglobal=False # WE ARE IN LOCAL FUNCS 
        PROCList.append(PROCCOUNTER+1) # GET ME THE FUNCTION QUADS
        PROCCOUNTER = int(result)-2 # JUMP TO THE FUNCTION

    # OPERATOR BEING "  RETURN  "
    elif int(operator)==30:
        if localsensor(int(leftoperand)):
            GLOBALmemory.simmemory[int(result)]= localmemory.simmemory[int(leftoperand)]
        elif globalsensor(int(leftoperand)):
            GLOBALmemory.simmemory[int(result)]= GLOBALmemory.simmemory[int(leftoperand)]
        if not STACKofexecs:
            Scopesensorglobal = True
        else:
            localmemory=STACKofexecs.pop()
        PROCCOUNTER = PROCList.pop() - 1 # JUMP TO THE ACTUAL ADDRESS

    PROCCOUNTER+=1
    if(PROCCOUNTER==len(Quads)):
        print("Llego al final de la lista de Quadruplos")
        sys.exit()