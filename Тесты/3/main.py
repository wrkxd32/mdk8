class Text_Greeting:
    def greeting(self, name):
        return f"Меня зовут {name}" if name else ""

    def empty_string(self, arg):
        return len(arg) > 0

    def register_check(self, arg):
        return arg.islower()

    def long_check(self, arg):
        return len(arg) < 10

    def string_type(self, arg):
        return isinstance(arg, str)