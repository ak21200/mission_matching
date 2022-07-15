
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
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, '1 (Most preferred)'],
            [2, '2'],
            [3, '3'],
            [4, '4 (Least preferred)'],
        ]
    )

    Ember = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, '1 (Most preferred)'],
            [2, '2'],
            [3, '3'],
            [4, '4 (Least preferred)'],
        ]
    )
    CARE = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, '1 (Most preferred)'],
            [2, '2'],
            [3, '3'],
            [4, '4 (Least preferred)'],
        ]
    )
    BPAS = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, '1 (Most preferred)'],
            [2, '2'],
            [3, '3'],
            [4, '4 (Least preferred)'],
        ]
    )

# PAGES


class Ranking(Page):
    form_model = 'player'
    form_fields = ['CISWO', 'Ember', 'CARE', 'BPAS']

    @staticmethod
    def error_message(player, values):
        if set(values.values()) != set([1, 2, 3, 4]):
            return 'Each charity must have a unique ranking.  Please review your rankings below.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.vars['CISWO'] = player.CISWO
        participant.vars['Ember'] = player.Ember
        participant.vars['CARE'] = player.CARE
        participant.vars['BPAS'] = player.BPAS
        participant.vars['penalty'] = player.penalty
        participant.vars['charity_order'] = player.charity_order

        participant.vars['charity_rank'] = {}
        participant.vars['charity_rank'][player.CISWO] = "CISWO"
        participant.vars['charity_rank'][player.Ember] = "Ember"
        participant.vars['charity_rank'][player.CARE] = "CARE"
        participant.vars['charity_rank'][player.BPAS] = "BPAS"




page_sequence = [
    Ranking,
]
