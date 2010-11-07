import grok

class Example(grok.Application, grok.Container):

class OtherExample(grok.Application, grok.Container):
    pass

class Index(grok.View):
    pass # see app_templates/index.pt

