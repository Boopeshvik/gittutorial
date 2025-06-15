class Ipl():
    def __init__(self,teamname,teamlocation,player):
        self.teamname = teamname
        self.teamlocation = teamlocation
        self.player = player
    
    def ipl_team(self):
        print(self.teamname,self.teamlocation,self.player)

one = Ipl("RCB","Bangalore","Virat")
two = Ipl("MI","Mumbai","Rohit")
one.ipl_team()
two.ipl_team()