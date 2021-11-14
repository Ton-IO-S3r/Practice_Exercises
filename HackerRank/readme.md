****** ¡IMPORTANTE! POR FAVOR LEA ANTES DE EMPEZAR ******
Este reto está dividido en tres secciones (Back End, Front End, Base de Datos) para evaluar las habilidades requeridas del ingeniero.
Usted va a tener 2 horas y 30 minutos (150 minutos) para completar los retos después de empezar.  Monitoree su tiempo y termine de trabajar cuando se termine el tiempo indicado.
Cuando termine con los retos, cierre esta pestaña en su navegador y responda al email con este enlace indicando que ya ha completado los retos y está listo(a) para una revisión.
Las respuestas son automáticamente guardadas, así que no se preocupe de ello.
Puede avanzar a la siguiente pregunta si no tiene una respuesta para la pregunta actual.
Nosotros no tenemos expectativas de que sobresalgan en todas las áreas del reto.
Puede probar su código en el entorno de programación local de su computadora o en editores en línea.
No dude en añadir comentarios en su código.
Por favor no modifique las preguntas del reto.
Por favor escriba sus respuestas solamente en Inglés.

Reto de Programación Back End (Su respuesta puede ser escrita en el lenguaje de su preferencia)
============================================================================

Problema 1:
Devuelva un arreglo con el monto de impuestos en centavos de un determinado monto en dólares y porcentaje de impuesto.

def getTaxesInCents(amount:float, tax:float):
  '''
      Function to get the amount of taxes of the given amount (amount) and given percentage (tax) - PYTHON
  '''
  # check arguments to be numbers
  if (type(amount) == int or type(amount) == float) and (type(tax) == int or type(tax) == float):
    #return corresponding taxes in cents and tax percentage
    return [amount*tax,tax]
    

Problema 2:
 Dado las siguientes cartas, ['A',1,2,3,4,5,6,7,8,9,10,'J','K','Q'], escriba una función que baraje las cartas usando la función randint.
 El módulo random incluye una función básica randint(a, b) que devuelve un número aleatorio entre a y b (incluyendo ambos puntos).
 
 Ejemplo:
 Cartas de entrada = ['A',1,2,3,4,5,6,7,8,9,10,'J','K','Q'].
 Resultado =  ['Q',K,2,3,4,5,6,7,8,9,10,'1','A','J'] o pueden ser mezcladas en cualquier orden.

def shuffleCards(cards_list):
  '''
      Function to shuffle the given cards
  '''
  a=set()
  while len(a)<len(cards_list):
    a.add(cards_list[randint(0,len(cards_list)-1)])
  
  return a

Problema 3:
Dada una cadena de carácteres s, devuelva la suma de las vocales en la cadena si el valor de la vocal aumenta por 1 de acuerdo a la orden de las mismas.

Ejemplo:
Entrada = s: "Welcome to Indonesia", valor de vocales: a = 1, e = 2, i = 3, o = 4, u = 5 
Resultado = 22 (1 a's = 1*1 = 1 +  3 e's = 3*2 = 6 +  1 i's = 1*3 = 3 + 3 o's = 3*4 = 12)

def countVowelsValue(phrase):
  vowels_arr=['a','e','i','o','u']
  counter=0
  
  #Change phrase to lowercase
  phrase=phrase.lower()
  
  #create a list with vowels found in phrase
  phrase_vowels = [i for i in phrase if i in vowels_arr]
  
  #add to counter each vowel's value from vowels list and return result
  for vowel in phrase_vowels:
    counter += vowels_arr.index(vowel)+1
  return counter

Problema 4:
Escriba una versión recursiva de la función previa (o la versión iterativa si ya escribió la versión recursiva).

Problema 5:
Escriba una expresión regular para buscar cualquier palabra de 4 a 9 letras que contenga las palabras "odoo", "code" o "work".



Reto de Programación Front End (JS/TS/CSS)
=====================================

Problema 6:
https://gist.github.com/sna-odoo/70229f8bc4c3a232324b3c70ca9d2e6b
Cree una caja de dimensiones 3*3 usando la propiedad flex.  Cada caja deberá mostrar un 0 en el centro.

Problema 7:
Implemente un contador en el desarrollo previo, cada suma deberá aumentarse sólo por un click en su respectiva caja.

Problema 8:
Implemente un botón en el desarrollo previo con el texto "click here".  Después de presionar el botón, las sumas en cada caja deberán aumentarse por 1 con 1 segundo de intervalo entre cada aumento.

Problema 9:
Cuente todas las veces que la palabra "odoo.sh" aparece en todas las secciones de https://www.odoo.sh/faq, incluyendo etiquetas div plegables usando jQuery.


Reto de Base de Datos (SQL)
=====================================

Problema 10:
Escriba una declaración SQL para crear tablas en la base de datos para almacenar los detalles básicos de un sitio ecommerce.

    10.1):
    Cada usuario tiene un nombre, apellido, dirección y identificador de ciudad para almacenar la referencia padre.  La tabla para la ciudad tiene columnas para id y nombre.
    
    Con la condición de que estas tablas contienen 10000 usuarios y 30 ciudades...
    
    
    
    10.2) Escriba una declaración SQL para buscar ciudades con el número más alto de usuarios y devuelva el id de ciudad, nombre, y número de usuarios en orden descendiente.
    10.3) ¿Cómo poblaría las tablas con datos arbitrarios de prueba para las tablas creadas en el primer problema?

