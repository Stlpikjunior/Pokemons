import json
f = open('pokemons.json')
data = json.load(f)
new_data = {}
n_data = {}
word = ["super effective","normal effective","not very effective","no effect"]
koefficients = [2,1,1/2,0]
adress = 0
for eff in data: #i je efektivita
   for typen in data[eff]:
      if adress ==0:
          new_data[typen] = {}
      for hit in data[eff][typen]:
          new_data[typen][hit]=koefficients[adress]
   adress +=1

def fight(ft:int,st:int,teams:list):
    teams = teams.strip().split(",")
    ft_att = 0
    first_team = [i.strip().split(",") for i in teams[:ft]]
    st_att = 0
    second_team = [i.strip().split(",") for i in teams[st:]]
   
    for i in first_team:
        for y in second_team:
            if len(i) == 1:
                if len(y) == 1:
                    ft_att += new_data[i[0]][y[0]]
                if len(y) == 2:
                    ft_att += new_data[i[0]][y[0]] * new_data[i[0]][y[1]]
            if len(i) == 2:
                if len(y) == 1:
                    x = max(new_data[i[0]][y[0]], new_data[i[1]][y[0]])
                    ft_att += x
                if len(y) == 2:
                    x = max(new_data[i[0]][y[0]] * new_data[i[0]][y[1]], new_data[i[1]][y[0]] * new_data[i[1]][y[1]])
                    ft_att += x
    for i in second_team:
        for y in first_team:
            if len(i) == 1:
                if len(y) == 1:
                    st_att += new_data[i[0]][y[0]]
                if len(y) == 2:
                    st_att += new_data[i[0]][y[0]] * new_data[i[0]][y[1]]
            if len(i) == 2:
                if len(y) == 1:
                    x = max(new_data[i[0]][y[0]], new_data[i[1]][y[0]])
                    st_att += x
                if len(y) == 2:
                    x = max(new_data[i[0]][y[0]] * new_data[i[0]][y[1]], new_data[i[1]][y[0]] * new_data[i[1]][y[1]])
                    st_att += x
                    
    outcome = "The winner is: "
    ft_att = round(ft_att,1)
    st_att = round(st_att,1)
    if ft_att > st_att:
        outcome += "ME"
    elif st_att > ft_att:
        outcome += "FOE"
    elif ft_att == st_att:
        outcome = "DRAW"

    return(ft_att,st_att,outcome)


print(attack(3,3,"Fire Steel,Bug Rock, Water Rock, Water Dark, Electric, Electric Fairy"))
