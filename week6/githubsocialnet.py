import requests
from directedgraph import DirectedGraph

class Request:
    URL = "https://api.github.com/users/{}"
    URL_FOLLOWERS = "https://api.github.com/users/{}/followers"
    URL_FOLLOWING = "https://api.github.com/users/{}/following"
    load = {'client_id': 'befa30e0ad417c6026e3', 'client_secret': \
        '41ca8e46d1b54ec8335e3cb13f019f80ab4fb0d3'}

    def __init__(self, url = ''):
        self.rqst = requests.get(url, params = Request.load)


    @staticmethod
    def get_request_for_user(username):
        return requests.get(Request.URL.format(username), \
            params=Request.load).json()

    @staticmethod
    def get_request_followers_user(username):
        follower_dict = requests.get(Request.URL_FOLLOWERS.format(username), \
            params=Request.load).json()
        return [str(user['login']).strip('u') for user in follower_dict]

    @staticmethod
    def get_request_following_user(username):
        following_dict = requests.get(Request.URL_FOLLOWING.format(username), \
            params=Request.load).json()
        return [str(user['login']).strip('u') for user in following_dict]


class GitHubSocialNetwork:
    HEAD = 'animilh'
    def __init__(self):
        self.network = DirectedGraph()

    def get_network_for(self, user):
        return {'following' : list(Request.get_request_following_user(user)), \
            'followers' : list(Request.get_request_followers_user(user))}

    def build_GitHub_social_network(self, username, level):
        if level > 4:
            raise Exception("Cannot build GitHubSocialNetwork for level > 4")
        if level <= 0:
            return
        next_cycle = set()

        mynet = self.get_network_for(username)
        for follower in mynet['followers']:
            self.network.add_edge(follower, username)
            next_cycle.add(follower)

        for following in mynet['following']:
            self.network.add_edge(username, following)
            next_cycle.add(following)

        while level > 0:
            level -= 1
            for user in next_cycle:
                self.build_GitHub_social_network(user, level)

        return self.network



    def do_you_follow(self, user):
        return user in self.network[GitHubSocialNetwork.HEAD]

    def do_you_follow_indirectly(self, user):
        return self.network.path_between(GitHubSocialNetwork.HEAD, user)

    def does_he_she_follows(self, user):
        return GitHubSocialNetwork.HEAD in self.network.get_neighbors_for(user)

    def does_he_she_follows_indirectly(self, user):
        return self.network.path_between(user, GitHubSocialNetwork.HEAD)

    def who_follows_you_back(self):
        result = []
        for follower in self.get_network_for(GitHubSocialNetwork.HEAD) \
            ['followers']:
            result.append(follower)
            for following in self.get_network_for(GitHubSocialNetwork.HEAD) \
                ['following']:
                if self.network.path_between(following, follower):
                    result.extend(self.network.get_path_between(following, \
                        follower))
        result_u = set(result)
        return result_u
