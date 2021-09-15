from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Subsession


class Anagraphics (Page):
    form_model = 'player'
    form_fields = ['age']

    def is_displayed(self):
        return self.round_number == 1

class ResultsWaitPage(WaitPage):
    pass

class Questions(Page):
    form_model = 'player'
    form_fields = ['choices']

    def vars_for_template(self):
        news_title = str(Constants.news_title_fake[self.round_number]),
        news_text = str(Constants.news_text_fake[self.round_number]),
        source = 'Corriere'
        return{
        'news_title': news_title,
        'news_text': news_text,
        'source': source,
        'round_number':self.round_number,
        }
    


class Check_Anagraphics(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'your_age': self.player.age
        }

class Results(Page):
    def is_displayed(self):
        return self.round_number == 10

page_sequence = [Anagraphics, Check_Anagraphics, Questions, ResultsWaitPage, Results]
