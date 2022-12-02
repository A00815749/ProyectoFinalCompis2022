class Semanticcube:
    def __init__ (self):
        # Dict for Our Symbols for the Rlike lang
        self.operatorsymbol = {
            1: '+',
            2: '-',
            3: '*',
            4: '/',
            5: '<',
            6: '<=',
            7: '>',
            8: '>=',
            9: '==',
            10: '<>',
            11: '&',
            12: '|',
            13: '=',
            14 :'and'
        }

        # dict types for the lang
        self.types = {
            1: 'int',
            2: 'float',
            3: 'char',
            4: 'bool',
            5: 'CTEINT', 
            6: 'CTEFLOAT', 
            7: 'CTECHAR',  
            8: 'CTESTRING',
            9: 'ERROR',
        }

        self.commonsensor = {
            #By order, starting with types
            #Integer left hand
            self.types[1]: {
                #int right hand
                self.types[1]: {
                    self.operatorsymbol[1] : self.types[1], #integer adding integer results in integer, and so on and on
                    self.operatorsymbol[2] : self.types[1],
                    self.operatorsymbol[3] : self.types[1],
                    self.operatorsymbol[4] : self.types[1],
                    self.operatorsymbol[5] : self.types[4],
                    self.operatorsymbol[6] : self.types[4],
                    self.operatorsymbol[7] : self.types[4],
                    self.operatorsymbol[8] : self.types[4],
                    self.operatorsymbol[9] : self.types[4],
                    self.operatorsymbol[10] : self.types[4],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[1],
                    self.operatorsymbol[14] : self.types[9]
                },
                # float right hand
                self.types[2]:{
                    self.operatorsymbol[1] : self.types[2],
                    self.operatorsymbol[2] : self.types[2],
                    self.operatorsymbol[3] : self.types[2],
                    self.operatorsymbol[4] : self.types[2],
                    self.operatorsymbol[5] : self.types[4],
                    self.operatorsymbol[6] : self.types[4],
                    self.operatorsymbol[7] : self.types[4],
                    self.operatorsymbol[8] : self.types[4],
                    self.operatorsymbol[9] : self.types[4],
                    self.operatorsymbol[10] : self.types[4],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[9],
                    self.operatorsymbol[14] : self.types[9]
                },

                #char right hand
                self.types[3]:{
                    self.operatorsymbol[1] : self.types[9],
                    self.operatorsymbol[2] : self.types[9],
                    self.operatorsymbol[3] : self.types[9],
                    self.operatorsymbol[4] : self.types[9],
                    self.operatorsymbol[5] : self.types[9],
                    self.operatorsymbol[6] : self.types[9],
                    self.operatorsymbol[7] : self.types[9],
                    self.operatorsymbol[8] : self.types[9],
                    self.operatorsymbol[9] : self.types[9],
                    self.operatorsymbol[10] : self.types[9],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[9],
                    self.operatorsymbol[14] : self.types[9]
                },

                #bool right hand
                self.types[4]:{
                    self.operatorsymbol[1] : self.types[9],
                    self.operatorsymbol[2] : self.types[9],
                    self.operatorsymbol[3] : self.types[9],
                    self.operatorsymbol[4] : self.types[9],
                    self.operatorsymbol[5] : self.types[9],
                    self.operatorsymbol[6] : self.types[9],
                    self.operatorsymbol[7] : self.types[9],
                    self.operatorsymbol[8] : self.types[9],
                    self.operatorsymbol[9] : self.types[9],
                    self.operatorsymbol[10] : self.types[9],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[9],
                    self.operatorsymbol[14] : self.types[9]
                },
            },

            # Float left hand
            self.types[2]: {
                #Int right hand
                self.types[1]: {
                    self.operatorsymbol[1] : self.types[2], 
                    self.operatorsymbol[2] : self.types[2],
                    self.operatorsymbol[3] : self.types[2],
                    self.operatorsymbol[4] : self.types[2],
                    self.operatorsymbol[5] : self.types[4],
                    self.operatorsymbol[6] : self.types[4],
                    self.operatorsymbol[7] : self.types[4],
                    self.operatorsymbol[8] : self.types[4],
                    self.operatorsymbol[9] : self.types[4],
                    self.operatorsymbol[10] : self.types[4],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[9],
                    self.operatorsymbol[14] : self.types[9]
                },
                # float right hand
                self.types[2]:{
                    self.operatorsymbol[1] : self.types[2],
                    self.operatorsymbol[2] : self.types[2],
                    self.operatorsymbol[3] : self.types[2],
                    self.operatorsymbol[4] : self.types[2],
                    self.operatorsymbol[5] : self.types[4],
                    self.operatorsymbol[6] : self.types[4],
                    self.operatorsymbol[7] : self.types[4],
                    self.operatorsymbol[8] : self.types[4],
                    self.operatorsymbol[9] : self.types[4],
                    self.operatorsymbol[10] : self.types[4],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[2],
                    self.operatorsymbol[14] : self.types[9]
                },

                #char right hand
                self.types[3]:{
                    self.operatorsymbol[1] : self.types[9],
                    self.operatorsymbol[2] : self.types[9],
                    self.operatorsymbol[3] : self.types[9],
                    self.operatorsymbol[4] : self.types[9],
                    self.operatorsymbol[5] : self.types[9],
                    self.operatorsymbol[6] : self.types[9],
                    self.operatorsymbol[7] : self.types[9],
                    self.operatorsymbol[8] : self.types[9],
                    self.operatorsymbol[9] : self.types[9],
                    self.operatorsymbol[10] : self.types[9],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[9],
                    self.operatorsymbol[14] : self.types[9]
                },

                #bool right hand
                self.types[4]:{
                    self.operatorsymbol[1] : self.types[9],
                    self.operatorsymbol[2] : self.types[9],
                    self.operatorsymbol[3] : self.types[9],
                    self.operatorsymbol[4] : self.types[9],
                    self.operatorsymbol[5] : self.types[9],
                    self.operatorsymbol[6] : self.types[9],
                    self.operatorsymbol[7] : self.types[9],
                    self.operatorsymbol[8] : self.types[9],
                    self.operatorsymbol[9] : self.types[9],
                    self.operatorsymbol[10] : self.types[9],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[9],
                    self.operatorsymbol[14] : self.types[9]
                },
            },

            # char left hand
            self.types[3]: {
                # Int right hand
                self.types[1]: {
                    self.operatorsymbol[1] : self.types[9],
                    self.operatorsymbol[2] : self.types[9],
                    self.operatorsymbol[3] : self.types[9],
                    self.operatorsymbol[4] : self.types[9],
                    self.operatorsymbol[5] : self.types[9],
                    self.operatorsymbol[6] : self.types[9],
                    self.operatorsymbol[7] : self.types[9],
                    self.operatorsymbol[8] : self.types[9],
                    self.operatorsymbol[9] : self.types[9],
                    self.operatorsymbol[10] : self.types[9],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[9],
                    self.operatorsymbol[14] : self.types[9]
                },
                # float right hand
                self.types[2]:{
                    self.operatorsymbol[1] : self.types[9],
                    self.operatorsymbol[2] : self.types[9],
                    self.operatorsymbol[3] : self.types[9],
                    self.operatorsymbol[4] : self.types[9],
                    self.operatorsymbol[5] : self.types[9],
                    self.operatorsymbol[6] : self.types[9],
                    self.operatorsymbol[7] : self.types[9],
                    self.operatorsymbol[8] : self.types[9],
                    self.operatorsymbol[9] : self.types[9],
                    self.operatorsymbol[10] : self.types[9],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[9],
                    self.operatorsymbol[14] : self.types[9]
                },

                #char right hand
                self.types[3]:{
                    self.operatorsymbol[1] : self.types[9],
                    self.operatorsymbol[2] : self.types[9],
                    self.operatorsymbol[3] : self.types[9],
                    self.operatorsymbol[4] : self.types[9],
                    self.operatorsymbol[5] : self.types[9],
                    self.operatorsymbol[6] : self.types[9],
                    self.operatorsymbol[7] : self.types[9],
                    self.operatorsymbol[8] : self.types[9],
                    self.operatorsymbol[9] : self.types[4],
                    self.operatorsymbol[10] : self.types[4],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[3],
                    self.operatorsymbol[14] : self.types[9]
                },

                #bool right hand
                self.types[4]:{
                    self.operatorsymbol[1] : self.types[9],
                    self.operatorsymbol[2] : self.types[9],
                    self.operatorsymbol[3] : self.types[9],
                    self.operatorsymbol[4] : self.types[9],
                    self.operatorsymbol[5] : self.types[9],
                    self.operatorsymbol[6] : self.types[9],
                    self.operatorsymbol[7] : self.types[9],
                    self.operatorsymbol[8] : self.types[9],
                    self.operatorsymbol[9] : self.types[9],
                    self.operatorsymbol[10] : self.types[9],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[9],
                    self.operatorsymbol[14] : self.types[9]
                },
            },

            #bool left hand
            self.types[4]: {
                #Int right hand
                self.types[1]: {
                    self.operatorsymbol[1] : self.types[9],  
                    self.operatorsymbol[2] : self.types[9],
                    self.operatorsymbol[3] : self.types[9],
                    self.operatorsymbol[4] : self.types[9],
                    self.operatorsymbol[5] : self.types[9],
                    self.operatorsymbol[6] : self.types[9],
                    self.operatorsymbol[7] : self.types[9],
                    self.operatorsymbol[8] : self.types[9],
                    self.operatorsymbol[9] : self.types[9],
                    self.operatorsymbol[10] : self.types[9],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[9],
                    self.operatorsymbol[14] : self.types[9]
                },
                # float right hand
                self.types[2]:{
                    self.operatorsymbol[1] : self.types[9],
                    self.operatorsymbol[2] : self.types[9],
                    self.operatorsymbol[3] : self.types[9],
                    self.operatorsymbol[4] : self.types[9],
                    self.operatorsymbol[5] : self.types[9],
                    self.operatorsymbol[6] : self.types[9],
                    self.operatorsymbol[7] : self.types[9],
                    self.operatorsymbol[8] : self.types[9],
                    self.operatorsymbol[9] : self.types[9],
                    self.operatorsymbol[10] : self.types[9],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[9],
                    self.operatorsymbol[14] : self.types[9]
                },

                #char right hand
                self.types[3]:{
                    self.operatorsymbol[1] : self.types[9],
                    self.operatorsymbol[2] : self.types[9],
                    self.operatorsymbol[3] : self.types[9],
                    self.operatorsymbol[4] : self.types[9],
                    self.operatorsymbol[5] : self.types[9],
                    self.operatorsymbol[6] : self.types[9],
                    self.operatorsymbol[7] : self.types[9],
                    self.operatorsymbol[8] : self.types[9],
                    self.operatorsymbol[9] : self.types[9],
                    self.operatorsymbol[10] : self.types[9],
                    self.operatorsymbol[11] : self.types[9],
                    self.operatorsymbol[12] : self.types[9],
                    self.operatorsymbol[13] : self.types[9],
                    self.operatorsymbol[14] : self.types[9]
                },

                #bool right hand
                self.types[4]:{
                    self.operatorsymbol[1] : self.types[9],
                    self.operatorsymbol[2] : self.types[9],
                    self.operatorsymbol[3] : self.types[9],
                    self.operatorsymbol[4] : self.types[9],
                    self.operatorsymbol[5] : self.types[4],
                    self.operatorsymbol[6] : self.types[4],
                    self.operatorsymbol[7] : self.types[4],
                    self.operatorsymbol[8] : self.types[4],
                    self.operatorsymbol[9] : self.types[4],
                    self.operatorsymbol[10] : self.types[4],
                    self.operatorsymbol[11] : self.types[4],
                    self.operatorsymbol[12] : self.types[4],
                    self.operatorsymbol[13] : self.types[4],
                    self.operatorsymbol[14] : self.types[4]
                },
            },
        }

    # function to get the semantic check type
    def getType(self, left, right, operator):
        return self.commonsensor[left][right][operator]

    #Checking with printf
    def printcheck(self, left, right, operator):
        print("Expected type for the quadruple provided is " + self.getType(left,right,operator))
        