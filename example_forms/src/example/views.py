import grok
from models import Person
from example.app import Example
from zope.formlib.widgets import RadioWidget as _RadioWidget
from zope.schema import Bool, TextLine, Datetime, Choice
import uuid


class Index(grok.View):
    grok.context(Example)

    def list_of_persons(self):
        return self.context.keys()


def RadioWidget(field, request):
     vocabulary = field.vocabulary
     widget = _RadioWidget(field, vocabulary, request)
     return widget

PERSON_FIELDS = {'name': TextLine(title=u'Nome',description=u'Informe o teu nome:'),
                 'date_of_birth': Datetime(title=u'Data de Nascimento',
                          description=u'Informe sua data de nascimento'),
                 'gender': Choice(title=u'Sexo',description=u'',values=(u'Masculino',u'Feminino',))}

class ViewPerson(grok.DisplayForm):

    grok.name('index')
    grok.context(Person)

    form_fields = grok.Fields(**PERSON_FIELDS)

class EditPerson(grok.EditForm):
    grok.name('editar')
    grok.context(Person)

    form_fields = grok.Fields(**PERSON_FIELDS)

    @grok.action(u'Editar Pessoa')
    def edit_person(self,**data):
        self.applyData(self.context,**data)
        self.redirect('index')


class AddPerson(grok.AddForm):

    grok.name('adicionar')
    grok.context(Example)

    form_fields = grok.Fields(**PERSON_FIELDS)
    form_fields['gender'].custom_widget = RadioWidget

    @grok.action(u"Create a object")
    def creating_a_object(self, **data):
        self.create(str(uuid.uuid4()) ,**data)
        self.redirect('index')

    def create(self,a_id, **data):
        a_person = Person(**data)
        self.context[a_id] = a_person


