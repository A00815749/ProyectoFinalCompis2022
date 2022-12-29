
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'STRING ID PLUS REST TIMES DIVIDE GREATER GREATERAND LESSER LESSERAND SAME NOTSAME NOT EQUAL LEFTBR RIGHTBR LEFTPAR RIGHTPAR LEFTSQR RIGHTSQR COLON SEMICOLON COMMA CTEINT CTEFLOAT CTECHAR PROGRAM MAIN FUNCTION VARS INT FLOAT CHAR STR RETURN READ WRITE AND OR IF THEN ELSE WHILE DO FOR TO VOID TRUE FALSE MEDIA MEDIANA MODA VARIANZA STDEV PLOTXY\n    program : PROGRAM ID neuraltablefunctions SEMICOLON varsgl modules MAIN LEFTPAR RIGHTPAR LEFTBR statutes RIGHTBR\n    \n    neuraltablefunctions :\n    \n    varsgl : VARS vars\n            | empty\n    \n    vars : typing COLON ID varsarr varsmul vars\n            | empty\n    \n    varsarr : LEFTSQR CTEINT RIGHTSQR\n        | empty\n    \n    varsmul : COMMA ID varsarr varsmul\n            | SEMICOLON\n    \n    modules : FUNCTION functype ID funcparam\n            | empty\n    \n    functype : VOID\n            | typing\n    \n    funcparam : LEFTPAR parameters RIGHTPAR SEMICOLON varsgl LEFTBR statutes RIGHTBR modules\n    \n    typing : INT\n            | FLOAT\n            | CHAR\n    \n    parameters : typing COLON ID idarray mulparams\n            | empty\n    \n    mulparams : COMMA parameters\n            | empty\n    \n    statutes : assign statutesaux\n            | reading statutesaux\n            | writing statutesaux\n            | returning statutesaux\n            | ifing statutesaux\n            | whiling statutesaux\n            | foring statutesaux\n            | exp statutesaux\n            | specialfunc statutesaux\n    \n    statutesaux : statutes \n                | empty\n    \n    specialfunc : empty\n    \n    assign : ID idarray EQUAL exp SEMICOLON \n    \n    writing : WRITE LEFTPAR auxwrite mulwrite RIGHTPAR SEMICOLON\n    \n    auxwrite : writetyping\n            | exp\n    \n    writetyping : STRING\n            | CTECHAR\n    \n    mulwrite : COMMA auxwrite mulwrite\n            | empty\n    \n    reading : READ LEFTPAR ID idarray mulread RIGHTPAR SEMICOLON\n    \n    mulread : COMMA ID idarray mulread\n            | empty\n    \n    returning : RETURN LEFTPAR exp RIGHTPAR SEMICOLON\n    \n    ifing : IF LEFTPAR exp RIGHTPAR THEN LEFTBR statutes RIGHTBR elsing\n    \n    elsing : ELSE LEFTBR statutes RIGHTBR\n            | empty\n    \n    whiling : WHILE LEFTPAR exp RIGHTPAR DO LEFTBR statutes RIGHTBR\n    \n    foring : FOR ID idarray EQUAL exp TO exp DO LEFTBR statutes RIGHTBR\n    \n    idarray : LEFTSQR exp RIGHTSQR\n            | empty\n    \n    exp : andexp exp1\n    \n    exp1 : OR exp\n        | empty\n    \n    andexp : boolexp andexp1\n    \n    andexp1 : AND andexp\n        | empty\n    \n    boolexp : arithexp boolexp1\n    \n    boolexp1 : GREATER arithexp\n        | GREATERAND arithexp\n        | LESSER arithexp\n        | LESSERAND arithexp\n        | SAME arithexp\n        | NOTSAME arithexp\n        | NOT arithexp\n        | empty\n    \n    arithexp : geoexp arithexp1\n    \n    arithexp1 : PLUS arithexp\n        | REST arithexp\n        | empty\n    \n    geoexp : finexp geoexp1\n    \n    geoexp1 : TIMES geoexp\n        | DIVIDE geoexp\n        | empty\n    \n    finexp : LEFTPAR exp RIGHTPAR\n            | cteexp\n    \n    cteexp : CTEINT\n            | CTEFLOAT\n            | CTECHAR\n            | ID paramsexp\n    \n    paramsexp : LEFTPAR paramsexp2 RIGHTPAR\n                | idarray\n    \n    paramsexp2 : exp auxparamsexp2\n            | empty\n    \n    auxparamsexp2 : COMMA exp auxparamsexp2\n            | empty\n    \n    empty : \n    \n    debug : empty\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,80,],[0,-1,]),'ID':([2,15,16,17,19,20,21,22,32,37,40,41,43,44,45,46,47,48,49,50,51,57,58,59,60,61,62,63,64,65,66,67,69,73,74,75,76,77,79,83,92,93,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,124,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,161,165,170,171,175,178,182,191,193,194,195,197,204,205,207,209,210,211,214,215,],[3,-16,-17,-18,24,-13,-14,25,40,71,-89,79,40,40,40,40,40,40,40,40,40,97,-89,-34,-89,-89,-89,-89,-78,-79,-80,-81,122,-84,-82,79,-53,79,-89,-34,131,79,79,79,79,-54,79,-56,-57,79,-59,-60,79,79,79,79,79,79,79,-68,-69,79,79,-72,-73,79,79,-76,79,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,79,79,79,40,-35,190,-46,-36,40,40,79,-43,-89,-50,-47,-49,40,40,-51,-48,]),'SEMICOLON':([3,4,25,29,31,58,60,61,62,63,64,65,66,67,68,71,72,74,76,79,98,100,101,103,104,112,113,116,117,120,123,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,157,158,159,167,180,189,],[-2,5,-89,38,-8,-89,-89,-89,-89,-89,-78,-79,-80,-81,121,-89,-7,-82,-53,-89,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,38,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,175,-52,-83,182,191,197,]),'VARS':([5,121,],[7,7,]),'FUNCTION':([5,6,7,8,12,14,36,38,70,156,196,],[-89,10,-89,-4,-3,-6,-89,-10,-5,-9,10,]),'MAIN':([5,6,7,8,9,11,12,14,27,36,38,70,156,196,202,],[-89,-89,-89,-4,18,-12,-3,-6,-11,-89,-10,-5,-9,-89,-15,]),'INT':([7,10,28,36,38,156,173,],[15,15,15,15,-10,-9,15,]),'FLOAT':([7,10,28,36,38,156,173,],[16,16,16,16,-10,-9,16,]),'CHAR':([7,10,28,36,38,156,173,],[17,17,17,17,-10,-9,17,]),'LEFTBR':([7,8,12,14,26,36,38,70,121,154,156,183,184,206,208,],[-89,-4,-3,-6,32,-89,-10,-5,-89,171,-9,193,194,210,211,]),'VOID':([10,],[20,]),'COLON':([13,15,16,17,34,],[22,-16,-17,-18,69,]),'LEFTPAR':([18,24,32,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,63,64,65,66,67,73,74,75,76,77,79,83,93,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,124,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,161,165,170,171,175,182,191,193,194,195,197,204,205,207,209,210,211,214,215,],[23,28,41,77,41,41,41,41,41,41,41,41,41,41,92,93,94,95,96,-89,-34,-89,-89,-89,-89,-78,-79,-80,-81,-84,-82,41,-53,41,77,-34,41,41,41,41,-54,41,-56,-57,41,-59,-60,41,41,41,41,41,41,41,-68,-69,41,41,-72,-73,41,41,-76,41,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,41,41,41,41,-35,-46,-36,41,41,41,-43,-89,-50,-47,-49,41,41,-51,-48,]),'RIGHTPAR':([23,28,33,35,58,60,61,62,63,64,65,66,67,74,76,77,78,79,98,100,101,103,104,112,113,116,117,120,122,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,143,144,145,146,147,148,149,150,151,152,153,155,158,159,160,162,163,164,166,172,173,174,176,177,179,181,187,188,190,192,198,203,],[26,-89,68,-20,-89,-89,-89,-89,-89,-78,-79,-80,-81,-82,-53,-89,129,-89,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,-89,159,-89,-86,-77,-84,-89,-89,-37,-38,-39,-40,167,168,169,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-89,-52,-83,-85,-88,-89,180,-42,-19,-89,-22,-89,189,-45,-89,-21,-87,-89,-41,-89,-44,]),'LEFTSQR':([25,40,71,79,97,122,131,190,],[30,75,30,75,75,75,75,75,]),'COMMA':([25,29,31,58,60,61,62,63,64,65,66,67,71,72,74,76,79,98,100,101,103,104,112,113,116,117,120,122,123,127,129,130,131,132,133,134,135,136,141,142,143,144,145,146,147,148,149,150,151,152,153,155,158,159,163,176,181,190,198,],[-89,37,-8,-89,-89,-89,-89,-89,-78,-79,-80,-81,-89,-7,-82,-53,-89,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,-89,37,161,-77,-84,-89,165,-37,-38,-39,-40,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,173,-52,-83,178,161,165,-89,178,]),'CTEINT':([30,32,40,41,43,44,45,46,47,48,49,50,51,58,59,60,61,62,63,64,65,66,67,73,74,75,76,77,79,83,93,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,124,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,161,165,170,171,175,182,191,193,194,195,197,204,205,207,209,210,211,214,215,],[39,65,-89,65,65,65,65,65,65,65,65,65,65,-89,-34,-89,-89,-89,-89,-78,-79,-80,-81,-84,-82,65,-53,65,-89,-34,65,65,65,65,-54,65,-56,-57,65,-59,-60,65,65,65,65,65,65,65,-68,-69,65,65,-72,-73,65,65,-76,65,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,65,65,65,65,-35,-46,-36,65,65,65,-43,-89,-50,-47,-49,65,65,-51,-48,]),'READ':([32,40,43,44,45,46,47,48,49,50,51,58,59,60,61,62,63,64,65,66,67,73,74,76,79,83,98,100,101,103,104,112,113,116,117,120,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,171,175,182,191,193,194,197,204,205,207,209,210,211,214,215,],[52,-89,52,52,52,52,52,52,52,52,52,-89,-34,-89,-89,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-34,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,52,-35,-46,-36,52,52,-43,-89,-50,-47,-49,52,52,-51,-48,]),'WRITE':([32,40,43,44,45,46,47,48,49,50,51,58,59,60,61,62,63,64,65,66,67,73,74,76,79,83,98,100,101,103,104,112,113,116,117,120,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,171,175,182,191,193,194,197,204,205,207,209,210,211,214,215,],[53,-89,53,53,53,53,53,53,53,53,53,-89,-34,-89,-89,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-34,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,53,-35,-46,-36,53,53,-43,-89,-50,-47,-49,53,53,-51,-48,]),'RETURN':([32,40,43,44,45,46,47,48,49,50,51,58,59,60,61,62,63,64,65,66,67,73,74,76,79,83,98,100,101,103,104,112,113,116,117,120,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,171,175,182,191,193,194,197,204,205,207,209,210,211,214,215,],[54,-89,54,54,54,54,54,54,54,54,54,-89,-34,-89,-89,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-34,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,54,-35,-46,-36,54,54,-43,-89,-50,-47,-49,54,54,-51,-48,]),'IF':([32,40,43,44,45,46,47,48,49,50,51,58,59,60,61,62,63,64,65,66,67,73,74,76,79,83,98,100,101,103,104,112,113,116,117,120,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,171,175,182,191,193,194,197,204,205,207,209,210,211,214,215,],[55,-89,55,55,55,55,55,55,55,55,55,-89,-34,-89,-89,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-34,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,55,-35,-46,-36,55,55,-43,-89,-50,-47,-49,55,55,-51,-48,]),'WHILE':([32,40,43,44,45,46,47,48,49,50,51,58,59,60,61,62,63,64,65,66,67,73,74,76,79,83,98,100,101,103,104,112,113,116,117,120,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,171,175,182,191,193,194,197,204,205,207,209,210,211,214,215,],[56,-89,56,56,56,56,56,56,56,56,56,-89,-34,-89,-89,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-34,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,56,-35,-46,-36,56,56,-43,-89,-50,-47,-49,56,56,-51,-48,]),'FOR':([32,40,43,44,45,46,47,48,49,50,51,58,59,60,61,62,63,64,65,66,67,73,74,76,79,83,98,100,101,103,104,112,113,116,117,120,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,171,175,182,191,193,194,197,204,205,207,209,210,211,214,215,],[57,-89,57,57,57,57,57,57,57,57,57,-89,-34,-89,-89,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-34,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,57,-35,-46,-36,57,57,-43,-89,-50,-47,-49,57,57,-51,-48,]),'CTEFLOAT':([32,40,41,43,44,45,46,47,48,49,50,51,58,59,60,61,62,63,64,65,66,67,73,74,75,76,77,79,83,93,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,124,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,161,165,170,171,175,182,191,193,194,195,197,204,205,207,209,210,211,214,215,],[66,-89,66,66,66,66,66,66,66,66,66,66,-89,-34,-89,-89,-89,-89,-78,-79,-80,-81,-84,-82,66,-53,66,-89,-34,66,66,66,66,-54,66,-56,-57,66,-59,-60,66,66,66,66,66,66,66,-68,-69,66,66,-72,-73,66,66,-76,66,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,66,66,66,66,-35,-46,-36,66,66,66,-43,-89,-50,-47,-49,66,66,-51,-48,]),'CTECHAR':([32,40,41,43,44,45,46,47,48,49,50,51,58,59,60,61,62,63,64,65,66,67,73,74,75,76,77,79,83,93,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,124,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,161,165,170,171,175,182,191,193,194,195,197,204,205,207,209,210,211,214,215,],[67,-89,67,67,67,67,67,67,67,67,67,67,-89,-34,-89,-89,-89,-89,-78,-79,-80,-81,-84,-82,67,-53,67,-89,-34,136,67,67,67,-54,67,-56,-57,67,-59,-60,67,67,67,67,67,67,67,-68,-69,67,67,-72,-73,67,67,-76,67,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,67,136,67,67,-35,-46,-36,67,67,67,-43,-89,-50,-47,-49,67,67,-51,-48,]),'RIGHTBR':([32,40,42,43,44,45,46,47,48,49,50,51,58,59,60,61,62,63,64,65,66,67,73,74,76,79,81,82,83,84,85,86,87,88,89,90,91,98,100,101,103,104,112,113,116,117,120,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,171,175,182,186,191,193,194,197,199,200,204,205,207,209,210,211,212,213,214,215,],[-89,-89,80,-89,-89,-89,-89,-89,-89,-89,-89,-89,-89,-34,-89,-89,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-23,-32,-33,-24,-25,-26,-27,-28,-29,-30,-31,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,-89,-35,-46,196,-36,-89,-89,-43,204,205,-89,-50,-47,-49,-89,-89,214,215,-51,-48,]),'RIGHTSQR':([39,58,60,61,62,63,64,65,66,67,74,76,79,98,100,101,103,104,112,113,116,117,120,125,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,],[72,-89,-89,-89,-89,-89,-78,-79,-80,-81,-82,-53,-89,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,158,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,]),'EQUAL':([40,73,76,97,140,158,],[-89,124,-53,-89,170,-52,]),'TIMES':([40,63,64,65,66,67,73,74,76,79,129,130,136,158,159,],[-89,118,-78,-79,-80,-81,-84,-82,-53,-89,-77,-84,-81,-52,-83,]),'DIVIDE':([40,63,64,65,66,67,73,74,76,79,129,130,136,158,159,],[-89,119,-78,-79,-80,-81,-84,-82,-53,-89,-77,-84,-81,-52,-83,]),'PLUS':([40,62,63,64,65,66,67,73,74,76,79,117,120,129,130,136,152,153,158,159,],[-89,114,-89,-78,-79,-80,-81,-84,-82,-53,-89,-73,-76,-77,-84,-81,-74,-75,-52,-83,]),'REST':([40,62,63,64,65,66,67,73,74,76,79,117,120,129,130,136,152,153,158,159,],[-89,115,-89,-78,-79,-80,-81,-84,-82,-53,-89,-73,-76,-77,-84,-81,-74,-75,-52,-83,]),'GREATER':([40,61,62,63,64,65,66,67,73,74,76,79,113,116,117,120,129,130,136,150,151,152,153,158,159,],[-89,105,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-69,-72,-73,-76,-77,-84,-81,-70,-71,-74,-75,-52,-83,]),'GREATERAND':([40,61,62,63,64,65,66,67,73,74,76,79,113,116,117,120,129,130,136,150,151,152,153,158,159,],[-89,106,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-69,-72,-73,-76,-77,-84,-81,-70,-71,-74,-75,-52,-83,]),'LESSER':([40,61,62,63,64,65,66,67,73,74,76,79,113,116,117,120,129,130,136,150,151,152,153,158,159,],[-89,107,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-69,-72,-73,-76,-77,-84,-81,-70,-71,-74,-75,-52,-83,]),'LESSERAND':([40,61,62,63,64,65,66,67,73,74,76,79,113,116,117,120,129,130,136,150,151,152,153,158,159,],[-89,108,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-69,-72,-73,-76,-77,-84,-81,-70,-71,-74,-75,-52,-83,]),'SAME':([40,61,62,63,64,65,66,67,73,74,76,79,113,116,117,120,129,130,136,150,151,152,153,158,159,],[-89,109,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-69,-72,-73,-76,-77,-84,-81,-70,-71,-74,-75,-52,-83,]),'NOTSAME':([40,61,62,63,64,65,66,67,73,74,76,79,113,116,117,120,129,130,136,150,151,152,153,158,159,],[-89,110,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-69,-72,-73,-76,-77,-84,-81,-70,-71,-74,-75,-52,-83,]),'NOT':([40,61,62,63,64,65,66,67,73,74,76,79,113,116,117,120,129,130,136,150,151,152,153,158,159,],[-89,111,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-69,-72,-73,-76,-77,-84,-81,-70,-71,-74,-75,-52,-83,]),'AND':([40,60,61,62,63,64,65,66,67,73,74,76,79,104,112,113,116,117,120,129,130,136,143,144,145,146,147,148,149,150,151,152,153,158,159,],[-89,102,-89,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-60,-68,-69,-72,-73,-76,-77,-84,-81,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,]),'OR':([40,58,60,61,62,63,64,65,66,67,73,74,76,79,101,103,104,112,113,116,117,120,129,130,136,142,143,144,145,146,147,148,149,150,151,152,153,158,159,],[-89,99,-89,-89,-89,-89,-78,-79,-80,-81,-84,-82,-53,-89,-57,-59,-60,-68,-69,-72,-73,-76,-77,-84,-81,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,]),'TO':([58,60,61,62,63,64,65,66,67,74,76,79,98,100,101,103,104,112,113,116,117,120,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,185,],[-89,-89,-89,-89,-89,-78,-79,-80,-81,-82,-53,-89,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,195,]),'DO':([58,60,61,62,63,64,65,66,67,74,76,79,98,100,101,103,104,112,113,116,117,120,129,130,141,142,143,144,145,146,147,148,149,150,151,152,153,158,159,169,201,],[-89,-89,-89,-89,-89,-78,-79,-80,-81,-82,-53,-89,-54,-56,-57,-59,-60,-68,-69,-72,-73,-76,-77,-84,-55,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-75,-52,-83,184,206,]),'STRING':([93,165,],[135,135,]),'THEN':([168,],[183,]),'ELSE':([204,],[208,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'neuraltablefunctions':([3,],[4,]),'varsgl':([5,121,],[6,154,]),'empty':([5,6,7,25,28,32,36,40,43,44,45,46,47,48,49,50,51,58,60,61,62,63,71,77,79,97,121,122,127,131,132,155,163,171,173,176,181,190,193,194,196,198,204,210,211,],[8,11,14,31,35,59,14,76,83,83,83,83,83,83,83,83,83,100,103,112,116,120,31,128,76,76,8,76,162,76,166,174,179,59,35,162,166,76,59,59,11,179,209,59,59,]),'modules':([6,196,],[9,202,]),'vars':([7,36,],[12,70,]),'typing':([7,10,28,36,173,],[13,21,34,13,34,]),'functype':([10,],[19,]),'funcparam':([24,],[27,]),'varsarr':([25,71,],[29,123,]),'parameters':([28,173,],[33,187,]),'varsmul':([29,123,],[36,156,]),'statutes':([32,43,44,45,46,47,48,49,50,51,171,193,194,210,211,],[42,82,82,82,82,82,82,82,82,82,186,199,200,212,213,]),'assign':([32,43,44,45,46,47,48,49,50,51,171,193,194,210,211,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'reading':([32,43,44,45,46,47,48,49,50,51,171,193,194,210,211,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'writing':([32,43,44,45,46,47,48,49,50,51,171,193,194,210,211,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'returning':([32,43,44,45,46,47,48,49,50,51,171,193,194,210,211,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'ifing':([32,43,44,45,46,47,48,49,50,51,171,193,194,210,211,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'whiling':([32,43,44,45,46,47,48,49,50,51,171,193,194,210,211,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'foring':([32,43,44,45,46,47,48,49,50,51,171,193,194,210,211,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'exp':([32,41,43,44,45,46,47,48,49,50,51,75,77,93,94,95,96,99,124,161,165,170,171,193,194,195,210,211,],[50,78,50,50,50,50,50,50,50,50,50,125,127,134,137,138,139,141,157,176,134,185,50,50,50,201,50,50,]),'specialfunc':([32,43,44,45,46,47,48,49,50,51,171,193,194,210,211,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'andexp':([32,41,43,44,45,46,47,48,49,50,51,75,77,93,94,95,96,99,102,124,161,165,170,171,193,194,195,210,211,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,142,58,58,58,58,58,58,58,58,58,58,]),'boolexp':([32,41,43,44,45,46,47,48,49,50,51,75,77,93,94,95,96,99,102,124,161,165,170,171,193,194,195,210,211,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'arithexp':([32,41,43,44,45,46,47,48,49,50,51,75,77,93,94,95,96,99,102,105,106,107,108,109,110,111,114,115,124,161,165,170,171,193,194,195,210,211,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,143,144,145,146,147,148,149,150,151,61,61,61,61,61,61,61,61,61,61,]),'geoexp':([32,41,43,44,45,46,47,48,49,50,51,75,77,93,94,95,96,99,102,105,106,107,108,109,110,111,114,115,118,119,124,161,165,170,171,193,194,195,210,211,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,152,153,62,62,62,62,62,62,62,62,62,62,]),'finexp':([32,41,43,44,45,46,47,48,49,50,51,75,77,93,94,95,96,99,102,105,106,107,108,109,110,111,114,115,118,119,124,161,165,170,171,193,194,195,210,211,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'cteexp':([32,41,43,44,45,46,47,48,49,50,51,75,77,93,94,95,96,99,102,105,106,107,108,109,110,111,114,115,118,119,124,161,165,170,171,193,194,195,210,211,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'idarray':([40,79,97,122,131,190,],[73,130,140,155,163,198,]),'paramsexp':([40,79,],[74,74,]),'statutesaux':([43,44,45,46,47,48,49,50,51,],[81,84,85,86,87,88,89,90,91,]),'exp1':([58,],[98,]),'andexp1':([60,],[101,]),'boolexp1':([61,],[104,]),'arithexp1':([62,],[113,]),'geoexp1':([63,],[117,]),'paramsexp2':([77,],[126,]),'auxwrite':([93,165,],[132,181,]),'writetyping':([93,165,],[133,133,]),'auxparamsexp2':([127,176,],[160,188,]),'mulwrite':([132,181,],[164,192,]),'mulparams':([155,],[172,]),'mulread':([163,198,],[177,203,]),'elsing':([204,],[207,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID neuraltablefunctions SEMICOLON varsgl modules MAIN LEFTPAR RIGHTPAR LEFTBR statutes RIGHTBR','program',12,'p_PROGRAM','myLexerParser.py',250),
  ('neuraltablefunctions -> <empty>','neuraltablefunctions',0,'p_NEURALTABLEFUNCTIONS','myLexerParser.py',256),
  ('varsgl -> VARS vars','varsgl',2,'p_VARSGL','myLexerParser.py',264),
  ('varsgl -> empty','varsgl',1,'p_VARSGL','myLexerParser.py',265),
  ('vars -> typing COLON ID varsarr varsmul vars','vars',6,'p_VARS','myLexerParser.py',270),
  ('vars -> empty','vars',1,'p_VARS','myLexerParser.py',271),
  ('varsarr -> LEFTSQR CTEINT RIGHTSQR','varsarr',3,'p_VARSARR','myLexerParser.py',276),
  ('varsarr -> empty','varsarr',1,'p_VARSARR','myLexerParser.py',277),
  ('varsmul -> COMMA ID varsarr varsmul','varsmul',4,'p_VARSMUL','myLexerParser.py',282),
  ('varsmul -> SEMICOLON','varsmul',1,'p_VARSMUL','myLexerParser.py',283),
  ('modules -> FUNCTION functype ID funcparam','modules',4,'p_MODULES','myLexerParser.py',291),
  ('modules -> empty','modules',1,'p_MODULES','myLexerParser.py',292),
  ('functype -> VOID','functype',1,'p_FUNCTYPE','myLexerParser.py',297),
  ('functype -> typing','functype',1,'p_FUNCTYPE','myLexerParser.py',298),
  ('funcparam -> LEFTPAR parameters RIGHTPAR SEMICOLON varsgl LEFTBR statutes RIGHTBR modules','funcparam',9,'p_FUNCPARAM','myLexerParser.py',303),
  ('typing -> INT','typing',1,'p_TYPING','myLexerParser.py',308),
  ('typing -> FLOAT','typing',1,'p_TYPING','myLexerParser.py',309),
  ('typing -> CHAR','typing',1,'p_TYPING','myLexerParser.py',310),
  ('parameters -> typing COLON ID idarray mulparams','parameters',5,'p_PARAMETERS','myLexerParser.py',315),
  ('parameters -> empty','parameters',1,'p_PARAMETERS','myLexerParser.py',316),
  ('mulparams -> COMMA parameters','mulparams',2,'p_MULPARAMS','myLexerParser.py',321),
  ('mulparams -> empty','mulparams',1,'p_MULPARAMS','myLexerParser.py',322),
  ('statutes -> assign statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',329),
  ('statutes -> reading statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',330),
  ('statutes -> writing statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',331),
  ('statutes -> returning statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',332),
  ('statutes -> ifing statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',333),
  ('statutes -> whiling statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',334),
  ('statutes -> foring statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',335),
  ('statutes -> exp statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',336),
  ('statutes -> specialfunc statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',337),
  ('statutesaux -> statutes','statutesaux',1,'p_STATUTESAUX','myLexerParser.py',342),
  ('statutesaux -> empty','statutesaux',1,'p_STATUTESAUX','myLexerParser.py',343),
  ('specialfunc -> empty','specialfunc',1,'p_SPECIALFUNC','myLexerParser.py',348),
  ('assign -> ID idarray EQUAL exp SEMICOLON','assign',5,'p_ASSIGN','myLexerParser.py',355),
  ('writing -> WRITE LEFTPAR auxwrite mulwrite RIGHTPAR SEMICOLON','writing',6,'p_WRITING','myLexerParser.py',364),
  ('auxwrite -> writetyping','auxwrite',1,'p_AUXWRITE','myLexerParser.py',369),
  ('auxwrite -> exp','auxwrite',1,'p_AUXWRITE','myLexerParser.py',370),
  ('writetyping -> STRING','writetyping',1,'p_WRITETYPING','myLexerParser.py',375),
  ('writetyping -> CTECHAR','writetyping',1,'p_WRITETYPING','myLexerParser.py',376),
  ('mulwrite -> COMMA auxwrite mulwrite','mulwrite',3,'p_MULWRITE','myLexerParser.py',381),
  ('mulwrite -> empty','mulwrite',1,'p_MULWRITE','myLexerParser.py',382),
  ('reading -> READ LEFTPAR ID idarray mulread RIGHTPAR SEMICOLON','reading',7,'p_READING','myLexerParser.py',389),
  ('mulread -> COMMA ID idarray mulread','mulread',4,'p_MULREAD','myLexerParser.py',394),
  ('mulread -> empty','mulread',1,'p_MULREAD','myLexerParser.py',395),
  ('returning -> RETURN LEFTPAR exp RIGHTPAR SEMICOLON','returning',5,'p_RETURNING','myLexerParser.py',402),
  ('ifing -> IF LEFTPAR exp RIGHTPAR THEN LEFTBR statutes RIGHTBR elsing','ifing',9,'p_IFING','myLexerParser.py',412),
  ('elsing -> ELSE LEFTBR statutes RIGHTBR','elsing',4,'p_ELSING','myLexerParser.py',417),
  ('elsing -> empty','elsing',1,'p_ELSING','myLexerParser.py',418),
  ('whiling -> WHILE LEFTPAR exp RIGHTPAR DO LEFTBR statutes RIGHTBR','whiling',8,'p_WHILING','myLexerParser.py',426),
  ('foring -> FOR ID idarray EQUAL exp TO exp DO LEFTBR statutes RIGHTBR','foring',11,'p_FORING','myLexerParser.py',433),
  ('idarray -> LEFTSQR exp RIGHTSQR','idarray',3,'p_IDARRAY','myLexerParser.py',442),
  ('idarray -> empty','idarray',1,'p_IDARRAY','myLexerParser.py',443),
  ('exp -> andexp exp1','exp',2,'p_EXP','myLexerParser.py',449),
  ('exp1 -> OR exp','exp1',2,'p_EXP1','myLexerParser.py',454),
  ('exp1 -> empty','exp1',1,'p_EXP1','myLexerParser.py',455),
  ('andexp -> boolexp andexp1','andexp',2,'p_ANDEXP','myLexerParser.py',460),
  ('andexp1 -> AND andexp','andexp1',2,'p_ANDEXP1','myLexerParser.py',465),
  ('andexp1 -> empty','andexp1',1,'p_ANDEXP1','myLexerParser.py',466),
  ('boolexp -> arithexp boolexp1','boolexp',2,'p_BOOLEXP','myLexerParser.py',471),
  ('boolexp1 -> GREATER arithexp','boolexp1',2,'p_BOOLEXP1','myLexerParser.py',476),
  ('boolexp1 -> GREATERAND arithexp','boolexp1',2,'p_BOOLEXP1','myLexerParser.py',477),
  ('boolexp1 -> LESSER arithexp','boolexp1',2,'p_BOOLEXP1','myLexerParser.py',478),
  ('boolexp1 -> LESSERAND arithexp','boolexp1',2,'p_BOOLEXP1','myLexerParser.py',479),
  ('boolexp1 -> SAME arithexp','boolexp1',2,'p_BOOLEXP1','myLexerParser.py',480),
  ('boolexp1 -> NOTSAME arithexp','boolexp1',2,'p_BOOLEXP1','myLexerParser.py',481),
  ('boolexp1 -> NOT arithexp','boolexp1',2,'p_BOOLEXP1','myLexerParser.py',482),
  ('boolexp1 -> empty','boolexp1',1,'p_BOOLEXP1','myLexerParser.py',483),
  ('arithexp -> geoexp arithexp1','arithexp',2,'p_ARITHEXP','myLexerParser.py',488),
  ('arithexp1 -> PLUS arithexp','arithexp1',2,'p_ARITHEXP1','myLexerParser.py',493),
  ('arithexp1 -> REST arithexp','arithexp1',2,'p_ARITHEXP1','myLexerParser.py',494),
  ('arithexp1 -> empty','arithexp1',1,'p_ARITHEXP1','myLexerParser.py',495),
  ('geoexp -> finexp geoexp1','geoexp',2,'p_GEOEXP','myLexerParser.py',500),
  ('geoexp1 -> TIMES geoexp','geoexp1',2,'p_GEOEXP1','myLexerParser.py',505),
  ('geoexp1 -> DIVIDE geoexp','geoexp1',2,'p_GEOEXP1','myLexerParser.py',506),
  ('geoexp1 -> empty','geoexp1',1,'p_GEOEXP1','myLexerParser.py',507),
  ('finexp -> LEFTPAR exp RIGHTPAR','finexp',3,'p_FINEXP','myLexerParser.py',512),
  ('finexp -> cteexp','finexp',1,'p_FINEXP','myLexerParser.py',513),
  ('cteexp -> CTEINT','cteexp',1,'p_CTEEXP','myLexerParser.py',518),
  ('cteexp -> CTEFLOAT','cteexp',1,'p_CTEEXP','myLexerParser.py',519),
  ('cteexp -> CTECHAR','cteexp',1,'p_CTEEXP','myLexerParser.py',520),
  ('cteexp -> ID paramsexp','cteexp',2,'p_CTEEXP','myLexerParser.py',521),
  ('paramsexp -> LEFTPAR paramsexp2 RIGHTPAR','paramsexp',3,'p_PARAMSEXP','myLexerParser.py',529),
  ('paramsexp -> idarray','paramsexp',1,'p_PARAMSEXP','myLexerParser.py',530),
  ('paramsexp2 -> exp auxparamsexp2','paramsexp2',2,'p_PARAMSEXP2','myLexerParser.py',535),
  ('paramsexp2 -> empty','paramsexp2',1,'p_PARAMSEXP2','myLexerParser.py',536),
  ('auxparamsexp2 -> COMMA exp auxparamsexp2','auxparamsexp2',3,'p_AUXPARAMSEXP2','myLexerParser.py',541),
  ('auxparamsexp2 -> empty','auxparamsexp2',1,'p_AUXPARAMSEXP2','myLexerParser.py',542),
  ('empty -> <empty>','empty',0,'p_empty','myLexerParser.py',548),
  ('debug -> empty','debug',1,'p_DEBUG','myLexerParser.py',560),
]
