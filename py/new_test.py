class A(object):
    def __new__(cls):
        print("__New__", cls.__name__)

        return object.__new__(B, (object,), name='wang')
        #return super().__new__(B, (object,), name='wang')

    def __init(self):
        print("!!!!!!!!A init")


class B(object):
    name="yanwei"
    def __init__(self, name):
        print("!!!!!!!! B init ")
        print("This is B")
        self.name = name



c = A()
print(c.name)
