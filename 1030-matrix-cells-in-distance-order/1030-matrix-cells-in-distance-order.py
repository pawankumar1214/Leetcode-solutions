class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        result = []
        visited = [[False] * cols for _ in range(rows)]
        queue = deque()

        queue.append((rCenter, cCenter))
        visited[rCenter][cCenter] = True

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c = queue.popleft()
            result.append([r, c])

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        return result