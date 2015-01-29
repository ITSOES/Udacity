# from Movietrailersite import media2
# mobj = media2.Movie
# print(mobj.__name__, mobj.__module__)

class Family:
    class Parent():
        template = 'signasdfASDFASDFup.html'
        def __init__(self, last_name, eye_color):
            print('Parent Constructor Called')
            self.last_name = last_name
            self.eye_color = eye_color

        def show_info(self):
            print('Last Name - ' + self.last_name)
            print('Eye Color - '+self.eye_color)

    class Child(Parent):
        def __init__(selef, last_name, eye_color, number_of_toys):
            print('Child Constructor Called')
            # Parent.__init__(selef, last_name, eye_color)
            super(Family.Child, selef).__init__(last_name, eye_color)
            selef.number_of_toys = number_of_toys

        def show_info(self):
            print('Last Name - ' + self.last_name)
            print('Eye Color - '+self.eye_color)
            print('Number of toys - '+str(self.number_of_toys))


class Parent:
    template = 'signup.html'
    print('Parent class defined')
    def __init__(self, last_name, eye_color):
        print('Parent Constructor Called')
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print('Last Name - ' + self.last_name)
        print('Eye Color - '+self.eye_color)

class Child(Parent):
    Parent.template = 'Happy'
    template = 'fun'

    def __init__(selef, last_name, eye_color, number_of_toys):
        print('Child Constructor Called')
        # Parent.__init__(selef, last_name, eye_color)
        super(Child, selef).__init__(last_name, eye_color)
        selef.number_of_toys = number_of_toys

    def show_info(self):
        print('Last Name - ' + self.last_name)
        print('Eye Color - '+self.eye_color)
        print('Number of toys - '+str(self.number_of_toys))

the_cyruses = Family
print(Family.Child)





billy_cyrus = Family.Parent('Cyrus', 'blue')
print('Billy Cyrus - ', billy_cyrus.last_name)
print()

miley_cyrus = Family.Child('Cyrus', 'Blue', 5)
print()
print('Miley Cyrus\'s last name is ', miley_cyrus.last_name)
print('Miley Cyrus\'s number of toys is ', miley_cyrus.number_of_toys)
# miley_cyrus = Child
print('Miley Cyrus\'s __name__ is ', miley_cyrus)
print()
miley_cyrus.show_info()
# miley_cyrus
print()
print()

f = Parent('Robertson', 'red')
d = Parent
kid = Child('Pickles', 'red', 5)

kid2 = Child('Picskles', 'blue', 2)


print(Parent.template)
print(d('asdf','aw').template, kid.template)

kid2.template = 'drunk.html'
# d.template = 'ra'
Child.template = 'What happens now?'
print(d.template, f.template, kid.template)
print(kid2.template)