def final(maze, start, end, path=[]):
    if start == end:
        return path + [start]

    x, y = start
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    maze[x][y] = "#"

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == "-":
            new_path = final(maze, (nx, ny), end, path + [start])
            if new_path:
                return new_path

    return []

maze = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "x", "-", "-", "#", "f", "#"],
    ["#", "#", "#", "-", "#", "#", "#"],
    ["#", "-", "#", "-", "-", "-", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]

start = (1, 1)
end = (1, 5)

path = final(maze, start, end)
print(path)