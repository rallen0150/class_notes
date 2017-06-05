from random import choice

ans = ['ROCK', 'PAPER', 'SCISSORS']
response = input("Do you choose ROCK, PAPER, or SCISSORS:\n>").upper()
while response != 'QUIT':
    com_choice = choice(ans)
    if response == 'ROCK':
        if com_choice == 'PAPER':
            print("{} beats {}. Computer Wins!!!\n".format(com_choice, response))
        elif com_choice == 'SCISSORS':
            print("{} beats {}. You Win!!!!\n".format(response, com_choice))
        else:
            print("Tie Game, both picked {}. Choose Again!\n".format(response))
    elif response == 'PAPER':
        if com_choice == 'SCISSORS':
            print("{} beats {}. Computer Wins!!!\n".format(com_choice, response))
        elif com_choice == 'ROCK':
            print("{} beats {}. You Win!!!!\n".format(response, com_choice))
        else:
            print("Tie Game, both picked {}. Choose Again!\n".format(response))
    elif response == 'SCISSORS':
        if com_choice == 'ROCK':
            print("{} beats {}. Computer Wins!!!\n".format(com_choice, response))
        elif com_choice == 'PAPER':
            print("{} beats {}. You Win!!!!\n".format(response, com_choice))
        else:
            print("Tie Game, both picked {}. Choose Again!\n".format(response))
    elif response == 'QUIT':
        break
    else:
        print("Invalid Option!!\n")
    response = input("Pick agian, or type 'quit' to end the game:\n>").upper()
print("Thank you for playing Rock, Paper, Scissors!")
