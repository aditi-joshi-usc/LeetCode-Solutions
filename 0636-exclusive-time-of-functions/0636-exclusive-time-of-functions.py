class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []

        prev_time = 0
        res = [0] * n
        for log in logs:
            id, action, time = log.split(':')
            id, time = int(id), int(time)

            if action == 'start':
                if stack:
                    res[stack[-1]] += time-prev_time
                stack.append(id)
                prev_time = time
            else:
                res[stack.pop()] += time - prev_time +1
                prev_time = time + 1

        return res