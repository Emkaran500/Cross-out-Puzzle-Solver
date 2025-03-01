import matplotlib.pyplot as plt
import numpy as np

def read_puzzle_from_file(filename):
    """Reads a puzzle grid from a text file and returns it as a 2D list."""
    with open(filename, 'r') as file:
        grid = [line.strip().split() for line in file]
    return grid

def read_solutions_from_file(filename):
    """Reads multiple valid crossed-out solutions from a text file formatted with multiple answers."""
    solutions = []
    with open(filename, 'r') as file:
        current_solution = set()
        for line in file:
            line = line.strip()
            if line.startswith("Answer"):  # New solution block starts
                if current_solution:
                    solutions.append(current_solution)
                    current_solution = set()
            elif line.startswith("crossedout"):
                parts = line.split("crossedout(")[1:]
                for part in parts:
                    coords = part.split(")")[0].split(",")
                    r, c = int(coords[0]) - 1, int(coords[1]) - 1
                    current_solution.add((r, c))
        if current_solution:
            solutions.append(current_solution)  # Append the last solution
    return solutions

def visualize_solutions(grid, solutions):
    """Displays all valid solutions for the puzzle grid, including grid lines."""
    rows, cols = len(grid), len(grid[0])
    num_solutions = len(solutions)
    for model_num, solution in enumerate(solutions, start=1):
        fig, ax = plt.subplots(figsize=(cols, rows))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(0, cols)
        ax.set_ylim(0, rows)
        ax.invert_yaxis()
    
        # Draw grid lines
        for r in range(rows + 1):
            ax.plot([0, cols], [r, r], "k-", lw=1)
        for c in range(cols + 1):
            ax.plot([c, c], [0, rows], "k-", lw=1)
        
        # Fill the grid with letters and cross-outs
        for r in range(rows):
            for c in range(cols):
                symbol = grid[r][c]
                if (r, c) in solution:
                    ax.add_patch(plt.Rectangle((c, r), 1, 1, color="gray", alpha=0.5))
                    ax.text(c + 0.5, r + 0.5, symbol, ha="center", va="center", fontsize=12, color="black", fontweight="bold")
                else:
                    ax.text(c + 0.5, r + 0.5, symbol, ha="center", va="center", fontsize=12, color="black")
        
        ax.set_title(f"Cross-Out Puzzle Solution - Model {model_num} of {num_solutions}")
        plt.show()

puzzle_grid = read_puzzle_from_file("puzzle.txt")
solutions = read_solutions_from_file("solutions.txt")
visualize_solutions(puzzle_grid, solutions)