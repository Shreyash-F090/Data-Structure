import time
from colorama import init, Fore, Style

init(autoreset=True)


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.next = None


class Squad:
    def __init__(self):
        self.captain = None

    def recruit_captain(self, player_id):
        new_player = Player(player_id)
        new_player.next = self.captain
        self.captain = new_player

    def recruit_player(self, player_id):
        new_player = Player(player_id)

        if self.captain is None:
            self.captain = new_player
            return

        last_player = self.captain
        while last_player.next:
            last_player = last_player.next

        last_player.next = new_player

    def recruit_at_slot(self, player_id, slot):
        new_player = Player(player_id)

        if slot == 0:
            new_player.next = self.captain
            self.captain = new_player
            return

        current_player = self.captain

        for _ in range(slot - 1):
            if current_player is None:
                raise IndexError("Invalid squad slot.")
            current_player = current_player.next

        new_player.next = current_player.next
        current_player.next = new_player

    def remove_by_id(self, target_player):
        current_player = self.captain

        if current_player is not None:
            if current_player.player_id == target_player:
                self.captain = current_player.next
                current_player = None
                return

        while current_player is not None:
            if current_player.player_id == target_player:
                break

            previous_player = current_player
            current_player = current_player.next

        if current_player is None:
            return

        previous_player.next = current_player.next
        current_player = None

    def remove_by_slot(self, slot):
        if self.captain is None:
            return

        current_player = self.captain

        if slot == 0:
            self.captain = current_player.next
            current_player = None
            return

        for _ in range(slot - 1):
            current_player = current_player.next

            if current_player is None or current_player.next is None:
                raise IndexError("Invalid squad slot.")

        next_player = current_player.next.next
        current_player.next = None
        current_player.next = next_player

    def show_squad(self):
        current_player = self.captain

        if current_player is None:
            print(Fore.RED + "No players in the BGMI squad.")
            return

        print(Fore.GREEN + "\nCurrent BGMI Squad:")

        while current_player:
            print(f"[Player {current_player.player_id}] --> ", end="")
            current_player = current_player.next

        print("Lobby")


def show_menu():
    print("\n" + Style.BRIGHT + Fore.YELLOW + "===== BGMI Squad Manager =====")
    print("1. Recruit Captain")
    print("2. Recruit Player")
    print("3. Recruit Player at Slot")
    print("4. Remove Player by ID")
    print("5. Remove Player by Slot")
    print("6. Show Squad")
    print("7. Exit Match")

def main():
    bgmi_squad = Squad()

    print(Fore.CYAN + Style.BRIGHT)
    print("=" * 45)
    print("        Shreyash Kadam S091")
    print("        BGMI Squad Manager")
    print("=" * 45)

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
                target_player = int(input("Enter Player ID to remove: "))
                bgmi_squad.remove_by_id(target_player)
                print(Fore.RED + "Player has left the squad!")

            elif option == 5:
                slot = int(input("Enter squad slot to remove: "))
                bgmi_squad.remove_by_slot(slot)
                print(Fore.RED + f"Player removed from squad slot {slot}!")

            elif option == 6:
                bgmi_squad.show_squad()

            elif option == 7:
                print(Fore.CYAN + "\nReturning to Lobby...")
                print(Fore.GREEN + "Match Finished! GG")
                break

            else:
                print(Fore.YELLOW + "Invalid option. Try again.")

        except ValueError:
            print(Fore.YELLOW + "Please enter numbers only.")

        except IndexError as error:
            print(Fore.RED + f"Error: {error}")

        except Exception as error:
            print(Fore.RED + f"Error: {error}")

        time.sleep(1)


if __name__ == "__main__":
    main()
