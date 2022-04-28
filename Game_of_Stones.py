# THE GAME OF NIMS/STONES
# In this game two players sit in front of a pile of 100 stones. They take turns, each removing between 1 and 5 stones (assuming there are at least 5 stones left in 
# the pile). The person who removes the last stone(s) wins.
# Write a program to play this game. Like many programs, we have to use nested loops.
# In the outermost loop, we want to keep playing until we are out of stones.
# Inside that, we want to keep alternating players. 
# Finally, we might want to have an innermost loop that checks if the user's input is valid. Is it an integer? Is it a valid number between 1 and 5? 
# Are there enough stones in the pile to take off this many? if any of these answers are no, we should tell the user and re-ask them the question. 




Total = 100
Max = 5
pile = Total
while pile > 0:
    #Player 1's Turn
    while True:
        print("It's Player 1's Turn")
        p1_value = int(input("Enter number of stones:"))
        # Checks that player 1 only takes between 1 and 5 stones. If so, substracts them from the pile. Otherwise, tells player 1 to pick a number from 1 to 5.
        if p1_value <= Max and p1_value <= pile and p1_value > 0:
            pile -= p1_value
            print(pile)
            # Checks to see if there are any stones left. If not, player 1 wins.
            if pile == 0:
                print("Player 1 Wins!")
                break
            break
           
        else:
            print("ERROR! PICK A NUMBER FROM 1 TO 5 AND MAKE SURE YOU DON'T TRY TO TAKE MORE THAN WHAT IS AVAILABLE")
    

    #Player 2's Turn
    # This condition is added to check whether player 1 has already taken all the stones, in which case there is no need to continue the game.
    if pile > 0:
        while True:
            print("It's Player 2's Turn")
            p2_value = int(input("Enter number of stones:"))
            # Checks that player 2 only takes between 1 and 5 stones. If so, substracts them from the pile. Otherwise, tells player 1 to pick a number from 1 to 5.
            if p2_value <= Max and p2_value <= pile and p2_value > 0:
                pile -= p2_value
                print(pile)
                # Checks to see if there are any stones left. If not, player 2 wins.
                if pile == 0:
                    print("Player 2 Wins!")
                    break
                break
            else: 
                print("ERROR! PICK A NUMBER FROM 1 TO 5 AND MAKE SURE YOU DON'T TRY TO TAKE MORE THAN WHAT IS AVAILABLE")
    else:
        break
    continue
        