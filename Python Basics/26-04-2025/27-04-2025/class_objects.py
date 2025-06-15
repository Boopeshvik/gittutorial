class Home():
    def __init__(self,buildername,buildingsize,buildinglocation,buildingname):
        self.buildername = buildername
        self.buildingsize = buildingsize
        self.buildinglocation = buildinglocation
        self.buildingname =buildingname
    
    def buy_home(self,customer_name):
        print("Congratulation",customer_name,"you have got the house from",self.buildername,self.buildinglocation,self.buildingsize,self.buildingname)
        
house_supplier1 = Home("Appaswamy","1000sqft","London","Skyine")
house_supplier2 = Home("grand","3000sqft","Stevenage","Swingate")

house_supplier1.buy_home("Boopesh")
house_supplier1.buy_home("Naveena")
house_supplier2.buy_home("Viyan")
