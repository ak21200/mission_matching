
from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'mission_pe'
    players_per_group = None
    num_rounds = 1



class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    import itertools
    treatments = itertools.cycle(
        itertools.product([True, False], [True, False])
    )
    for p in subsession.get_players():
        treatment = next(treatments)
        p.charity_order = treatment[0]
        p.penalty = treatment[1]



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    penalty = models.BooleanField()
    charity_order = models.BooleanField()

    CISWO = models.IntegerField(
        label="CISWO",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1,'1 (Most preferred charity)'],
            [2, '2'],
            [3,'3'],
            [4,'4 (Do not support)'],
        ]
    )

    Ember = models.IntegerField(
        label="The Crowd: Ember",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, '1 (Most preferred charity)'],
            [2, '2'],
            [3, '3'],
            [4, '4 (Do not support)'],
        ]
    )
    CARE = models.IntegerField(
        label="CARE",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, '1 (Most preferred charity)'],
            [2, '2'],
            [3, '3'],
            [4, '4 (Do not support)'],
        ]
    )
    BPAS = models.IntegerField(
        label="BPAS",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, '1 (Most preferred charity)'],
            [2, '2'],
            [3, '3'],
            [4, '4 (Do not support)'],
        ]
    )
# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['CISWO', 'Ember', 'CARE', 'BPAS']

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CISWO'] + values['Ember'] + values['CARE'] + values['BPAS'] !=10:
            return 'Each charity must have a unique rank. Please check your ranking.'
    def error_message(player, values):
        print('values is', values)
        if values['CISWO']*values['CISWO'] + values['Ember']*values['Ember'] + values['CARE']*values['CARE'] + values['BPAS']*values['BPAS'] !=30:
            return 'Each charity must have a unique rank. Please check your ranking.'

    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.vars['CISWO'] = player.CISWO
        participant.vars['Ember'] = player.Ember
        participant.vars['CARE'] = player.CARE
        participant.vars['BPAS'] = player.BPAS
        participant.vars['penalty'] = player.penalty
        participant.vars['charity_order'] = player.charity_order

page_sequence = [MyPage]
