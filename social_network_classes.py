# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
from json import JSONEncoder 
from collections import namedtuple

def customDecoder(Dict):
    return namedtuple('X', Dict.keys())(*Dict.values())



class SocialNetwork:
    def __init__(self):
        self.list_of_messages = []
        self.list_of_people = []
        self.index_list_of_people = 0
        self.index_list_of_messages = 0
        self.current_user = Person(0, 0, 0)

    def add_current_user(self, current_user):
        self.current_user = current_user
        pass

    def  create_account(self):
        name = input("insert name for new user: ")
        age = input("insert age for new user: ")
        password = input("insert password for the new user: ")
        self.list_of_people.insert(self.index_list_of_people, Person(name, age, password))
        self.index_list_of_people += 1

        #implement function that creates account here
        print("Creating ...")
        pass

    def send_message(self, texter):
        
        pass


class Person:
    def __init__(self, name, age, password):
        self.name = name
        self.year = age
        self.friendlist_index = 0
        self.friendlist = [] #string just saves the name  of the friend
        self.inbox_messages_index = 0
        self.inbox_messages = [] #string just saves the texter, and then visualise the messages from this texter
        self.password = password

    def change_name(self):
        new_name = input("New name: ")
        self.name = new_name
        pass

    def change_age(self):
        new_age = input("New age: ")
        self.age = new_age
        pass

    def add_friend(self, name_friend_to_add):
        self.friendlist.insert(self.friendlist_index, name_friend_to_add) 
        self.friendlist_index += 1  
        #implement adding friend. Hint add to self.friendlist
        pass

    def write_message(self): #this is all right
        print("\n Send message to: ")
        for i in range(0, self.friendlist_index): #showing all the frinds
            print("\n", i, ". ", self.friendlist[i])
        
        receiver_index = input("insert the number for the person you want to text: ") #deciding who to write the message to
        receiver_index = int(receiver_index)

        text = input("write the message text: ") #wirting the message
        message = Message (text, self.friendlist[receiver_index], self) #creating a message object

        return message #returning the message object
        pass

    def receive_message(self, social_network):
        print("Inbox messages: ")
        for i in range(0, social_network.index_list_of_messages): #check all the messages
            if(social_network.list_of_messages[i].receiver == self ): #only checks the one whose whose reiver is 
                print("New Message from ", social_network.list_of_messages[i].texter) #print the name of the texter
                
                self.inbox_messages.insert(self.messages_index, social_network.list_of_messages[i].texter)  #add the message texter to the list of messages 
                self.messages_index += 1


        #check for all messages in the system and visualise the ones whose receiver is self
        pass

class Message:
    def __init__(self, text, receiver, texter):
        self.text = text
        self.receiver = receiver #just saves the name
        self.texter = texter #just save sthe name, not an object otherwise there are proboem with json data reading

