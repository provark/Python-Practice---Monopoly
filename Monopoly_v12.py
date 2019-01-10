#!/usr/bin/env python3

#********************************#
### CHAPTER 1: Property class ###
# test comment
class Property:
    def __init__(self, name, color, price, rent, rent_h1, rent_h2, rent_h3, rent_h4, rent_h5,
                 house_cost, mortgage, houses = 0, mort_status = False):
        self.name = name
        self.color = color
        self.price = price
        self.rent = rent
        self.rent_h1 = rent_h1
        self.rent_h2 = rent_h2
        self.rent_h3 = rent_h3
        self.rent_h4 = rent_h4
        self.rent_h5 = rent_h5
        self.houses = houses
        self.house_cost = house_cost
        self.mortgage = mortgage
        self.mort_status = mort_status
        
Med_Ave = Property("purple: Mediterranean Avenue", "purple",
                   60, 2, 10, 30, 90, 160, 250, 50, 30) 
Bal_Ave = Property("purple: Baltic Avenue", "purple",
                   60, 4, 20, 60, 180, 320, 450, 50, 30)

Ori_Ave = Property("blue:   Oriental Avenue", "blue",
                   100, 6, 30, 90, 270, 400, 550, 50, 50)
Ver_Ave = Property("blue:   Vermont Avenue", "blue",
                   100, 6, 30, 90, 270, 400, 550, 50, 50)
Con_Ave = Property("blue:   Connecticut Avenue", "blue",
                   100, 8, 40, 100, 300, 450, 600, 50, 60)

Cha_Pla = Property("pink:   St. Charles Place", "pink",
                   140, 10, 50, 150, 450, 625, 750, 100, 70)
Sta_Ave = Property("pink:   States Avenue", "pink",
                   140, 10, 50, 150, 450, 625, 750, 100, 70)
Vir_Ave = Property("pink:   Virginia Avenue", "pink",
                   160, 12, 60, 180, 500, 700, 900, 100, 80)

Jam_Pla = Property("orange: St. James Place", "orange",
                   180, 14, 70, 200, 550, 750, 950, 100, 90)
Ten_Ave = Property("orange: Tennesee Avenue", "orange",
                   180, 14, 70, 200, 550, 750, 950, 100, 90)
New_Ave = Property("orange: New York Avenue", "orange",
                   200, 16, 80, 220, 600, 800, 1000, 100, 100)

Ken_Ave = Property("red:    Kentucky Avenue", "red",
                   220, 18, 90, 250, 700, 875, 1050, 150, 110)
Ind_Ave = Property("red:    Indiana Avenue", "red",
                   220, 18, 90, 250, 700, 875, 1050, 150, 110)
Ill_Ave = Property("red:    Illinois Avenue", "red",
                   240, 20, 100, 300, 750, 925, 1100, 150, 120) 

Atl_Ave = Property("yellow: Atlantic Avenue", "yellow",
                   260, 22, 110, 330, 800, 975, 1150, 150, 130)
Ven_Ave = Property("yellow: Ventnor Avenue", "yellow",
                   260, 22, 110, 330, 800, 975, 1150, 150, 130)
Mar_Gar = Property("yellow: Marvin Gardens", "yellow",
                   280, 24, 120, 360, 850, 1025, 1200, 150, 140)

Pac_Ave = Property("green:  Pacific Avenue", "green",
                   300, 26, 130, 390, 900, 1100, 1275, 200, 150)
Nor_Ave = Property("green:  North Carolina Avenue", "green",
                   300, 26, 130, 390, 900, 1100, 1275, 200, 150)
Pen_Ave = Property("green:  Pennsylvania Avenue", "green",
                   320, 28, 150, 450, 1000, 1200, 1400, 200, 160)

Par_Pla = Property("indigo: Park Place", "indigo",
                   350, 35, 175, 500, 1100, 1300, 1500, 200, 175)
Boardw  = Property("indigo: Boardwalk", "indigo",
                   400, 50, 200, 600, 1400, 1700, 2000, 200, 200)

Uti_Ele = Property("Utility Electric Company", "utility",
                   0, 0, 0, 0, 0, 0, 0, 0, 75)
Uti_Wat = Property("Utility Water Works", "utility",
                   0, 0, 0, 0, 0, 0, 0, 0, 75)

RR_Read = Property("Reading Railroad", "railroad",
                   0, 0, 0, 0, 0, 0, 0, 0, 100)
RR_Penn = Property("Pennsylvania Railroad", "railroad",
                   0, 0, 0, 0, 0, 0, 0, 0, 100)
RR_BO = Property("B&O Railroad", "railroad",
                 0, 0, 0, 0, 0, 0, 0, 0, 100)
RR_Short = Property("Short Line Railroad", "railroad",
                    0, 0, 0, 0, 0, 0, 0, 0, 100)

# Creating the game board - a total of 40 squares
board = (["GO"], [Med_Ave.name, Med_Ave.price, Med_Ave], ["Community Chest 1"], [Bal_Ave.name, Bal_Ave.price, Bal_Ave],
         ["Income Tax - pay 10% or $200"], ["Reading Railroad", 200, RR_Read], [Ori_Ave.name, Ori_Ave.price, Ori_Ave], ["Chance 1"],
         [Ver_Ave.name, Ver_Ave.price, Ver_Ave], [Con_Ave.name, Con_Ave.price, Con_Ave], ["Visiting jail"],
         [Cha_Pla.name, Cha_Pla.price, Cha_Pla], ["Utility Electric Company", 150, Uti_Ele], [Sta_Ave.name, Sta_Ave.price, Sta_Ave],
         [Vir_Ave.name, Vir_Ave.price, Vir_Ave], ["Pennsylvania Railroad", 200, RR_Penn], [Jam_Pla.name, Jam_Pla.price, Jam_Pla],
         ["Community Chest 2"], [Ten_Ave.name, Ten_Ave.price, Ten_Ave], [New_Ave.name, New_Ave.price, New_Ave],
         ["Free Parking"], [Ken_Ave.name, Ken_Ave.price, Ken_Ave], ["Chance 2"], [Ind_Ave.name, Ind_Ave.price, Ind_Ave],
         [Ill_Ave.name, Ill_Ave.price, Ill_Ave], ["B&O Railroad", 200, RR_BO], [Atl_Ave.name, Atl_Ave.price, Atl_Ave],
         [Ven_Ave.name, Ven_Ave.price, Ven_Ave], ["Utility Water Works", 150, Uti_Wat], [Mar_Gar.name, Mar_Gar.price, Mar_Gar],
         ["GO TO JAIL"], [Pac_Ave.name, Pac_Ave.price, Pac_Ave], [Nor_Ave.name, Nor_Ave.price, Nor_Ave], ["Community Chest 3"],
         [Pen_Ave.name, Pen_Ave.price, Pen_Ave], ["Short Line Railroad", 200, RR_Short], ["Chance 3"],
         [Par_Pla.name, Par_Pla.price, Par_Pla], ["Luxury Tax - pay $75"], [Boardw.name, Boardw.price, Boardw])
         
#need property list to determine whether a property is available for purchase
property_list = [item for item in board if (len(item) > 1) and (type(item[1]) == int)]
chance_list = [["Pay $50 to Red Cross", 100], ["Pay fishing license fee of $100", 100], ["Pay $30 for a parking ticket", 30],
               ["Bank error in your favor, collect $150", 150], ["Collect $50 for blood donation", 50],
               ["Collect $100 bill you found on street", 100], ["Pay dance contest fee of $65.", 65],
               ["You got a gift card from Starbucks. Collect $25", 25], ["Pay driver's licens fee of $30.", 30],
               ["GET OUT OF JAIL FREE!", 0], ["Collect $120 for fixing your friend's ghost trap.", 120]]

community_chest = [["Your car broke down. Pay $200 for repairs", 200], ["Your rich aunt left inheritance. Collect $300.", 300],
                   ["You got 100K points on your credit card. Collect $100", 100], ["You went to emergency room due to sniffles, pay $100", 35],
                   ["HOA special assessment, pay $50", 50], ["You sold a paperclip necklace on Ebay, collect $73", 73],
                   ["Pay $80 to the knight who captured the monster hiding in your closet", 50],
                   ["You found a gift card someone gave you for your birthday 3 years ago. Collect $100", 100],
                   ["You sued your neighbor because his dog pooped in your mailbox. Collect $250", 250],
                   ["GET OUT OF JAIL FREE!", 0], ["You took your pet cockroach to the vet for stomach problems. Pay $80", 80]]

#*****************************************************************#
### CHAPTER 2: Player class with a number of methods, including the all-important move method ###

import random
class Player:
    def __init__(self, name, cash):
        self.count = 0
        self.name = name
        self.cash = cash
        self.prop = [] # this will contain just the property names, so it's easier to see and print
        self.prop_object = [] # this will contain the property object, so you can use attributes
        self.board_index = 0
        self.turn_count = 0 # this will be used to count turns sitting in jail
        self.net_worth = self.cash
        self.get_out = 0
      
    #TRADE METHOD allowing players to exchange cash and property with each other
    def trade_prop(self):
 
        print("Who do you want to tade with? \n")
        for player in player_list:
            print("  Player " + str(player_list.index(player) + 1) + "\t" + player + "\n")
        while True:
            trader = input("Enter other player number: ")
            if trader == "1":
                trader = Player1
                if trader.name == self.name:
                    print("You cannot trade with yourself, only another player.")
                    continue
                else:
                    break
              
            if trader == "2":
                trader = Player2
                if trader.name == self.name:
                    print("You cannot trade with yourself, only another player.")
                    continue
                else:
                    break
              
            if trader == "3": 
                if len(player_list) > 2:
                    trader = Player3
                    if trader.name == self.name:
                        print("You cannot trade with yourself, only another player.")
                        continue
                    else:
                        break
                else: 
                    print("Only two players in game: choose player 1 or 2")
                    continue
              
            if trader == "4": 
                if len(player_list) > 3:
                    trader = Player4
                    if trader.name == self.name:
                        print("You cannot trade with yourself, only another player.")
                        continue
                    else:
                        break
                else: 
                    print("Only three players in game: choose player 1, 2, or 3")
                    continue
            else:
                print("Invalid input: enter number 1-4")
                continue

        print(trader.name + " has the following cash and property: \n")
        print("$" + str(trader.cash) + "\n")
        if len(trader.prop) > 0:
            for index, item in enumerate(trader.prop, start = 1):
                print("  " + str(index) + "  " + item + "\n")
        else:
              print(trader.name + " has no property.")

        # This is only time I ask player to enter name of property. This allows one prompt for both cash & property.      
        give_prop = input("\tWhat do you want to GIVE? \n\tEnter just first name of property (e.g, 'Baltic')"
                          " or cash amount (just numbers) \n\tEnter 0 if you want to give nothing.\n")
        
        receive_prop = input("\tWhat do you want to RECEIVE? \n\tEnter property name (e.g., 'Baltic') or cash amount (just numbers)"
                             "\n\tEnter 0 if you want to receive nothing\n")              
        # this try/except sequence determines whether input is cash or property
        try: 
            give_prop = int(give_prop)
            confirm = input("Confirm: you want to GIVE $" + str(give_prop) + " to " + trader.name + "? Type Y or N.")
            if confirm.lower() == "y":
                self.cash -= give_prop
                trader.cash += give_prop
                print("\n\t Transfer Completed. \n")
        except:
            confirm = input("Confirm: you want to GIVE " + str(give_prop) + " to " + trader.name + "? Type Y or N.")
            if confirm.lower() == "y":
                test_num = len(self.prop)
                for item in self.prop_object:
                    #I need to think of how to prevent player from entering 'blue' or 'avenue', for example, and getting all properties
                    # And to make it apply to railroads and utilities
                    #this appends/removes from the two player.property lists (I should probably make it one)
                    if give_prop.lower() in item.name.lower():
                        trader.prop.append(item.name)
                        trader.prop_object.append(item)
                        self.prop.remove(item.name)
                        self.prop_object.remove(item)
                        print("\n\t Transfer completed. \n")
                        break
                # Checks to see if transfer occurred
                if test_num == len(self.prop):
                    print("\n\t Transfer failed. \n")
            else:
                pass
        
        
        try: 
            receive_prop = int(receive_prop)
            confirm = input("Confirm: you want to RECEIVE $" + str(receive_prop) + " from " + trader.name + "? Type Y or N.")
            if confirm.lower() == "y":
                self.cash += receive_prop
                trader.cash -= receive_prop
                print("\n\t Transfer Completed. \n")
        except:
            confirm = input("Confirm: you want to RECEIVE " + str(receive_prop) + " from " + trader.name + "? Type Y or N.")
            if confirm.lower() == "y":
                test_num = len(trader.prop)
                for item in trader.prop_object:
                    if give_prop.lower() in item.name.lower():
                        self.prop.append(item.name)
                        self.prop_object.append(item)
                        trader.prop.remove(item.name)
                        trader.prop_object.remove(item)
                        print("\n\t Transfer completed. \n")
                        break
                if test_num == len(self.prop):
                    print("\n\t Transfer failed. \n")
            else:
                pass
     
    # PAY RENT METHOD. If player lands on another's square, this method
    # forces the player to pay rent depending on number of house on property.
    # This method will be called in the player.move method
    # Note, Utility pay rent action is coded in the player.move method
    def pay_rent(self, player, p_position):
        if not "Railroad" in p_position[0] and not "Utility" in p_position[0]:
            print("\n" + p_position[0][8:] + " is owned by " + player.name)
            if p_position[2].houses == 0: 
                print("\n\t$$$  Pay rent to player in the amount of $" + str(p_position[2].rent))
                player.cash += p_position[2].rent
                self.cash -= p_position[2].rent
            elif p_position[2].houses == 1: 
                print("\n\t$$$  This property contains 1 house. Pay player $" + str(p_position[2].rent_h1))
                player.cash += p_position[2].rent_h1
                self.cash -= p_position[2].rent_h1
            elif p_position[2].houses == 2: 
                print("\n\t$$$  This property contains 2 houses. Pay player $" + str(p_position[2].rent_h2))
                player.cash += p_position[2].rent_h2
                self.cash -= p_position[2].rent_h2
            elif p_position[2].houses == 3: 
                print("\n\t$$$  This property contains 3 houses. Pay player $" + str(p_position[2].rent_h3))
                player.cash += p_position[2].rent_h3
                self.cash -= p_position[2].rent_h3
            elif p_position[2].houses == 4: 
                print("\n\t$$$  This property contains 4 houses. Pay player $" + str(p_position[2].rent_h4))
                player.cash += p_position[2].rent_h4
                self.cash -= p_position[2].rent_h4
            elif p_position[2].houses == 5: 
                print("\n\t$$$  This property contains a hotel. Sorry. Pay player $" + str(p_position[2].rent_h5))
                player.cash += p_position[2].rent_h5
                self.cash -= p_position[2].rent_h5
        elif "Railroad" in p_position[0]:
            print("\n" + p_position[0] + " is owned by " + player.name)
            test_string = " ".join(player.prop) 
            if test_string.count("Railroad") == 1:
                print("\n\t$$$  " + player.name + " owns 1 railroad. Pay $25.") 
                player.cash += 25
                self.cash -= 25
            if test_string.count("Railroad") == 2:
                print("\n\t$$$  " + player.name + " owns 2 railroads. Pay $50.") 
                player.cash += 50
                self.cash -= 50
            if test_string.count("Railroad") == 3:
                print("\n\t$$$  " + player.name + " owns 3 railroads. Pay $100.") 
                player.cash += 100
                self.cash -= 100
            if test_string.count("Railroad") == 4:
                print("\n\t$$$  " + player.name + " owns 4 railroads. Pay $200.") 
                player.cash += 200
                self.cash -= 200
        print("\nThis money has been deducted from your account. Your balance is now $" + str(self.cash) + "\n")
        
    
    # MONOPOLY CHECK METHOD. Checks if player has monopoly; returns list of monopolies
    def monopoly_check(self):
        test_string = " ".join(self.prop)
        monopoly_list = []
        # Note, if Railroads and Utilities are not defined Property objects,
        # this code will cause error during monopoly check
        if test_string.count("purple") == 2:
            for item in self.prop_object:
                if item.color == "purple":
                    print("this works")
                    monopoly_list.append(item)
        if test_string.count("blue") == 3:
            for item in self.prop_object:
                if item.color == "blue":
                    monopoly_list.append(item)
        if test_string.count("pink") == 3:
            for item in self.prop_object:
                if item.color == "pink":
                    monopoly_list.append(item)    
        if test_string.count("orange") == 3:
            for item in self.prop_object:
                if item.color == "orange":
                    monopoly_list.append(item)
        if test_string.count("red") == 3:
            for item in self.prop_object:
                if item.color == "red":
                    monopoly_list.append(item)
        if test_string.count("yellow") == 3:
            for item in self.prop_object:
                if item.color == "yellow":
                    monopoly_list.append(item)
        if test_string.count("green") == 3:
            for item in self.prop_object:
                if item.color == "green":
                    monopoly_list.append(item) 
        if test_string.count("indigo") == 2:
            for item in self.prop_object:
                if item.color == "indigo":
                    monopoly_list.append(item)
        for item in monopoly_list:
            if item.mort_status == True: # checks if mortgaged
                monopoly_list.remove(item)
        return monopoly_list # a list of objects 

    # MORTGAGE METHOD (includes selling buildings)
    def mortgage_sell(self):
        non_mortgaged_list = [item for item in self.prop_object if item.mort_status == False]
        mortgaged_list = []
        print("\nHere are your properties available to mortgage: \n")
        for index, item in enumerate(non_mortgaged_list):
            print("  " + str(index + 1) + "  " + item.name + ".  Mortgage Value:  $" + str(item.mortgage))
        while True:
            mort_input = input("\nEnter property number you'd like to mortgage (or 'q' to quit): ")
            if mort_input == "q":
                break
            else:
                try:
                    mort_input = int(mort_input)
                    mort_prop = non_mortgaged_list[mort_input - 1]
                    if mort_prop.houses > 0:
                        while True:
                            print("\nYou have " + mort_prop.houses +
                                  " building[s] on this property that you must sell before mortgaging.")
                            if mort_prop.houses == 5:
                                print("\nThe fact that you have five buildings means that you have a hotel (which includes four houses)")
                            print("\nYou can sell each building (house or hotel) for $" + str(mort_prop.house_cost/2))
                            input1 = ("\n\tEnter total number of buildings you wish to sell: ")
                            try:
                                num_bldg = int(num_build)
                                if num_bldg > mort_prop.houses:
                                    print("\nNice try, but you cannot sell more buildings than you have.")
                                elif num_bldg < 1:
                                    print("\nYou cannot sell less than one building.")
                                else:
                                    mort_prop.houses -= num_bldg
                                    sell_price = (num_bldg * mort_prop.house_cost)/2
                                    self.cash += sell_price
                                    print("\n You have sold " + str(num_bldg) + " buildings for a total of $" + str(sell_price))
                                    break
                            except:
                                print("\nInvalid input. Enter a valid number.")
                                continue
            
                    if mort_prop.houses == 0:
                        conf = input("\nPress Enter to confirm you want to mortgage " + mort_prop.name + " or press 'q' to return to menu.")
                        if conf == "q":
                            break
                        else:
                            self.cash += mort_prop.mortgage
                            mort_prop.mort_status = True
                            print("\nYou have mortgaged:  " + mort_prop.name + ". \n") 
                            print("You can no longer receive rent or buy houses for this property until you pay off mortgage.\n")
                except:
                    print("\nInvalid input. Enter a valid number.")
                    continue
        print("\nYour cash balance is now $" + str(self.cash))
        
    # UNMORTGAGE METHOD            
    def unmortgage(self):
        mortgaged_list = [item for item in self.prop_object if item.mort_status == True]
        print("\nHere are your mortgaged properties: ")
        for index, item in enumerate(mortgaged_list):
            print("  " + str(index + 1) + "  " + item.name + ".  Mortgage Value:  $" + str(item.mortgage) + "\n")
        while True:
            unmort_input = input("\nEnter property number you'd like to unmortgage (or press 'q' to exit): ")
            if unmort_input == "q":
                break
            else:
                try:
                    unmort_input = int(unmort_input)
                    unmort_prop = mortgaged_list[unmort_input - 1]
                    self.cash -= unmort_prop.mortgage
                    unmort_prop.mort_status = False
                    print("\nYou have unmortgaged:  " + unmort_prop.name + ". \n") 
                    print("You now can receive rent and buy houses for this property.\n")          
                except:
                    print("\nInvalid input. Enter a valid number.")
                    continue                

    #*** MOVE METHOD ***#. Implements the player's move, including dealings with properties
    def move(self):
        # Rolling the dice
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        total_roll = die_1 + die_2
        jackpot = 1000
        print("\n" + self.name.capitalize() + ", you rolled a " + str(die_1) + " and " + str(die_2) + ", for a total of " + str(total_roll) + "\n")
        if die_1 == die_2:
            print("\n[::][::]  You rolled doubles!  [::][::] \n")
            
        # Moving player on the board
        if self.board_index + total_roll <=39: #this to make sure we don't go over square 39, outside the board index 
            player_position = board[self.board_index + total_roll] #E.g., if self.board_index == 0 and total_roll == 10, then player_position == "Free Parking" 
        elif self.board_index + total_roll > 39:
            self.board_index = (self.board_index + total_roll) - 40
            player_position = board[self.board_index]
            print("$***$  You passed GO! Collect $200.  $***$ \n")
            self.cash += 200
        print("\tYou landed on " + player_position[0] + "\n")
        if player_position[0] in self.prop:
            print("\tYou own this property.\n")
        self.board_index += total_roll # this counts the board index by the total roll amount, thereby advancing the player on the board
       
        # Dealing with the properties/squares on which player landed.
        
        # First dealing with properties that can be bought - streets, railroads, utilities
        if player_position in property_list:
            #print("player_position: ", player_position)
            #print("property_list: ", property_list)
            # The Property.name strings (index 0 of player_position) begin with color (e.g., "Blue"),
            # and I want to avoid repeating the color od property in print statements
            # So the following conditional is used to slice the color from non-railroad properties in print statements
            if "Railroad" in player_position[0] or "Utility" in player_position[0]:
                prop_name = player_position[0]
            else:
                prop_name = player_position[0][8:]
            print("\n" + prop_name + " is unowned, so you may buy it from the bank. \n")
            print("\tYour cash balance is $" + str(self.cash) + "\n")
            buy_prompt = input("Would you like to buy " + prop_name + " for $" + str(player_position[1]) + "? Type Y or N.")
            if buy_prompt.lower() == "y":
                # pops the property from property_list and appends property name to self.prop attribute
                # this will do the same for the propery object
                bought_prop = property_list.pop(property_list.index(player_position))
                self.prop.append(bought_prop[0]) # appends property name
                self.prop_object.append(bought_prop[2]) # appends property object to another list
                self.cash -= player_position[1] 
                print("\t--- Congratulations! You just bought " + prop_name + ". --- \n")
                #print("Your properties are now as follows: ", [item[0] for item in self.prop], "\n")
            else:
                pass
            
        # Rent Payment: this part forces player to pay rent if property is owned by another
        elif not player_position in property_list and len(player_position) > 1:
            if player_position[0].startswith("Utility") == False:
                if Player1.name in player_list and player_position[0] in Player1.prop and self.name != Player1.name:
                    self.pay_rent(Player1, player_position)
                elif Player2.name in player_list and player_position[0] in Player2.prop and self.name != Player2.name:           
                    self.pay_rent(Player2, player_position)
                elif Player3.name in player_list and player_position[0] in Player3.prop and self.name != Player3.name:            
                    self.pay_rent(Player3, player_position)
                elif Player4.name in player_list and player_position[0] in Player4.prop and self.name != Player4.name:            
                    self.pay_rent(Player4, player_position)
                    
            # Utility is a special case requiring use of total_roll variable,
            # so I figured it's simpler to include it here rather than creating a separate method
            else:
                print("\n" + player_position[0] + " is owned by " + player.name)
                test_string = " ".join(player.prop) 
                if test_string.count("Utility") == 1:
                    print("\n" + player.name + " owns 1 utility. Pay 4 times the total dice roll.")
                    print("\t$$$  Your total dice roll was " + str(total_roll) + ", so you must pay $" + str(total_roll * 4))
                    player.cash += total_roll * 4
                    self.cash -= total_roll * 4
                if test_string.count("Utility") == 2:
                    print("\n" + player.name + " owns both utilities. Pay 10 times the total dice roll.")
                    print("\t$$$  Your total dice roll was " + str(total_roll) + ", so you must pay $" + str(total_roll * 10))
                    player.cash += total_roll * 10
                    self.cash -= total_roll * 10           
                print("\n\t This money has been deducted from your account. Your balance is now $" + str(self.cash) + "\n")
    
        # Other Squares: dealing with other squares - tax, chance/community chest, jail, jackpot
        elif player_position == board[20]:
            print("$***$  YOU WON THE JACKPOT!!!  $***$ \n")
            print(" ***  $" + str(jackpot) + " has been added to your account! \n")
            self.cash += jackpot
            #print("\t your balance is now $" + str(self.cash) + "\n")
        elif player_position == board[30]:
            print("|||  Go to jail :( Pay $50 to get out.  |||\n")
            player_position = board[10]
            self.cash -= 50 
            jackpot += 50
            #print("\t your balance is now $" + str(self.cash) + "\n")
        elif player_position == board[38]:
            print("\t$$$  Pay tax of $75. Money is automatically withdrawn from your account. \n")
            self.cash -= 75
            jackpot += 75
            #print("\t your balance is now $" + str(self.cash) + "\n")          
        elif player_position == board[4]:
            if self.cash * 0.10 >= 200:
                print("\t$$$  Your cash balance is over $2000, so you must pay $200,"
                      " which will be automatically withdrawn from your account. \n")
                self.cash -= 200
                jackpot += 200
                #print("\t your balance is now $" + str(self.cash) + "\n")
            else:
                print("\t$$$  Your cash balance is less than $2000, so you must pay 10%, or $" +
                      str(self.cash * 0.10) + "\n")
                self.cash = self.cash - (self.cash * 0.10)
                jackpot += (self.cash * 0.10)
                #print("\t your balance is now $" + str(self.cash) + "\n")
                
        # Community Chest        
        elif player_position in [board[2], board[17], board[33]]: 
            cc_prompt = input("\nPress Enter to see Community Chest card. \n") # creates extra anticipation before flip
            if cc_prompt == "" or cc_prompt != "":
                cc_card = community_chest.pop(0) # pop first card from cc list
                print("-- " + cc_card[0])

                if "pay" in cc_card[0].lower():
                    self.cash -= cc_card[1]
                elif "collect" in cc_card[0].lower():
                    self.cash += cc_card[1]
                elif "JAIL" in cc_card[0]:
                    self.get_out += 1
                community_chest.append(cc_card) # append cc_card back to end of list
                print("-- Your cash balance is now $" + str(self.cash) + "\n")   
                
        # Chance   
        elif player_position in [board[7], board[22], board[36]]: # this is chance
            c_prompt = input("\nPress Enter to see Chance card. \n") 
            if c_prompt == "" or c_prompt != "":
                c_card = chance_list.pop(0)
                print("-- " + c_card[0])
                if "pay" in c_card[0].lower():
                    self.cash -= c_card[1]
                elif "collect" in c_card[0].lower():
                    self.cash += c_card[1]
                elif "JAIL" in c_card[0]:
                    self.get_out += 1
                chance_list.append(c_card)
                print("-- Your cash balance is now $" + str(self.cash) + "\n")
                
        # Trade Options: gives option to trade or print status or build houses  
        while True:
            action = input("\n\tWould you like to trade with another player or build house/hotel (if applicable)?"
                           "\n\n\tType 't' to trade' or 'b' to build', or press Enter to skip.")
            # ************
            # ************ I'll put a "secret" admin code here to test game quickly
            if action == "password":
                print("Your position:", self.board_index)
                s_prompt = input("Enter square you want to be on (press Enter to skip): ")
                if s_prompt != "":
                    s_prompt = int(s_prompt)
                    self.board_index = board[s_prompt]
                    print("Your position:", self.board_index)
                else:
                    pass
                s2_prompt = input("Enter cash you want to receive: ")
                self.cash += int(s2_prompt)
                print("Your cash:", self.cash)
                print("Available properties: ")
                for index, item in enumerate(property_list):
                    print(index, item, sep='  ')
                while True:
                    s3_prompt = input("Enter property you want to obtain or 'q': ")
                    try:
                        s3_prompt = int(s3_prompt)
                        taken_prop = property_list.pop(s3_prompt)
                        self.prop.append(taken_prop[0])
                        self.prop_object.append(taken_prop[2])
                    except:
                        if s3_prompt == 'q':
                            print("Your properties:")
                            for index, item in enumerate(self.prop):
                                print(index, item, sep='  ')
                            break
                        elif s3_prompt == "property_list":
                            print("Property_list", property_list)
                        elif s3_prompt == "self.prop":
                            print("self.prop: ", self.prop)
                        elif s3_prompt == "self.prop_object":                           
                            print("self.prop_object: ", self.prop_object)
                        #elif s3_prompt == "m_list":
                         #   print("m_list", m_list)
            #*******************
            elif action != "" and action not in ["t", "tr", "tra", "trad", "trade", "b", "bu", "bui", "buil", "build"]:
                print("Invalid input. Only 'b', 't', or Enter are accepted.")
                continue
            elif action == "":
                break
            elif action in ["t", "tr", "tra", "trad", "trade"]:
                self.trade_prop()
                break
            # Build Houses ************
            elif action in ["b", "bu", "bui", "buil", "build"]:               
                m_list = self.monopoly_check() # this is a list of objects
                #print("\nPrinting m-list: ", m_list) #this works
                if len(m_list) < 2:
                    print("\nYou have no monopolies on which to build. \n")
                    continue
                #**************
                else:    
                    print("Here are your monopoly properties: \n")
                    name_list = [item.name for item in m_list]
                    for index, item in enumerate(name_list, start=1):
                        print(index, item, sep='  ')
                        #the above code works - prints required items
                    while True:
                        m_answer = input("\nEnter the property number (from above list) you wish to build on (or 'q' to quit): ")
                        if m_answer == 'q':
                            break
                        elif m_answer.isdigit() == False:
                            print("Invalid input. Enter integer.")
                            continue             
                        else:
                            m_answer = int(m_answer)
                            build_prop = self.prop_object[m_answer - 1]
                            print("\nOkay. You will build one house or hotel on " + build_prop.name + "\n") 
                            #print("build_prop: ", build_prop)
                            #print("board[1] and board[3]: ", board[1], board[3]) #confirmed build_prop == board[]
                            build_prop.houses += 1
                            print("\nbuild_prop.houses: ", build_prop.houses)
                            #print("board[3][2].houses: ", board[3][2].houses)
                            #for lyst in board:
                             #   if len(lyst) > 2 and lyst[2] == build_prop:
                              #      build_index = board.index(lyst)
                               #     board[build_index][2].houses += 1
                            # check for only one house at a time and for equal build of houses on each property, for each monopoly
                            # effectively, it builds house as requested, but if the difference is more than one, the house is removed.
                            house_check_list = []
                            for item in m_list: # m_list is list of objects comprising a monopoly (i.e., all red properties)
                                #print("m_list ", m_list) # this checks out
                                if item.color == build_prop.color:
                                    house_check_list.append(item.houses)
                            print("\nhouse check list", house_check_list)
                            if abs(build_prop.houses - max(house_check_list)) > 1:
                                print("\nFor each monopoly, the number of houses on each property cannot differ by more than one. You must build equally.\n")
                                build_prop.houses -= 1
                                assert build_prop.houses >= 0
                                continue
                            if max(house_check_list) != 0 and max(house_check_list) == min(house_check_list):
                                print("\nEach " + build_prop.color + " property now contains " + str(build_prop.houses) + " houses.\n")
                                break
                    #except:
                         #   print("Invalid input. Enter integer.")
                          #  continue             
 
        # End of turn process - includes dealing with mortgages and double rolls
        # here we transfer all properties acquired in trading (rather than purchase) to player.prop and player.prop_object 
        print("\n *** You have $" + str(self.cash) + "\n")
        mortgage_test = [item.mortgage for item in self.prop_object if item.mort_status == True]
        if len(mortgage_test) > 0 and self.cash > max(mortgage_test):
            mort_input = input("Would you like to unmortgage any properties? Type Y or N: ")
            if mort_input.lower() == "y":
                self.unmortgage()
            else:
                pass
        if self.cash < 0 and len(self.prop_object) > 0:
            print("Because you have negative cash, you must mortgage or sell properties to stay in the game.\n")
            self.mortgage_sell()
        
        unmortgaged_list = [item.name for item in self.prop_object if item.mort_status == False]
        mortgaged_list = [item.name for item in self.prop_object if item.mort_status == True]
        if len(self.prop_object) > 0:
            print(" *** Your properties are: \n")
            for index, item in enumerate(self.prop_object, start = 1):
                print("\t" + str(index) + "  " + item.name)
            if len(mortgaged_list) > 0:
                print("\n *** Your mortgaged properties are: \n")
                for index, item in enumerate(mortgaged_list, start = 1):
                    print("\t" + str(index) + "  " + item)
        else:
            print("You have no properties. \n")
        
        if self.cash < 0 and len(unmortgaged_list) == 0:
            return "bankrupt"
        elif die_1 == die_2:
            return {"doubles": "doubles", "player position": player_position, "player cash": self.cash, "player properties": self.prop}      
        else:
            print("\n --- END TURN for " + self.name + " --- \n")
            print(border)
            return {"player position": player_position, "player cash": self.cash, "player properties": self.prop}
        #return ("You are located on: " + player_position + "\n" + "You now have $" + self.cash + "\n" + "Your properties are:" self.prop)
         
    
### CHAPTER 3: Creating a list of players and starting the game
# function to create player list from input
def set_game():
    player_list = []        
    
    while len(player_list) <= 4:
        p1_name = input("Enter first player name or token: ")
        if p1_name != "":
            player_list.append(p1_name)
            
        p2_name = input("Enter second player name or token: ")
        if p2_name != "":
            player_list.append(p2_name)       
        
        p3_name = input("Enter third player name or token. If no third player, enter 'none': ")
        if p3_name != "" and p3_name != "none":
            player_list.append(p3_name)                
        else: 
            break
        
        p4_name = input("Enter fourth player name or token. If no fourth player, enter 'none': ")
        if p4_name != "" and p4_name != "none":
            player_list.append(p4_name)
            break
        else: 
            break
        
    return player_list

# Calling the set-game function and printing list of players. 
player_list = set_game()
border = ("\n" + ("*" * 30) + "\n")
print(border)
print("Great! New game started successfully. Here are the players: \n")
random.shuffle(chance_list)
random.shuffle(community_chest)
for player in player_list:
    print("Player " + str(player_list.index(player) + 1) + "\t" + player + "\n")
print(border)
        
# Creating individual players from player_list and assigning each a cash balance 
Player1 = Player(player_list[0], 1000)
Player2 = Player(player_list[1], 1000)
if len(player_list) > 2:
    Player3 = Player(player_list[2], 1000)
if len(player_list) > 3: 
    Player4 = Player(player_list[3], 1000)

### CHAPTER 4: Moving the game along
# The code moving the game is a while loop. But first, we define a meta move function
# that will call the beefy player.move method, to make the code more compact.

def player_move(player):
    loser_list = []
    while True:
        # Dealing with jail situations
        if player.board_index == 30:
            if player.turn_count > 3:
                print("\n" + player.name + ", you've sat in jail for three turns. You are now free to go. \n")
                pass
            else:
                jail_prompt = input("\n" + player.name + ", do you want to pay $50 "
                                    "(or use a GOOJF card if available) to get out of jail? Type Y or N: ")
                if jail_prompt.lower() == "n":
                    player.turn_count += 1
                    break
                else:
                    player.turn_count = 0
                    if player.get_out > 0:
                        player.get_out -= 1
                        print("\nYou used your GET OUT OF JAIL FREE card! Continue turn.\n")
                        pass
                    else:
                        player.cash -= 50
                        print("\nYou paid $50 to get out of jail! Great deal! Continue turn. \n")
                        pass
        print(player.name.capitalize() + ", you are on square " + str(player.board_index) + ":  " + board[player.board_index][0])  
        prompt = input("\n\t[::] " + player.name.capitalize() + ", your turn to roll. Press Enter to roll dice or 'q' to quit: ")
        if prompt.lower() in ["q", "quit," "qu", "qui"]:
            return "quit"
        elif prompt.lower() == "":
            # calling the player.move() method described in Player class
            # player.move() returns dictionary with board position, cash, and property list
            player_status = player.move()
            if player_status == "bankrupt":
                print(border)
                print("\n*** Sorry, you went bankrupt. You're out of the game. :( *** \n")
                print(border)
                player_list.remove(player.name)
                loser_list.append(player.name)
                
            # dealing with doubles
            elif "doubles" in player_status and player.board_index != 30:
                print("\n[::][::]  Since your rolled doubles, you get to roll again.\n")
                result2 = player.move()
                if "doubles" in result2:
                    print("\n[::][::]  Because you rolled doubles a second time, you get to roll again."
                          " But if you roll doubles one more time, you go to jail.\n")
                    result3 = player.move()
                    if "doubles" in result3:
                        print("\n[::][::]  You rolled doubles three times. GO TO JAIL! \n")
                        player.board_index = 30        
            

            return player_status
            break
        else:
            print("Invalid input. Press Enter or 'q' \n")
            continue
            # player_status is a dictionary showing the player position, cash, and properties

                
while len(player_list) > 1:
    if Player1.name in player_list and len(player_list) > 1:
        p1_move = player_move(Player1)
        if p1_move == "quit":
            break
        print(border)
    
    if Player2.name in player_list and len(player_list) > 1:
        p2_move = player_move(Player2)
        if p2_move == "quit":
            break
        print(border)
        
    # I'm using try/except for players 3 & 4 to avoid NameErrors.
    # Specifically, without the try/except, if only 2 players in game, I would get an error after player 2 turn (NameError: name 'Player3' is not defined).
    # This is because I chose to create Players by first creating a player list and then
    # defining each Player instance based on the index of players in that list. (I probably could have done it differently). This means that I can only
    # define Players 3 and 4 on condition that player_list contains 3 and 4 players, respectively (otherwise index out of range error). So Player3 is only defined
    # if player_list contains 3 items. But, without try/except, if there are only 2 players, the program tries to run the Player3 code but does not recognize Player3
    # (Player3 not defined because player list < 3). If instead of try/except I try something like elif len(player_list) > 3, the game won't work if only Player3 and Player1,
    # for example, are left in the game.
    
    try:
        if Player3.name in player_list and len(player_list) > 1:
            result3 = player_move(Player3)
            if result3 == "quit":
                break
            print(border)
    except:
        pass
    
    try:
        if Player4.name in player_list and len(player_list) > 1:
            result4 = player_move(Player4)
            if result4 == "quit":
                break         
            print(border)
    except:
        pass
    
if len(player_list) == 1:
    for player in player_list:
        print(border + "\n")
        print ("\n*** " + player.upper() + " IS THE WINNER!!! CONGRATULATIONS! ***\n")
        print(border + "\n")
    end_game = input("press q to exit game: ") 
