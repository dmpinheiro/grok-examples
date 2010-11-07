from zope.interface import Interface


class IDateUtility(Interface):

    def now(self):
        """ Return a datetime object return the time at the moment.
        """


class IQuizUtility(Interface):

    def answer(question):
        """ Give a answner based on a pre-defined question.
        """

