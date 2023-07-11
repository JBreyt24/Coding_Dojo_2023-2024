



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


    def enroll(self):

        if self.is_rewards_member:
            print("User already a member")
            return False

        self.is_rewards_member = True

        self.gold_card_points = 200


    def spend_points(self, amount):

        if self.gold_card_points < amount:
            print("You don't have enough points")
            return
        
        self.gold_card_points = self.gold_card_points - amount


user1 = User("John", "Browne", "browneuments@gmail.com", "33")
user1.enroll()
user1.spend_points(50)
user1.display_info()

user2 = User("Acle", "Kahney", "4Dstudios@gmail.com", "36")
user2.enroll()
user2.spend_points(80)
user2.display_info()

user3 = User("Olly", "Steele", "OliverSteele@gmail.com", "31")
user3.enroll()
user3.spend_points(210)
user3.display_info()