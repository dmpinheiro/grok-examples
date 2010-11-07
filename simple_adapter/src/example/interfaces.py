#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from zope.interface import Interface

class IPortaVGA(Interface):
    "Conexao de video usando VGA"

    def conectar_entrada_vga(cable):
        "Conecta a um cabo de video VGA."

class IPortaMiniDVI(Interface):
    "Conexao de Video usando MiniDVI."

    def conectar_entrada_minidvi(cable):
        "Conecta a um cabo de video MiniDVI."
