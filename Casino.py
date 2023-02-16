from random import randint


class Casino:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.balance = 1_500_000_000

    def show_info(self):
        print(self.name, "has", len(self.customers), "customers, and the balance is", self.balance, "USD")

    def check_customer(self, customer, fee):
        if customer.balance < fee:
            # print("Not enough money!")
            return False

        self.get_money(customer, fee)

        return True

    def get_money(self, customer, fee):
        customer.balance -= fee
        self.balance += fee

    def give_money(self, customer, amount):
        self.balance -= amount
        customer.balance += amount

    def slots(self, customer):
        allowed = self.check_customer(customer, 5)

        if not allowed:
            return

        if randint(0, 4) == 0:
            #print("You won 3x times the money you put in")
            self.give_money(customer, 15)
        else:
            #print("You lost!")
            pass

    def cups(self, customer):
        allowed = self.check_customer(customer, 10)

        if not allowed:
            return

        if randint(0, 2) == 0:
            #print("You won 2x times the money you put in")
            self.give_money(customer, 20)
        else:
            #print("You lost!")
            pass

    def plinko(self, customer):
        allowed = self.check_customer(customer, 20)

        if not allowed:
            return

        index = 0

        for _ in range(0, 16):
            if randint(0, 1):
                index += 1
            else:
                index -= 1

        index = abs(index)

        multipliers = [0.1, 0.2, 0.3, 0.5, 0.75, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        self.give_money(customer, 20 * multipliers[index])

    def saper(self, customer):
        allowed = self.check_customer(customer, 50)

        if not allowed:
            return

        bombs = [0, 1, 2]

        dead = False

        for _ in range(0, 15):
            if randint(0, 24) in bombs:
                dead = True
                break

        if not dead:
            self.give_money(customer, 250)


class Customer:
    def __init__(self, name: str, second_name: str, balance: int):
        self.name = name
        self.secondName = second_name
        self.balance = balance
        self.first_balance = balance

    def show_info(self):
        print(self.name, self.secondName, "went from", self.first_balance, "to", self.balance)


# Constants
AMOUNT_OF_CLIENTS = 1000
AMOUNT_OF_SLOTS_SIMULATIONS = 1000
AMOUNT_OF_CUPS_SIMULATIONS = 1000
AMOUNT_OF_PLINKO_SIMULATIONS = 1000
AMOUNT_OF_SAPER_SIMULATIONS = 1000

casino = Casino("Golden grin")

# Client generator
names = ["John", "Max", "Caroline", "Andrew", "Donald"]
second_names = ["Bon Jovi", "Kolonko", "Kozub", "Tate", "Trump"]

for _ in range(1, AMOUNT_OF_CLIENTS):
    name = names[randint(0, 4)]
    second_name = second_names[randint(0, 4)]
    balance = randint(50, 1000)

    client = Customer(name, second_name, balance)

    casino.customers.append(client)

# Casino simulation
for _ in range(0, AMOUNT_OF_SLOTS_SIMULATIONS):
    casino.slots(casino.customers[randint(0, len(casino.customers) - 1)])

for _ in range(0, AMOUNT_OF_CUPS_SIMULATIONS):
    casino.cups(casino.customers[randint(0, len(casino.customers) - 1)])

for _ in range(0, AMOUNT_OF_PLINKO_SIMULATIONS):
    casino.plinko(casino.customers[randint(0, len(casino.customers) - 1)])

for _ in range(0, AMOUNT_OF_SAPER_SIMULATIONS):
    casino.saper(casino.customers[randint(0, len(casino.customers) - 1)])

for client in casino.customers:
    client.show_info()

casino.show_info()
