import os
import time
import random
import tools

def GetGrid(length: int) -> list[list[str]]:
    grille: list[list[str]] = []
    i: int = 0
    while i < length:
        line: list[str] = []
        j: int = 0
        while j < length:
            line.append("0")
            j += 1

        grille.append(line)
        i += 1

    return grille

def RandomSpawn():
    row = random.randint(0, GRID_LENGTH - 1)
    col = random.randint(0, GRID_LENGTH - 1)
    
    if grid[row][col] == "0":
        n = random.randint(0, 10)
        if n < PROBA:
            n = "4"
        else:
            n = "2"        
        grid[row][col] = n


GRID_LENGTH: int = tools.ask_int()
PROBA: int = tools.ask_proba()
grid: list[list[str]] = GetGrid(GRID_LENGTH)

i: int = 0
while i < GRID_LENGTH:
    print(grid[i])
    i += 1

RandomSpawn()
RandomSpawn()

time.sleep(2.0)
os.system('cls' if os.name == 'nt' else 'clear')

i = 0
while i < GRID_LENGTH:
    print(grid[i])
    i += 1

def play(self, event):
    clicked_btn = event.widget

