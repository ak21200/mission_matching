from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    app_to_pay = models.StringField()
    charity_to_pay = models.StringField()
    round_to_pay = models.IntegerField()


# FUNCTIONS
# PAGES

charity_names = {
    "CISWO": "CISWO (Coal Industry Social Welfare Organisation)",
    "Ember": "The Crowd: Ember",
    "CARE": "CARE (Christian Action, Research, and Education)",
    "BPAS": "BPAS (British Pregnancy Advisory Service)",
}

class PaymentInfo(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'charity_name': charity_names[player.participant.donation_charity],
        }


page_sequence = [
    PaymentInfo
]
