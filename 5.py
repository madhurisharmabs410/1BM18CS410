class CallDetail:
    def __init__(self):
        self.call_made = None
        self.called = None
        self.duration = None
        self.type = None


class Util:
    def __init__(self):
        self.list_of_call_objects = []

    def parse_customer(self,list_of_call_string):
        for i in range(len(list_of_call_string)):
            lis = list_of_call_string[i].split(",")
            self.list_of_call_objects.append(lis)
            
    def print1(self):
        for i in range(len(self.list_of_call_objects)):
            print("call_made:",self.list_of_call_objects[i][0] ,end="\n")
            print("called_to:",self.list_of_call_objects[i][1] ,end="\n")
            print("Duration:",self.list_of_call_objects[i][2] ,end="\n")
            print("Type:",self.list_of_call_objects[i][3] ,end="\n")


    

call = '9990000001,9330000001,23,STD'
call2 = '9990000001,9330000002,54,local'
call3 = '9990000001,9330000003,6,ISD'
list_of_call_string = [call,call2,call3]
x=Util()
x.parse_customer(list_of_call_string)
x.print1()
