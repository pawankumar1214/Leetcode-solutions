class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        
        starting_cities = {path[0] for path in paths}
        for path in paths:
            if path[1] not in starting_cities:
                return path[1]
                