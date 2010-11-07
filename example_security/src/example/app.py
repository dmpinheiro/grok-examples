#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import grok
import permissions

class Example(grok.Application, grok.Container):
    pass

class Segredo(grok.View):
    grok.require("example.homeaccess")

    def render(self,**kwargs):
        return """<html>
                 <body>
                 <img src="" tal:attributes="static/malandro.jpg"/>
                 </body>
                 </html>
                 """

class Index(grok.View):
    grok.require(permissions.VerHome)

    @grok.require("example.register")
    def available_users(self):
        return u"Greetings Stranger!"
