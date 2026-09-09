from collections import deque


class Solution:
    def floodFill(self, image, sr, sc, color):
        original_color = image[sr][sc]

        if original_color == color:
            return image

        rows, cols = len(image), len(image[0])

        queue = deque([(sr, sc)])
        visited = {(sr, sc)}

        image[sr][sc] = color

        while queue:
            r, c = queue.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if (
                        image[nr][nc] == original_color
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        image[nr][nc] = color
                        queue.append((nr, nc))

        return image