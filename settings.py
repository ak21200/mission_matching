import itertools
from os import environ



SESSION_CONFIGS = (
    dict(
        name='Experiment',
        app_sequence=[
            'welcome',
            'stage1',
            'mission_pe',
            'stage2',
            'stage3',
            'survey',
            'payment_info'
        ],
        num_demo_participants=6,
        task_seconds=15,
        stage_index_offset=0,
        charity_round_offset=0,
    ),
dict(
        name='Experiment_V4',
        app_sequence=[
            'welcome',
            'stage1',
            'mission_pe',
            'stage2',
            'stage3',
            'survey',
            'payment_info_4'
        ],
        num_demo_participants=6,
        task_seconds=15,
        stage_index_offset=0,
        charity_round_offset=0,
    ),
dict(
        name='Experiment_V5',
        app_sequence=[
            'welcome',
            'stage1',
            'mission_pe',
            'stage2',
            'stage3',
            'survey',
            'payment_info_5'
        ],
        num_demo_participants=6,
        task_seconds=15,
        stage_index_offset=0,
        charity_round_offset=0,
    ),
dict(
        name='Experiment_V6',
        app_sequence=[
            'welcome',
            'stage1',
            'mission_pe',
            'stage2',
            'stage3',
            'survey',
            'payment_info_6'
        ],
        num_demo_participants=6,
        task_seconds=15,
        stage_index_offset=0,
        charity_round_offset=0,
    ),
dict(
        name='Experiment_V7',
        app_sequence=[
            'welcome',
            'stage1',
            'mission_pe',
            'stage2',
            'stage3',
            'survey',
            'payment_info_7'
        ],
        num_demo_participants=6,
        task_seconds=15,
        stage_index_offset=0,
        charity_round_offset=0,
    ),
dict(
        name='Experiment_V8',
        app_sequence=[
            'welcome',
            'stage1',
            'mission_pe',
            'stage2',
            'stage3',
            'survey',
            'payment_info_8'
        ],
        num_demo_participants=6,
        task_seconds=15,
        stage_index_offset=0,
        charity_round_offset=0,
    ),
dict(
        name='Experiment_V9',
        app_sequence=[
            'welcome',
            'stage1',
            'mission_pe',
            'stage2',
            'stage3',
            'survey',
            'payment_info_9'
        ],
        num_demo_participants=6,
        task_seconds=15,
        stage_index_offset=0,
        charity_round_offset=0,
    ),
)

#FUNCTIONS


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    'CISWO',
    'Ember',
    'CARE',
    'BPAS',
    'treatment',
    'penalty',
    'charity_order',
    'is_dropout',
    'app_payoffs',
    'stage_donation',
    'rounds',
    'app_to_pay',
    'donation_charity',
]
SESSION_FIELDS = ['params']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
"""


SECRET_KEY = '2307692050879'

INSTALLED_APPS = ['otree''slider_task']
