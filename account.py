class Account:
    def __init__(self, name: str) -> None:
        '''
        The init function is responsible for creating an instance of the Account class with a name and account balance
        :param name: Takes in a string and assigns it to a private variable
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        Deposit is responsible for adding to the account balance, but only positive values are accepted
        :param amount: This variable holds how much is being deposited into the balance
        :return: What is returned is a boolean value that if True the amount deposited is successful, if False it was unsuccessful
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        '''
        Withdraw is responsible for taking out an amount from the balance. It can only take out a amount greater than zero and less than the blance
        :param amount: The amount that you would like to withdraw from the balance
        :return: A boolean value of True or False is returned depending if it was successful or not
        '''
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        '''
        Gets the current amount of the balance
        :return: The amount within the balance is returned
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Gets the name that was given to it
        :return: The name that it was given is returned
        '''
        return self.__account_name
