import socket
import threading
import pathlib
import json
from config import connect
import config
import signal
import sys

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        # print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self):
        print("Connexion de %s:%s" % (self.ip, self.port, ))

        message = self.clientsocket.recv(999999999).decode()
        data = None
        cursor = None
        connection = None
        try:
            data = json.loads(message)
            connection = connect()
            with connection.cursor() as cursor:
                # Vérification / Création de l'unité
                sql_get_unite = "SELECT * FROM `unite` where id = %s"
                cursor.execute(sql_get_unite, data['num_unite'])
                if cursor.fetchone() == None:
                    sql_insert_unite = "INSERT INTO unite(id, site_id) VALUES (%s, 1)"
                    cursor.execute(sql_insert_unite, data['num_unite'])
                # Insertion des données de l'unitée
                for automate in data['automates']:
                    sql_insert_automate = """INSERT INTO data(
                        unite_id,
                        automate_id,
                        type,
                        temp_cuve,
                        temp_ext,
                        poids_lait,
                        mesure_ph,
                        mesure_kplus,
                        mesure_nacl,
                        salmonelle,
                        ecoli,
                        listeria
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(sql_insert_automate, (
                        data['num_unite'],
                        automate['num_automate'],
                        automate['type'],
                        automate['degre_cuve'],
                        automate['degre_ext'],
                        automate['poids_lait'],
                        automate['ph'],
                        automate['k'],
                        automate['nacl'],
                        automate['bact_salm'],
                        automate['bact_ecoli'],
                        automate['bact_list']
                    ))
            connection.commit()
            self.clientsocket.send('Données insérées en base'.encode())
            print('Données insérées')
        except:
            self.clientsocket.send('error'.encode())
            print("Unexpected error:", sys.exc_info()[0])
        finally:
            if cursor != None:
                cursor.close()
            if connection != None:
                connection.close()
            if self.clientsocket != None:
                self.clientsocket.close()

        print("Déconnexion de %s:%s" % (self.ip, self.port, ))

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((config.address, config.port))
print("En écoute à l'adresse "+str(config.address)+":"+str(config.port))
while True:
    tcpsock.listen(10)
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
