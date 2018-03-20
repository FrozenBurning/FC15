from numpy import *
from math import *
import pprint

Tower_Level = [[],[]]
i = 1

#inputs
Tower_Num = int(input("tower nums:"))
for items in (input("tower level splited by ,:")).split(','):
    Tower_Level[0].append(i)
    Tower_Level[1].append(int(items))

Line_Attack = float(input("Troop in attack online:"))
Line_Defense = float(input("Troop in defense online:"))
Troop_Num = float(input("Troop in total:"))
Rounds = int(input("Rounds num："))



#const
Force_Ability = {'TroopRecover':{'Tech Assumed':[2,4,6,8,10],
                                  'Description':[1.05,1.1,1.15,1.2,1.25]},
                 'LineExtending':{'Tech Assumed':[2,4,6,8,10],
                                   'Description':[1.1,1.2,1.3,1.4,1.5]},
                 'ActionsNum':{'Tech Assumed':[3,5,7],
                                'Description':[0.5,1,1.5]},
                 'Defense':{'Tech Assumed':[2,4,6,8,10],
                             'Description':[1.05,1.1,1.15,1.2,1.25]}
                 }

Strategy = {'Attack':{'N':{'N':1.5,'A':1.5,'D':1,'G':1.5},
                       'A':{'N':3,'A':1.5,'D':1,'G':6},
                       'D':{'N':1,'A':1,'D':1,'G':1},
                       'G':{'N':3,'A':1.5,'D':1,'G':1.5}},
            'Confront':{'N':{'N':1,'A':1,'D':1,'G':1},
                         'A':{'N':2,'A':1,'D':1,'G':4},
                         'D':{'N':1,'A':3,'D':1,'G':1},
                         'G':{'N':2,'A':1,'D':1,'G':1}},
            'Recover':{'N':1,'A':1,'D':0.5,'G':1.5},
            'Tech Assumed':{'N':{'N':0,'A':3,'D':3,'G':3},
                              'A':{'N':2,'A':0,'D':5,'G':5},
                              'D':{'N':2,'A':5,'D':0,'G':5},
                              'G':{'N':2,'A':5,'D':5,'G':0}}
            }
Tech_Value = [0,0.15,0.2,0.25,0.3,0.3]
Troop_Recover = [0,1,1.5,2,2.5,3]


#calculate
Tech = 0
Expectation_Value = float(input("Expection Value:"))
Current_Value = 0
Tech = float(input("Tech now:"))

Level_Sum = 0
for items in Tower_Level[1]:
    Level_Sum += items

Action_Num = int(Tower_Num/2 + 1)

#以下是模型需要的参数
action_num = 3
tower_num = 1.5
tech_force = 1.2
tech_strategy = 1.5
tower_level = 1
line_attack_plus = 1.1
line_defense_plus = 1.1

#模型计算
while(abs(Current_Value - Expectation_Value) > 0.1):
    tech_value = (Troop_Num * 0.05 / 2) * tech_force + Level_Sum * tech_strategy
    Current_Value = 0
    Current_Value += Action_Num * action_num  + Tower_Num * tower_num + Level_Sum * tower_level + Tech * tech_value + Troop_Num + Line_Attack * line_attack_plus + Line_Defense * line_defense_plus
    Correction = (Current_Value - Expectation_Value)/Expectation_Value #误差百分比
    action_num = (1 - tanh(Correction))* action_num
    tower_num = (1 - tanh(Correction))* tower_num
    tech_force = (1 - tanh(Correction)) * tech_force * ((Troop_Num*0.05/2)/((Troop_Num*0.05/2) + Level_Sum))
    tech_strategy = (1- tanh(Correction))* tech_strategy * ((Level_Sum) / ((Troop_Num * 0.05 / 2) + Level_Sum))
    tower_level = (1 - tanh(Correction)) * tower_level
    line_attack_plus = (1 - tanh(Correction)) * line_attack_plus
    line_defense_plus = (1 - tanh(Correction)) * line_defense_plus

result = {'action_num':action_num,'tower_num':tower_num,'tech_force':tech_force,'tech_strategy':tech_strategy,'tower_level':tower_level,'LAP':line_attack_plus,'LDP':line_defense_plus}
pprint.pprint (result)