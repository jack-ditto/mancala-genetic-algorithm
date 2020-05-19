from Game import Game
import random
import copy


class Generation:

    def __init__(self, pop_num, pct_breed=.3, mutation_prob=.001, generations=5):

        self.population = [Game() for g in range(pop_num)]
        self.pct_breed = pct_breed
        self.mutation_prob = mutation_prob
        self.generations = generations
        self.curr_best = 0

        self.board = [
            # [0, 0],  Top Score hole - in practice doesn't matter
            [1, 0],  # 0
            [5, 4],  # 1
            [2, 1],  # 2
            [3, 1],  # 3
            [2, 0],  # 4
            [0, 2],  # 5
            [0]      # Score hole
        ]

        for g in self.population:

            board = copy.deepcopy(self.board)
            g.setBoard(board=board)

            # Continue moving with random choices while you can
            while g.moving:
                move = random.randint(0, 5)
                g.move(move)
                g.chromosome += str(move)

    def breed_population(self):

        self.population.sort(key=lambda x: x.getScore(), reverse=True)

        old_gen = self.population.copy()

        top_pct = int(len(old_gen) * self.pct_breed)

        # First take top percent
        fittest = old_gen[:top_pct]

        new_gen = []

        for i in range(0, len(fittest), 2):

            # If the fitness size is a weird number, just skip the last
            if(i >= len(fittest) - 2):
                continue

            # Cross breed the chromosomes of 2 parents
            chrom_1 = fittest[i].chromosome[:len(
                fittest[i].chromosome)//2] + fittest[i+1].chromosome[len(fittest[i+1].chromosome)//2:]

            chrom_2 = fittest[i+1].chromosome[:len(
                fittest[i+1].chromosome)//2] + fittest[i].chromosome[len(fittest[i].chromosome)//2:]

            # Create two new children
            new_child_1 = Game()
            new_child_2 = Game()

            # Give the children the board
            new_child_1.setBoard(board=copy.deepcopy(self.board))
            new_child_2.setBoard(board=copy.deepcopy(self.board))

            # Set children's game state based on chromosome
            new_child_1.move_from_chrom(chrom_1)
            new_child_2.move_from_chrom(chrom_2)

            # Mutate children
            self.mutate(new_child_1)
            self.mutate(new_child_2)

            # Add children to new generation
            new_gen.append(new_child_1)
            new_gen.append(new_child_2)

        # Previous bests move on too
        for n in old_gen:
            if n.getScore() >= self.curr_best:
                new_gen.append(n)

        # Set population to new generation
        self.population = new_gen

        if self.compute_best_score() > self.curr_best:
            self.curr_best = self.compute_best_score()
            print("set new best to ", self.curr_best)

    def run(self):

        for i in range(self.generations):
            self.breed_population()
            print("Breeded new population with size", len(self.population))

        print("Best score:", self.compute_best_score())
        print("Best Chromosome:", self.population[0].chromosome)

    def compute_best_score(self):
        self.population.sort(
            key=lambda x: x.getScore(), reverse=True)

        if len(self.population) > 0:
            return self.population[0].getScore()

        return 0

    def mutate(self, g):

        for i in range(len(g.chromosome)):

            if random.random() < self.mutation_prob:
                # print("Mutated!")
                list_crom = list(g.chromosome)
                list_crom[i] = str(random.randint(0, 5))
                g.chromosome = ''.join(list_crom)


g = Generation(100000, pct_breed=.3, mutation_prob=.001, generations=10)
g.run()
