ticket = '2026091734-Type 01-Client 3420a-no me funciona la internet'

# Sustituir los - por *
# Sustituir Type por Tipo
# Sustituir Client por Cliente
# Sustituir los clientes con número 34 por SPAIN 
# Todo deber estar en mayúsculas
# SALIDA:
# 2026091705*TIPO 01*CLIENTE SPAIN20A*NO ME FUNCIONA LA INTERNET

ticket_modificado = ticket.replace(
    '-','*').replace(
        'Type','Tipo').replace(
            'Client','Cliente').replace(
                'Cliente 34','Cliente Spain').upper()
print(ticket_modificado)