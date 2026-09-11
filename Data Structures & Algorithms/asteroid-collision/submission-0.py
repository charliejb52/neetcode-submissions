class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        def check_collisions(going, left):
            if going == [] or going[-1] < 0:
                going.append(left)
                return going
            # tie, both destroyed
            elif going[-1] == -1 * left:
                going.pop()
                return going
            # + is bigger, - destroyed
            elif going[-1] > -1 * left:
                return going
            # - is bigger, + is destroyed and check the next in the stack
            elif going[-1] < -1 * left:
                going.pop()
                return check_collisions(going, left)
            

        going = []

        for a in asteroids:

            if a > 0:
                going.append(a)
            else:
                going = check_collisions(going, a)
        
        return going



        