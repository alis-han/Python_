class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2

    def distance(self):
        (x1,y1)=self.coor1
        (x2,y2)=self.coor2

        print(((x2-x1)**2+(y2-y1)**2)**0.5)
    
    def slope(self):
        (x1,y1)=self.coor1
        (x2,y2)=self.coor2
        
        print((y2-y1)/(x2-x1))

coordinate1 = (3,2)
coordinate2 = (8,10)
(x1,y1)=coordinate1
(x2,y2)=coordinate2

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()

# class Cylinder:
    
#     def __init__(self,height=1,radius=1):
#         self.height=height
#         self.radius=radius
        
#     def volume(self):
#         print("{:.2f}".format(3.14*self.radius*self.radius*self.height))
    
#     def surface_area(self):
#         print("{:.1f}".format(2*3.14*self.radius*self.height+2*3.14*self.radius*self.radius))

# c = Cylinder(2,3)
# c.volume()
# c.surface_area()