__author__ = 'Srinivasan'


class P:
    def __init__(self, notes_list):
        if not isinstance(notes_list,(list,)):
            raise TypeError('Pattern constructor requires a list')

        self.list = notes_list
        self.current_state = self.list

    def get(self):
        return self.current_state

    def reset(self):
        self.current_state = self.list

    def palindrome(self):
        self.reset()
        reverse = self.list[::-1]
        self.current_state = self.current_state + reverse
        return self

    def loop(self, iterations):
        self.current_state *= 3
        return self

    def converge(self):
        out = self.current_state[:]

        for i in range(0, len(self.current_state)):
            out += self.current_state[:-i]

        self.current_state = out[:]
        return self

