from common.automate import Automate
class Unite:

    def __init__(self, num_unite):
        self.num_unite = num_unite
        self.automates = []
        for num_automate in range(10):
            a = Automate(num_automate)
            while self.type_exist(a.type):
                a = Automate(num_automate)
            # a.print_param()
            self.automates.append(a)

    def type_exist(self, type_automate):
        for auto in self.automates:
            if auto.type == type_automate:
                return True
            
        return False