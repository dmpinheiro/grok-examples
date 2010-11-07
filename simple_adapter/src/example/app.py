#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import grok
from interfaces import IPortaVGA, IPortaMiniDVI

class Example(grok.Application, grok.Container):
    pass

class Index(grok.View):
    pass # see app_templates/index.pt


class AdaptadorDVItoVGA(grok.Adapter):
    grok.implements(IPortaVGA)
    grok.context(IPortaMiniDVI)

    def conectar_entrada_vga(self,cable):
        self.context.conectar_entrada_minidvi(self)
        print "Conectando o adaptador VGA."

class Macbook(object):
    grok.implements(IPortaMiniDVI)

    def conectar_entrada_minidvi(self, cable):
        print "Conectando na Porta MiniDVI em um Macbook."


class NotebookHP(object):
    grok.implements(IPortaVGA)

    def conectar_entrada_vga(self,cable):
        print "Conectando na porta VGA de um notebook HP."

class Projetor(object):
    pass

def plugar_laptop_em_um_projetor(laptop,projetor):
    dispositivo_vga = IPortaVGA(laptop,None)
    if dispositivo_vga is None:
        print "Voce precisa de um adaptador."
    else:
        dispositivo_vga.conectar_entrada_vga(projetor)
