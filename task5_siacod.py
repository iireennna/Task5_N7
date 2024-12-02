def wave_algorithm(map, start, end, teleports):

    d = 0
    r = len(map)
    c = len(map[0])
    wave = [[-1 for _ in range(c)] for _ in range(r)]
    wave[start[0]][start[1]] = d
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while True:
        wave_updated = False
        for x in range(r):
            for y in range(c):
                if wave[x][y] == d:
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < r and 0 <= ny < c:
                            if (map[nx][ny] in ['.', 'T1', 'T2'] and wave[nx][ny] == -1):
                                wave[nx][ny] = d + 1
                                wave_updated = True

                    if (x, y) in teleports:
                        tx, ty = teleports[(x, y)]
                        if wave[tx][ty] == -1:
                            wave[tx][ty] = d + 1
                            wave_updated = True
        d = d + 1
        if wave[end[0]][end[1]] != -1:
            break
        if not wave_updated:
            return None

    p = []
    if wave[end[0]][end[1]] != -1:
        e = end
        while e != start:
            p.append(e)
            x, y = e
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    if wave[nx][ny] == wave[x][y] - 1:
                        e = nx, ny
                        break
            else:
                for ent, exit in teleports.items():
                    if (x, y) == exit and wave[ent[0]][ent[1]] == wave[x][y] - 1:
                        e = ent
                        break

        p.append(start)
        p.reverse()
        return p
    else:
        return None


if __name__ == "__main__":
    map = [
        ['.', '.', '.', 'x', '.'],
        ['T1', 'x', 'T2', 'x', '.'],
        ['.', 'x', '.', '.', '.'],
        ['.', '.', '.', 'x', 'T2'],
        ['.', 'T1', '.', '.', '.'],
    ]

    '''map = [
        ['.', '.', '.', 'x', '.'],
        ['.', 'x', '.', 'x', '.'],
        ['.', 'x', '.', '.', '.'],
        ['x', '.', 'x', 'x', 'x'],
        ['.', '.', '.', '.', '.'],
    ]'''
    '''map = [
            ['.', '.', '.', 'x', '.'],
            ['.', 'x', '.', 'x', '.'],
            ['.', 'x', '.', '.', '.'],
            ['.', '.', '.', 'x', 'x'],
            ['.', '.', '.', '.', '.'],
        ]'''

    #start = (4, 4)
    #end = (0, 0)
    start = (0, 0)
    end = (4, 4)
    teleports = {
        #(0, 0): (4, 4),
        (1, 0): (4, 1),
        (3, 4): (1, 2)
    }

    p = wave_algorithm(map, start, end, teleports)
    if p:
        print("Путь найден:", p)
    else:
        print("Путь не найден")
