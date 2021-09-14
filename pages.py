from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Anagraphics (Page):
    form_model = 'player'
    form_fields = ['age']


class ResultsWaitPage(WaitPage):
    pass

class Questions(Page):
    form_model = 'player'
    form_fields = ['Q1']
    


class Results(Page):
    def vars_for_template(self):
        return {
            'your_age': self.player.age
        }


page_sequence = [Anagraphics, Questions, ResultsWaitPage, Results]
