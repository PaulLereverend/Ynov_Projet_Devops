import config, signal, sys, smtplib, socket, threading, pathlib, json
from config import connect
from email.message import EmailMessage
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
                #si le num unite n'est pas correct on insert toutes les données dans la table erreur
                if num_unite < 1 or num_unite > 5:
                    print("ERROR num_unite : "+data['num_unite'])
                    data['num_unite'] = '999'
                    isValid = False
                
                if isValid == True:
                    table = 'data'
                    # Vérification / Création de l'unité
                    sql_get_unite = "SELECT * FROM `unite` where id = %s"
                    cursor.execute(sql_get_unite, data['num_unite'])
                    if cursor.fetchone() == None:
                        sql_insert_unite = "INSERT INTO unite(id, site_id) VALUES (%s, 1)"
                        cursor.execute(sql_insert_unite, data['num_unite'])
                else:
                    table = 'data_error'

                for automate in data['automates']:
                    #si unite valide on vérifie les data
                    if isValid == True:
                        table = 'data'
                        if (automate['num_automate'] < 1 or automate['num_automate'] > 10):
                            print("ERROR num_automate : "+automate['num_automate'])
                            table = 'data_error'
                        if (automate['type'] < 47648 or automate['type'] > 47663):
                            print("ERROR type : "+str(automate['type']))
                            table = 'data_error'
                        if (automate['degre_cuve'] < 0.0 or automate['degre_cuve'] > 100.0):
                            print("ERROR degre_cuve : "+str(automate['degre_cuve']))
                            table = 'data_error'
                        if (automate['poids_lait'] < 0.0 or automate['poids_lait'] > 10000.0):
                            print("ERROR poids_lait : "+str(automate['poids_lait']))
                            table = 'data_error'
                    
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
                    if table == 'data_error' and isValid == True:
                        send_mail(data['num_unite'], automate)
                        
                if isValid == False:
                    send_mail(data['num_unite'], automate)
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

def send_mail(num_unite, data_automate):
    msg = EmailMessage()
    msg.set_content("""\
    Bonjour,

    Une erreur a été détectée :

    Unité : """+num_unite+"""
    Numéro d'automate : """+str(data_automate['num_automate'])+"""
    Type de l'automate : """+str(data_automate['type'])+"""
    Température de la cuve : """+str(data_automate['degre_cuve'])+""" °C
    Température extérieur : """+str(data_automate['degre_ext'])+""" °C
    Poids du lait en cuve : """+str(data_automate['poids_lait'])+""" Kg
    Mesure pH : """+str(data_automate['ph'])+"""
    Mesure K+ : """+str(data_automate['k'])+""" mg/L
    Concentration de NaCl : """+str(data_automate['nacl'])+""" g/L
    Niveau bactérien salmonelle : """+str(data_automate['bact_salm'])+""" ppm
    Niveau bactérien E-coli : """+str(data_automate['bact_ecoli'])+""" ppm
    Niveau bactérien Listéria : """+str(data_automate['bact_list'])+""" ppm
    

    Ce message a été généré automatiquement, merci de ne pas y répondre.""")
    msg['Subject'] = 'Erreur unité '+num_unite+' automate '+str(data_automate['num_automate'])
    msg['From'] = 'devopsaubonbeurre@gmail.com'
    msg['To'] = 'hugo.huet@ynov.com'

    s = smtplib.SMTP_SSL('smtp.gmail.com', '465')
    s.ehlo()
    s.login('devopsaubonbeurre@gmail.com', 'ynovdevops')
    s.send_message(msg)
    s.quit()
    print("email send !")

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((config.address, config.port))
print("En écoute à l'adresse "+str(config.address)+":"+str(config.port))
while True:
    tcpsock.listen(10)
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
