class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for a in asteroids:
            collided = False
            while res and res[-1] > 0 and a < 0:
                if res[-1] < -a:
                    res.pop()
                    continue
                elif res[-1] == -a:
                    res.pop()
                    collided = True
                    break
                else:
                    collided = True
                    break
            if not collided:
                res.append(a)
                
                

        return res

                
            