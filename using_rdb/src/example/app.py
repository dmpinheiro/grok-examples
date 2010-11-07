import grok
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relation
from megrok import rdb
from z3c.saconfig import EngineFactory, GloballyScopedSession
from z3c.saconfig.interfaces import (IEngineFactory, IScopedSession,
        IEngineCreatedEvent)


TEST_DSN = 'sqlite:///:memory:'
metadata = rdb.MetaData()
engine_factory = EngineFactory(TEST_DSN)
scoped_session = GloballyScopedSession()

grok.global_utility(engine_factory, provides=IEngineFactory, direct=True)
grok.global_utility(scoped_session, provides=IScopedSession, direct=True)

class Example(grok.Application, grok.Container):
    pass

class Index(grok.View):
    grok.context(Example)
    pass # see app_templates/index.pt


class Cursos(rdb.Container):
    pass

class Departamento(rdb.Model):
    rdb.metadata(metadata)
    id = Column('id',Integer, primary_key=True)
    nome = Column('nome',String(50))
    cursos = relation('Curso',
            backref='departamento',
            collection_class=Cursos)

class Curso(rdb.Model):
    rdb.metadata(metadata)

    id = Column('id',Integer, primary_key=True)
    departmento_id = Column('departamento_id', Integer,
                   ForeignKey('departamento.id'))
    nome = Column('nome',String(50))

@grok.subscribe(IEngineCreatedEvent)
def engine_criada(event):
    rdb.setupDatabase(metadata)
