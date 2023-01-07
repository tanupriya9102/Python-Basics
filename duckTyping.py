class Horse:
    def walk(self):
        print("Tagdak")
class Duck:
    def walk(self):
        print("Thapak")
        
def Func(obj):
    obj.walk()
    
d=Duck()
h=Horse()

Func(d)
Func(h)
