import grok
from datetime import datetime

from example.interfaces import IDateUtility, IQuizUtility

class Example(grok.Application, grok.Container):
    pass

class Index(grok.View):
    grok.context(Example)

class ComicQuizUtility(grok.LocalUtility):

    grok.name("comic")
    grok.implements(IQuizUtility)

class DateUtility(grok.GlobalUtility):
    grok.implements(IDateUtility)

    def now(self):
        return datetime.now()

