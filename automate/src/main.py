from common.unite import Unite
import sys, json, os, time;
import socket

def run(num_unite):
    u = Unite(num_unite)
    print(u.num_unite)
    
    data = {}
    data['num_unite'] = u.num_unite
    data['automates'] = []
    for automate in u.automates:
        data['automates'].append({
            'num_automate' : automate.num_automate,
            'type' : automate.type,
            'degre_cuve' : automate.degre_cuve,
            'degre_ext' : automate.degre_ext,
            'poids_lait' : automate.poids_lait,
            'ph' : automate.ph,
            'k' : automate.k,
            'nacl' : automate.nacl,
            'bact_salm' : automate.bact_salm,
            'bact_ecoli' : automate.bact_ecoli,
            'bact_list' : automate.bact_list
        })
    
    dirPath = os.path.join(os.path.dirname(__file__), 'data')
    fileName = 'paramunite_'+u.num_unite+'_'+time.strftime("%d%m%Y%H%M%S")+'.json'
    with open(dirPath+'/'+fileName, 'w') as outfile:
        json.dump(data, outfile)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("", 1111))
    s.send(fileName.encode())
    response = s.recv(100).decode()
    print(response)

if __name__ == '__main__':
    if sys.argv.__len__() > 1:
        while True:
            run(sys.argv[1])
            time.sleep(60)