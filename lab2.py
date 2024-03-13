import random

class Room:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]

    def place_agent(self, x, y):
        self.grid[y][x] = 'A'

    def place_dirt(self, x, y):
        self.grid[y][x] = 'D'

    def is_valid_move(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def clean_dirt(self, x, y):
        if self.grid[y][x] == 'D':
            self.grid[y][x] = '.'

    def display(self):
        for row in self.grid:
            print(''.join(row))

class Agent:
    def __init__(self, room):
        self.room = room
        self.x = 0
        self.y = 0

    def move_up(self):
        if self.room.is_valid_move(self.x, self.y - 1):
            self.room.clean_dirt(self.x, self.y - 1)
            self.y -= 1

    def move_down(self):
        if self.room.is_valid_move(self.x, self.y + 1):
            self.room.clean_dirt(self.x, self.y + 1)
            self.y += 1

    def move_left(self):
        if self.room.is_valid_move(self.x - 1, self.y):
            self.room.clean_dirt(self.x - 1, self.y)
            self.x -= 1

    def move_right(self):
        if self.room.is_valid_move(self.x + 1, self.y):
            self.room.clean_dirt(self.x + 1, self.y)
            self.x += 1

def main():
    width, height = 10, 10
    room = Room(width, height)
    agent = Agent(room)
    room.place_agent(random.randint(0, width - 1), random.randint(0, height - 1))

    for i in range(10):
        room.place_dirt(random.randint(0, width - 1), random.randint(0, height - 1))

    while True:
        room.display()
        action = input("Enter action (w/a/s/d to move, q to quit): ")

        if action == 'q':
            break
        elif action == 'w':
            agent.move_up()
        elif action == 'a':
            agent.move_left()
        elif action == 's':
            agent.move_down()
        elif action == 'd':
            agent.move_right()

if __name__ == '__main__':
    main()