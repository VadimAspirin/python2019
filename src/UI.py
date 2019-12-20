class InputForm:
    def __init__(self, message, empty_string=False):
        self.message = message
        self.empty_string = empty_string
        self.items = []

    def addItem(self, mess):
        self.items.append(mess)

    def generate(self):
        out_params = []
        print(f"\n{self.message}")
        for i in self.items:
            out = input(f"{i} > ")
            if not out and not self.empty_string:
                raise ValueError("input error")
            out_params.append(out)
        return out_params


class Menu:
    def __init__(self, message):
        self.message = message
        self.items = []

    def addItem(self, mess, func):
        self.items.append({"mess": mess, 
                           "func": func})

    def _exit(self):
        return 0

    def exitItem(self, mess):
        self.addItem(mess, self._exit)

    def print(self):
        print(f"\n{self.message}")
        for i in range(len(self.items)):
            print(f"{i}. {self.items[i]['mess']}")

    def selectItem(self, num_item):
        func = self.items[num_item]['func']
        return func()

    def generate(self):
         while True:
            self.print()
            try:
                option_num = int(input("> "))
                out = self.selectItem(option_num)
                if out == 0:
                    break
            except Exception as e:
                print(f"\nWarning: try again: {str(e)}")