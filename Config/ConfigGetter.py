from Config.settings import DATABASE, SERVER_API
from Utils.utilClass import LazyProperty

class ConfigGetter:
    def __init__(self, choice_db_type):
        self.choice_db_type = choice_db_type

    @LazyProperty
    def db_type(self):
        return DATABASE[self.choice_db_type]['DBTYPE']

    @LazyProperty
    def db_host(self):
        return DATABASE[self.choice_db_type]['HOST']

    @LazyProperty
    def db_port(self):
        return DATABASE[self.choice_db_type]['PORT']

    @LazyProperty
    def db_name(self):
        return DATABASE[self.choice_db_type]['NAME']

    @LazyProperty
    def db_user(self):
        return DATABASE[self.choice_db_type]['USER']

    @LazyProperty
    def db_password(self):
        return DATABASE[self.choice_db_type]['PASSWORD']

    @LazyProperty
    def api_host(self):
        return SERVER_API.get('HOST')

    @LazyProperty
    def api_port(self):
        return SERVER_API.get('PORT')

    @LazyProperty
    def db_hname(self):
        return DATABASE[self.choice_db_type].get('HNAME')