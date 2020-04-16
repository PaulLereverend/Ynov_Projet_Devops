import socket, threading, pathlib, json
from config import connect

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        # print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
        print("Connexion de %s:%s" % (self.ip, self.port, ))

        r = self.clientsocket.recv(999999).decode()
        pathFile = pathlib.Path().joinpath(pathlib.Path().absolute(), '../automate/src/data', r)
        with open(pathFile, 'rb') as json_file:
            data = json.load(json_file)
            connection = connect()
            try:
                with connection.cursor() as cursor:
                    # Vérification / Création de l'unité
                    sql_get_unite = "SELECT * FROM `unite` where id = %s"
                    cursor.execute(sql_get_unite, data['num_unite'])
                    if cursor.fetchone() == None:
                        sql_insert_unite = "INSERT INTO unite(id, site_id) VALUES (%s, 1)"
                        cursor.execute(sql_insert_unite, data['num_unite'])
                    # Insertion des données de l'unitée
                    for automate in data['automates']:
                        sql_insert_automate = """INSERT INTO automate(
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
                print('Données insérées')
            finally:
                if cursor != None:
                    cursor.close()
                if connection != None:
                    connection.close()

        self.clientsocket.send('Fichier reçu par le collecteur'.encode())
        print("Déconnexion de %s:%s" % (self.ip, self.port, ))

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",1111))

while True:
    tcpsock.listen(10)
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()