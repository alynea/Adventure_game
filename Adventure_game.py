
import time
import random
# global variables
cash_prices = [1, 1000, 2500, 5000, 10000,
               50000, 100000, 250000, 500000, 1000000]
selected_suitcaseCash = 0
opened_suitcases = {}
suitcases = {}


def set_suitcase_cashprices():

    global suitcases
    global cash_prices
    suitcases = dict(enumerate(random.sample(cash_prices, 10), 1))


def intro():

    print_pause("\nWelcome to Deal or No Deal\n", 2)
    print_pause("\nToday you have the opportunity to walk"
                "away with a huge cash price", 2)
    print_pause("Inorder to do that you have to be lucky, "
                "gutsy and have a great sense of timing.\n", 2)
    print_pause("\nExcited! Then lets get started!\n", 2)
    print_pause("\nInfront of you are 10 suitcases. "
                "We dont know what is in each of these 10 cases", 2)
    print_pause("We do know that there is a huge cash price of $1 million "
                "in one of these cases.\n", 2)
    print_pause("\nEach case holds a different amount - anywhere between "
                "$1 million to $1.\n", 2)


def print_pause(message_to_print, sec):

    print(message_to_print)
    time.sleep(sec)


def get_userSelection(numberOfSuitcases):

    user_selectionList = []
    global suitcases
    numberOfSuitcases = int(numberOfSuitcases)
    for x in range(numberOfSuitcases):
        while True:
            user_SelectionString = input("\nSelect suitcase = ")
            if (user_SelectionString.isdigit()):
                print(user_SelectionString)
                suitcaseNum = int(user_SelectionString)
                if suitcaseNum in suitcases.keys():
                    user_selectionList.append(suitcaseNum)
                    break
                else:
                    print("\nOops! That suitcase does not exist.")
            else:
                print("\nMust enter a valid number.")
    return user_selectionList


def eliminate(numberOfSuitcases):
    display_suitcases()
    global opened_suitcases
    user_selectionList = get_userSelection(numberOfSuitcases)
    current_round_suitcases = {}
    for i in user_selectionList:
        indexNum = int(i)
        opened_suitcases[indexNum] = suitcases.pop(indexNum, None)
        current_round_suitcases[indexNum] = opened_suitcases.get(indexNum)

    print_pause("\nHere is the cash value of the suitcases you picked.\n ", 2)
    cashValue_display = ""
    for item in current_round_suitcases.keys():
        cashValue_display = "[" + str(item) + "] " + "=" + "$" \
                            + str(current_round_suitcases.get(item))
        print(cashValue_display)


def display_suitcases():
    print_pause("\nHere are your suitcases\n", 2)
    global suitcases
    display = ""
    for item in suitcases.keys():
        display = display + "[" + str(item) + "] "
    print(display)


def display_cashValue():

    global suitcases
    cashValue_display = ""
    for item in suitcases.keys():
        cashValue_display = "[" + str(item) + "] " + \
                            "=" + "$" + str(suitcases.get(item))
        print(cashValue_display)


def get_offer():

    global suitcases
    suitcases_value = suitcases.values()
    suitcase_average = int(sum(suitcases_value)/len(suitcases_value))
    offer = int(suitcase_average * (1/len(suitcases_value) + 1))
    if offer >= 1000000:
        offer = 850000
    print("\nThe Bank's offer = $" + str(offer) + "\n")
    return offer


def offer_deal():

    global opened_suitcases
    isContinue = True
    print_pause("\nGreat choices. The Bank just called"
                "and they want to make an offer.", 2)
    offer = get_offer()
    print_pause("\nThats a generous offer from the bank!\n"
                "Here are your options-\n"
                "\nDeal: Take the Bank's deal and "
                "go home with $" + str(offer) + "\n"
                "No Deal: Move to next round and pick suitcases\n", 2)

    while True:
        players_response = input("\nDeal or No Deal?\n").lower()
        if "no deal" in players_response:
            isContinue = True
            break
        elif "deal" in players_response:
            isContinue = False
            print_pause("Congratualtions! You go home with \n" + str(offer), 2)
            break
        else:
            print_pause("\nI don't understand. Deal or No Deal\n", 2)
    return isContinue


def get_userSuitcase():

    global suitcases
    global selected_suitcaseCash

    while True:
        display_suitcases()
        suitcaseNum = input("\nPick a case, which you think might contain"
                            " the $1 million.This will be your suitcase."
                            "(Enter a number 1-10)\n")
        if (suitcaseNum.isdigit()):
            if int(suitcaseNum) in suitcases.keys():
                selected_suitcaseCash = suitcases.pop(int(suitcaseNum), None)
                break
            else:
                print_pause("\nEnter a number 1-10.\n", 2)
        else:
            print_pause("Must enter a number. Try again!\n", 2)
    print_pause("\nExcellent! We are ready for your first Deal\n", 2)


def final_round():

    print_pause("\nYou are down to two suitcases!\n", 2)
    print_pause("There are no more offers. You have two choices-\n", 1)
    print_pause("\nStick with your suitcase.\n"
                "\nTrade it in with the last one. \n", 2)
    while True:
        user_choice = input("\nWould you like to open "
                            "your suitcase? Enter yes or no.\n")
        if "yes" in user_choice:
            print_pause("\nCongratualtions! You go home"
                        " with $" + str(selected_suitcaseCash), 2)
            break
        elif "no" in user_choice:
            print_pause("\nCongratualtions! You go home with \n", 2)
            display_cashValue()
            break
        else:
            print_pause("\nI don't understand. Enter yes or no.\n", 2)


def play_game():

    set_suitcase_cashprices()
    get_userSuitcase()
    isContinue: True
    for s in range(2):
        eliminate(3)
        isContinue = offer_deal()
        if isContinue is False:
            break
    if isContinue is False:
        return

    for s in range(2):
        eliminate(1)
        isContinue = offer_deal()
        if isContinue is False:
            break
    if isContinue is True:
        final_round()


def end_game():

    print_pause("\nThanks for playing Deal or No Deal\n", 2)
    play_again()


def play_again():

    while True:
        player_response = input("Would you like to play again?"
                                "Enter yes or no\n").lower()
        if "yes" in player_response:
            start_game()
        elif "no" in player_response:
            print_pause("Goodbye!", 2)
            break
        else:
            print_pause("\nI don't understand. Enter yes or no\n", 2)


def start_game():
    intro()
    while True:
        start = input("\nAre you ready to play? Y/N\n")

        if start == "y":
            player = input("\nEnter your name?\n").lower()
            print_pause("\nHello " + player + ", let's play!!\n", 2)
            play_game()
            end_game()
            break
        elif start == "n":
            print_pause("\nOk, Goodbye!\n", 2)
            break
        else:
            print_pause("\nI don't understand.\n", 2)


start_game()
