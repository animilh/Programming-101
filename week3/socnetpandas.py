import re
import json
import os
from pprint import pprint

class Panda:
    GENDERS = ['male','female']
    def __init__(self, name, email, gender):
        self.__name = str(name)

        if not re.search(r'[\w.-]+@[\w.-]+.\w+', email):
            raise ValueError("Invalid email")
        self.__email = email

        if gender not in self.GENDERS:
            raise ValueError ("The gener of panda is invalid")
        self.__gender = gender


    def __str__(self):
        return "Panda {}, email {}, gender {}".format(self.name(), self.email(), self.gender())


    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name() == other.name() and self.email() == other.email() and self.gender() == other.gender()


    def __hash__(self):
        return hash(self.__str__())

    def __iter__(self):
        return iter(self.__str__())

    def name(self):
        return self.__name

    def gender(self):
        return self.__gender

    def email(self):
        return self.__email


class PandaSocialNetwork:

    def __init__(self):
        self.network = {}

    def get_value(self, data):
        self.network = data

    def __getitem__(self, index):
        return self.network[index]

    def __iter__(self):
        return iter(self.network)

    def has_panda(self, panda):
        return panda in self.network

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise Exception("Panda already in network")
        self.network[panda] = []

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise Exception("{} and {} are already friends".format(panda1, panda2))

        self.network[panda1].append(panda2)
        self.network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return panda1 in self.network[panda2] and panda2 in self.network[panda1]

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False
        return self.network[panda]

    def connection_level(self, panda1, panda2):
        if not (self.has_panda(panda1) and self.has_panda(panda2)):
            return False

        queue = [[panda1]]
        visited = set()
        # current_panda = Panda('','current@abv.bg',"male")

        while len(queue) != 0:
            #Gets the first path in the queue
            path = queue.pop(0)
#            print (path)

            #Gets the last node in the path
            current_panda = path[-1]
#            print (current_panda)

            #Check if we have found panda2
#            if isinstance(current_panda, Panda):
            if current_panda == panda2:
                return len(path) - 1
            #Check if the node is already visited      if not (self.has_panda(panda1) and self.has_panda(panda2)):

            if current_panda not in visited:
                # enumerate all adjacent nodes, construct a new path and push it into the queue
                for neighbour in self.network.get(current_panda,[]):
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                #Mark the current node as visited
                visited.add(current_panda)

        if panda2 not in visited:
            return -1


    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) not in (-1, 'False')


    def how_many_gender_in_network(self, level, panda, gender):
        if level < 1:
            raise ValueError("The level must be at least 1")

        if gender not in Panda.GENDERS:
            raise ValueError("The gender must be male or female")

        start_level = 1
        count = 0
        while start_level <= level:
            count_fr = [1 for pandafr in self.find_friend(start_level, panda) if pandafr.gender() == gender]
            count += sum(count_fr)
            start_level += 1

        return count

    def find_friend(self, level, panda):
        if level < 1:
            raise ValueError("The level must be at least 1")

        return[pandak for pandak in self.network.keys() if self.connection_level(pandak, panda) == level]





def main():
    network = PandaSocialNetwork()
    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    rado = Panda("Rado", "rado@pandamail.com", "male")
    tony = Panda("Tony", "tony@pandamail.com", "female")
    deni = Panda("Deni", "deni@pandamail.com", "female")
    ani = Panda("Ani", "ani@pandamail.com", "female")
    emil = Panda("Emo", "emo@pandamail.com", "male")

    for panda in [ivo, rado, tony, deni, ani, emil]:
        network.add_panda(panda)

    network.make_friends(ivo, rado)
    network.make_friends(rado, tony)
    network.make_friends(tony, deni)
    network.make_friends(ani, deni)
    network.make_friends(emil, deni)
    network.make_friends(tony, ani)

    # for pandak in list(network.network.keys()):
    #     print pandak.name()

    print (network.find_friend(2,tony))
    print (network.how_many_gender_in_network(2, tony, 'male'))
    # print (network.are_connected(rado, ani))

    # with open('data.txt', 'r+') as outfile:
    #     json.dump(str(network.__dict__), outfile)

#   inputfile = open('data.txt','r')
    # data = []
    # with open('data.txt') as f:
    #     for line in f:
    #         data.append(json.loads(line))

    # network.get_value(data)




    # for k in network:
    #     print (k)

    # print(network.connection_level(ivo, rado))# == 1 # True
    # print(network.connection_level(ivo, tony))# == 2 # True
    # print(network.connection_level(ivo, deni))
    # print(network.connection_level(ivo, emil))
        #    network.how_many_gender_in_network(1, rado, "female") == 1 # True

if __name__ == '__main__':
    main()


    # deni = Panda("Deni", "deni@pandamail.com", "female")

