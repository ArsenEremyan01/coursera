class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  # Источники света
        self.map[5][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def _get_lighten_and_obstacles(self, grid):
        lig = []
        obs = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    lig.append((j, i))
                if grid[i][j] == -1:
                    obs.append((j, i))
        return lig, obs

    def lighten(self, grid):
        dim = (len(grid[0]), len(grid))
        self.adaptee.set_dim(dim)
        lig, obs = self._get_lighten_and_obstacles(grid)
        self.adaptee.set_lights(lig)
        self.adaptee.set_obstacles(obs)
        return self.adaptee.generate_lights()

if __name__ == '__main__':
    system = System()
    lights = Light((1, 1))
    adapter = MappingAdapter(lights)
    system.get_lightening(adapter)


"""Более оптимальный вариант"""
# # Реализуем адаптер для класса
# class MappingAdapter:
#
#     def __init__(self, adaptee):
#         # Сохраним адаптируемый объект
#         self.adaptee = adaptee
#
#     def lighten(self, grid):
#         # Определим метод рассчета освещенности
#         dim = (len(grid[0]), len(grid))  # Определение размера карты
#         self.adaptee.set_dim(dim)  # Установка размера карты в адаптируемом объекте
#         # Инициализируем пустые списки препятствий и источников света
#         obst = []
#         lght = []
#         # Считаем положения объектов с исходной карты
#         for i in range(dim[0]):
#             for j in range(dim[1]):
#                 if grid[j][i] == 1:
#                     lght.append((i, j))
#                 elif grid[j][i] == -1:
#                     obst.append((i, j))
#         # Передадим положения объектов адаптируемому объекту
#         self.adaptee.set_lights(lght)
#         self.adaptee.set_obstacles(obst)
#         # Вернем полученную карту освещенности
#         return self.adaptee.grid