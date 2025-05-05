class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def findAreaDiff(line):
            areaAbove = 0.0
            areaBelow = 0.0

            for x, y , side in squares:
                area = side * side

                if line >= y+side:
                    areaBelow += area
                elif line <= y:
                    areaAbove += area
                else:
                    len_above = y + side - line
                    len_below = line - y
                    areaAbove += len_above * side
                    areaBelow += len_below * side

            return areaAbove - areaBelow

        low = min(y for _, y, _ in squares)
        high = max(y + side for _, y, side in squares)

        for _ in range(60):
            mid = (low + high) / 2.0
            diff = findAreaDiff(mid)
           
            if diff > 0:
                low = mid 
            else:
                high = mid

        return high
