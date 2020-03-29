import automate.src.common.constants as constant
import random

class Automate:
    def __init__(self, num_automate):
        self.num_automate = num_automate
        self.type = random.randrange(constant.TYPE_MIN, constant.TYPE_MAX, 1)
        # self.type = hex(random.randrange(constant.TYPE_MIN, constant.TYPE_MAX, 1))
        self.degre_cuve = random.randrange(constant.DEGRE_CUVE_MIN*100, constant.DEGRE_CUVE_MAX*100, 0.1*100)/100
        self.degre_ext = random.randrange(constant.DEGRE_EXT_MIN*100, constant.DEGRE_EXT_MAX*100, 0.1*100)/100
        self.poids_lait = random.randrange(constant.POIDS_LAIT_MIN, constant.POIDS_LAIT_MAX, 1)
        # produit fini ??
        self.ph = random.randrange(constant.PH_MIN*100, constant.PH_MAX*100, 0.1*100)/100
        self.k = random.randrange(constant.K_MIN, constant.K_MAX, 1)
        self.nacl = random.randrange(constant.NACL_MIN*100, constant.NACL_MAX*100, 0.1*100)/100
        self.bact_salm = random.randrange(constant.BACT_SALM_MIN, constant.BACT_SALM_MAX, 1)
        self.bact_ecoli = random.randrange(constant.BACT_ECOLI_MIN, constant.BACT_ECOLI_MAX, 1)
        self.bact_list = random.randrange(constant.BACT_LIST_MIN, constant.BACT_LIST_MAX, 1)

    def print_param(self):
        print(self.num_automate, end="|")
        print(self.type, end="|")
        print(self.degre_cuve, end="|")
        print(self.degre_ext, end="|")
        print(self.poids_lait, end="|")
        print(self.ph, end="|")
        print(self.k, end="|")
        print(self.nacl, end="|")
        print(self.bact_salm, end="|")
        print(self.bact_ecoli, end="|")
        print(self.bact_list)