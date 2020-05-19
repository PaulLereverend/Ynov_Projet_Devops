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
                isValid = True
                num_unite = int(data['num_unite'])
                if num_unite < 1 or num_unite > 5:
                    isValid = False
                else:
                    for auto in data['automates']:
                        if (auto['num_automate'] < 1 or auto['num_automate'] > 10):
                            print("ERROR num_automate : "+auto['num_automate'])
                            isValid = False
                            break
                        if (auto['type'] < 47648 or auto['type'] > 47663):
                            print("ERROR type : "+str(auto['type']))
                            isValid = False
                            break
                        if (auto['degre_cuve'] < 0.0 or auto['degre_cuve'] > 100.0):
                            print("ERROR degre_cuve : "+str(auto['degre_cuve']))
                            isValid = False
                            break
                        if (auto['poids_lait'] < 0.0 or auto['poids_lait'] > 10000.0):
                            print("ERROR poids_lait : "+str(auto['poids_lait']))
                            isValid = False
                            break
                
                if isValid == True:
                    # Vérification / Création de l'unité
                    sql_get_unite = "SELECT * FROM `unite` where id = %s"
                    cursor.execute(sql_get_unite, data['num_unite'])
                    if cursor.fetchone() == None:
                        sql_insert_unite = "INSERT INTO unite(id, site_id) VALUES (%s, 1)"
                        cursor.execute(sql_insert_unite, data['num_unite'])
                # Insertion des données de l'unitée
                if isValid == True:
                    table = 'data'
                else:
                    table = 'data_error'
                for automate in data['automates']:
                    sql_insert_automate = "INSERT INTO "+table+"""(
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
            print('Données insérées : '+table)
        except:
            self.clientsocket.send('error'.encode())
            print("Unexpected error:", sys.exc_info())
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
