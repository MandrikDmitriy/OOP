class Graph:
    def __init__(self, data, is_show=True):
        self.data = data
        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            return " ".join(map(str, self.data))

    def show_graph(self):
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            print(f"Графическое отображеие дынных: {self.show_table()}")

    def show_bar(self):
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            print(f"Столбчатая диаграмма: {self.show_table()}")

    def set_show(self, is_show):
        self.is_show = is_show


data_graph = [8, 11, 10, -32, 0, 7, 18]
data_graph_2 = [1, 2, 3]
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()

gp = Graph(data_graph_2)
gp.show_bar()
gp.set_show(False)
gp.show_table()
