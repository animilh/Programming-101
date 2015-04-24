from githubsocialnet import GitHubSocialNetwork

username = input("Enter a username : ")
myusername = 'animilh'
net = GitHubSocialNetwork()
net.build_GitHub_social_network(myusername, 2)
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

