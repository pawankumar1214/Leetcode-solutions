class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        def get_slope(p1, p2):
            return [p2[1] - p1[1], p2[0] - p1[0]]
        
        dy1, dx1 = get_slope(points[0], points[1])
        dy2, dx2 = get_slope(points[1], points[2])

        return dy1 * dx2 != dy2 * dx1