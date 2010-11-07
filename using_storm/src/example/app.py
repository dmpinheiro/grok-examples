import grok
from nva.stormcontainer import StormContainer
from storm.locals import Storm, Int, Unicode, Reference

class Example(grok.Application, grok.Container):
    pass

class Grupo(StormContainer, grok.Container):

    def __init__(self):
        super(Grupo,self).__init__()
        self.setClassName('example.app.Pessoa')
        self.setStoreUtilityName('test')

class Compania(StormContainer, grok.Container):

    def __init__(self):
        super(Compania,self).__init__()
        self.setClassName('example.app.Departamento')
        self.setStoreUtilityName('test')

class Departamento(grok.Model,Storm):
    __storm_table__ = "departamento"
    id_departamento = Int(primary=True)
    nome = Unicode()

class Pessoa(grok.Model,Storm):
    __storm_table__ = "pessoa"
    id_pessoa = Int(primary=True)
    nome = Unicode()
    departamento = Reference(id_pessoa, Departamento.id_departamento)

@grok.subscribe(Example, grok.ApplicationInitializedEvent)
def define_store(obj, event):
    from zope.component import getUtility
    zstorm = getUtility(IZStorm)
    zstorm.set_default_uri("test", "sqlite:")
    store = zstorm.get('test')
    store.execute("")
    result = store.execute("""
     CREATE TABLE pessoa (
            id_pessoa INTEGER PRIMARY KEY,
            nome VARCHAR,
            departamento INTEGER NOT NULL);
     CREATE TABLE departamento (
            id_departamento INTEGER PRIMARY KEY,
            nome VARCHAR);
    """)
    store.commit()
