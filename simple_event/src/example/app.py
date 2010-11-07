import grok
import random
import uuid
from datetime import datetime

class Example(grok.Application, grok.Container):
    pass

class Conteudo(grok.Model):

    def __init__(texto):
        self.texto = texto

class Index(grok.View):
    grok.context(Example)

class Criar(grok.View):

    grok.context()
    def render(self, **kwargs):
        x = 0
        texto_loco= ""
        while x<30:
            numero = random.randint(0,255)
            texto_loco+=chr(numero)
            x=x+1
        uid = str(uuid.uuid4())
        self[uid] = texto_loco
        self.redirect('index')

@grok.subscribe(Example,grok.ObjectAddedEvent)
def registrar_inclusao(obj,event):
    inclusoes =  getattr(obj,'inclusoes',None)
    if inclusoes is not None:
        inclusoes


@grok.subscribe(Example,grok.ObjectRemovedEvent)
def criar_historico(obj,event):
    pass
