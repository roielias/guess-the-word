import random
import json
players_list = []# a list with players names
my_point_counter = {}# a dictionary the will contant the score of users
user_input =int(input("how much players will play: "))# enter how much players will play

# read the words from the json file
with open('words.json', 'r') as file:# ask from loging system open the file in read mood
    data = json.load(file)# creat a verible with the data of file
    words_list = data['words']# take only the requires words from data

for i in range(user_input):# a loop that will get the players
    players_name = input("enter the player name: ")
    players_list.append(players_name)# insert the player to list
    my_point_counter[players_name] = 0# inited the values of dictionary
player_index = 0# the index of the players list, every iterete will add 1
current_player = players_list[player_index]# the name of the current player

length = len(words_list)-1
for i in range(length):# a loop that itarate on every words from list
    random_index =random.randint(0,len(words_list))
    cover_word = '_'*len(words_list[random_index])# the current word - covered
    discover_word = words_list[random_index]# the current word

    guess_list = []# a list that will contain all the guess that was, it will insure that the guess not will return  

    while discover_word != cover_word:# a loop that continue until all the word will discovered
        print(f"it is {current_player}'s turn")# print the name of the current player
        score = my_point_counter[current_player]# the amount of his scores
        print(f"your scores is:{score}")
        print (cover_word)# print the covered word for the player woll see what he need to guess
    
        # loop that ןinsure that the input is one new char, else will ask a new one
        while True:
            guess = input("enter one char: ").lower()# get the guess from th user
            if guess.isalpha() and len(guess) == 1 and guess not in guess_list:
               break
            print("Invalid input. Please enter a single new letter.")
     
        for i in range (len (discover_word)):# a loop that itarate on the word for check if the guess is true or false  

            if discover_word[i] == guess:
                cover_word = cover_word[:i] + guess +cover_word[i+1:]# updet the covered word to be with the guess char
            guess_list.append(guess)# full the guess list with the guess that was

            
        if guess in discover_word:# if the guess is correct
            for char in discover_word:# a loop that check how meny times the correct guess in the word
               if char == guess:
                  my_point_counter[current_player]+=1# add a point for the current player in dictionary


        else:
            print("guess wrong...")
            player_index += 1# change to the next player

        if player_index >= len(players_list):# insure that when we finish to play with every players we will return from the beginning on everyone 
            player_index = player_index % len(players_list)
        current_player = players_list[player_index]# updet the current player into loop fo it will change

    words_list.remove(words_list[random_index])# remove the word that guessed for insure that it no will return
    print(f"well done {discover_word} guessed")

    print(my_point_counter)
the_winner = max(my_point_counter, key=my_point_counter.get)# checking who is the winner - who that has the max points
max_value = my_point_counter[the_winner]
print("the winner is: ", the_winner)
print("his scores amount is :", max_value)
        




