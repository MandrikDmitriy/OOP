class LessonItem:
    attr = {'title': str, 'practices': int, 'duration': int}

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.attr and type(value) is self.attr[key]:
            if (key == 'practices' or key == 'duration') and value > 0:
                object.__setattr__(self, key, value)
        else:
            raise TypeError('Incorrect type of assigned data')

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in self.attr:
            raise AttributeError('Attribute cannot be deleted')

        object.__delattr__(self, item)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        if len(self.lessons) - 1 >= indx:
            self.lessons.pop(indx)


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        if len(self.modules) - 1 >= indx:
            self.modules.pop(indx)


course = Course('Python OOP')
module_1 = Module('Part One')
module_1.add_lesson(LessonItem('lesson 1', 7, 1000))
module_1.add_lesson(LessonItem('Lesson 2', 10, 1200))
module_1.add_lesson(LessonItem('Lesson 3', 5, 800))
course.add_module(module_1)
module_2 = Module('Part Two')
module_2.add_lesson(LessonItem('Lesson_1', 8, 1100))
module_2.add_lesson(LessonItem('Lesson_2', 15, 1500))
course.add_module(module_2)
