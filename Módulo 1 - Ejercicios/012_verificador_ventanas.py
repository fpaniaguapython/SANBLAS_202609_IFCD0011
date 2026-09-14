def comprobar_ventana_1():
    print('Comprobando ventana 1')
    return True

def comprobar_ventana_2():
    print('Comprobando ventana 2')
    return False

def comprobar_ventana_3():
    print('Comprobando ventana 3')
    return True

# if ((comprobar_ventana_1()==True) 
#     and (comprobar_ventana_2()==True) 
#         and (comprobar_ventana_3())):
#     print('Están todas cerradas')
# else:
#     print('Alguna ventana está abierta')

if ((comprobar_ventana_1()==True) 
    & (comprobar_ventana_2()==True) 
        & (comprobar_ventana_3())):
    print('Están todas cerradas')
else:
    print('Alguna ventana está abierta')