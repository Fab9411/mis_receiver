from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import pandas as pd


author = 'Fabio Torreggiani'

doc = """
In this experiment, participants are asked to read news articles and to label them as reliable or fake,
by only observing their text and source. Sources will be divided in reliable and fake.
Reliable sources will publish a fixed and high percentage of reliable news, while
fake sources will publish a fixed and low percentage of reliable news.
Both sources will be fictional and with as neutral names as possible.
In the control group, the two types of sources will publish the same percentage of reliable news.
In the three treatments, the two types of sources will differ in their publishing activity:
    - T1: 100/0 -> reliable sources publish 100 percent of reliable news
    - T2: 90/10
    - T3: 80/20
"""


class Constants(BaseConstants):
    name_in_url = 'mis_receiver'
    players_per_group = None
    num_rounds = 10
    n_tot_news = num_rounds         # how many news we want to use -> default: equal to n of rounds
    perc_fake = 0.5                 # percentage of fake news we want in our df
    perc_true = 1 - perc_fake       # percentage of reliable news we want in our df
    fake_df = pd.read_csv("mis_receiver/data/fake_df.csv")
    fake_df['type'] = 'fake'
    true_df = pd.read_csv("mis_receiver/data/true_df.csv")
    true_df['type'] = 'reliable'
    
    # the dataset of news is built by randomly picking the chosen percentage of fake and reliable news
    # from the two dataset. Fixing the random state, the list is consistent from one implementation
    # of the experiment to the other. We also randomize (with fixed seed) the order and reset the index
    news_df = pd.concat([fake_df.sample(n = int(n_tot_news*perc_fake), random_state = 1234), 
                         true_df.sample(n = int(n_tot_news*perc_true), random_state= 1234)]).sample(frac = 1, random_state = 1234).reset_index(drop = True)



class Subsession(BaseSubsession):
    news_title = models.CharField()
    news_text = models.CharField()
    news_source = models.CharField()

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(choices = range(18, 99, 1))
    choices = models.CharField()
