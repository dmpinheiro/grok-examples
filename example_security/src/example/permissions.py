import grok


class UmaPermissao(grok.Permission):
    grok.name("example.register")

class VerHome(grok.Permission):
    grok.name("example.homeaccess")

