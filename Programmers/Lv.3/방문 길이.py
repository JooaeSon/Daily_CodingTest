def chkVisited(visited, beforePosY, beforePosX, currPosY, currPosX):
    visited.add(((beforePosY, beforePosX), (currPosY, currPosX)))
    visited.add(((currPosY, currPosX), (beforePosY, beforePosX)))


def solution(dirs):
    visited = set()
    currPosX = 0
    currPosY = 0

    for action in dirs:
        beforePosX = currPosX
        beforePosY = currPosY
        if action == 'U' and currPosY - 1 >= -5:
            currPosY = currPosY - 1
            chkVisited(visited, beforePosY, beforePosX, currPosY, currPosX)

        elif action == 'D' and currPosY + 1 <= 5:
            currPosY = currPosY + 1
            chkVisited(visited, beforePosY, beforePosX, currPosY, currPosX)

        elif action == 'R' and currPosX + 1 <= 5:
            currPosX = currPosX + 1
            chkVisited(visited, beforePosY, beforePosX, currPosY, currPosX)

        elif action == 'L' and currPosX - 1 >= -5:
            currPosX = currPosX - 1
            chkVisited(visited, beforePosY, beforePosX, currPosY, currPosX)

    return len(visited) // 2