import time
from colorama import init, Fore, Style

init(autoreset=True)


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.next = None
        self.previous = None


class Squad:
    def __init__(self):
        self.captain = None

    def recruit_captain(self, player_id):
        new_player = Player(player_id)

        if self.captain is None:
            self.captain = new_player
        else:
            new_player.next = self.captain
            self.captain.previous = new_player
            self.captain = new_player

    def recruit_player(self, player_id):
        new_player = Player(player_id)

        if self.captain is None:
            self.captain = new_player
        else:
            current_player = self.captain

            while current_player.next:
                current_player = current_player.next

            current_player.next = new_player
            new_player.previous = current_player

    def recruit_at_slot(self, player_id, slot):
        if slot == 0:
            self.recruit_captain(player_id)
            return

        new_player = Player(player_id)
        current_player = self.captain

        for _ in range(slot):
            if current_player is None:
                raise IndexError("Invalid squad slot.")
            current_player = current_player.next

        if current_player is None:
            raise IndexError("Invalid squad slot.")

        new_player.next = current_player
        new_player.previous = current_player.previous

        if current_player.previous:
            current_player.previous.next = new_player

        current_player.previous = new_player

    def remove_captain(self):
        if self.captain is None:
            return

        if self.captain.next is None:
            self.captain = None
        else:
            self.captain = self.captain.next
            self.captain.previous = None

    def remove_last_player(self):
        if self.captain is None:
            return

        if self.captain.next is None:
            self.captain = None
        else:
            current_player = self.captain

            while current_player.next:
                current_player = current_player.next

            current_player.previous.next = None

    def remove_player_at_slot(self, slot):
        if self.captain is None:
            return

        current_player = self.captain

        for _ in range(slot):
            if current_player is None:
                raise IndexError("Invalid squad slot.")
            current_player = current_player.next

        if current_player is None:
            raise IndexError("Invalid squad slot.")

        if current_player.previous:
            current_player.previous.next = current_player.next

        if current_player.next:
            current_player.next.previous = current_player.previous

    def show_squad(self):
        current_player = self.captain

        if current_player is None:
            print(Fore.RED + "No players in the BGMI squad.")
            return

        print(Fore.GREEN + "\nCurrent BGMI Squad:")

        while current_player:
            print(f"[Player {current_player.player_id}] <--> ", end="")
            current_player = current_player.next

        print("Lobby")

    def search_player(self, player_id):
        current_player = self.captain

        while current_player:
            if current_player.player_id == player_id:
                return True
            current_player = current_player.next

        return False

    def squad_size(self):
        current_player = self.captain
        total_players = 0

        while current_player:
            total_players += 1
            current_player = current_player.next

        return total_players


def show_menu():
    print("\n" + Style.BRIGHT + Fore.YELLOW + "===== BGMI Doubly Squad Manager =====")
    print("1. Recruit Captain")
    print("2. Recruit Player")
    print("3. Recruit Player at Slot")
    print("4. Remove Captain")
    print("5. Remove Last Player")
    print("6. Remove Player at Slot")
    print("7. Show Squad")
    print("8. Search Player")
    print("9. Squad Size")
    print("10. Exit Match")

def main():
    bgmi_squad = Squad()

    print(Fore.CYAN + Style.BRIGHT)
    print("=" * 50)
    print("          Shreyash Kadam S091")
    print("      BGMI Doubly Squad Manager")
    print("=" * 50)

    while True:
        show_menu()

        try:
            option = int(input(Style.RESET_ALL + "\nEnter your choice: "))

            if option == 1:
                player_id = int(input("Enter Player ID: "))
                bgmi_squad.recruit_captain(player_id)
                print(Fore.GREEN + "Player became the Captain!")

            elif option == 2:
                player_id = int(input("Enter Player ID: "))
                bgmi_squad.recruit_player(player_id)
                print(Fore.GREEN + "Player joined the squad!")

            elif option == 3:
                player_id = int(input("Enter Player ID: "))
                slot = int(input("Enter squad slot: "))
                bgmi_squad.recruit_at_slot(player_id, slot)
                print(Fore.GREEN + f"Player joined at squad slot {slot}!")

            elif option == 4:
                bgmi_squad.remove_captain()
                print(Fore.RED + "Captain has left the squad!")

            elif option == 5:
                bgmi_squad.remove_last_player()
                print(Fore.RED + "Last player removed from the squad!")

            elif option == 6:
                slot = int(input("Enter squad slot to remove: "))
                bgmi_squad.remove_player_at_slot(slot)
                print(Fore.RED + f"Player removed from squad slot {slot}!")

            elif option == 7:
                bgmi_squad.show_squad()

            elif option == 8:
                player_id = int(input("Enter Player ID to search: "))

                if bgmi_squad.search_player(player_id):
                    print(Fore.GREEN + "Player found in the squad!")
                else:
                    print(Fore.RED + "Player not found.")

            elif option == 9:
                print(Fore.BLUE + f"Total Players in Squad: {bgmi_squad.squad_size()}")

            elif option == 10:
                print(Fore.CYAN + "\nReturning to Lobby...")
                print(Fore.GREEN + "Match Finished! GG")
                break

            else:
                print(Fore.YELLOW + "Invalid option. Please try again.")

        except ValueError:
            print(Fore.YELLOW + "Please enter numbers only.")

        except IndexError as error:
            print(Fore.RED + f"Error: {error}")

        except Exception as error:
            print(Fore.RED + f"Error: {error}")

        time.sleep(1)


if __name__ == "__main__":
    main()
