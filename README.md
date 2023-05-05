# A.I. Assignment
Auto Grader
```bash
python autograder.py
```
## Search Problem
### <ins>Tiny Maze Search</ins> 
* Tiny Maze
```bash
python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
```
### <ins>Depth First Search</ins>
* Tiny Maze: 
```bash 
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs 
```
* Medium Maze
```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs 
```
* Big Maze
```bash
python pacman.py -l bigMaze -z .8 -p SearchAgent -a fn=dfs 
```

### <ins>Breadth First Search</ins>
* Tiny Maze: 
```bash 
python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs 
```
* Medium Maze
```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```
* Big Maze
```bash
python pacman.py -l bigMaze -z .8 -p SearchAgent -a fn=bfs
```
### <ins>Uniform Cost Search</ins>
* Tiny Maze
```bash
python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs
```
* Medium Maze
```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```
* Medium Dotted Maze
```bash
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
```
* Medium Scary Maze
```bash
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```
* Big Maze
```bash
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=ucs
```
### <ins>A* Search</ins>
* Big Maze
```bash
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
* Open Maze
```bash
python pacman.py -l openMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
## Corners Problem
### <ins>Breadth First Search</ins>
* Tiny Corners
```bash
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
* Medium Corners
```bash
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
### <ins>A* Search</ins>
```bash
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
## Food Search Problem
### <ins>A* Search</ins>
```bash
python pacman.py -l testSearch -p AStarFoodSearchAgent
```
```bash
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```
## Closest Dot Search
### <ins>A* Search</ins>
```bash
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
```