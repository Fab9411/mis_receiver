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
    fake_df = pd.read_csv("mis_receiver/data/fake_df.csv")
    true_df = pd.read_csv("mis_receiver/data/true_df.csv")
    news_title_fake = fake_df.loc[:,'title']
    news_title_true = true_df.loc[:,'title']
    news_text_fake = fake_df.loc[:,'text']
    news_text_true = true_df.loc[:,'text']



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(choices = range(18, 99, 1))
    choices = models.CharField()
