import sys
class league_stat:
    country=""
    def __init__(self,country):
        self.country=country
        
    def calculate(self):
        '''Calculates stats of the team/country and returns its performance in a list.'''
        win=loss=draw=match_played=for_team=against_team=diff=points=0
        for position in range(len(data)):
            if self.country in data[position]:
                match_played+=1
                #data format: [country , country's score , opponent , opponent's score] 
                # the index of scores is 1 or 3 in data list.
                countryscore_index=data[position].index(self.country)+1
                opponentscore_index=4-countryscore_index
                goal_scored,goal_conceded=int(data[position][countryscore_index]),int(data[position][opponentscore_index])
                #comparing scores 
                if goal_scored>goal_conceded:win,points=win+1,points+3
                elif goal_scored< goal_conceded: loss+=1
                else: draw,points=draw+1,points+1
                
                for_team+=goal_scored
                against_team+=goal_conceded
                diff=for_team-against_team

        return [self.country,match_played,win,draw,loss,for_team,against_team,diff,points]

if __name__=='__main__':
    with open("results.csv","r") as file:
        data=file.readlines()
    #organizing data in [country,country's score,opponent,opponent's score] format in a list
    data=[a.split(',') for a in data]
    #oragnizing a list of countries in the results and removing duplicate occurances of country name
    countries=list(set([a[i] for a in data for i in range(0,4,2)]))
    #printing string entered through CLI
    if len(sys.argv)!=1: print("\n",sys.argv[1].ljust(0) ,"\n",("="*len(sys.argv[1])).ljust(0))

    #making a scoreboard list which contains the analyzed stats of the object 
    scoreboard=[]
    for country in countries:
        stats=league_stat(country)
        scoreboard.append(stats.calculate())
    
    #sorting data in scoreboard with respect to diff then points
    def get_secondLast(unsorted_list):return unsorted_list[-2]
    scoreboard.sort(reverse=True ,key=get_secondLast)
    def get_Last(unsorted_list):return unsorted_list[-1]
    scoreboard.sort(reverse=True ,key=get_Last)

    print("P    W    D    L    F    A    DIFF PTS".center(78))
    for stat in scoreboard: 
        print(f"{stat[0]:<20}{stat[1]:<5}{stat[2]:<5}{stat[3]:<5}{stat[4]:<5}{stat[5]:<5}{stat[6]:<5}{stat[7]:<5}{stat[8]:<5}")
