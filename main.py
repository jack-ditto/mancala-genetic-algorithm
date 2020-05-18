class Game:

    def __init__(self):
        # Total score for a game
        self.total_score = 0
        self.board = [
            # [0, 0],  Top Score hole - in practice doesn't matter
            [0, 0],  # 0
            [0, 0],  # 1
            [0, 0],  # 2
            [0, 0],  # 3
            [0, 0],  # 4
            [0, 0],  # 5
        ]

    def move(self, hole):
        '''
        Called to initiate a move. Initiate a move by choosing a hole on your side.
        '''

        # Num beads in selected hole
        num_beads = self.board[hole][0]

        # Set hole to 0 since you are "picking up" the beads
        self.board[hole][0] = 0

        # Set starting index to next hole
        curr_index, side = self.next_index(hole, 0)

        # Recursively move until we land on a score or on a 0 hole
        self.move_recursive(curr_index, num_beads, side)

    def move_recursive(self, curr_index, num_beads, side):
        '''
        Called to initiate a move. Initiate a move by choosing a hole on your side.
        '''

        scored = False
        for i in range(num_beads):

            # We haven't scored and we are about to
            if curr_index == 5 and side == 0 and not scored:
                self.total_score += 1
                scored = True
                continue

            if curr_index == 0 and side == 1:
                scored = False

            self.board[curr_index][side] += 1
            print("Added to", curr_index)
            self.printGame()
            input()

            tmp_index, tmp_side = curr_index, side
            curr_index, side = self.next_index(curr_index, side)

        # Move ended on a score
        if tmp_index == 5 and tmp_side == 0:
            return True

        # We land on a hole with beads in it
        if(self.board[tmp_index][tmp_side] > 1):
            num_beads = self.board[tmp_index][tmp_side]
            self.board[tmp_index][tmp_side] = 0
            self.move_recursive(
                curr_index, num_beads, side)

        # We land on an empty hole
        return False

    def next_index(self, curr_index, curr_side):

        if curr_side == 0:

            if curr_index == 5:
                return curr_index, 1

            return curr_index + 1, 0

        if curr_side == 1:

            if curr_index == 0:
                return curr_index, 0

            return curr_index - 1, 1

    def printGame(self):
        for i in range(len(self.board)):
            print(self.board[i])

        print(f"  {self.total_score}")

    def setBoard(self, board=[]):

        if board:
            self.board = board
            return

        for s in range(2):
            print("Home side...")
            for i in range(len(self.board)-1):

                p = int(input(f"Number is pos {i+1}"))
                self.board[i][s] = p

    def calcBestMoveAvalanche():
        best_score = 0
        best_pos = 0

        for i in range(len(self.board)):
            temp_game = Game()
            temp_game.setBoard(board=self.board)

            while temp_game.move(i):

                for i in range((len(self.board))):
                    temp_game.move(i)

            if(temp_game.total_score > best_score):
                best_score = temp_game.total_score
                best_pos = i+1


g = Game()
# g.setBoard()
# g.printGame()
g.move(1)
g.printGame()
# print()
# g.printGame()
