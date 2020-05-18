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
            [0, 4],  # 2
            [0, 0],  # 3
            [0, 0],  # 4
            [10, 2],  # 5
            [0]      # Score hole
        ]

        # Move is ongoing
        self.moving = False

        # String in order of moves made
        self.chromosome = ""

    def move(self, hole, side=0):
        '''
        Called to initiate a move. 
        '''

        self.chromosome += str(hole)

        self.moving = True

        # Num beads in selected hole
        num_beads = self.board[hole][side]

        # Set hole to 0 since you are "picking up" the beads
        self.board[hole][side] = 0

        # Set starting index to next hole
        curr_index, side = self.next_index(hole, side)

        # Keep the beads moving
        while self.moving:

            # Placing beads in hand
            for i in range(num_beads):

                # If current index is 6, we're adding to our score zone
                if curr_index == 6:

                    # Add to score zone
                    self.board[curr_index][0] += 1

                    if i == num_beads-1:
                        # print("Ended on a score zone!")
                        return

                else:
                    # Add bead to board
                    self.board[curr_index][side] += 1

                    if i == num_beads-1:

                        if self.board[curr_index][side] > 1:
                            # Call recursively until we end on empty or score zone
                            return self.move(curr_index, side)

                # Get the next hole
                curr_index, side = self.next_index(curr_index, side)

            self.moving = False
            # print("Ended on an empty hole!")

    def next_index(self, curr_index, curr_side):
        '''
        Calculates the index of the next hole given a current index and side

        Returns index, side
        '''

        if curr_side == 0:

            if curr_index == 6:
                return 5, 1

            return curr_index + 1, 0

        if curr_side == 1:

            if curr_index == 0:
                return curr_index, 0

            return curr_index - 1, 1

    def printGame(self):
        ''' Prints gamestate '''

        for i in range(len(self.board)):
            print(self.board[i])

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

    def getScore(self):
        return self.board[6][0]
