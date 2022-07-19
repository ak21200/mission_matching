from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'payment_info_s3'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    donation_amount = models.IntegerField()
    charity_to_pay = models.StringField()
    payment_app = models.StringField()


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
        participant = player.participant

        if player.id_in_group % 3 == 0:
            participant.payment_app = "stage1"
        if player.id_in_group % 3 == 1:
            participant.payment_app = "stage2"
        else:
            participant.payment_app = "stage3"

        participant.payoff = participant.app_payoffs[participant.payment_app]
        player.payment_app = participant.payment_app
        participant.donation_charity = participant.vars['charity_rank'][4]
        return {
            'charity_name': charity_names[player.participant.donation_charity],
        }


page_sequence = [
    PaymentInfo
]
