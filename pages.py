from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Subsession
from mis_receiver import models


class Anagraphics (Page):
    form_model = 'player'
    form_fields = ['age']

    def is_displayed(self):
        return self.round_number == 1

class Check_Anagraphics(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'your_age': self.player.age
        }

class Questions(Page):
    form_model = 'player'
    form_fields = ['choices']


    def vars_for_template(self):
        # selecting the row of the news_df that corresponds to the current round
        row = Constants.news_df.iloc[self.round_number - 1, :]
        self.subsession.news_title = row['title']
        self.subsession.news_text = row['text']
        self.subsession.news_type = row['type']
        
        return{
        'news_title': row['title'],
        'news_text': row['text'],
        'source': row['type'],
        'round_number':self.round_number,
        }

class Results(Page):
    """
    In this page we show the answer of the player, the correct answer, the relative payoff and the
    total payoff.
    IMPORTANT: to be shows only when 'debunking' mechanism is wanted
    To be done:
        - include debunking treatment and make this page dependent on it
    """

    def is_displayed(self):
        return self.session.config['debunking'] == True 
    
    
    def vars_for_template(self):
        if self.subsession.news_type == self.player.choices:
            self.player.payoff = 1
        else:
            self.player.payoff = 0

        return{
        'news_type': self.subsession.news_type,
        'choice': self.player.choices
        }       
    

class Final_Results(Page):
    def is_displayed(self):
        return self.round_number == 10
    
page_sequence = [Anagraphics, Check_Anagraphics, Questions, Results, Final_Results]
