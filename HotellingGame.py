# This project is to practice playing the Hotelling Game with students.
# It takes input from two players.
# It then shows them their moves.
# It then returns a score to them based on their position in the game.
# Future versions will have more options.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#Take a player number and prompt them for their move.
def getMove(PlayerNumber):
    move = -1
    while(move < 0 or move > 1):
        move = float(input("Where would you like to move, Player "+ str(PlayerNumber) + "? (0,1):"))
        if(move < 0 or move > 1):
            print("That is an invalid move, Player "+ str(PlayerNumber) + 
                  ". It must be between 0 and 1, inclusive.")
    print("You have moved to: " + str(move) + "!  Good move.", move)
    return move

#Take a set of moves and return scores for each position.
def getHotellingScores(move_array):
    #prep payoff array for return.
    payoff_array = move_array
    #sort payoff
    move_array.sort()
    print("We saw placements at:")
    print(move_array)
    for i in range(len(move_array)):
        #print(i)
        if i==0 : # bottom edge
            payoff_array[i] = (move_array[i]-0)**2 * 0.5 + (move_array[i+1]-move_array[i])**2 * 0.5 * 0.5
        elif i == len(move_array)-1: #top edge
            payoff_array[i] = (move_array[i]-move_array[i-1])**2 * 0.5 * 0.5 + (1-move_array[i])**2 * 0.5
        else:
            payoff_array[i] = (move_array[i]-move_array[i-1])**2 * 0.5 * 0.5 + (move_array[i+1]-move_array[i])**2 * 0.5 * 0.5
    print("So the payoffs for each player are:")
    print(payoff_array)
    return payoff_array

#Make a picture! Good lookin'!
# Setup a plot such that only the bottom spine is shown
def setup(ax):
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00)
    ax.tick_params(which='major', length=5)
    ax.tick_params(which='minor', width=0.75)
    ax.tick_params(which='minor', length=2.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.patch.set_alpha(0.0)

    
p1_move = getMove(1)
p2_move = getMove(2)

ax = plt.subplot()
setup(ax)
ax.xaxis.set_major_locator(ticker.AutoLocator())
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.axvline(x=p1_move, ymax = 0.25, color = "red")
ax.axvline(x=p2_move, ymax = 0.25, color = "blue")

ax.text(0.0, 1, "Firm Positions", fontsize=14, transform=ax.transAxes)

getHotellingScores([p1_move, p2_move])

