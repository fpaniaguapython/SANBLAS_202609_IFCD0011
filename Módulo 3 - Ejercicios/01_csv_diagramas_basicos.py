import csv
import matplotlib.pyplot as plt

def create_line_diagram(x_data, y_data):
    plt.plot(x_data, y_data)
    plt.title('Ventas trimestrales')
    plt.xlabel('Trimestres')
    plt.ylabel('Billones €')
    plt.show()

def create_bar_diagram(x_data, y_data):
    #plt.bar(x=x_data, height=y_data)
    plt.bar(x_data, y_data)
    plt.title('Ventas trimestrales')
    plt.xlabel('Trimestres')
    plt.ylabel('Billones €')
    plt.show()


trimestres = list()
ventas = []

with open('./data/datos.csv', mode='rt', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',') # Proporciona diccionarios
    # reader = csv.reader(csvfile, delimiter=',') # Proporciona listas
    for row in reader:
        #print(row['Trimestre'])
        #print(row.get('Trimestre'))
        trimestres.append(row['Trimestre'])
        ventas.append(int(row['Facturacion']))
    print(trimestres)
    print(ventas)

create_bar_diagram(trimestres, ventas)
#create_line_diagram(trimestres, ventas)