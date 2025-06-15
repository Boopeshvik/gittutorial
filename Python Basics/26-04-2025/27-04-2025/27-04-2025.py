class Home():
    def __init__(self):
        self.property_size = "100"
        self.property_location = "London"
        self.property_name = "Apart"
        self.house_left = 100
        
    def buy_house(self,customername):
        self.house_left-=1
        self.house_left = self.house_left-1
        print("house left is",self.house_left)
        print("Congratulation",customername, "you have got the property size of",self.property_size,self.property_location,self.property_name)

builder_manager = Home()
builder_manager.buy_house("Viyan")
builder_manager.buy_house("Vikram")
builder_manager.buy_house("Naveena")

class IPL():
    def __init__(self,Teamname,Teamcolor,Teamlocation,Topplayer):
        self.Teamname = Teamname
        self.Teamcolor = Teamcolor
        self.Teamlocation = Teamlocation
        self.Topplayer = Topplayer
    def ipl_team(self):
        print("Your team name is",self.Teamname,"whose color is",self.Teamcolor,"and they are from",self.Teamlocation,"its all about",self.Topplayer)
ipl_team1 =IPL("RCB","RED","Banglore","Kohli")
ipl_team2 = IPL("MI","Blue","Mumbai","All")

ipl_team1.ipl_team()
ipl_team2.ipl_team()