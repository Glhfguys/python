import random

class PuzzleGame:
    def __init__(self, size):
        self.size = size
        self.board = self.generate_board()
        self.solution = self.board.copy()
        random.shuffle(self.board)

    def generate_board(self):
        board = [i for i in range(1, self.size**2)]
        board.append(0)  # Representing empty space with 0
        return board

    def display_board(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i*self.size + j], end="\t")
            print()

    def move(self, number):
        index = self.board.index(number)
        empty_index = self.board.index(0)

        if index // self.size == empty_index // self.size or index % self.size == empty_index % self.size:
            self.board[empty_index], self.board[index] = self.board[index], self.board[empty_index]
            return True
        else:
            print("Invalid move!")
            return False

    def check_win(self):
        return self.board == self.solution

# Example usage:

size = 3  # Size of the puzzle (3x3)
game = PuzzleGame(size)

print("Welcome to the Puzzle Game!")
print("Here is the initial board:")
game.display_board()

while not game.check_win():
    print("\nEnter a number to move (0 to quit): ")
    try:
        number = int(input())
        if number == 0:
            print("Thanks for playing!")
            break
        elif number < 0 or number > size**2 - 1:
            print("Invalid input! Please enter a number between 1 and", size**2 - 1)
            continue
        else:
            if game.move(number):
                print("Moved successfully!")
                game.display_board()
                if game.check_win():
                    print("Congratulations! You've solved the puzzle!")
                    break
            else:
                continue
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
