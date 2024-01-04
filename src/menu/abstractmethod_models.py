from abc import ABC, abstractmethod




class UserInterface(ABC):
    @abstractmethod
    def display(self):
        raise NotImplementedError()

    @abstractmethod
    def user_choice(self):
        raise NotImplementedError()

    def display_print(self, prompt):
        return print(prompt)

    def user_choice_input(self, prompt):
        return prompt