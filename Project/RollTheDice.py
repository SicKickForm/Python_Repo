import random 

# Roll The Dice
print('Which mode do you play?')
Mode = input('Enter S for solo and M for multiplayer mode: ')
Numbers = [1,2,3,4,5,6]


def Continue(P1_Point, P2_Point):
    Continue_Command = input('Enter C to continue and Q to quit: ')
    if Continue_Command == "C":
        Solo(P1_Point, P2_Point)
    elif Continue_Command == "Q" :
        pass

def Solo(P1_Point, P2_Point):
    Roll_Command = input('Enter R to roll: ')
    if Roll_Command == 'R':
        P_Num = random.choice(Numbers)
        S_Num = random.choice(Numbers)
        print('Your dice is ' + str(P_Num))
        print('System dice is ' + str(S_Num))
        if P_Num > S_Num:
            print('You Won!')
            P1_Point += 1
        elif P_Num == S_Num:
            print('Tie!')
        elif S_Num > P_Num:
            print('Opponent Lost!')
            P2_Point += 1
        print('Player: ' + str(P1_Point) + ' Opponent: ' + str(P2_Point))
        Continue(P1_Point, P2_Point)
    else:
        print("Game over")


def Continue2(People, Rolls, Points):
    Continue_Command = input('Enter C to continue and Q to quit: ')
    if Continue_Command == "C":
        Multi(People, Rolls, Points)
    elif Continue_Command == "Q" :
        pass
    
def Multi(People, Rolls, Points):
    Rolls.clear()
    for i in range(People):
        Roll_Command = input((f'Player {i} Enter R to toll: '))
        if Roll_Command == 'R':
            P_Num = random.choice(Numbers)
            Rolls.append(P_Num)
            print(f'Player {i} dice is ' + str(P_Num))
        else:
            print('Try Again')
    
    Winner = max(Rolls)
    print(f"Player {Rolls.index(Winner)} won!")
    Points[Rolls.index(Winner)] += 1    
    print("Points: " + str(Points))
    Continue2(People, Rolls, Points)
    
def Play():               
    if Mode == 'S':
        P1_Point = 0
        P2_Point = 0
        Solo(P1_Point, P2_Point)
    elif Mode == 'M':
        People = int(input('How many people are playing? '))
        Rolls = []
        Points = []
        for i in range(People):
            Points.append(0)
        Multi(People, Rolls, Points)

Play()
