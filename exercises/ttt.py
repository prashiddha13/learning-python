import itertools

box = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

t = itertools.cycle(('O', 'X'))

def print_board():

    print()
    print(f" {box[0]}  |  {box[1]}  |  {box[2]} ")
    print("----+-----+----")
    print(f" {box[3]}  |  {box[4]}  |  {box[5]} ")
    print("----+-----+----")
    print(f" {box[6]}  |  {box[7]}  |  {box[8]} ")
    print()

def verify():

    if ((box[0] == box[1] == box[2]) and box[0] != ' ') or ((box[3] == box[4] == box[5]) and box[3] != ' ') or ((box[6] == box[7] == box[8]) and box[6] != ' ') or ((box[0] == box[3] == box[6]) and box[0] != ' ') or ((box[1] == box[4] == box[7]) and box[1] != ' ') or ((box[2] == box[5] == box[8]) and box[2] != ' ') or ((box[0] == box[4] == box[8]) and box[0] != ' ') or ((box[2] == box[4] == box[6]) and box[2] != ' '):
        return("over")
    elif ((box[0] != ' ') and (box[1] != ' ') and (box[2] != ' ') and (box[3] != ' ') and (box[4] != ' ') and (box[5] != ' ') and (box[6] != ' ') and (box[7] != ' ') and (box[8] != ' ')):
        return("tie")
    else:
        pass

def main():

    running = True

    while running:
        print_board()
        print("(1-9)")

        turn = next(t) #Method to use .cycle() in itertools, that cycles through the options, which in this case are only two, and thus, causes alternation. 

        if turn == 'O':
            O = True
            X = False
        elif turn == 'X':
            X = True
            O = False

        while O:
            try:
                playerO = int(input("Player O: "))
            except (ValueError, UnboundLocalError):
                print("Please enter numbers between 1 and 9 to register your input. ")
                continue

            try:
                if box[playerO - 1] == ' ':
                    box[playerO - 1] = 'O'
                else:
                    print("Box is occupied.")
                    continue

                if not box[playerO - 1] == ' ':     
                    break
            except IndexError:
                print("Please enter numbers between 1 and 9 to register your input. ")

        while X:
            try:
                playerX = int(input("Player X: "))
            except (ValueError, UnboundLocalError):
                print("Please enter numbers between 1 and 9 to register your input. ")
                continue

            try:
                if box[playerX - 1] == ' ':
                    box[playerX - 1] = 'X'
                else:
                    print("Box is occupied.")
                    continue
                    
                if not box[playerX - 1] == ' ':               
                    break
            except IndexError:
                print("Please enter numbers between 1 and 9 to register your input. ")
        
        verification = verify()

        if verification == "over" or verification == "tie":
            running = False
            print_board()
        else:
            pass
            

    if O and verification != "tie":
        print("Player O Wins!")
    elif X and verification != "tie":
        print("Player X Wins!")
    elif verification == "tie":
        print("It's a draw. ")
        
if __name__ == "__main__":
    main()