class Player:
    def __init__(self,pn,pa,pc,pr,pw,pm):
        self.player_name = pn
        self.player_age = pa
        self.player_country=pc
        self.player_runs=pr
        self.player_wicket=pw
        self.player_matches=pm
    def player_details(self):
        print(f"Player Name: {self.player_name}")
        print(f"Player Age: {self.player_age}")
        print(f"Player Country: {self.player_country}")
        print(f"Player Runs: {self.player_runs}")
        print(f"Player Wicket: {self.player_wicket}")
        print(f"Player Matches: {self.player_matches}")
class Team:
    def __init__(self,name,nop):
        self.name = name
        self.playerlist=[]
        for i in range(nop):
            pn=input("enter player name")
            pa=int(input("enter player age"))
            pc=input("enter player country")
            pr=int(input("enter player runs"))
            pw=int(input("enter player wickets"))
            pm=int(input("enter player matches"))
            self.playerlist.append(Player(pn,pa,pc,pr,pw,pm))
    def max_runs(self):
        maxruns=0
        maxruns_scorres=""
        for i in self.playerlist:
            if i.player_runs>maxruns:
                maxruns=i.player_runs
                maxruns_scorres=i.player_name
        print(f"{maxruns_scorres} scored most runs: {maxruns} ")
    def max_wickets(self):
        maxwickets=0
        maxwickets_scorres=""
        for i in self.playerlist:
            if i.player_wicket>maxwickets:
                maxwickets=i.player_wicket
                maxwickets_scorres=i.player_name
        print(f"{maxwickets_scorres} takes most wickets: {maxwickets} ")
    def team_details(self):
        print(f"Team Name: {self.name}")
        print("team details:")
        for i in self.playerlist:
            i.player_details()
RCB=Team("RCB",3)
RCB.max_wickets()
RCB.max_runs()
RCB.team_details()

