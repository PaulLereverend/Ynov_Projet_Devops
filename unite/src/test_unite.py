from common.unite import Unite
from common.automate import Automate


class TestUnite:
    def test_num_unite(self):
        assert u.num_unite >= 1 and u.num_unite <= 5


class TestAutomate:
    def test_num_automate(self):
        for auto in u.automates:
            print(auto.num_automate)
            assert auto.num_automate >= 1 and auto.num_automate <= 2

    def test_type_automate(self):
        for auto in u.automates:
            print(auto.type)
            assert auto.type >= 0X0000BA20 and auto.type <= 0X0000BA2F

    def test_temp_cuve(self):
        for auto in u.automates:
            print(auto.degre_cuve)
            assert auto.degre_cuve >= 0.0 and auto.degre_cuve <= 100.0

    def test_poids_lait_cuve(self):
        for auto in u.automates:
            print(auto.poids_lait)
            assert auto.poids_lait >= 0.0 and auto.poids_lait < 10000.0


u = Unite(2)
