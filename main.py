from Game import Game


class Generation:

    def __init__(self, pop_num):

        self.population = []

        # Create population
        for n in range(pop_num):
            g = Game()
            self.population.append(g)

            g.move(n)
            while g.moving:
                g.move()
