class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        dim = (len(grid[0]), len(grid))
        self.adaptee.set_dim(dim)
        lights = [[j, i] for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 1]
        obstacles = [[j, i] for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == -1]
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()