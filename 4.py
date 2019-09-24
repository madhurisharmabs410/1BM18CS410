class University:
    def __init__(self):
        self.id=0;
        self.age=0;
        self.marks=0;

    def validate_marks(self):
        if self.marks > 0 and self.marks <= 100:
            return True
        else:
            return False

    def validate_age(self):
        if self.age>=20:
            return True
        else:
            return False

    def checkquali(self):
        if self.validate_marks() and self.validate_age():
            if self.marks >=65:
                return True
            else:
                return False
        else:
            False

    def setter(self,n,a,m):
        self.id=n;
        self.age=a;
        self.marks=m

    def getter(self):
        print("Id",self.id);
        print("Age",self.age);
        print("Marks",self.marks);
        #print("Given information is valid",self.checkquali());
        if self.checkquali():
                print("Valid");
        else:
                print("Invalid");


a1=University()
a1.setter(1,25,95)
a1.getter()
print("")
a2=University()
a2.setter(2,21,90)
a2.getter()


