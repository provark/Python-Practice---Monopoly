#this function sets up the players and tokens
def set_game():
    player_dict = {}
    token_list = []
    
    def set_player_token(name):           
        token = input(name + ": what token would you like - car, ship, dog, or hat? ") 
        while True:       
            if token not in ["car", "ship", "dog", "hat"]:
                token = input("Not allowed: choose car, ship, dog, hat: ")                
            elif token in token_list:
                token = input("Token already taken: choose another: ")
            else:
                token_list.append(token)
                break
        player_dict[name].append(token)            
        
    
    while len(player_dict) <= 4:
        p1_name = input("Enter first player name: ")
        if p1_name != "":
            p1_name = "Player 1 - " + p1_name  
            player_dict[p1_name] = []
        set_player_token(p1_name)

            
        p2_name = input("Enter second player name: ")
        if p2_name != "":
            p2_name = "Player 2 - " + p2_name
            player_dict[p2_name] = []
        set_player_token(p2_name)
        
        
        p3_name = input("Enter third player name or 'none': ")
        if p3_name != "" and p3_name != "none":
            p3_name = "Player 3 - " + p3_name
            player_dict[p3_name] = []                 
        else: 
            break
        set_player_token(p3_name)
        
        
        p4_name = input("Enter fourth player name or 'none': ")
        if p4_name != "" and p4_name != "none":
            p4_name = "Player 4 - " + p4_name
            player_dict[p4_name] = []
        else:
            break
        set_player_token(p4_name)
        
    return player_dict 

#the next code sequence assigns the global variables that I felt were necessary to create a player class. 
#Think it's necessary to identify the players by number to keep track of who's turn it is.
#This should also initiate the set_game() sequence and assign the player dictionary to a variable

player_dict = set_game()
print(player_dict)
for key in player_dict:
    if key.startswith("Player 1"):
        Player_1 = key
    elif key.startswith("Player 2"):
        Player_2 = key
    elif key.startswith("Player 3"):
        Player_3 = key
    elif key.startswith("Player 4"):
        Player_4 = key

# Property class
class Property:
    def __init__(self, color, cost, rent = 0, house_cost = 0, hotel_cost = 0, mortgage = 0)
        self.color = color
        self.cost = cost
        self.rent = rent
        self.house_cost = house_cost
        self.hotel_cost = hotel_cost
        self.mortgage = mortgage
        
 #Med_Ave = Property(brown, 60, 
 #After defining property class, will create the board--I'm thinking a tuple of dictionaries.
 board = (none,["GO"],[Med_Ave.name, Med_Ave.cost], ["Community Chest"],   
 

# Player class, with several class methods to allow players to pay each other and trade property cards 
class Player:
    def __init__(self, name, token):
        self.count = 0
        self.name = name
        self.token = token
        self.cash = 1500
        self.prop = []
        
    def pay_player(self):
        payment = input("How much do you want to pay: ")
        payment = int(payment)
        receiver = input("Pay which player? Enter player number: ")
        if int(receiver) == 1:
            receiver = Player1
        elif int(receiver) == 2:
            receiver = Player2
        elif int(receiver) == 3: 
            if len(player_dict) > 2:
                receiver = Player3
            else: 
                receiver = input("Only two players: enter other player number, 1 or 2: ")
        elif int(receiver) == 4: 
            if len(player_dict) > 3:
                receiver = Player4
            else: 
                receiver = input("Only three players: enter other player number, 1, 2 or 3: ")
        else:
            receiver = input("Invalid input: enter number 1-4: ")
        receiver.cash += payment
        self.cash -= payment
        status = receiver.name + " now has $" + str(receiver.cash) + "\n" + self.name + " now has $" + str(self.cash)
        print(status)
        return status
        

Player1 = Player(Player_1, player_dict[Player_1])
Player2 = Player(Player_2, player_dict[Player_2])
if len(player_dict) > 2:
    Player3 = Player(Player_3, player_dict[Player_3])
elif len(player_dict) > 3: 
    Player4 = Player(Player_4, player_dict[Player_4])
