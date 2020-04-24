from common.unite import Unite
import sys, json, os, time;

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
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    fileName = 'paramunite_'+u.num_unite+'_'+time.time().__trunc__().__str__()+'.json'
    with open(dirPath+'/'+fileName, 'w') as outfile:
        json.dump(data, outfile)

if __name__ == '__main__':
    if sys.argv.__len__() > 1:
        while True:
            run(sys.argv[1])
            time.sleep(5)
    else:
        print("Numéro d'unité en argument manquant")