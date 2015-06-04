from githubsocialnet import GitHubSocialNetwork

myusername = input("Enter your GitHub username : ")
username = input("Enter GitHub username of a person you are searching for : ")
level = int(input("Enter the level of the graph : "))
net = GitHubSocialNetwork()
net.build_GitHub_social_network(myusername, level)
print("Your network for level {}".format(level))
print(net.get_network_for(myusername))
print("Do you follow user with username {}?".format(username))
if net.do_you_follow(username):
    print("Yes")
else:
    print("No")

print("Does someone with username {} follows you?".format(username))
if net.does_he_she_follows(username):
    print("Yes")
else:
    print("No")

print("How many people from your followers follows you back?")
print(net.who_follows_you_back())

