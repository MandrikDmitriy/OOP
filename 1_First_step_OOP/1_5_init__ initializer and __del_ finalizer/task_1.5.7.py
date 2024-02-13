class CPU:

    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:

    def __init__(self, name, cpu, *mem_slots):
        self.total_mem_slots = 4
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots[:self.total_mem_slots]

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name},{self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память:' + ";".join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]


mb = MotherBoard('asus', CPU('intel', '3000Mhz'),
                 Memory('corsar', '1024Gb'), Memory('gig', '512 Gb'))
print(mb.get_config())