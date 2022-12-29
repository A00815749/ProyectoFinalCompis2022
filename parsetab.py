
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'STRING ID PLUS REST TIMES DIVIDE GREATER GREATERAND LESSER LESSERAND SAME NOTSAME NOT EQUAL LEFTBR RIGHTBR LEFTPAR RIGHTPAR LEFTSQR RIGHTSQR COLON SEMICOLON COMMA CTEINT CTEFLOAT CTECHAR PROGRAM MAIN FUNCTION VARS INT FLOAT CHAR STR RETURN READ WRITE AND OR IF THEN ELSE WHILE DO FOR TO VOID TRUE FALSE MEDIA MEDIANA MODA VARIANZA STDEV PLOTXY\n    program : PROGRAM ID neuraltablefunctions SEMICOLON varsgl modules MAIN LEFTPAR RIGHTPAR LEFTBR statutes RIGHTBR\n    \n    neuraltablefunctions :\n    \n    varsgl : VARS vars\n            | empty\n    \n    vars : typing COLON ID varsarr varsmul vars\n            | empty\n    \n    varsarr : LEFTSQR CTEINT RIGHTSQR\n        | empty\n    \n    varsmul : COMMA ID varsarr varsmul\n            | SEMICOLON\n    \n    modules : FUNCTION functype ID funcparam\n            | empty\n    \n    functype : VOID\n            | typing\n    \n    funcparam : LEFTPAR parameters RIGHTPAR SEMICOLON varsgl LEFTBR statutes RIGHTBR modules\n    \n    typing : INT\n            | FLOAT\n            | CHAR\n    \n    parameters : typing COLON ID idarray mulparams\n            | empty\n    \n    mulparams : COMMA parameters\n            | empty\n    \n    statutes : assign statutesaux\n            | reading statutesaux\n            | writing statutesaux\n            | returning statutesaux\n            | ifing statutesaux\n            | whiling statutesaux\n            | foring statutesaux\n            | exp statutesaux\n            | specialfunc statutesaux\n    \n    statutesaux :\n    \n    specialfunc : empty\n    \n    assign : ID idarray EQUAL exp SEMICOLON\n    \n    writing : WRITE LEFTPAR auxwrite mulwrite RIGHTPAR SEMICOLON\n    \n    auxwrite : writetyping\n            | exp\n    \n    writetyping : STRING\n            | CTECHAR\n    \n    mulwrite : COMMA auxwrite mulwrite\n            | empty\n    \n    reading : READ LEFTPAR ID idarray mulread RIGHTPAR SEMICOLON\n    \n    mulread : COMMA ID idarray mulread\n            | empty\n    \n    returning : RETURN LEFTPAR exp RIGHTPAR SEMICOLON\n    \n    ifing : IF LEFTPAR exp RIGHTPAR THEN LEFTBR statutes RIGHTBR elsing\n    \n    elsing : ELSE LEFTBR statutes RIGHTBR\n            | empty\n    \n    whiling : WHILE LEFTPAR exp RIGHTPAR DO LEFTBR statutes RIGHTBR\n    \n    foring : FOR ID idarray EQUAL exp TO exp DO LEFTBR statutes RIGHTBR\n    \n    idarray : LEFTSQR exp RIGHTSQR\n            | empty\n    \n    exp : andexp exp1\n    \n    exp1 : OR exp\n        | empty\n    \n    andexp : boolexp andexp1\n    \n    andexp1 : AND andexp\n        | empty\n    \n    boolexp : arithexp boolexp1\n    \n    boolexp1 : GREATER arithexp\n        | GREATERAND arithexp\n        | LESSER arithexp\n        | LESSERAND arithexp\n        | SAME arithexp\n        | NOTSAME arithexp\n        | NOT arithexp\n        | empty\n    \n    arithexp : geoexp arithexp1\n    \n    arithexp1 : PLUS arithexp\n        | REST arithexp\n        | empty\n    \n    geoexp : finexp geoexp1\n    \n    geoexp1 : TIMES geoexp\n        | DIVIDE geoexp\n        | empty\n    \n    finexp : LEFTPAR exp RIGHTPAR\n            | cteexp\n    \n    cteexp : CTEINT\n            | CTEFLOAT\n            | CTECHAR\n            | ID paramsexp\n    \n    paramsexp : LEFTPAR paramsexp2 RIGHTPAR\n                | idarray\n    \n    paramsexp2 : exp auxparamsexp2\n            | empty\n    \n    auxparamsexp2 : COMMA exp auxparamsexp2\n            | empty\n    \n    empty : \n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,80,],[0,-1,]),'ID':([2,15,16,17,19,20,21,22,32,37,41,57,69,75,77,90,91,92,93,94,97,100,103,104,105,106,107,108,109,112,113,116,117,122,159,163,168,169,176,191,192,193,208,209,],[3,-16,-17,-18,24,-13,-14,25,40,71,79,95,120,79,79,129,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,40,188,40,40,79,40,40,]),'SEMICOLON':([3,4,25,29,31,58,60,61,62,63,64,65,66,67,68,71,72,74,76,79,96,98,99,101,102,110,111,114,115,118,121,127,128,139,140,141,142,143,144,145,146,147,148,149,150,151,155,156,157,165,178,187,],[-2,5,-88,38,-8,-88,-88,-88,-88,-88,-77,-78,-79,-80,119,-88,-7,-81,-52,-88,-53,-55,-56,-58,-59,-67,-68,-71,-72,-75,38,-76,-83,-54,-57,-60,-61,-62,-63,-64,-65,-66,-69,-70,-73,-74,173,-51,-82,180,189,195,]),'VARS':([5,119,],[7,7,]),'FUNCTION':([5,6,7,8,12,14,36,38,70,154,194,],[-88,10,-88,-4,-3,-6,-88,-10,-5,-9,10,]),'MAIN':([5,6,7,8,9,11,12,14,27,36,38,70,154,194,200,],[-88,-88,-88,-4,18,-12,-3,-6,-11,-88,-10,-5,-9,-88,-15,]),'INT':([7,10,28,36,38,154,171,],[15,15,15,15,-10,-9,15,]),'FLOAT':([7,10,28,36,38,154,171,],[16,16,16,16,-10,-9,16,]),'CHAR':([7,10,28,36,38,154,171,],[17,17,17,17,-10,-9,17,]),'LEFTBR':([7,8,12,14,26,36,38,70,119,152,154,181,182,204,206,],[-88,-4,-3,-6,32,-88,-10,-5,-88,169,-9,191,192,208,209,]),'VOID':([10,],[20,]),'COLON':([13,15,16,17,34,],[22,-16,-17,-18,69,]),'LEFTPAR':([18,24,32,40,41,52,53,54,55,56,75,77,79,91,92,93,94,97,100,103,104,105,106,107,108,109,112,113,116,117,122,159,163,168,169,191,192,193,208,209,],[23,28,41,77,41,90,91,92,93,94,41,41,77,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'RIGHTPAR':([23,28,33,35,58,60,61,62,63,64,65,66,67,74,76,77,78,79,96,98,99,101,102,110,111,114,115,118,120,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,143,144,145,146,147,148,149,150,151,153,156,157,158,160,161,162,164,170,171,172,174,175,177,179,185,186,188,190,196,201,],[26,-88,68,-20,-88,-88,-88,-88,-88,-77,-78,-79,-80,-81,-52,-88,127,-88,-53,-55,-56,-58,-59,-67,-68,-71,-72,-75,-88,157,-88,-85,-76,-83,-88,-88,-36,-37,-38,-39,165,166,167,-54,-57,-60,-61,-62,-63,-64,-65,-66,-69,-70,-73,-74,-88,-51,-82,-84,-87,-88,178,-41,-19,-88,-22,-88,187,-44,-88,-21,-86,-88,-40,-88,-43,]),'LEFTSQR':([25,40,71,79,95,120,129,188,],[30,75,30,75,75,75,75,75,]),'COMMA':([25,29,31,58,60,61,62,63,64,65,66,67,71,72,74,76,79,96,98,99,101,102,110,111,114,115,118,120,121,125,127,128,129,130,131,132,133,134,139,140,141,142,143,144,145,146,147,148,149,150,151,153,156,157,161,174,179,188,196,],[-88,37,-8,-88,-88,-88,-88,-88,-77,-78,-79,-80,-88,-7,-81,-52,-88,-53,-55,-56,-58,-59,-67,-68,-71,-72,-75,-88,37,159,-76,-83,-88,163,-36,-37,-38,-39,-54,-57,-60,-61,-62,-63,-64,-65,-66,-69,-70,-73,-74,171,-51,-82,176,159,163,-88,176,]),'CTEINT':([30,32,41,75,77,91,92,93,94,97,100,103,104,105,106,107,108,109,112,113,116,117,122,159,163,168,169,191,192,193,208,209,],[39,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'READ':([32,169,191,192,208,209,],[52,52,52,52,52,52,]),'WRITE':([32,169,191,192,208,209,],[53,53,53,53,53,53,]),'RETURN':([32,169,191,192,208,209,],[54,54,54,54,54,54,]),'IF':([32,169,191,192,208,209,],[55,55,55,55,55,55,]),'WHILE':([32,169,191,192,208,209,],[56,56,56,56,56,56,]),'FOR':([32,169,191,192,208,209,],[57,57,57,57,57,57,]),'RIGHTBR':([32,40,42,43,44,45,46,47,48,49,50,51,58,59,60,61,62,63,64,65,66,67,73,74,76,79,81,82,83,84,85,86,87,88,89,96,98,99,101,102,110,111,114,115,118,127,128,139,140,141,142,143,144,145,146,147,148,149,150,151,156,157,169,173,180,184,189,191,192,195,197,198,202,203,205,207,208,209,210,211,212,213,],[-88,-88,80,-32,-32,-32,-32,-32,-32,-32,-32,-32,-88,-33,-88,-88,-88,-88,-77,-78,-79,-80,-83,-81,-52,-88,-23,-24,-25,-26,-27,-28,-29,-30,-31,-53,-55,-56,-58,-59,-67,-68,-71,-72,-75,-76,-83,-54,-57,-60,-61,-62,-63,-64,-65,-66,-69,-70,-73,-74,-51,-82,-88,-34,-45,194,-35,-88,-88,-42,202,203,-88,-49,-46,-48,-88,-88,212,213,-50,-47,]),'CTEFLOAT':([32,41,75,77,91,92,93,94,97,100,103,104,105,106,107,108,109,112,113,116,117,122,159,163,168,169,191,192,193,208,209,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'CTECHAR':([32,41,75,77,91,92,93,94,97,100,103,104,105,106,107,108,109,112,113,116,117,122,159,163,168,169,191,192,193,208,209,],[67,67,67,67,134,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,134,67,67,67,67,67,67,67,]),'RIGHTSQR':([39,58,60,61,62,63,64,65,66,67,74,76,79,96,98,99,101,102,110,111,114,115,118,123,127,128,139,140,141,142,143,144,145,146,147,148,149,150,151,156,157,],[72,-88,-88,-88,-88,-88,-77,-78,-79,-80,-81,-52,-88,-53,-55,-56,-58,-59,-67,-68,-71,-72,-75,156,-76,-83,-54,-57,-60,-61,-62,-63,-64,-65,-66,-69,-70,-73,-74,-51,-82,]),'EQUAL':([40,73,76,95,138,156,],[-88,122,-52,-88,168,-51,]),'TIMES':([40,63,64,65,66,67,73,74,76,79,127,128,134,156,157,],[-88,116,-77,-78,-79,-80,-83,-81,-52,-88,-76,-83,-80,-51,-82,]),'DIVIDE':([40,63,64,65,66,67,73,74,76,79,127,128,134,156,157,],[-88,117,-77,-78,-79,-80,-83,-81,-52,-88,-76,-83,-80,-51,-82,]),'PLUS':([40,62,63,64,65,66,67,73,74,76,79,115,118,127,128,134,150,151,156,157,],[-88,112,-88,-77,-78,-79,-80,-83,-81,-52,-88,-72,-75,-76,-83,-80,-73,-74,-51,-82,]),'REST':([40,62,63,64,65,66,67,73,74,76,79,115,118,127,128,134,150,151,156,157,],[-88,113,-88,-77,-78,-79,-80,-83,-81,-52,-88,-72,-75,-76,-83,-80,-73,-74,-51,-82,]),'GREATER':([40,61,62,63,64,65,66,67,73,74,76,79,111,114,115,118,127,128,134,148,149,150,151,156,157,],[-88,103,-88,-88,-77,-78,-79,-80,-83,-81,-52,-88,-68,-71,-72,-75,-76,-83,-80,-69,-70,-73,-74,-51,-82,]),'GREATERAND':([40,61,62,63,64,65,66,67,73,74,76,79,111,114,115,118,127,128,134,148,149,150,151,156,157,],[-88,104,-88,-88,-77,-78,-79,-80,-83,-81,-52,-88,-68,-71,-72,-75,-76,-83,-80,-69,-70,-73,-74,-51,-82,]),'LESSER':([40,61,62,63,64,65,66,67,73,74,76,79,111,114,115,118,127,128,134,148,149,150,151,156,157,],[-88,105,-88,-88,-77,-78,-79,-80,-83,-81,-52,-88,-68,-71,-72,-75,-76,-83,-80,-69,-70,-73,-74,-51,-82,]),'LESSERAND':([40,61,62,63,64,65,66,67,73,74,76,79,111,114,115,118,127,128,134,148,149,150,151,156,157,],[-88,106,-88,-88,-77,-78,-79,-80,-83,-81,-52,-88,-68,-71,-72,-75,-76,-83,-80,-69,-70,-73,-74,-51,-82,]),'SAME':([40,61,62,63,64,65,66,67,73,74,76,79,111,114,115,118,127,128,134,148,149,150,151,156,157,],[-88,107,-88,-88,-77,-78,-79,-80,-83,-81,-52,-88,-68,-71,-72,-75,-76,-83,-80,-69,-70,-73,-74,-51,-82,]),'NOTSAME':([40,61,62,63,64,65,66,67,73,74,76,79,111,114,115,118,127,128,134,148,149,150,151,156,157,],[-88,108,-88,-88,-77,-78,-79,-80,-83,-81,-52,-88,-68,-71,-72,-75,-76,-83,-80,-69,-70,-73,-74,-51,-82,]),'NOT':([40,61,62,63,64,65,66,67,73,74,76,79,111,114,115,118,127,128,134,148,149,150,151,156,157,],[-88,109,-88,-88,-77,-78,-79,-80,-83,-81,-52,-88,-68,-71,-72,-75,-76,-83,-80,-69,-70,-73,-74,-51,-82,]),'AND':([40,60,61,62,63,64,65,66,67,73,74,76,79,102,110,111,114,115,118,127,128,134,141,142,143,144,145,146,147,148,149,150,151,156,157,],[-88,100,-88,-88,-88,-77,-78,-79,-80,-83,-81,-52,-88,-59,-67,-68,-71,-72,-75,-76,-83,-80,-60,-61,-62,-63,-64,-65,-66,-69,-70,-73,-74,-51,-82,]),'OR':([40,58,60,61,62,63,64,65,66,67,73,74,76,79,99,101,102,110,111,114,115,118,127,128,134,140,141,142,143,144,145,146,147,148,149,150,151,156,157,],[-88,97,-88,-88,-88,-88,-77,-78,-79,-80,-83,-81,-52,-88,-56,-58,-59,-67,-68,-71,-72,-75,-76,-83,-80,-57,-60,-61,-62,-63,-64,-65,-66,-69,-70,-73,-74,-51,-82,]),'TO':([58,60,61,62,63,64,65,66,67,74,76,79,96,98,99,101,102,110,111,114,115,118,127,128,139,140,141,142,143,144,145,146,147,148,149,150,151,156,157,183,],[-88,-88,-88,-88,-88,-77,-78,-79,-80,-81,-52,-88,-53,-55,-56,-58,-59,-67,-68,-71,-72,-75,-76,-83,-54,-57,-60,-61,-62,-63,-64,-65,-66,-69,-70,-73,-74,-51,-82,193,]),'DO':([58,60,61,62,63,64,65,66,67,74,76,79,96,98,99,101,102,110,111,114,115,118,127,128,139,140,141,142,143,144,145,146,147,148,149,150,151,156,157,167,199,],[-88,-88,-88,-88,-88,-77,-78,-79,-80,-81,-52,-88,-53,-55,-56,-58,-59,-67,-68,-71,-72,-75,-76,-83,-54,-57,-60,-61,-62,-63,-64,-65,-66,-69,-70,-73,-74,-51,-82,182,204,]),'STRING':([91,163,],[133,133,]),'THEN':([166,],[181,]),'ELSE':([202,],[206,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'neuraltablefunctions':([3,],[4,]),'varsgl':([5,119,],[6,152,]),'empty':([5,6,7,25,28,32,36,40,58,60,61,62,63,71,77,79,95,119,120,125,129,130,153,161,169,171,174,179,188,191,192,194,196,202,208,209,],[8,11,14,31,35,59,14,76,98,101,110,114,118,31,126,76,76,8,76,160,76,164,172,177,59,35,160,164,76,59,59,11,177,207,59,59,]),'modules':([6,194,],[9,200,]),'vars':([7,36,],[12,70,]),'typing':([7,10,28,36,171,],[13,21,34,13,34,]),'functype':([10,],[19,]),'funcparam':([24,],[27,]),'varsarr':([25,71,],[29,121,]),'parameters':([28,171,],[33,185,]),'varsmul':([29,121,],[36,154,]),'statutes':([32,169,191,192,208,209,],[42,184,197,198,210,211,]),'assign':([32,169,191,192,208,209,],[43,43,43,43,43,43,]),'reading':([32,169,191,192,208,209,],[44,44,44,44,44,44,]),'writing':([32,169,191,192,208,209,],[45,45,45,45,45,45,]),'returning':([32,169,191,192,208,209,],[46,46,46,46,46,46,]),'ifing':([32,169,191,192,208,209,],[47,47,47,47,47,47,]),'whiling':([32,169,191,192,208,209,],[48,48,48,48,48,48,]),'foring':([32,169,191,192,208,209,],[49,49,49,49,49,49,]),'exp':([32,41,75,77,91,92,93,94,97,122,159,163,168,169,191,192,193,208,209,],[50,78,123,125,132,135,136,137,139,155,174,132,183,50,50,50,199,50,50,]),'specialfunc':([32,169,191,192,208,209,],[51,51,51,51,51,51,]),'andexp':([32,41,75,77,91,92,93,94,97,100,122,159,163,168,169,191,192,193,208,209,],[58,58,58,58,58,58,58,58,58,140,58,58,58,58,58,58,58,58,58,58,]),'boolexp':([32,41,75,77,91,92,93,94,97,100,122,159,163,168,169,191,192,193,208,209,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'arithexp':([32,41,75,77,91,92,93,94,97,100,103,104,105,106,107,108,109,112,113,122,159,163,168,169,191,192,193,208,209,],[61,61,61,61,61,61,61,61,61,61,141,142,143,144,145,146,147,148,149,61,61,61,61,61,61,61,61,61,61,]),'geoexp':([32,41,75,77,91,92,93,94,97,100,103,104,105,106,107,108,109,112,113,116,117,122,159,163,168,169,191,192,193,208,209,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,150,151,62,62,62,62,62,62,62,62,62,62,]),'finexp':([32,41,75,77,91,92,93,94,97,100,103,104,105,106,107,108,109,112,113,116,117,122,159,163,168,169,191,192,193,208,209,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'cteexp':([32,41,75,77,91,92,93,94,97,100,103,104,105,106,107,108,109,112,113,116,117,122,159,163,168,169,191,192,193,208,209,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'idarray':([40,79,95,120,129,188,],[73,128,138,153,161,196,]),'paramsexp':([40,79,],[74,74,]),'statutesaux':([43,44,45,46,47,48,49,50,51,],[81,82,83,84,85,86,87,88,89,]),'exp1':([58,],[96,]),'andexp1':([60,],[99,]),'boolexp1':([61,],[102,]),'arithexp1':([62,],[111,]),'geoexp1':([63,],[115,]),'paramsexp2':([77,],[124,]),'auxwrite':([91,163,],[130,179,]),'writetyping':([91,163,],[131,131,]),'auxparamsexp2':([125,174,],[158,186,]),'mulwrite':([130,179,],[162,190,]),'mulparams':([153,],[170,]),'mulread':([161,196,],[175,201,]),'elsing':([202,],[205,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID neuraltablefunctions SEMICOLON varsgl modules MAIN LEFTPAR RIGHTPAR LEFTBR statutes RIGHTBR','program',12,'p_PROGRAM','myLexerParser.py',251),
  ('neuraltablefunctions -> <empty>','neuraltablefunctions',0,'p_NEURALTABLEFUNCTIONS','myLexerParser.py',257),
  ('varsgl -> VARS vars','varsgl',2,'p_VARSGL','myLexerParser.py',265),
  ('varsgl -> empty','varsgl',1,'p_VARSGL','myLexerParser.py',266),
  ('vars -> typing COLON ID varsarr varsmul vars','vars',6,'p_VARS','myLexerParser.py',271),
  ('vars -> empty','vars',1,'p_VARS','myLexerParser.py',272),
  ('varsarr -> LEFTSQR CTEINT RIGHTSQR','varsarr',3,'p_VARSARR','myLexerParser.py',277),
  ('varsarr -> empty','varsarr',1,'p_VARSARR','myLexerParser.py',278),
  ('varsmul -> COMMA ID varsarr varsmul','varsmul',4,'p_VARSMUL','myLexerParser.py',283),
  ('varsmul -> SEMICOLON','varsmul',1,'p_VARSMUL','myLexerParser.py',284),
  ('modules -> FUNCTION functype ID funcparam','modules',4,'p_MODULES','myLexerParser.py',292),
  ('modules -> empty','modules',1,'p_MODULES','myLexerParser.py',293),
  ('functype -> VOID','functype',1,'p_FUNCTYPE','myLexerParser.py',298),
  ('functype -> typing','functype',1,'p_FUNCTYPE','myLexerParser.py',299),
  ('funcparam -> LEFTPAR parameters RIGHTPAR SEMICOLON varsgl LEFTBR statutes RIGHTBR modules','funcparam',9,'p_FUNCPARAM','myLexerParser.py',304),
  ('typing -> INT','typing',1,'p_TYPING','myLexerParser.py',309),
  ('typing -> FLOAT','typing',1,'p_TYPING','myLexerParser.py',310),
  ('typing -> CHAR','typing',1,'p_TYPING','myLexerParser.py',311),
  ('parameters -> typing COLON ID idarray mulparams','parameters',5,'p_PARAMETERS','myLexerParser.py',316),
  ('parameters -> empty','parameters',1,'p_PARAMETERS','myLexerParser.py',317),
  ('mulparams -> COMMA parameters','mulparams',2,'p_MULPARAMS','myLexerParser.py',322),
  ('mulparams -> empty','mulparams',1,'p_MULPARAMS','myLexerParser.py',323),
  ('statutes -> assign statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',330),
  ('statutes -> reading statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',331),
  ('statutes -> writing statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',332),
  ('statutes -> returning statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',333),
  ('statutes -> ifing statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',334),
  ('statutes -> whiling statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',335),
  ('statutes -> foring statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',336),
  ('statutes -> exp statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',337),
  ('statutes -> specialfunc statutesaux','statutes',2,'p_STATUTES','myLexerParser.py',338),
  ('statutesaux -> <empty>','statutesaux',0,'p_STATUTESAUX','myLexerParser.py',343),
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
]
