# Default args value
DEFAULT_ARGS_VALUES = {
    'format': 'db',
    'format_choices': ['db', 'pdf', 'xml', 'json', 'html', 'csv'],
    'outputdirectory': '.'
}


DEFAULT_SOURCES_LINKS = {
    'un': 'https://www.un.org/en/observances/list-days-weeks'
}

DEFAULT_OUTPUT_COLOR = {
    'evt_doc':  {"fill_color" : "red", "back_color" : "white"},
    'evt_link':  {"fill_color" : "black", "back_color" : "white"}
}

DEFAULT_DB_CONFIG = {
    "user" : "root", 
    "password" : "Your_Database_Password", 
    "host" : "localhost", 
    "database" :"intercalendar"
}

DEFAULT_OUTPUT_DIR = "output/"