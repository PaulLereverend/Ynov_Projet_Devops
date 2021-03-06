import os
import socket
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import config


class ExampleHandler(FileSystemEventHandler):
    def on_created(self, event):  # when file is created
        sendData(event, False)

def sendData(event, isRetry):
    with open(event.src_path, 'r') as outfile:
        fileContent = outfile.read()
        if fileContent != "":
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            print("Connexion au collecteur à l'adresse " + str(config.address) + ':' + str(config.port))
            s.connect((config.address, config.port))
            # print("envoie des données : ", fileContent)
            s.send(fileContent.encode())
            response = s.recv(100).decode()
            print(response)
            if response == "error" and isRetry == False:
                sendData(event, True)


print("En écoute : si nouveau fichier")
observer = Observer()
event_handler = ExampleHandler()  # create event handler
# set observer to use created handler in directory
dirPath = os.path.join(os.path.dirname(__file__), 'data')
observer.schedule(event_handler, path=dirPath)
observer.start()

# sleep until keyboard interrupt, then stop + rejoin the observer
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
