# Utilizando expresiones regulares:
# 1. Verificar que un DNI es correcto (8 + letra) - 7
# 2. Verificar que un IBAN es correcto - 2
# 3. Verificar que un email es correcto - 5
# 4. Verificar que una contraseña está bien construida: - 3
# - Mínimo 6 caracteres
# - Tiene dígitos numéricos
# - Tiene caracteres
# - Tiene caracteres especiales (#, @, $)
# - No contiene ninguna palabra del diccionario español
import re

dni = input('Introduce tu DNI:')

# fullmatch devuelve un objeto si el texto encaja POR COMPLETO
# con la expresión regular 
if re.fullmatch(r"\d{8}[A-Za-z]", dni):
    print("DNI correcto")
else:
    print("DNI incorrecto")
