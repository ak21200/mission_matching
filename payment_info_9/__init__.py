from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'payment_info_9'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    donation_amount = models.IntegerField()
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
        participant = player.participant
        participant.payoff = participant.app_payoffs['stage3']
        participant.donation_charity = participant.vars['charity_rank'][4]
        return {
            'charity_name': charity_names[player.participant.donation_charity],
        }


class ResultsWaitPage(WaitPage):
    body_text = "Please wait while payments are being calculated"
    wait_for_all_players = True

page_sequence = [
    ResultsWaitPage,
    PaymentInfo
]
