import requests
import pyfiglet
import time

# URL del servidor
url = 'http://ec2-34-207-117-75.compute-1.amazonaws.com:8000'

def query_service(file_route):
    # Lee el contenido del archivo
    with open(file_route, 'rb') as file:
        file_data = file.read()
    # Envía una solicitud POST al servidor con el archivo como datos adjuntos
    response = requests.post(url, data=file_data)
    print(response.content.decode('utf-8'))

def start():
    flag = True
    while (flag is True):
        print(pyfiglet.figlet_format("Gungnir AI"))
        print(" Welcome to the ultimate antimalware detector service \n")
        route = input("Enter the path and name of the file : ")
        query_service(route)
        choice = input("Do you want to search again? (y/n) ")
        if choice.upper() != 'Y':
            flag = False
            

if __name__ == '__main__':
    start()
