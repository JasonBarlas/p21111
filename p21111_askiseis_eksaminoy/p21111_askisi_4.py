import random


list_of_Tens = ["J", "Q", "K", 10]
def riggify(k_set, flipped):
    if k_set == 1:
        if flipped == False:
            while xartia[-1][0] not in list_of_Tens:
                xartia.append(xartia.pop(0))
        elif flipped == True:
            while xartia[-1][0] in list_of_Tens:
                xartia.append(xartia.pop(0))
        else:               #<-- No chance of going through this case.
            random.shuffle(xartia)


results1="null"
results2="null"
for k2 in range(0,2):
    counter1=0
    counter2=0
    counterD=0
    for k1 in range(0,100):
        xartia = []
        figures = ["J", "Q", "K"]
        xarti = [i for i in range(1, 11)] + figures
        color = ["H", "S", "C", "D"]
        for i in xarti:
            for j in color:
                xartia.append([i,j])
        random.shuffle(xartia)

        flip_player = False
        riggify(k2, flip_player)

        player1=[]
        sum1=0
        while sum1<16:
            sum1=0
            player1.append(xartia.pop())
            # print (player1)
            for card in player1:
                if card[0] in figures:
                    sum1=sum1+10
                else:
                    sum1=sum1+card[0]
            #print(sum1)
        if sum1>21:
            #print("P2 wins!")
            counter2+=1
        else:
            '''
            sxolia pollwn
            grammwn
            '''

            #print("P2 joins the game") #let me add one more player

            flip_player = True
            riggify(k2, flip_player)

            player2=[]
            sum2=0
            while sum2<16:
                sum2=0
                player2.append(xartia.pop())
                # print (player2)
                for card in player2:
                    if card[0] in figures:
                        sum2=sum2+10
                    else:
                        sum2=sum2+card[0]
                #print(sum2)
            if sum2>21:
                sum2=0
            if sum1>sum2:
                #print("P1 wins!")
                counter1+=1
            elif sum2>sum1:
                #print("P2 wins!")
                counter2+=1
            else:
                #print("draw!")
                counterD+=1
    if k2==1:
        results2= "P1 won: " + str(counter1) + " times" + " || " + "P2 won: " + str(counter2) + " times" + " || " + "Number of Draws: " + str(counterD)
    else:
        results1= "P1 won: " + str(counter1) + " times" + " || " + "P2 won: " + str(counter2) + " times" + " || " + "Number of Draws: " + str(counterD)
print ("-----------------------")
print ("First 100 Rounds Results: ||", results1)
print ("Rigged 100 Rounds Results: ||", results2)
print ("-----------------------")
