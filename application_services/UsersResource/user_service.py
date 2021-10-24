from application_services.BaseApplicationResource import BaseRDBApplicationResource

from database_services.RDBService import RDBService


class UserResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    def get_data_resource_info(cls):
        return 'aaaaaF21E6156', 'users'

    @classmethod
    def get_by_template(cls, template):
        res = RDBService.find_by_template("hw1_db", "users", template,"everything")
        print("THIS IS RES",res)
        return res