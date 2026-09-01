class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:
            return image

        def change_color(x, y):
            if x >= len(image) or x < 0 or y >= len(image[0]) or y < 0 or image[x][y] != start_color: 
                return
            image[x][y] = color
            change_color(x + 1, y)
            change_color(x - 1, y)
            change_color(x, y + 1)
            change_color(x, y - 1)
        
        change_color(sr, sc)
        return image

            