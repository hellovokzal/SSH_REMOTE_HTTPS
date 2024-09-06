from requests import *
from os import *

home = """
=========================
=                       =
=      SSH MOd.         =
=                       =
=========================
"""

system("clear")

link = input("Enter domain: ")

if get(f"https://{link}/") == "localhost@root":
    system("clear")
else:
    print("Connection failed!")
    exit()
    
# home
    
print(home)
    
while True:
    ssh_remote = input(get(f"https://{link}/"))
    with requests.get(f"https://{link}/{ssh_remote}", stream=True) as response:
            # Обработка получаемых данных по строкам
            for line in response.iter_lines():
                if line:
                    # Декодируем байты в строку
                    event_data = line.decode('utf-8')
                    event_data = event_data[len("data: "):]
                    print(event_data, end="\r", flush=True)
