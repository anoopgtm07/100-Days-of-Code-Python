# simple instagram follower and following model


class User:
    def __init__(self, id, username):  # takes id and username as attributes and initializes them to object
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):  # method to increase followers count
        user.followers += 1
        self.following += 1


user_1 = User('1', 'anup')
user_2 = User('2', 'gautam')

user_1.follow(user_2)  # case where user 1 follows user 2
print(f"{user_1.username} has {user_1.followers} followers.")
print(f"{user_1.username} has {user_1.following} following.")
print(f"{user_2.username} has {user_2.followers} followers")
print(f"{user_2.username} has {user_2.following} following.")
