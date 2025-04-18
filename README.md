# Infinite Craft Solver

If you are high and drunk (as me when writing this) and can't figure out how to
craft something in Infinite Craft, this is the right place for you.

This is a solver for the game [Infinite Craft](https://neal.fun/infinite-craft/), which is a game where you can craft items from other items. The game has a large number of items and recipes, and the goal of the solver is to find the shortest path to craft a specific item from a given set of items. The solver uses a breadth-first search algorithm to explore all possible combinations of items and recipes, and it can handle large numbers of items and recipes efficiently.

## Features

- Able to find the shortest path to craft a specific item from a given set of items.
- Can handle large numbers of items and recipes efficiently.
- Fun to use.
- Bypassing Cloudflare and other anti-bot measures.

## Usage

Quick setup:

```bash
git clone https://github.com/Armemius/InfiniteCraftSolver
python -m venv pyvenv
source pyvenv/bin/activate
pip install -r requirements.txt
```

Fetch the recipes and items and generate the `elements.txt` file:

```bash
python fetch.py
```

Recipe finder (needs `elements.txt` to be generated first):

```bash
python solver.py --target <target_item>
```
