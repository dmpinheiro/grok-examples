import grok
from permissions import VerHome, UmaPermissao


class Membro(grok.Role):
    grok.name("example.Membro")
    grok.permissions( 'example.ViewHome', 'example.register',)
#    grok.permissions( ViewHome, UmaPermissao,)
