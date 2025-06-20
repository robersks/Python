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

x = ['Rober','Fabian']