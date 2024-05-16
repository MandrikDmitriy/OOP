class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __setattr__(self, key, value):
        if key == 'old' or key == 'score':
            object.__setattr__(self, key, int(value))
        else:
            object.__setattr__(self, key, value)

    def __bool__(self):
        return True if self.score > 0 else False


with open('task_3.7.4.txt', 'r', encoding='utf-8') as file:
    lst_in = list(x.split(';') for x in file.read().splitlines())

print(lst_in)
players = list(Player(*i) for i in lst_in)
players_filter = list(filter(bool, players))
print(players_filter)
for i in players_filter:
    print(i.name, i.old, i.score)
