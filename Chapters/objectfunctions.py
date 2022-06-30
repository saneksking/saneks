class Parents:
    def __init__(self):
        self.a = 1
        print('Parents Object Created!')

    @staticmethod
    def say():
        print('Hello!')


class Child(Parents):
    def __init__(self):
        super().__init__()
        print('Child Object Created!')


parents = Parents()
child = Child()

print(isinstance(parents, Parents))
print(isinstance(child, Parents))
print(isinstance(parents, (Parents, int)))
print(isinstance(parents, Child))
issubclass(Child, Parents)
issubclass(Parents, Parents)
issubclass(Child, int)
issubclass(Child, (int, Parents))
'''try:
    print(isinstance(parents, MyClass))
except NameError:
    print('Not such class!')'''

