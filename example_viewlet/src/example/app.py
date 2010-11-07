import grok

class Example(grok.Application, grok.Container):
    pass

class Index(grok.View):
    pass


class AreadoUsuario(grok.ViewletManager):
    grok.view(Index)
    grok.name('example.main')

class UserName(grok.Viewlet):
    grok.name('user')
    grok.order(30)
    grok.viewletmanager(AreadoUsuario)

    def render(self):
        return "Hello!"

class Preferences(grok.Viewlet):
    grok.name('preferences')
    grok.order(10)
    grok.viewletmanager(AreadoUsuario)

    def render(self):
        return "Greetings!"
