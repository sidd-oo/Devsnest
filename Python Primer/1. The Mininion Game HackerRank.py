# hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    str_length = len(string)
    player1 = 0
    player2 = 0
    for i in range(str_length):
        if string[i] in "AEIOU":
            player1 += str_length - i
        else:
            player2 +=str_length - i

    if player1 < player2:
        print("Stuart %d" %player2)
    elif player1 > player2:
        print("Kevin %d" %player1)
    else:
        print("Draw")
            


if __name__ == '__main__':
    s = input()
    minion_game(s)