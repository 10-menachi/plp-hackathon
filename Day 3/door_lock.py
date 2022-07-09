from datetime import datetime
from getpass import getpass


class DoorLock:
    """
Door lock implementation instantiating the class\n
`lock = DoorLock("1234") ` or `lock = DoorLock` the password is optional
so \nif you wish to change the password you can do so using the instance\n 
method setter i.e `lock.password="password"`
    """

    def __init__(self, password="1234") -> None:
        # self._password= ''
        self._commands: dict = {"open": "open", "quit": "quit",
                                "close": "close", "help": ["help", "--help", "-h"]}
        self._password: str = password
        self._is_authenticated: bool = False
        self._is_locked: bool = False
        self._running: bool = True

    @property
    def commands(self) -> dict:
        return self._commands

    @property
    def running(self) -> bool:
        return self._running

    @running.setter
    def running(self, value: bool) -> None:
        """ Indicate app running state"""
        self._running = value

    @property
    def locked(self) -> bool:
        """Return door lock state"""
        return self._is_locked

    @locked.setter
    def locked(self, value: bool) -> None:
        """ Setter for app lock state"""
        self._is_locked = value

    @property
    def password(self) -> str:
        """Get door lock password"""
        return self._password

    @property
    def authenticated(self) -> bool:
        """Return status if a user is granted access to the system"""
        return self._is_authenticated

    @authenticated.setter
    def authenticated(self, value: bool) -> None:
        """Change door access status"""
        self._is_authenticated = value

    @password.setter
    def password(self, value: str) -> None:
        self._password = value

    def unlock_door(self):
        """Unlock locked door"""
        self.locked = False

    def lock_door(self):
        """Lock unlocked door"""
        self.locked = True

    @staticmethod
    def help():
        h = """
For help commands use:
close - Close door
open - Open door
quit - Terminate program
        """
        print(h)

    @staticmethod
    def print_date() -> None:
        """print current """
        return datetime.now()

    def main(self):
        """
Main function that executes the logic for opening the door and closing the door
This runs on an endless loop to execute user commands and produce the required output

        """
        print(""" Welcome to automated door locking system """.center(80, "*"))
        while self.running:
            while not self.authenticated:
                password = getpass("Enter your password to continue: ")
                if not password == self.password:
                    print("Invalid password please try again..")
                    continue
                else:
                    self.authenticated = True
            commands = self.commands.values()
            msg = "[enter command]> "
            user_command = input(msg).lower().strip()
            if user_command in self.commands['help']:
                self.__class__.help()

            elif(user_command not in commands):
                print("Invalid input. use for -h or --help or help")

            elif user_command == self._commands['quit']:
                print(f"Door Last open at {self.__class__.print_date()}")
                self.running = False

            elif user_command == self.commands['open']:
                if not self.locked:
                    print("the door is already open".title())

                else:
                    self.unlock_door()
                    print("The door is now open")
            elif user_command == self.commands['close']:
                if self.locked:
                    print("Door is already locked")
                else:
                    self.lock_door()
                    print("The door is now locked")

    @staticmethod
    def run():
        door_lock = DoorLock("12345")
        door_lock.main()


if __name__ == "__main__":
    DoorLock.run()