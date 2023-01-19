# ProyectoFinalCompis2022
 Proyecto Final para la materia de Compiladores en donde se tiene que crear un compilador adjunto con una maquina virtual basado en una propuesta de proyecto

Diciembre 1 Agregando el documento de propuesta de proyecto en la que se basara todo el programa, similar a los que intente construir los pasados semestres con el mismo lenguaje, pero esta vez trabajando desde la base sin guiarme en otros proyectos. Importando el lexer y parser simplificado de pasados proyectos.

Diciembre 2 Revisando el lenguaje base para ver si tiene sentido, revision del cubo semantico y arreglos.

Diciembre 20 ~ Diciembre 29 Revision de la sintaxis y de bugs, arreglo de estos, codificiacion y revision de la creacion de la tabla de funciones simple, junto con la adicion de la tabla de variables global y local

Diciembre 30 ~ Enero 6 Arreglo del guardado de variables locales, inicializacion de logica de aritmetica y expresiones, inicio del uso de bloques de memoria virtuales, agregado de fondos falsos para el manejo de parentesis en expresiones, agregar la seccion de lectura, escritura, asignacion y de decision if-else

Enero 7 ~ 10 Inicio de la maquina virtual, agregado de la seccion de ciclos while y for, manejando la parte inicial de la logica de funciones, revision de la mapa de memoria de ejecucion de la maquina virtual

Enero 11 ~ 12 Avance de la maquina virtual con secciones de los booleanos y saltos, con secciones iniciales de parametros de funciones, Debuggeo de la PilaO y descubrimiento de la falta de guardado de expresiones constantes y la necesidad de guardar ciertos tokens en la gramatica.

Enero 13 Agregado de la logica inicial de vectores, debuggeo de la seccion de parametros y primeros exitos corriendo el archivo de stress para funciones. 

Enero 14 Intentos varios de hacer funcionar vectores, revision de los otros documentos de prueba

Enero 15 Se logro terminar todo excepto vectores, se concentro en documentacion y se hizo una primera entrega

Enero 17 ~ 18 Se siguio trabajando en vectores


## SECTION FOR PENDING PROBLEMS TO CHECK BETWEEN CODING SESSIONS ###
 VECTORS PART IN THE VM IS ADVANCING, THERE ARE NO PROBLEMS STORING THE ADDRESSES AT THE POINTERS, AND THE NUM VALUES AT THE ADDRESS, JUST HAVE TO BE CAREFUL WHEN DOING THE PARTS OF THE POINTERSENSOR THAT MODIFY THE LEFTOPERAND, RIGHTOPERAND,RESULT
 DO THE NESTING OF FUNCTIONS CORRECTLY
 GLOBAL POINTERSENSOR SECTIONS IN VM MUST BE CORRECTED

 WE CAN ONLY HANDLE ONE FUNCTION AT THE TIME DUE TO THE LOGIC AT THE PARSER
 IT RUNS THE STATUTES.TXT IFING,WHILING,FORING,STRESS,FIBONACCI,FACTORIAL,READING, VOIDING, FIND TEST FILES COMPLETELY
 