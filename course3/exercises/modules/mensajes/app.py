"""
# Al importar se ejecuta el codigo que se esta importando
import mensajes.saludos as saludos

saludos.saludar()

# # # #

from mensajes.saludos import saludar, despedir

saludar()
despedir()
"""

from mensajes.bienvenida.saludos import *
from mensajes.despedida.adios import *

Saludo()
Despedida()
