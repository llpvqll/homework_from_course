class Parent:
    def parent_method(self):
        print("First parent class")


class Parent2:
    def parent_method2(self):
        print("Second parent class")


class Parent3:
    def parent_method3(self):
        print("Third parent class")


class Child(Parent2, Parent, Parent3):
    def child_method(self):
        print("The child method")


child = Child()
child.parent_method()
child.parent_method2()
child.parent_method3()
