class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        print("{:.2f}".format(3.14*self.radius*self.radius*self.height))
    
    def surface_area(self):
        print("{:.1f}".format(2*3.14*self.radius*self.height+2*3.14*self.radius*self.radius))

c = Cylinder(2,3)
c.volume()
c.surface_area()