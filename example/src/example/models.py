import grok
from persistent.list import PersistentList
class Carro(grok.Model):

    def __init__(self,nome, modelo=None,ano=None,opcionais=None):
        self.nome
        self.modelo=None
        self.ano=None
        self.opcionais = PersistentList(opcionais)

    def say_greetings(self):
        print "Hello, my friend! Stay awhile and listen!"


    def incluir_opcional(self,opcional):
        self.opcionais.append(opcional)
        self._p_changed = True
