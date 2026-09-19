class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        next_bans = [] # stack for all of the bans that have been made, either R or D
                  # corresponding to which party is next to be banned from voting
        
        bans = [False] * len(senate)

        tot_dire = 0
        tot_rad = 0

        for s in senate:
            if s == "D":
                tot_dire += 1

        tot_rad = len(senate) - tot_dire


        i = 0
        banned_dire = 0
        banned_rad = 0

        while(True):
            if banned_dire == tot_dire:
                return "Radiant"
            if banned_rad == tot_rad:
                return "Dire"

            if not bans[i]:
                curr = senate[i]

                if next_bans and next_bans[-1] == curr:
                    next_bans.pop()
                    bans[i] = True
                    if curr == "D":
                        banned_dire += 1
                    if curr == "R":
                        banned_rad += 1
                        
                else:
                    if curr == "D":
                        next_bans.append("R")
                    if curr == "R":
                        next_bans.append("D")
                    


            i += 1
            if i == len(senate):
                i = 0

            
