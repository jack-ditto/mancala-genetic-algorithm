class Game:

    def __init__(self):
        # Total score for a game
        self.total_score = 0

        # Game board
        # "Side" is either 1 or 0 representing index of subarrays
        self.board = [
            # [0, 0],  Top Score hole - in practice doesn't matter
            [0, 0],  # 0
            [0, 0],  # 1
            [0, 0],  # 2
            [0, 0],  # 3
            [0, 0],  # 4
            [0, 0],  # 5
        ]

        # Move is ongoing
        self.moving = False

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

        # Keep the beads moving
        while self.moving:

            # Placing beads in hand
            for i in range(num_beads):

                # TODO: Handle scoring

                # Add bead to board
                self.board[curr_index][side] += 1

                # TODO: check if last bead is on your score zone or on a hole with beads.
                # Set self.moving accordingly

                # Get the next hole
                curr_index, side = self.next_index(curr_index, side)

    def next_index(self, curr_index, curr_side):
        '''
        Calculates the index of the next hole given a current index and side

        Returns index, side
        '''

        if curr_side == 0:

            if curr_index == 5:
                return curr_index, 1

            return curr_index + 1, 0

        if curr_side == 1:

            if curr_index == 0:
                return curr_index, 0

            return curr_index - 1, 1

    def printGame(self):
        ''' Prints gamestate '''

        for i in range(len(self.board)):
            print(self.board[i])

        print(f"  {self.total_score}")

    def setBoard(self, board=[]):
        ''' Set board'''

        if board:
            self.board = board
            return

        for s in range(2):
            print("Home side...")
            for i in range(len(self.board)-1):

                p = int(input(f"Number is pos {i+1}"))
                self.board[i][s] = p
