from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Subsession
from mis_receiver import models


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
        # selecting the row of the news_df that corresponds to the current round
        row = Constants.news_df.iloc[self.round_number - 1, :]
        return{
        'news_title': row['title'],
        'news_text': row['text'],
        'source': row['type'],
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
