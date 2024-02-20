class AppStore:
    def __init__(self):
        self.dict_app = {}

    def add_application(self, app):
        self.dict_app.setdefault(app.name, app.blocked)

    def remove_application(self, app):
        self.dict_app.pop(app.name)

    def bloc_application(self, app):
        self.dict_app[app.name] = True

    def total_apps(self):
        return len(self.dict_app)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_1 = Application('App_1')
app_2 = Application('App_2')
app_3 = Application('App_3')
store.add_application(app_1)
store.add_application(app_2)
store.add_application(app_3)
store.bloc_application(app_2)
store.remove_application(app_3)
print(store.total_apps())
print(store.dict_app)
