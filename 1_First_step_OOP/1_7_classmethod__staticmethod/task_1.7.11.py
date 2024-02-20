class Viber:
    messages = {}

    @classmethod
    def add_message(cls, msg):
        cls.messages[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        key = id(msg)
        if key in cls.messages:
            cls.messages.pop(id(msg))

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

        # if msg.fl_like == False:
        #     msg.fl_like = True
        # else:
        #     msg.fl_like = False

    @classmethod
    def show_last_message(cls, number):
        for i in tuple(cls.messages.values())[-number:]:
            print(i)

    @classmethod
    def total_massages(cls):
        return len(cls.messages)


class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


msg = Message('Hello everyone!')
Viber.add_message(msg)
Viber.add_message(Message('This is course of Python OOP.'))
Viber.add_message(Message('What do you think about course'))
Viber.set_like(msg)
Viber.remove_message(msg)
Viber.show_last_message(2)