class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        max_time = releaseTimes[0]
        max_key = keysPressed[0]

        for i in range(1, len(keysPressed)):
            curr_time = releaseTimes[i] - releaseTimes[i - 1]
            curr_key = keysPressed[i]

            if curr_time == max_time:
                max_key = max(curr_key, max_key)
            elif curr_time > max_time:
                max_time = curr_time
                max_key = curr_key
        
        return max_key