import common.constants as constants
import random

class Automate:
    def __init__(self, num_automate):
        self.num_automate = num_automate
        self.type = random.randrange(constants.TYPE_MIN, constants.TYPE_MAX, 1)
        # self.type = hex(random.randrange(constants.TYPE_MIN, constants.TYPE_MAX, 1))
        self.degre_cuve = random.randrange(constants.DEGRE_CUVE_MIN*100, constants.DEGRE_CUVE_MAX*100, 0.1*100)/100
        self.degre_ext = random.randrange(constants.DEGRE_EXT_MIN*100, constants.DEGRE_EXT_MAX*100, 0.1*100)/100
        self.poids_lait = random.randrange(constants.POIDS_LAIT_MIN, constants.POIDS_LAIT_MAX, 1)
        self.ph = random.randrange(constants.PH_MIN*100, constants.PH_MAX*100, 0.1*100)/100
        self.k = random.randrange(constants.K_MIN, constants.K_MAX, 1)
        self.nacl = random.randrange(constants.NACL_MIN*100, constants.NACL_MAX*100, 0.1*100)/100
        self.bact_salm = random.randrange(constants.BACT_SALM_MIN, constants.BACT_SALM_MAX, 1)
        self.bact_ecoli = random.randrange(constants.BACT_ECOLI_MIN, constants.BACT_ECOLI_MAX, 1)
        self.bact_list = random.randrange(constants.BACT_LIST_MIN, constants.BACT_LIST_MAX, 1)

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