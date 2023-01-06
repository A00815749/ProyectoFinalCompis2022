
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'STRING ID PLUS REST TIMES DIVIDE GREATER GREATERAND LESSER LESSERAND SAME NOTSAME NOT EQUAL LEFTBR RIGHTBR LEFTPAR RIGHTPAR LEFTSQR RIGHTSQR COLON SEMICOLON COMMA CTEINT CTEFLOAT CTECHAR PROGRAM MAIN FUNCTION VARS INT FLOAT CHAR STR RETURN READ WRITE AND OR IF THEN ELSE WHILE DO FOR TO VOID TRUE FALSE MEDIA MEDIANA MODA VARIANZA STDEV PLOTXY\n    program : PROGRAM neuraltablefunctions SEMICOLON varsgl modules MAIN LEFTPAR RIGHTPAR LEFTBR statutes RIGHTBR\n    \n    neuraltablefunctions : ID\n    \n    varsgl : VARS vars\n            | empty\n    \n    vars : typing COLON neuralinsertvar varsarr varsmul vars\n            | empty\n    \n    neuralinsertvar : ID\n    \n    varsarr : LEFTSQR CTEINT RIGHTSQR\n        | empty\n    \n    varsmul : COMMA neuralinsertvar varsarr varsmul\n            | SEMICOLON\n    \n    modules : FUNCTION functype neuralinsertfuncname funcparam\n            | empty\n    \n    neuralinsertfuncname : ID\n    \n    functype : VOID\n            | typing\n    \n    funcparam : LEFTPAR parameters RIGHTPAR SEMICOLON varsgl LEFTBR statutes RIGHTBR neuralendfuncs modules\n    \n    neuralendfuncs : \n    \n    typing : INT\n            | FLOAT\n            | CHAR\n    \n    parameters : typing COLON ID idarray mulparams\n            | empty\n    \n    mulparams : COMMA parameters\n            | empty\n    \n    statutes : assign statutesaux\n            | reading statutesaux\n            | writing statutesaux\n            | returning statutesaux\n            | ifing statutesaux\n            | whiling statutesaux\n            | foring statutesaux\n            | exp statutesaux\n            | specialfunc statutesaux\n    \n    statutesaux : statutes \n                | empty\n    \n    specialfunc : empty\n    \n    assign : neuralassign1 idarray neuralassign2 exp SEMICOLON \n    \n    neuralassign1 : ID\n    \n    neuralassign2 : EQUAL\n    \n    writing : WRITE LEFTPAR auxwrite mulwrite RIGHTPAR SEMICOLON\n    \n    auxwrite : writetyping\n            | exp\n    \n    writetyping : STRING\n            | CTECHAR\n    \n    mulwrite : COMMA auxwrite mulwrite\n            | empty\n    \n    reading : READ LEFTPAR neuralread idarray mulread RIGHTPAR SEMICOLON\n    \n    neuralread : ID\n    \n    mulread : COMMA ID idarray mulread\n            | empty\n    \n    returning : RETURN LEFTPAR exp RIGHTPAR SEMICOLON\n    \n    ifing : IF LEFTPAR exp neuralif THEN LEFTBR statutes RIGHTBR elsing\n    \n    neuralif : RIGHTPAR\n    \n    elsing : neuralelse LEFTBR statutes RIGHTBR\n            | empty\n    \n    neuralelse : ELSE\n    \n    whiling : WHILE LEFTPAR exp RIGHTPAR DO LEFTBR statutes RIGHTBR\n    \n    foring : FOR ID idarray EQUAL exp TO exp DO LEFTBR statutes RIGHTBR\n    \n    idarray : LEFTSQR exp RIGHTSQR\n            | empty\n    \n    exp : andexp exp1\n    \n    exp1 : OR exp\n        | empty\n    \n    andexp : boolexp andexp1\n    \n    andexp1 : neuraland andexp\n        | empty\n    \n    neuraland : AND\n    \n    boolexp : arithexp boolexp1\n    \n    boolexp1 : neuralbool arithexp\n        | empty\n    \n    neuralbool : GREATER \n        | GREATERAND \n        | LESSER \n        | LESSERAND \n        | SAME \n        | NOTSAME \n        | NOT \n    \n    arithexp : geoexp arithexp1\n    \n    arithexp1 : neuralarith arithexp\n        | empty\n    \n    neuralarith : PLUS\n                | REST\n    \n    geoexp : finexp geoexp1\n    \n    geoexp1 : neuralgeo geoexp\n        | empty\n    \n    neuralgeo : TIMES\n            | DIVIDE\n    \n    addparenth : LEFTPAR\n    \n    popparenth : RIGHTPAR\n    \n    finexp : addparenth exp popparenth\n            | cteexp\n    \n    cteexp : CTEINT\n            | CTEFLOAT\n            | CTECHAR\n            | ID paramsexp\n    \n    paramsexp : LEFTPAR paramsexp2 RIGHTPAR\n                | idarray\n    \n    paramsexp2 : exp auxparamsexp2\n            | empty\n    \n    auxparamsexp2 : COMMA exp auxparamsexp2\n            | empty\n    \n    empty : \n    \n    debug : empty\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,77,],[0,-1,]),'ID':([2,15,16,17,19,20,21,22,34,39,42,44,45,46,47,48,49,50,51,52,59,60,61,62,63,64,65,66,67,68,69,70,71,73,80,90,91,92,93,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,133,134,150,151,152,153,154,155,156,161,164,170,171,173,175,179,181,185,194,196,197,198,201,208,209,212,214,216,217,220,221,],[4,-19,-20,-21,25,-15,-16,27,60,27,-89,60,60,60,60,60,60,60,60,60,97,-103,-103,-37,-103,-103,-103,-103,129,-92,-93,-94,-95,131,-37,129,-61,137,129,129,129,129,-96,129,-98,-62,129,-64,-65,129,-67,-68,-69,129,-71,-72,-73,-74,-75,-76,-77,-78,-79,129,-81,-82,-83,-84,129,-86,-87,-88,-103,129,-40,-63,-66,-70,-80,-85,-91,-90,-60,129,129,-97,129,60,-38,193,-52,-41,60,60,129,-48,-103,-58,-53,-56,60,60,-59,-55,]),'SEMICOLON':([3,4,26,27,31,33,61,63,64,65,66,68,69,70,71,72,75,76,91,98,100,101,103,104,106,108,110,118,120,123,125,129,132,150,151,152,153,154,155,156,160,161,166,171,183,192,],[5,-2,-103,-7,40,-9,-103,-103,-103,-103,-103,-92,-93,-94,-95,130,-103,-8,-61,-96,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,-103,40,-63,-66,-70,-80,-85,-91,-90,179,-60,185,-97,194,201,]),'VARS':([5,130,],[7,7,]),'FUNCTION':([5,6,7,8,12,14,38,40,74,159,200,206,],[-103,10,-103,-4,-3,-6,-103,-11,-5,-10,-18,10,]),'MAIN':([5,6,7,8,9,11,12,14,29,38,40,74,159,200,206,211,],[-103,-103,-103,-4,18,-13,-3,-6,-12,-103,-11,-5,-10,-18,-103,-17,]),'INT':([7,10,30,38,40,159,177,],[15,15,15,15,-11,-10,15,]),'FLOAT':([7,10,30,38,40,159,177,],[16,16,16,16,-11,-10,16,]),'CHAR':([7,10,30,38,40,159,177,],[17,17,17,17,-11,-10,17,]),'LEFTBR':([7,8,12,14,28,38,40,74,130,157,159,186,187,210,213,215,],[-103,-4,-3,-6,34,-103,-11,-5,-103,175,-10,196,197,216,217,-57,]),'VOID':([10,],[20,]),'COLON':([13,15,16,17,36,],[22,-19,-20,-21,73,]),'LEFTPAR':([18,24,25,34,42,44,45,46,47,48,49,50,51,52,54,55,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,80,90,91,93,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,133,134,150,151,152,153,154,155,156,161,164,170,171,173,175,179,185,194,196,197,198,201,208,209,212,214,216,217,220,221,],[23,30,-14,42,-89,42,42,42,42,42,42,42,42,42,92,93,94,95,96,99,-103,-37,-103,-103,-103,-103,42,-92,-93,-94,-95,-37,42,-61,42,42,42,42,-96,42,-98,-62,42,-64,-65,42,-67,-68,-69,42,-71,-72,-73,-74,-75,-76,-77,-78,-79,42,-81,-82,-83,-84,42,-86,-87,-88,99,42,-40,-63,-66,-70,-80,-85,-91,-90,-60,42,42,-97,42,42,-38,-52,-41,42,42,42,-48,-103,-58,-53,-56,42,42,-59,-55,]),'RIGHTPAR':([23,30,35,37,61,63,64,65,66,68,69,70,71,91,98,99,100,101,103,104,106,108,110,118,120,123,125,128,129,131,136,137,138,139,140,141,142,143,144,145,147,148,149,150,151,152,153,154,155,156,158,161,162,163,165,171,172,174,176,177,178,180,182,184,189,191,193,195,199,202,207,],[28,-103,72,-23,-103,-103,-103,-103,-103,-92,-93,-94,-95,-61,-96,-103,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,156,-103,-103,-103,-49,-103,-42,-43,-44,-45,166,168,169,171,-103,-100,-63,-66,-70,-80,-85,-91,-90,-103,-60,-103,183,-47,-97,-99,-102,-22,-103,-25,192,-51,-103,-103,-24,-103,-46,-101,-103,-50,]),'LEFTSQR':([26,27,53,60,75,97,129,131,136,137,193,],[32,-7,90,90,32,90,90,90,90,-49,90,]),'COMMA':([26,27,31,33,61,63,64,65,66,68,69,70,71,75,76,91,98,100,101,103,104,106,108,110,118,120,123,125,129,131,132,136,137,138,139,140,141,142,148,150,151,152,153,154,155,156,158,161,162,171,184,189,193,202,],[-103,-7,39,-9,-103,-103,-103,-103,-103,-92,-93,-94,-95,-103,-8,-61,-96,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,-103,-103,39,-103,-49,164,-42,-43,-44,-45,173,-63,-66,-70,-80,-85,-91,-90,177,-60,181,-97,164,173,-103,181,]),'CTEINT':([32,34,42,44,45,46,47,48,49,50,51,52,60,61,62,63,64,65,66,67,68,69,70,71,80,90,91,93,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,133,134,150,151,152,153,154,155,156,161,164,170,171,173,175,179,185,194,196,197,198,201,208,209,212,214,216,217,220,221,],[41,69,-89,69,69,69,69,69,69,69,69,69,-103,-103,-37,-103,-103,-103,-103,69,-92,-93,-94,-95,-37,69,-61,69,69,69,69,-96,69,-98,-62,69,-64,-65,69,-67,-68,-69,69,-71,-72,-73,-74,-75,-76,-77,-78,-79,69,-81,-82,-83,-84,69,-86,-87,-88,-103,69,-40,-63,-66,-70,-80,-85,-91,-90,-60,69,69,-97,69,69,-38,-52,-41,69,69,69,-48,-103,-58,-53,-56,69,69,-59,-55,]),'READ':([34,44,45,46,47,48,49,50,51,52,60,61,62,63,64,65,66,68,69,70,71,80,91,98,100,101,103,104,106,108,110,118,120,123,125,129,150,151,152,153,154,155,156,161,171,175,179,185,194,196,197,201,208,209,212,214,216,217,220,221,],[54,54,54,54,54,54,54,54,54,54,-103,-103,-37,-103,-103,-103,-103,-92,-93,-94,-95,-37,-61,-96,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,-103,-63,-66,-70,-80,-85,-91,-90,-60,-97,54,-38,-52,-41,54,54,-48,-103,-58,-53,-56,54,54,-59,-55,]),'WRITE':([34,44,45,46,47,48,49,50,51,52,60,61,62,63,64,65,66,68,69,70,71,80,91,98,100,101,103,104,106,108,110,118,120,123,125,129,150,151,152,153,154,155,156,161,171,175,179,185,194,196,197,201,208,209,212,214,216,217,220,221,],[55,55,55,55,55,55,55,55,55,55,-103,-103,-37,-103,-103,-103,-103,-92,-93,-94,-95,-37,-61,-96,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,-103,-63,-66,-70,-80,-85,-91,-90,-60,-97,55,-38,-52,-41,55,55,-48,-103,-58,-53,-56,55,55,-59,-55,]),'RETURN':([34,44,45,46,47,48,49,50,51,52,60,61,62,63,64,65,66,68,69,70,71,80,91,98,100,101,103,104,106,108,110,118,120,123,125,129,150,151,152,153,154,155,156,161,171,175,179,185,194,196,197,201,208,209,212,214,216,217,220,221,],[56,56,56,56,56,56,56,56,56,56,-103,-103,-37,-103,-103,-103,-103,-92,-93,-94,-95,-37,-61,-96,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,-103,-63,-66,-70,-80,-85,-91,-90,-60,-97,56,-38,-52,-41,56,56,-48,-103,-58,-53,-56,56,56,-59,-55,]),'IF':([34,44,45,46,47,48,49,50,51,52,60,61,62,63,64,65,66,68,69,70,71,80,91,98,100,101,103,104,106,108,110,118,120,123,125,129,150,151,152,153,154,155,156,161,171,175,179,185,194,196,197,201,208,209,212,214,216,217,220,221,],[57,57,57,57,57,57,57,57,57,57,-103,-103,-37,-103,-103,-103,-103,-92,-93,-94,-95,-37,-61,-96,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,-103,-63,-66,-70,-80,-85,-91,-90,-60,-97,57,-38,-52,-41,57,57,-48,-103,-58,-53,-56,57,57,-59,-55,]),'WHILE':([34,44,45,46,47,48,49,50,51,52,60,61,62,63,64,65,66,68,69,70,71,80,91,98,100,101,103,104,106,108,110,118,120,123,125,129,150,151,152,153,154,155,156,161,171,175,179,185,194,196,197,201,208,209,212,214,216,217,220,221,],[58,58,58,58,58,58,58,58,58,58,-103,-103,-37,-103,-103,-103,-103,-92,-93,-94,-95,-37,-61,-96,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,-103,-63,-66,-70,-80,-85,-91,-90,-60,-97,58,-38,-52,-41,58,58,-48,-103,-58,-53,-56,58,58,-59,-55,]),'FOR':([34,44,45,46,47,48,49,50,51,52,60,61,62,63,64,65,66,68,69,70,71,80,91,98,100,101,103,104,106,108,110,118,120,123,125,129,150,151,152,153,154,155,156,161,171,175,179,185,194,196,197,201,208,209,212,214,216,217,220,221,],[59,59,59,59,59,59,59,59,59,59,-103,-103,-37,-103,-103,-103,-103,-92,-93,-94,-95,-37,-61,-96,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,-103,-63,-66,-70,-80,-85,-91,-90,-60,-97,59,-38,-52,-41,59,59,-48,-103,-58,-53,-56,59,59,-59,-55,]),'CTEFLOAT':([34,42,44,45,46,47,48,49,50,51,52,60,61,62,63,64,65,66,67,68,69,70,71,80,90,91,93,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,133,134,150,151,152,153,154,155,156,161,164,170,171,173,175,179,185,194,196,197,198,201,208,209,212,214,216,217,220,221,],[70,-89,70,70,70,70,70,70,70,70,70,-103,-103,-37,-103,-103,-103,-103,70,-92,-93,-94,-95,-37,70,-61,70,70,70,70,-96,70,-98,-62,70,-64,-65,70,-67,-68,-69,70,-71,-72,-73,-74,-75,-76,-77,-78,-79,70,-81,-82,-83,-84,70,-86,-87,-88,-103,70,-40,-63,-66,-70,-80,-85,-91,-90,-60,70,70,-97,70,70,-38,-52,-41,70,70,70,-48,-103,-58,-53,-56,70,70,-59,-55,]),'CTECHAR':([34,42,44,45,46,47,48,49,50,51,52,60,61,62,63,64,65,66,67,68,69,70,71,80,90,91,93,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,133,134,150,151,152,153,154,155,156,161,164,170,171,173,175,179,185,194,196,197,198,201,208,209,212,214,216,217,220,221,],[71,-89,71,71,71,71,71,71,71,71,71,-103,-103,-37,-103,-103,-103,-103,71,-92,-93,-94,-95,-37,71,-61,142,71,71,71,-96,71,-98,-62,71,-64,-65,71,-67,-68,-69,71,-71,-72,-73,-74,-75,-76,-77,-78,-79,71,-81,-82,-83,-84,71,-86,-87,-88,-103,71,-40,-63,-66,-70,-80,-85,-91,-90,-60,142,71,-97,71,71,-38,-52,-41,71,71,71,-48,-103,-58,-53,-56,71,71,-59,-55,]),'RIGHTBR':([34,43,44,45,46,47,48,49,50,51,52,60,61,62,63,64,65,66,68,69,70,71,78,79,80,81,82,83,84,85,86,87,88,91,98,100,101,103,104,106,108,110,118,120,123,125,129,150,151,152,153,154,155,156,161,171,175,179,185,190,194,196,197,201,203,204,208,209,212,214,216,217,218,219,220,221,],[-103,77,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-37,-103,-103,-103,-103,-92,-93,-94,-95,-26,-35,-36,-27,-28,-29,-30,-31,-32,-33,-34,-61,-96,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,-103,-63,-66,-70,-80,-85,-91,-90,-60,-97,-103,-38,-52,200,-41,-103,-103,-48,208,209,-103,-58,-53,-56,-103,-103,220,221,-59,-55,]),'RIGHTSQR':([41,61,63,64,65,66,68,69,70,71,91,98,100,101,103,104,106,108,110,118,120,123,125,129,135,150,151,152,153,154,155,156,161,171,],[76,-103,-103,-103,-103,-103,-92,-93,-94,-95,-61,-96,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,-103,161,-63,-66,-70,-80,-85,-91,-90,-60,-97,]),'EQUAL':([53,60,89,91,97,146,161,],[-103,-39,134,-61,-103,170,-60,]),'TIMES':([60,66,68,69,70,71,91,98,100,129,142,155,156,161,171,],[-103,126,-92,-93,-94,-95,-61,-96,-98,-103,-95,-91,-90,-60,-97,]),'DIVIDE':([60,66,68,69,70,71,91,98,100,129,142,155,156,161,171,],[-103,127,-92,-93,-94,-95,-61,-96,-98,-103,-95,-91,-90,-60,-97,]),'PLUS':([60,65,66,68,69,70,71,91,98,100,123,125,129,142,154,155,156,161,171,],[-103,121,-103,-92,-93,-94,-95,-61,-96,-98,-84,-86,-103,-95,-85,-91,-90,-60,-97,]),'REST':([60,65,66,68,69,70,71,91,98,100,123,125,129,142,154,155,156,161,171,],[-103,122,-103,-92,-93,-94,-95,-61,-96,-98,-84,-86,-103,-95,-85,-91,-90,-60,-97,]),'GREATER':([60,64,65,66,68,69,70,71,91,98,100,118,120,123,125,129,142,153,154,155,156,161,171,],[-103,111,-103,-103,-92,-93,-94,-95,-61,-96,-98,-79,-81,-84,-86,-103,-95,-80,-85,-91,-90,-60,-97,]),'GREATERAND':([60,64,65,66,68,69,70,71,91,98,100,118,120,123,125,129,142,153,154,155,156,161,171,],[-103,112,-103,-103,-92,-93,-94,-95,-61,-96,-98,-79,-81,-84,-86,-103,-95,-80,-85,-91,-90,-60,-97,]),'LESSER':([60,64,65,66,68,69,70,71,91,98,100,118,120,123,125,129,142,153,154,155,156,161,171,],[-103,113,-103,-103,-92,-93,-94,-95,-61,-96,-98,-79,-81,-84,-86,-103,-95,-80,-85,-91,-90,-60,-97,]),'LESSERAND':([60,64,65,66,68,69,70,71,91,98,100,118,120,123,125,129,142,153,154,155,156,161,171,],[-103,114,-103,-103,-92,-93,-94,-95,-61,-96,-98,-79,-81,-84,-86,-103,-95,-80,-85,-91,-90,-60,-97,]),'SAME':([60,64,65,66,68,69,70,71,91,98,100,118,120,123,125,129,142,153,154,155,156,161,171,],[-103,115,-103,-103,-92,-93,-94,-95,-61,-96,-98,-79,-81,-84,-86,-103,-95,-80,-85,-91,-90,-60,-97,]),'NOTSAME':([60,64,65,66,68,69,70,71,91,98,100,118,120,123,125,129,142,153,154,155,156,161,171,],[-103,116,-103,-103,-92,-93,-94,-95,-61,-96,-98,-79,-81,-84,-86,-103,-95,-80,-85,-91,-90,-60,-97,]),'NOT':([60,64,65,66,68,69,70,71,91,98,100,118,120,123,125,129,142,153,154,155,156,161,171,],[-103,117,-103,-103,-92,-93,-94,-95,-61,-96,-98,-79,-81,-84,-86,-103,-95,-80,-85,-91,-90,-60,-97,]),'AND':([60,63,64,65,66,68,69,70,71,91,98,100,108,110,118,120,123,125,129,142,152,153,154,155,156,161,171,],[-103,107,-103,-103,-103,-92,-93,-94,-95,-61,-96,-98,-69,-71,-79,-81,-84,-86,-103,-95,-70,-80,-85,-91,-90,-60,-97,]),'OR':([60,61,63,64,65,66,68,69,70,71,91,98,100,104,106,108,110,118,120,123,125,129,142,151,152,153,154,155,156,161,171,],[-103,102,-103,-103,-103,-103,-92,-93,-94,-95,-61,-96,-98,-65,-67,-69,-71,-79,-81,-84,-86,-103,-95,-66,-70,-80,-85,-91,-90,-60,-97,]),'TO':([61,63,64,65,66,68,69,70,71,91,98,100,101,103,104,106,108,110,118,120,123,125,129,150,151,152,153,154,155,156,161,171,188,],[-103,-103,-103,-103,-103,-92,-93,-94,-95,-61,-96,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,-103,-63,-66,-70,-80,-85,-91,-90,-60,-97,198,]),'DO':([61,63,64,65,66,68,69,70,71,91,98,100,101,103,104,106,108,110,118,120,123,125,129,150,151,152,153,154,155,156,161,169,171,205,],[-103,-103,-103,-103,-103,-92,-93,-94,-95,-61,-96,-98,-62,-64,-65,-67,-69,-71,-79,-81,-84,-86,-103,-63,-66,-70,-80,-85,-91,-90,-60,187,-97,210,]),'STRING':([93,164,],[141,141,]),'THEN':([167,168,],[186,-54,]),'ELSE':([208,],[215,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'neuraltablefunctions':([2,],[3,]),'varsgl':([5,130,],[6,157,]),'empty':([5,6,7,26,30,34,38,44,45,46,47,48,49,50,51,52,53,60,61,63,64,65,66,75,97,99,129,130,131,136,138,148,158,162,175,177,184,189,193,196,197,202,206,208,216,217,],[8,11,14,33,37,62,14,80,80,80,80,80,80,80,80,80,91,91,103,106,110,120,125,33,91,149,91,8,91,91,165,174,178,182,62,37,165,174,91,62,62,182,11,214,62,62,]),'modules':([6,206,],[9,211,]),'vars':([7,38,],[12,74,]),'typing':([7,10,30,38,177,],[13,21,36,13,36,]),'functype':([10,],[19,]),'neuralinsertfuncname':([19,],[24,]),'neuralinsertvar':([22,39,],[26,75,]),'funcparam':([24,],[29,]),'varsarr':([26,75,],[31,132,]),'parameters':([30,177,],[35,191,]),'varsmul':([31,132,],[38,159,]),'statutes':([34,44,45,46,47,48,49,50,51,52,175,196,197,216,217,],[43,79,79,79,79,79,79,79,79,79,190,203,204,218,219,]),'assign':([34,44,45,46,47,48,49,50,51,52,175,196,197,216,217,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'reading':([34,44,45,46,47,48,49,50,51,52,175,196,197,216,217,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'writing':([34,44,45,46,47,48,49,50,51,52,175,196,197,216,217,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'returning':([34,44,45,46,47,48,49,50,51,52,175,196,197,216,217,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'ifing':([34,44,45,46,47,48,49,50,51,52,175,196,197,216,217,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'whiling':([34,44,45,46,47,48,49,50,51,52,175,196,197,216,217,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'foring':([34,44,45,46,47,48,49,50,51,52,175,196,197,216,217,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'exp':([34,44,45,46,47,48,49,50,51,52,67,90,93,94,95,96,99,102,133,164,170,173,175,196,197,198,216,217,],[51,51,51,51,51,51,51,51,51,51,128,135,140,143,144,145,148,150,160,140,188,189,51,51,51,205,51,51,]),'specialfunc':([34,44,45,46,47,48,49,50,51,52,175,196,197,216,217,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'neuralassign1':([34,44,45,46,47,48,49,50,51,52,175,196,197,216,217,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'andexp':([34,44,45,46,47,48,49,50,51,52,67,90,93,94,95,96,99,102,105,133,164,170,173,175,196,197,198,216,217,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,151,61,61,61,61,61,61,61,61,61,61,]),'boolexp':([34,44,45,46,47,48,49,50,51,52,67,90,93,94,95,96,99,102,105,133,164,170,173,175,196,197,198,216,217,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'arithexp':([34,44,45,46,47,48,49,50,51,52,67,90,93,94,95,96,99,102,105,109,119,133,164,170,173,175,196,197,198,216,217,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,152,153,64,64,64,64,64,64,64,64,64,64,]),'geoexp':([34,44,45,46,47,48,49,50,51,52,67,90,93,94,95,96,99,102,105,109,119,124,133,164,170,173,175,196,197,198,216,217,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,154,65,65,65,65,65,65,65,65,65,65,]),'finexp':([34,44,45,46,47,48,49,50,51,52,67,90,93,94,95,96,99,102,105,109,119,124,133,164,170,173,175,196,197,198,216,217,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'addparenth':([34,44,45,46,47,48,49,50,51,52,67,90,93,94,95,96,99,102,105,109,119,124,133,164,170,173,175,196,197,198,216,217,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'cteexp':([34,44,45,46,47,48,49,50,51,52,67,90,93,94,95,96,99,102,105,109,119,124,133,164,170,173,175,196,197,198,216,217,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'statutesaux':([44,45,46,47,48,49,50,51,52,],[78,81,82,83,84,85,86,87,88,]),'idarray':([53,60,97,129,131,136,193,],[89,100,146,100,158,162,202,]),'paramsexp':([60,129,],[98,98,]),'exp1':([61,],[101,]),'andexp1':([63,],[104,]),'neuraland':([63,],[105,]),'boolexp1':([64,],[108,]),'neuralbool':([64,],[109,]),'arithexp1':([65,],[118,]),'neuralarith':([65,],[119,]),'geoexp1':([66,],[123,]),'neuralgeo':([66,],[124,]),'neuralassign2':([89,],[133,]),'neuralread':([92,],[136,]),'auxwrite':([93,164,],[138,184,]),'writetyping':([93,164,],[139,139,]),'paramsexp2':([99,],[147,]),'popparenth':([128,],[155,]),'mulwrite':([138,184,],[163,195,]),'neuralif':([144,],[167,]),'auxparamsexp2':([148,189,],[172,199,]),'mulparams':([158,],[176,]),'mulread':([162,202,],[180,207,]),'neuralendfuncs':([200,],[206,]),'elsing':([208,],[212,]),'neuralelse':([208,],[213,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM neuraltablefunctions SEMICOLON varsgl modules MAIN LEFTPAR RIGHTPAR LEFTBR statutes RIGHTBR','program',11,'p_PROGRAM','myLexerParser.py',467),
  ('neuraltablefunctions -> ID','neuraltablefunctions',1,'p_NEURALTABLEFUNCTIONS','myLexerParser.py',477),
  ('varsgl -> VARS vars','varsgl',2,'p_VARSGL','myLexerParser.py',488),
  ('varsgl -> empty','varsgl',1,'p_VARSGL','myLexerParser.py',489),
  ('vars -> typing COLON neuralinsertvar varsarr varsmul vars','vars',6,'p_VARS','myLexerParser.py',494),
  ('vars -> empty','vars',1,'p_VARS','myLexerParser.py',495),
  ('neuralinsertvar -> ID','neuralinsertvar',1,'p_NEURALINSERTVAR','myLexerParser.py',500),
  ('varsarr -> LEFTSQR CTEINT RIGHTSQR','varsarr',3,'p_VARSARR','myLexerParser.py',509),
  ('varsarr -> empty','varsarr',1,'p_VARSARR','myLexerParser.py',510),
  ('varsmul -> COMMA neuralinsertvar varsarr varsmul','varsmul',4,'p_VARSMUL','myLexerParser.py',515),
  ('varsmul -> SEMICOLON','varsmul',1,'p_VARSMUL','myLexerParser.py',516),
  ('modules -> FUNCTION functype neuralinsertfuncname funcparam','modules',4,'p_MODULES','myLexerParser.py',530),
  ('modules -> empty','modules',1,'p_MODULES','myLexerParser.py',531),
  ('neuralinsertfuncname -> ID','neuralinsertfuncname',1,'p_NEURALINSERTFUNCNAME','myLexerParser.py',536),
  ('functype -> VOID','functype',1,'p_FUNCTYPE','myLexerParser.py',546),
  ('functype -> typing','functype',1,'p_FUNCTYPE','myLexerParser.py',547),
  ('funcparam -> LEFTPAR parameters RIGHTPAR SEMICOLON varsgl LEFTBR statutes RIGHTBR neuralendfuncs modules','funcparam',10,'p_FUNCPARAM','myLexerParser.py',553),
  ('neuralendfuncs -> <empty>','neuralendfuncs',0,'p_NEURALENDFUNCS','myLexerParser.py',558),
  ('typing -> INT','typing',1,'p_TYPING','myLexerParser.py',564),
  ('typing -> FLOAT','typing',1,'p_TYPING','myLexerParser.py',565),
  ('typing -> CHAR','typing',1,'p_TYPING','myLexerParser.py',566),
  ('parameters -> typing COLON ID idarray mulparams','parameters',5,'p_PARAMETERS','myLexerParser.py',573),
  ('parameters -> empty','parameters',1,'p_PARAMETERS','myLexerParser.py',574),
  ('mulparams -> COMMA parameters','mulparams',2,'p_MULPARAMS','myLexerParser.py',579),
  ('mulparams -> empty','mulparams',1,'p_MULPARAMS','myLexerParser.py',580),
  ('statutes -> assign statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',598),
  ('statutes -> reading statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',599),
  ('statutes -> writing statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',600),
  ('statutes -> returning statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',601),
  ('statutes -> ifing statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',602),
  ('statutes -> whiling statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',603),
  ('statutes -> foring statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',604),
  ('statutes -> exp statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',605),
  ('statutes -> specialfunc statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',606),
  ('statutesaux -> statutes','statutesaux',1,'p_STATUTESAUX','myLexerParser.py',611),
  ('statutesaux -> empty','statutesaux',1,'p_STATUTESAUX','myLexerParser.py',612),
  ('specialfunc -> empty','specialfunc',1,'p_SPECIALFUNC','myLexerParser.py',617),
  ('assign -> neuralassign1 idarray neuralassign2 exp SEMICOLON','assign',5,'p_ASSIGN','myLexerParser.py',631),
  ('neuralassign1 -> ID','neuralassign1',1,'p_NEURALASSIGN1','myLexerParser.py',647),
  ('neuralassign2 -> EQUAL','neuralassign2',1,'p_NEURALASSIGN2','myLexerParser.py',658),
  ('writing -> WRITE LEFTPAR auxwrite mulwrite RIGHTPAR SEMICOLON','writing',6,'p_WRITING','myLexerParser.py',668),
  ('auxwrite -> writetyping','auxwrite',1,'p_AUXWRITE','myLexerParser.py',673),
  ('auxwrite -> exp','auxwrite',1,'p_AUXWRITE','myLexerParser.py',674),
  ('writetyping -> STRING','writetyping',1,'p_WRITETYPING','myLexerParser.py',682),
  ('writetyping -> CTECHAR','writetyping',1,'p_WRITETYPING','myLexerParser.py',683),
  ('mulwrite -> COMMA auxwrite mulwrite','mulwrite',3,'p_MULWRITE','myLexerParser.py',690),
  ('mulwrite -> empty','mulwrite',1,'p_MULWRITE','myLexerParser.py',691),
  ('reading -> READ LEFTPAR neuralread idarray mulread RIGHTPAR SEMICOLON','reading',7,'p_READING','myLexerParser.py',698),
  ('neuralread -> ID','neuralread',1,'p_NEURALREAD','myLexerParser.py',703),
  ('mulread -> COMMA ID idarray mulread','mulread',4,'p_MULREAD','myLexerParser.py',711),
  ('mulread -> empty','mulread',1,'p_MULREAD','myLexerParser.py',712),
  ('returning -> RETURN LEFTPAR exp RIGHTPAR SEMICOLON','returning',5,'p_RETURNING','myLexerParser.py',719),
  ('ifing -> IF LEFTPAR exp neuralif THEN LEFTBR statutes RIGHTBR elsing','ifing',9,'p_IFING','myLexerParser.py',735),
  ('neuralif -> RIGHTPAR','neuralif',1,'p_NEURALIF','myLexerParser.py',745),
  ('elsing -> neuralelse LEFTBR statutes RIGHTBR','elsing',4,'p_ELSING','myLexerParser.py',759),
  ('elsing -> empty','elsing',1,'p_ELSING','myLexerParser.py',760),
  ('neuralelse -> ELSE','neuralelse',1,'p_NEURALELSE','myLexerParser.py',765),
  ('whiling -> WHILE LEFTPAR exp RIGHTPAR DO LEFTBR statutes RIGHTBR','whiling',8,'p_WHILING','myLexerParser.py',783),
  ('foring -> FOR ID idarray EQUAL exp TO exp DO LEFTBR statutes RIGHTBR','foring',11,'p_FORING','myLexerParser.py',790),
  ('idarray -> LEFTSQR exp RIGHTSQR','idarray',3,'p_IDARRAY','myLexerParser.py',799),
  ('idarray -> empty','idarray',1,'p_IDARRAY','myLexerParser.py',800),
  ('exp -> andexp exp1','exp',2,'p_EXP','myLexerParser.py',809),
  ('exp1 -> OR exp','exp1',2,'p_EXP1','myLexerParser.py',814),
  ('exp1 -> empty','exp1',1,'p_EXP1','myLexerParser.py',815),
  ('andexp -> boolexp andexp1','andexp',2,'p_ANDEXP','myLexerParser.py',820),
  ('andexp1 -> neuraland andexp','andexp1',2,'p_ANDEXP1','myLexerParser.py',825),
  ('andexp1 -> empty','andexp1',1,'p_ANDEXP1','myLexerParser.py',826),
  ('neuraland -> AND','neuraland',1,'p_NEURALAND','myLexerParser.py',831),
  ('boolexp -> arithexp boolexp1','boolexp',2,'p_BOOLEXP','myLexerParser.py',844),
  ('boolexp1 -> neuralbool arithexp','boolexp1',2,'p_BOOLEXP1','myLexerParser.py',869),
  ('boolexp1 -> empty','boolexp1',1,'p_BOOLEXP1','myLexerParser.py',870),
  ('neuralbool -> GREATER','neuralbool',1,'p_NEURALBOOL','myLexerParser.py',875),
  ('neuralbool -> GREATERAND','neuralbool',1,'p_NEURALBOOL','myLexerParser.py',876),
  ('neuralbool -> LESSER','neuralbool',1,'p_NEURALBOOL','myLexerParser.py',877),
  ('neuralbool -> LESSERAND','neuralbool',1,'p_NEURALBOOL','myLexerParser.py',878),
  ('neuralbool -> SAME','neuralbool',1,'p_NEURALBOOL','myLexerParser.py',879),
  ('neuralbool -> NOTSAME','neuralbool',1,'p_NEURALBOOL','myLexerParser.py',880),
  ('neuralbool -> NOT','neuralbool',1,'p_NEURALBOOL','myLexerParser.py',881),
  ('arithexp -> geoexp arithexp1','arithexp',2,'p_ARITHEXP','myLexerParser.py',894),
  ('arithexp1 -> neuralarith arithexp','arithexp1',2,'p_ARITHEXP1','myLexerParser.py',916),
  ('arithexp1 -> empty','arithexp1',1,'p_ARITHEXP1','myLexerParser.py',917),
  ('neuralarith -> PLUS','neuralarith',1,'p_NEURALARITH','myLexerParser.py',922),
  ('neuralarith -> REST','neuralarith',1,'p_NEURALARITH','myLexerParser.py',923),
  ('geoexp -> finexp geoexp1','geoexp',2,'p_GEOEXP','myLexerParser.py',934),
  ('geoexp1 -> neuralgeo geoexp','geoexp1',2,'p_GEOEXP1','myLexerParser.py',955),
  ('geoexp1 -> empty','geoexp1',1,'p_GEOEXP1','myLexerParser.py',956),
  ('neuralgeo -> TIMES','neuralgeo',1,'p_NEURALGEO','myLexerParser.py',961),
  ('neuralgeo -> DIVIDE','neuralgeo',1,'p_NEURALGEO','myLexerParser.py',962),
  ('addparenth -> LEFTPAR','addparenth',1,'p_ADDPARENTH','myLexerParser.py',972),
  ('popparenth -> RIGHTPAR','popparenth',1,'p_POPPARENTH','myLexerParser.py',980),
  ('finexp -> addparenth exp popparenth','finexp',3,'p_FINEXP','myLexerParser.py',987),
  ('finexp -> cteexp','finexp',1,'p_FINEXP','myLexerParser.py',988),
  ('cteexp -> CTEINT','cteexp',1,'p_CTEEXP','myLexerParser.py',1016),
  ('cteexp -> CTEFLOAT','cteexp',1,'p_CTEEXP','myLexerParser.py',1017),
  ('cteexp -> CTECHAR','cteexp',1,'p_CTEEXP','myLexerParser.py',1018),
  ('cteexp -> ID paramsexp','cteexp',2,'p_CTEEXP','myLexerParser.py',1019),
  ('paramsexp -> LEFTPAR paramsexp2 RIGHTPAR','paramsexp',3,'p_PARAMSEXP','myLexerParser.py',1032),
  ('paramsexp -> idarray','paramsexp',1,'p_PARAMSEXP','myLexerParser.py',1033),
  ('paramsexp2 -> exp auxparamsexp2','paramsexp2',2,'p_PARAMSEXP2','myLexerParser.py',1038),
  ('paramsexp2 -> empty','paramsexp2',1,'p_PARAMSEXP2','myLexerParser.py',1039),
  ('auxparamsexp2 -> COMMA exp auxparamsexp2','auxparamsexp2',3,'p_AUXPARAMSEXP2','myLexerParser.py',1044),
  ('auxparamsexp2 -> empty','auxparamsexp2',1,'p_AUXPARAMSEXP2','myLexerParser.py',1045),
  ('empty -> <empty>','empty',0,'p_empty','myLexerParser.py',1051),
  ('debug -> empty','debug',1,'p_DEBUG','myLexerParser.py',1063),
]
