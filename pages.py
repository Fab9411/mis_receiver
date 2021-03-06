from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Subsession
from mis_receiver import models


class Anagraphics (Page):
    form_model = 'player'
    form_fields = ['age']


    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        # I call the setting_sources method for setting the source-type link according to the treatment
        Constants.setting_sources(self, Constants.news_df)
        return{
        'treatment': self.session.config['treatment']
        }

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
        self.subsession.source = row['source']
        
        return{
        'news_title': row['title'],
        'news_text': row['text'],
        'type': row['type'],
        'source': row['source'],
        'round_number':self.round_number,
        # here I load the image with the same name as title, while also filtering for special symbols and spaces
        # it chooses a different folder according to the specified setting in session config
        'image_name': "mis_receiver/images/{folder}/{file_name}.png".format(
            folder = 'facebook' if self.session.config['social'] else 'websites',
            file_name = row['title'].strip(' ').translate({ ord(c): None for c in u"\":!\\|/*<>?" }))
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
        return self.round_number == Constants.num_rounds
    
page_sequence = [Anagraphics, Check_Anagraphics, Questions, Results, Final_Results]
