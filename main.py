import os

def clear():
  """Limpia la pantalla de la terminal."""
  # Para Windows
  if os.name == 'nt':
    os.system('cls')
  # Para macOS y Linux
  else:
    os.system('clear')

clear()

texto_1 = "Texto 1"
texto_2 = 'Texto 2'
texto_3 = """ What is Lorem Ipsum?
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
    It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. 
   """
texto_4 = '''What is Lorem Ipsum?
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
    It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged.
    '''
    
var_int = 40        #Número entero
var_float = 40.89   #Númro con decimal

print (texto_1)