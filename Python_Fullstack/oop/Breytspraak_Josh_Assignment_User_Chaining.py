



class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("--------------------------------")
        print(f"First name:{self.first_name}")
        print(f"Last name:{self.last_name}")
        print(f"Email:{self.email}")
        print(f"Age:{self.age}")
        print(f"Member:{self.is_rewards_member}")
        print(f"Points:{self.gold_card_points}")
        print("--------------------------------")
        return self


    def enroll(self):

        if self.is_rewards_member:
            print("User already a member")
            return self

        self.is_rewards_member = True

        self.gold_card_points = 200

        return self

    def spend_points(self, amount):

        if self.gold_card_points < amount:
            print("You don't have enough points")
            return False
        
        self.gold_card_points = self.gold_card_points - amount


user1 = User("John", "Browne", "browneuments@gmail.com", "33").display_info()
user1.enroll().spend_points(50)

user2 = User("Acle", "Kahney", "4Dstudios@gmail.com", "36").display_info()
user2.enroll().spend_points(80)

user3 = User("Olly", "Steele", "OliverSteele@gmail.com", "31").display_info()
user3.enroll().spend_points(210)