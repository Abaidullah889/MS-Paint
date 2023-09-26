from tkinter import *
import math
from tkinter.colorchooser import askcolor
from turtle import width
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import colorchooser
from tkinter import simpledialog
from PIL import ImageGrab
from PIL import ImageTk





# n-polygon





#Kite
# # self.shape_id=self.canvas.create_polygon(
#           x1, y1,
#           x1 + (x2 - x1) / 2, y1 - 2 * (y2 - y1),
#           x2, y1,
#           x1 + (x2 - x1) / 4, y2,
#           x1 + (x2 - x1) / 4 * 3, y2,
#           outline="black", fill=""
#          )


#Pentagon
 
# radius = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
          # # Calculate angle between points of star
          # angle = 2 * math.pi / 5
    
          # # Calculate coordinates of star points
          # star_points = []
          # for i in range(5):
          #    x = x1 + radius * math.cos(i * angle)
          #    y = y1 + radius * math.sin(i * angle)
          #    star_points.append((x, y))





class Paint_Brush:
    def __init__(self,canvas,color,size):
        self.canvas = canvas  
        self.color = color    
        self.size = size 
        self.isDrawing=False
        self.last_pos=None
    def start_drawing(self,event):
        self.isDrawing=True
        self.last_pos=(event.x,event.y)
    def stop_drawing(self,event):
        self.isDrawing=False
    def draw(self,event):
        
                x1,y1=self.last_pos
                x2,y2=event.x,event.y
                # self.canvas.create_line(x1,y1,x2,y2,fill=self.color,width=self.size)
                self.canvas.create_line(x1,y1,x2,y2,fill=self.color,width=self.size,capstyle=ROUND)
                self.last_pos=(x2,y2) 

    def change_color(self, new_color):
        self.color = new_color

    def change_size(self, new_size):
        self.size = new_size
class Eraser:
     def __init__(self,canvas,color,size):
        self.canvas = canvas  
        self.color = "white"    
        self.size = size 
        self.isDrawing=False
        self.last_pos=None
     def start_drawing(self,event):
        self.isDrawing=True
        self.last_pos=(event.x,event.y)
     def stop_drawing(self,event):
        self.isDrawing=False
     def draw(self,event):
        
                x1,y1=self.last_pos
                x2,y2=event.x,event.y
                # self.canvas.create_line(x1,y1,x2,y2,fill=self.color,width=self.size)
                self.canvas.create_line(x1,y1,x2,y2,fill=self.color,width=self.size,capstyle=ROUND)
                self.last_pos=(x2,y2) 

     def change_color(self, new_color):
        self.color = new_color

     def change_size(self, new_size):
        self.size = new_size

class Circle:
     def __init__(self,canvas,fillcolor,outlinecolor):
          self.canvas=canvas
          self.fill_color=fillcolor
          self.outline_color=outlinecolor
          self.isDrawing=False
          self.last_pos_x=None
          self.last_pos_y=None
          self.shape_id=None
     def stop_drawing(self,event):
         self.isDrawing=False
         self.last_pos_x=None
         self.last_pos_y=None
         self.shape_id=None
     def draw(self,event):
          
          
          if self.shape_id is not None:
               self.canvas.delete(self.shape_id)
               

          if self.last_pos_x is None:
                self.last_pos_x,self.last_pos_y=event.x,event.y
                return
            


          radius=abs(self.last_pos_x-event.x)+abs(self.last_pos_y-event.y)
          
          x1,y1=(self.last_pos_x-radius),(self.last_pos_y-radius)
          x2,y2=(self.last_pos_x+radius),(self.last_pos_y+radius)
          
          if self.fill_color is None:   
            self.shape_id=self.canvas.create_oval(x1,y1,x2,y2,outline=self.outline_color,width=5)
          if self.fill_color is not None:
               self.shape_id=self.canvas.create_oval(x1,y1,x2,y2,fill=self.fill_color,outline=self.outline_color,width=5)
                 
     def change_outline(self,new_color):
          self.outline_color=new_color
     def change_fill(self,new_color):
          self.fill_color=new_color
class Rectangle:
     
     def __init__(self,canvas,fillcolor,outlinecolor):
          self.canvas=canvas
          self.fill_color=fillcolor
          self.outline_color=outlinecolor
          self.isDrawing=False
          self.last_pos_x=None
          self.last_pos_y=None
          self.shape_id=None   

     def stop_drawing(self,event):
         self.isDrawing=False
         self.last_pos_x=None
         self.last_pos_y=None
         self.shape_id=None
     def draw(self,event):
          
          if self.shape_id is not None:
               self.canvas.delete(self.shape_id)

          if self.last_pos_x is None:
                self.last_pos_x,self.last_pos_y=event.x,event.y
                return

          x1,y1=self.last_pos_x,self.last_pos_y
          x2,y2=event.x,event.y

          if self.fill_color is None:   
            self.shape_id=self.canvas.create_rectangle(x1,y1,x2,y2,outline=self.outline_color,width=5)
          if self.fill_color is not None:
               self.shape_id=self.canvas.create_rectangle(x1,y1,x2,y2,fill=self.fill_color,outline=self.outline_color,width=5)

     def change_outline(self,new_color):
          self.outline_color=new_color
     def change_fill(self,new_color):
          self.fill_color=new_color
class Oval:
     def __init__(self,canvas,fillcolor,outlinecolor):
          self.canvas=canvas
          self.fill_color=fillcolor
          self.outline_color=outlinecolor
          self.isDrawing=False
          self.last_pos_x=None
          self.last_pos_y=None
          self.shape_id=None  

     def stop_drawing(self,event):
         self.isDrawing=False
         self.last_pos_x=None
         self.last_pos_y=None
         self.shape_id=None    

     def draw(self,event):
          
          if self.shape_id is not None:
               self.canvas.delete(self.shape_id)

          if self.last_pos_x is None:
                self.last_pos_x,self.last_pos_y=event.x,event.y
                return

          x1,y1=self.last_pos_x,self.last_pos_y
          x2,y2=event.x,event.y

          if self.fill_color is None:   
            self.shape_id=self.canvas.create_oval(x1,y1,x2,y2,outline=self.outline_color,width=5)
          if self.fill_color is not None:
               self.shape_id=self.canvas.create_oval(x1,y1,x2,y2,fill=self.fill_color,outline=self.outline_color,width=5) 

     def change_outline(self,new_color):
          self.outline_color=new_color
     def change_fill(self,new_color):
          self.fill_color=new_color
class Straight_Line:
     def __init__(self,canvas,outlinecolor):
          self.canvas=canvas
          self.outline_color=outlinecolor
          self.isDrawing=False
          self.last_pos_x=None
          self.last_pos_y=None
          self.shape_id=None 

     def stop_drawing(self,event):
          self.isDrawing=False
          self.last_pos_x=None
          self.last_pos_y=None
          self.shape_id=None  

     def draw(self,event):
          
          if self.shape_id is not None:
               self.canvas.delete(self.shape_id)

          if self.last_pos_x is None:
                self.last_pos_x,self.last_pos_y=event.x,event.y
                return

          x1,y1=self.last_pos_x,self.last_pos_y
          x2,y2=event.x,event.y

          self.shape_id=self.canvas.create_line(x1,y1,x2,y2,fill=self.outline_color,width=5,capstyle=ROUND)

     def change_outline(self,new_color):
          self.outline_color=new_color
class Square:
     def __init__(self,canvas,fillcolor,outlinecolor):
          self.canvas=canvas
          self.fill_color=fillcolor
          self.outline_color=outlinecolor
          self.isDrawing=False
          self.last_pos_x=None
          self.last_pos_y=None
          self.shape_id=None   

     def stop_drawing(self,event):
         self.isDrawing=False
         self.last_pos_x=None
         self.last_pos_y=None
         self.shape_id=None

     def draw(self,event):
          
          if self.shape_id is not None:
               self.canvas.delete(self.shape_id)

          if self.last_pos_x is None:
                self.last_pos_x,self.last_pos_y=event.x,event.y
                return
          

          side_length = min(abs(self.last_pos_x - event.x), abs(self.last_pos_y - event.y))


          if self.last_pos_x < event.x:
            x2 = self.last_pos_x + side_length
          else:
            x2 = self.last_pos_x - side_length

          if self.last_pos_y < event.y:
            y2 = self.last_pos_y + side_length
          else:
            y2 = self.last_pos_y - side_length

          if self.fill_color is None:   
            self.shape_id=self.canvas.create_rectangle(self.last_pos_x,self.last_pos_y,x2,y2,outline=self.outline_color,width=5)
          if self.fill_color is not None:
               self.shape_id=self.canvas.create_rectangle(self.last_pos_x,self.last_pos_y,x2,y2,fill=self.fill_color,outline=self.outline_color,width=5)
    
    
     def change_outline(self,new_color):
          self.outline_color=new_color
     def change_fill(self,new_color):
          self.fill_color=new_color
class Triangle:
     def __init__(self,canvas,fillcolor,outlinecolor):
          self.canvas=canvas
          self.fill_color=fillcolor
          self.outline_color=outlinecolor
          self.isDrawing=False
          self.last_pos_x=None
          self.last_pos_y=None
          self.shape_id=None   

     def stop_drawing(self,event):
         self.isDrawing=False
         self.last_pos_x=None
         self.last_pos_y=None
         self.shape_id=None

     def draw(self,event):
          
          if self.shape_id is not None:
               self.canvas.delete(self.shape_id)

          if self.last_pos_x is None:
                self.last_pos_x,self.last_pos_y=event.x,event.y
                return
          
          x1=self.last_pos_x
          y1=self.last_pos_y
          x2=event.x
          y2=event.y


          if self.fill_color is None:   
             self.shape_id=self.canvas.create_polygon(x1,y1 , x2, y2, x2 - (x2 - x1),y2,outline=self.outline_color,fill="",width=5)
          if self.fill_color is not None:
             self.shape_id=self.canvas.create_polygon(x1,y1 , x2, y2, x2 - (x2 - x1),y2,fill=self.fill_color,outline=self.outline_color)

     def change_outline(self,new_color):
          self.outline_color=new_color
     def change_fill(self,new_color):
          self.fill_color=new_color
class Star:

     def __init__(self,canvas,fillcolor,outlinecolor):
          self.canvas=canvas
          self.fill_color=fillcolor
          self.outline_color=outlinecolor
          self.isDrawing=False
          self.last_pos_x=None
          self.last_pos_y=None
          self.shape_id=None   

     def stop_drawing(self,event):
         self.isDrawing=False
         self.last_pos_x=None
         self.last_pos_y=None
         self.shape_id=None

     def draw(self,event):
          
          if self.shape_id is not None:
               self.canvas.delete(self.shape_id)

          if self.last_pos_x is None:
                self.last_pos_x,self.last_pos_y=event.x,event.y
                return
          

          x1,y1=self.last_pos_x,self.last_pos_y
          x2,y2=event.x,event.y

          radius = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) / 2
          x_center = (x2 + x1) / 2
          y_center = (y2 + y1) / 2

          # Set the rotation angle in degrees
          angle_offset = 53.92

          # Draw the star shape
          star_points = []
          for i in range(5):
              angle = math.radians(i * 72 + angle_offset)
              x_outer = x_center + radius * math.cos(angle)
              y_outer = y_center + radius * math.sin(angle)
              star_points.append(x_outer)
              star_points.append(y_outer)

              angle_inner = math.radians(i * 72 + 36 + angle_offset)
              x_inner = x_center + radius / 2 * math.cos(angle_inner)
              y_inner = y_center + radius / 2 * math.sin(angle_inner)
              star_points.append(x_inner)
              star_points.append(y_inner)

          if self.fill_color is None: 
             self.shape_id=self.canvas.create_polygon(star_points, outline=self.outline_color, fill="",width=5)
          if self.fill_color is not None:
             self.shape_id=self.canvas.create_polygon(star_points, outline=self.outline_color, fill=self.fill_color,width=5)    

     def change_outline(self,new_color):
          self.outline_color=new_color
     def change_fill(self,new_color):
          self.fill_color=new_color
class Pentagon:

     def __init__(self,canvas,fillcolor,outlinecolor):
          self.canvas=canvas
          self.fill_color=fillcolor
          self.outline_color=outlinecolor
          self.isDrawing=False
          self.last_pos_x=None
          self.last_pos_y=None
          self.shape_id=None   

     def stop_drawing(self,event):
         self.isDrawing=False
         self.last_pos_x=None
         self.last_pos_y=None
         self.shape_id=None

     def draw(self,event):
          
          if self.shape_id is not None:
               self.canvas.delete(self.shape_id)

          if self.last_pos_x is None:
                self.last_pos_x,self.last_pos_y=event.x,event.y
                return
          

          x1,y1=self.last_pos_x,self.last_pos_y
          x2,y2=event.x,event.y

          radius = abs(x2 - x1) // 2
          x_center = (x2 + x1) // 2
          y_center = (y2 + y1) // 2
          angle_offset = 53.92


          pentagon_points = []
          for i in range(5):
            angle = math.radians(i * 72 + angle_offset)
            x = x_center + radius * math.cos(angle)
            y = y_center + radius * math.sin(angle)
            pentagon_points.append(x)
            pentagon_points.append(y)



          self.shape_id=self.canvas.create_polygon(pentagon_points, outline=self.outline_color, fill="",width=5)

     def change_outline(self,new_color):
          self.outline_color=new_color
     def change_fill(self,new_color):
          self.fill_color=new_color
class Hexagon:
     def __init__(self,canvas,fillcolor,outlinecolor):
          self.canvas=canvas
          self.fill_color=fillcolor
          self.outline_color=outlinecolor
          self.isDrawing=False
          self.last_pos_x=None
          self.last_pos_y=None
          self.shape_id=None   

     def stop_drawing(self,event):
         self.isDrawing=False
         self.last_pos_x=None
         self.last_pos_y=None
         self.shape_id=None

     def draw(self,event):
          
          if self.shape_id is not None:
               self.canvas.delete(self.shape_id)

          if self.last_pos_x is None:
                self.last_pos_x,self.last_pos_y=event.x,event.y
                return
          

          x1,y1=self.last_pos_x,self.last_pos_y
          x2,y2=event.x,event.y

          radius = abs(x2 - x1) // 2
          x_center = (x2 + x1) // 2
          y_center = (y2 + y1) // 2
          angle_offset = 53.92


          hexagon_points = []
          for i in range(6):
          #  angle = math.radians(i * 72 + angle_offset)
            angle = 2 * i * math.pi / 6
            x = x_center + radius * math.cos(angle)
            y = y_center + radius * math.sin(angle)
            hexagon_points.append(x)
            hexagon_points.append(y)



          self.shape_id=self.canvas.create_polygon(hexagon_points, outline=self.outline_color, fill="",width=5)

     def change_outline(self,new_color):
          self.outline_color=new_color
     def change_fill(self,new_color):
          self.fill_color=new_color

class Magnifier:
   
   def __init__(self, canvas):
        self.canvas = canvas
        self.canvas_width = 1200
        self.canvas_height = 600
        self.scale_factor = 1.0

   def zoom_in(self, event):
        x = event.x
        y = event.y
        
        # Increase the scale factor
        
        
        if self.scale_factor < 1.631: 
          self.scale_factor *= 1.1
          # Adjust the canvas size
          new_width = int(self.canvas_width * self.scale_factor)
          new_height = int(self.canvas_height * self.scale_factor)
          self.canvas.config(width=new_width, height=new_height)
          
          
          # Adjust the scroll region to include the zoomed area
          self.canvas.configure(scrollregion=self.canvas.bbox("all"))
          
          # Apply zooming transformation to the items on the canvas
          self.canvas.scale("all", x, y, 1.1, 1.1)
    
   def zoom_out(self, event):
        x = event.x
        y = event.y
        
        if self.scale_factor > 1.0:
          # Decrease the scale factor
          self.scale_factor /= 1.1
          # Adjust the canvas size
          new_width = int(self.canvas_width * self.scale_factor)
          new_height = int(self.canvas_height *self.scale_factor)
          self.canvas.config(width=new_width, height=new_height)
               
          # Adjust the scroll region to include the zoomed area
          self.canvas.configure(scrollregion=self.canvas.bbox("all"))
               
          # Apply zooming transformation to the items on the canvas
          self.canvas.scale("all", x, y, 1/1.1, 1/1.1)
          
class SelectionTool:
    
    def __init__(self, canvas,screen):
        self.screen=screen
        self.canvas = canvas

        self.start_x = None
        self.start_y = None
        self.selection = None

        self.cut_image = None
        self.selected_item = None
        self.offset_x = 0
        self.offset_y = 0
        self.nowMove=False

    def start_selection(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def track_selection(self, event):
        self.canvas.delete(self.selection)
        self.selection = self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y, outline="red",dash=TRUE
        )
        self.rect_x1=self.start_x
        self.rect_x2=event.x
        self.rect_y1=self.start_y
        self.rect_y2=event.y

    def end_selection(self, event):
        self.canvas.delete(self.selection)
        self.selection = self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y, outline="white",fill="white",tag="remove"
        )
        x1 = min(self.start_x, event.x)
        y1 = min(self.start_y, event.y)
        x2 = max(self.start_x, event.x)
        y2 = max(self.start_y, event.y)

        self.cut_image = ImageGrab.grab(bbox=(self.canvas.winfo_rootx() + x1+1,
                                               self.canvas.winfo_rooty() + y1+1,
                                               self.canvas.winfo_rootx() + x2-1,
                                               self.canvas.winfo_rooty() + y2))

        self.canvas.delete("pasted_image")
        self.image = ImageTk.PhotoImage(self.cut_image)
        self.selected_item = self.canvas.create_image(0, 0, anchor=NW, image=self.image, tags="pasted_image")
        self.cut_image = None

        if self.selected_item:
             self.canvas.unbind("<B1-Motion>")
             self.canvas.unbind("<ButtonRelease-1>")
             self.canvas.bind("<B1-Motion>", self.move_selection)
             self.canvas.bind("<ButtonRelease-1>", self.release_selection)


    def move_selection(self, event):
        if self.selected_item:
            if not self.offset_x and not self.offset_y:
                self.offset_x = event.x
                self.offset_y = event.y
            else:
                self.canvas.move(self.selected_item, event.x - self.offset_x, event.y - self.offset_y)
                self.offset_x = event.x
                self.offset_y = event.y

    def release_selection(self, event):
        self.offset_x = 0
        self.offset_y = 0

class Isoceles_Triangle:
     def __init__(self,canvas,fillcolor,outlinecolor):
          self.canvas=canvas
          self.last_pos_x=None
          self.last_pos_y=None
          self.id=None
          self.fill_color=fillcolor
          self.outline_color=outlinecolor

     def start_drawing(self,event):
          self.last_pos_x = event.x
          self.last_pos_y = event.y

     def continue_drawing(self,event):
       

       if self.id is not None:
               self.canvas.delete(self.id)

       x2 = event.x
       y2 = event.y

       # Calculate the base and height of the triangle
       base = abs(x2 - self.last_pos_x)
       height = abs(y2 - self.last_pos_y)

       # Determine the top vertex based on mouse movement direction
       if y2 < self.last_pos_y:
            top_x = self.last_pos_x - base / 2
            top_y = self.last_pos_y - height
       else:
            top_x = self.last_pos_x - base / 2
            top_y = self.last_pos_y + height

        # Clear the canvas and draw the triangle
       if self.fill_color is None:
          self.id=self.canvas.create_polygon(top_x, top_y, top_x + base, top_y, self.last_pos_x, self.last_pos_y,
                                   fill="", outline=self.outline_color,width=5)
       if self.fill_color is not None:
          self.id=self.canvas.create_polygon(top_x, top_y, top_x + base, top_y, self.last_pos_x, self.last_pos_y,
                                   fill=self.fill_color, outline=self.outline_color,width=5)     
 
     def stop_drawing(self,event):
         self.last_pos_x=None
         self.last_pos_y=None
         self.id=None
     def change_outline(self,new_color):
          self.outline_color=new_color
     def change_fill(self,new_color):
          self.fill_color=new_color

class N_Polygon:
     def __init__(self,canvas,fillcolor,outlinecolor):
          self.canvas=canvas
          self.fill_color=fillcolor
          self.outline_color=outlinecolor
          self.isDrawing=False
          self.last_pos_x=None
          self.last_pos_y=None
          self.shape_id=None   

     def stop_drawing(self,event):
         self.isDrawing=False
         self.last_pos_x=None
         self.last_pos_y=None
         self.shape_id=None

     def draw(self,event,value):
          
          if self.shape_id is not None:
               self.canvas.delete(self.shape_id)

          if self.last_pos_x is None:
                self.last_pos_x,self.last_pos_y=event.x,event.y
                return
          

          x1,y1=self.last_pos_x,self.last_pos_y
          x2,y2=event.x,event.y

          radius = abs(x2 - x1) // 2
          x_center = (x2 + x1) // 2
          y_center = (y2 + y1) // 2
          angle_offset = 63.92


          polygon_points = []
          for i in range(value):
            
            angle = 2 * i * math.pi / value
            x = x_center + radius * math.cos(angle)
            y = y_center + radius * math.sin(angle)
            polygon_points.append(x)
            polygon_points.append(y)



          self.shape_id=self.canvas.create_polygon(polygon_points, outline=self.outline_color, fill="",width=5)


     def change_outline(self,new_color):
          self.outline_color=new_color
     def change_fill(self,new_color):
          self.fill_color=new_color       

class Curve:
      def __init__(self,canvas,outlinecolor):
          self.canvas=canvas
          self.outline_color=outlinecolor
          self.isDrawing=False
          self.last_pos_x=None
          self.last_pos_y=None
          self.second_x=None
          self.second_y=None
          self.control_x=None
          self.control_y=None
          self.shape_id=None 
          self.shape2_id=None

      def start_drawing(self,event):
       self.last_pos_x,self.last_pos_y = event.x, event.y

      def draw_curve(self,event):
        
        if self.shape_id is not None:
               self.canvas.delete(self.shape_id)

        self.second_x=event.x
        self.second_y=event.y     

        # Draw the straight line or the quadratic Bezier curve based on dragging
        if self.control_x is None or self.control_y is None:
           # Draw the straight line if control point is not set
           self.shape_id=self.canvas.create_line(self.last_pos_x, self.last_pos_y, event.x, event.y, smooth=True, fill='black',width=5)
               



      def set_control_point(self,event):
        # Set the control point for transforming into a quadratic Bezier curve
        self.control_x, self.control_y = event.x, event.y
        if self.shape_id is not None:
               self.canvas.delete(self.shape_id)
        if self.shape2_id is not None:
               self.canvas.delete(self.shape2_id)

        self.shape2_id=self.canvas.create_line(self.last_pos_x, self.last_pos_y, self.control_x, self.control_y, self.second_x,self.second_y, smooth=True, fill='black',width=5)




class PaintApp:
    def __init__(self):
        self.screen=Tk()
        self.screen.title("Paint")
        self.color="Black"
        self.fillcolor=None
        self.image=None

     
        
       
        menu = Menu(self.screen)
        self.screen.config(menu=menu)
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save Canvas", command=self.save_canvas)
        file_menu.add_command(label="Load Canvas", command=self.load_canvas)



         # Buttons Frame
        self.frame=Frame(self.screen,width=1200,height=70,bg="Grey")
        self.frame.pack()

        # Draw Canvas
        self.canvas = Canvas(self.screen, width=1200, height=600, bg="white")
        self.canvas.pack()
        self.canvas.pack(fill='both', expand=True)



        #isoscles Triangle
        self.isoceles=Isoceles_Triangle(self.canvas,self.fillcolor,self.color)

        #N_Polygon Tool

        self.polygon=N_Polygon(self.canvas,self.fillcolor,self.color)

        #Curve Object
        self.curve=Curve(self.canvas,self.color)



        #Selection Tool
        self.selectionTool=SelectionTool(self.canvas,self.screen)
        # Piant Brush Object
        self.brush = Paint_Brush(self.canvas, self.color, 6)

        # Erases Object
        self.eraser=Eraser(self.canvas,self.color,5)

        #Circle Object
        self.circle=Circle(self.canvas,self.fillcolor,self.color)

        #Rectangle Object
        self.Rectangle=Rectangle(self.canvas,self.fillcolor,self.color)

        #Oval Object
        self.Oval=Oval(self.canvas,self.fillcolor,self.color)

        #Straight Line Object
        self.line=Straight_Line(self.canvas,self.color)

        #Square Object
        self.square=Square(self.canvas,self.fillcolor,self.color)

        #Traingle Object
        self.triangle=Triangle(self.canvas,self.fillcolor,self.color)

        #Star Object
        self.star=Star(self.canvas,self.fillcolor,self.color)

        #Pentagon Object
        self.pentagon=Pentagon(self.canvas,self.fillcolor,self.color)

        #Hexagon Object
        self.hexagon=Hexagon(self.canvas,self.fillcolor,self.color)

        #Magnifier Object
        self.magnifier=Magnifier(self.canvas)

        
        


        #Polygon Button
        self.polygon_button=Button(self.frame,text="Polygon",command=self.on_PolygonButton)
        self.polygon_button.place(x=630,y=35)


        #Selection Tool
        self.selection_button=Button(self.frame,text="Selection Tool",command=self.on_SelectionButton)
        self.selection_button.place(x=830,y=35)


        #Magnifier Tool
        self.Magnifier_button=Button(self.frame,text="Magnifier",command=self.on_MagnifierButton)
        self.Magnifier_button.place(x=950,y=5)

        #Eraser Tool
        self.eraser_button=Button(self.frame,text="Eraser",command=self.on_EraserButton)
        self.eraser_button.place(x=1020,y=5)
       
        #Color-Picker Tool
        self.colorpicker_button=Button(self.frame,text="Color-Picker",command=self.on_ColorPickerButton)
        self.colorpicker_button.place(x=720,y=5)

        #Hexagon Button
        self.hexagon_button=Button(self.frame,text="Hexagon", command=self.on_HexagonButton)
        self.hexagon_button.place(x=650,y=5)

        #Pentagon Button
        self.pentagon_button=Button(self.frame,text="Pentagon",command=self.on_PentagonButton)
        self.pentagon_button.place(x=580,y=5)

        #Star Button
        self.star_button=Button(self.frame,text="Star",command=self.on_StarButton)
        self.star_button.place(x=500,y=5)

        #Trianlge Button
        self.triangle_button=Button(self.frame,text="Triangle",command=self.on_TriangleButton)
        self.triangle_button.place(x=440,y=5)

        #RTrianlge Button
        self.triangle_button=Button(self.frame,text="Rtriangle",command=self.on_RTriagle_Button)
        self.triangle_button.place(x=740,y=35)

        #Square_Button
        self.square_button=Button(self.frame,text="Square",command=self.on_SquareButton)
        self.square_button.place(x=380,y=5)

        #Straight_Line Button
        self.line_button=Button(self.frame,text="Line",command=self.on_LineButton)
        self.line_button.place(x=330,y=5)

        # Curve Button
        self.line_button=Button(self.frame,text="Curve",command=self.on_CurveButton)
        self.line_button.place(x=580,y=35)




        #Oval Button
        self.oval_button=Button(self.frame,text="Oval",command=self.on_OvalButton)
        self.oval_button.place(x=280,y=5)
       
        #Circle Button
        self.circle_button=Button(self.frame,text="Circle",command=self.on_CircleButton)
        self.circle_button.place(x=150,y=5)

        #Rectangle Button
        self.rectangle_button=Button(self.frame,text="Rectangle",command=self.on_RectangleButton)
        self.rectangle_button.place(x=200,y=5)

        #Brush Button
        self.brush_button=Button(self.frame,text="Brush",command=self.on_BrushButton)
        self.brush_button.place(x=100,y=5)

        #Clear Button
        self.new_button=Button(self.frame,text="New",command=self.clear)
        self.new_button.place(x=5,y=5)

        #Select Brush Color Button
        self.color_button=Button(self.frame,text="Color",command=self.select_Brushcolor)
        self.color_button.place(x=50,y=5)

        #Select Eraser Color Button
        self.erasercolor_button=Button(self.frame,text="Eraser Color",command=self.select_Erasercolor)
        self.erasercolor_button.place(x=1080,y=5)




        #Brush Size Menu

        self.size_label = Label(self.frame, text="Brush Size")
        self.size_label.place(x=330,y=40)
        self.size_menu = OptionMenu(self.frame, IntVar(), 1, 5, 10, 15, command=self.brush.change_size)
        self.size_menu.place(x=400,y=35)

        #Eraser Size Menu

        self.size_label = Label(self.frame, text="Eraser Size")
        self.size_label.place(x=930,y=40)
        self.size_menu = OptionMenu(self.frame, IntVar(), 1, 5, 10, 15, command=self.eraser.change_size)
        self.size_menu.place(x=1000,y=35)



        #Fill Button
        self.fill_button=Button(self.frame,text="Fill",command=self.on_FillButton)
        self.fill_button.place(x=800,y=5)

        self.fillcolor_button=Button(self.frame,text="Fill-Color",command=self.select_Fillcolor)
        self.fillcolor_button.place(x=880,y=5)


     
    def on_PolygonButton(self):
         self.canvas.unbind("<Button-1>")
         self.canvas.unbind("<ButtonRelease-1>")
         self.canvas.unbind("<B1-Motion>")
         self.my_i=simpledialog.askinteger("Polygon","Enter the input",parent=self.screen)
         

         self.canvas.bind("<B1-Motion>",lambda event: self.polygon.draw(event,self.my_i))
         self.canvas.bind("<ButtonRelease-1>",self.polygon.stop_drawing)


    def on_RTriagle_Button(self):
         self.canvas.unbind("<Button-1>")
         self.canvas.unbind("<ButtonRelease-1>")
         self.canvas.unbind("<B1-Motion>")

         self.canvas.bind("<B1-Motion>",self.triangle.draw)
         self.canvas.bind("<ButtonRelease-1>",self.triangle.stop_drawing)
         
    def on_SelectionButton(self):
         self.canvas.unbind("<Button-1>")
         self.canvas.unbind("<ButtonRelease-1>")
         self.canvas.unbind("<B1-Motion>")

         self.canvas.bind("<Button-1>", self.selectionTool.start_selection)
         self.canvas.bind("<B1-Motion>", self.selectionTool.track_selection)
         self.canvas.bind("<ButtonRelease-1>", self.selectionTool.end_selection)
        
    def on_MagnifierButton(self):
         self.canvas.unbind("<Button-1>")
         self.canvas.unbind("<ButtonRelease-1>")
         self.canvas.unbind("<B1-Motion>")


         self.canvas.bind("<Button-1>", self.magnifier.zoom_in)
         self.canvas.bind("<Button-3>", self.magnifier.zoom_out)

    def on_FillButton(self):
         self.canvas.unbind("<Button-1>")
         self.canvas.unbind("<ButtonRelease-1>")
         self.canvas.unbind("<B1-Motion>")

         self.canvas.bind("<Button-1>",self.fill)
         
    def on_ColorPickerButton(self):
          self.canvas.unbind("<Button-1>")
          self.canvas.unbind("<ButtonRelease-1>")
          self.canvas.unbind("<B1-Motion>")

          self.canvas.bind("<Button-1>",self.color_picker)

    def on_HexagonButton(self):
         self.canvas.unbind("<Button-1>")
         self.canvas.unbind("<ButtonRelease-1>")
         self.canvas.unbind("<B1-Motion>")

         self.canvas.bind("<B1-Motion>",self.hexagon.draw)
         self.canvas.bind("<ButtonRelease-1>",self.hexagon.stop_drawing)

    def on_PentagonButton(self):
         self.canvas.unbind("<Button-1>")
         self.canvas.unbind("<ButtonRelease-1>")
         self.canvas.unbind("<B1-Motion>")

         self.canvas.bind("<B1-Motion>",self.pentagon.draw)
         self.canvas.bind("<ButtonRelease-1>",self.pentagon.stop_drawing)

    def on_StarButton(self):
         self.canvas.unbind("<Button-1>")
         self.canvas.unbind("<ButtonRelease-1>")
         self.canvas.unbind("<B1-Motion>")

         self.canvas.bind("<B1-Motion>",self.star.draw)
         self.canvas.bind("<ButtonRelease-1>",self.star.stop_drawing)

    def on_TriangleButton(self):
         self.canvas.unbind("<Button-1>")
         self.canvas.unbind("<ButtonRelease-1>")
         self.canvas.unbind("<B1-Motion>")

         self.canvas.bind("<Button-1>",self.isoceles.start_drawing)
         self.canvas.bind("<B1-Motion>", self.isoceles.continue_drawing)
         self.canvas.bind("<ButtonRelease-1>",self.isoceles.stop_drawing)

    def on_SquareButton(self):
         self.canvas.unbind("<Button-1>")
         self.canvas.unbind("<ButtonRelease-1>")
         self.canvas.unbind("<B1-Motion>")

         self.canvas.bind("<B1-Motion>",self.square.draw)
         self.canvas.bind("<ButtonRelease-1>",self.square.stop_drawing)

    def on_LineButton(self):
         # bind mouse events to the canvas
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<B1-Motion>")

            self.canvas.bind("<B1-Motion>",self.line.draw)
            self.canvas.bind("<ButtonRelease-1>",self.line.stop_drawing)



    def on_CurveButton(self):
         # bind mouse events to the canvas
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<B1-Motion>")
            self.canvas.bind("<Button-1>",self.curve.start_drawing)
            self.canvas.bind("<B3-Motion>", self.curve.set_control_point)

            self.canvas.bind("<B1-Motion>",self.curve.draw_curve)
  
    def on_OvalButton(self):
         # bind mouse events to the canvas
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<B1-Motion>")

            self.canvas.bind("<B1-Motion>",self.Oval.draw)
            self.canvas.bind("<ButtonRelease-1>",self.Oval.stop_drawing)
         
    def on_BrushButton(self):
            # bind mouse events to the canvas
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<B1-Motion>")

            self.canvas.bind("<Button-1>", self.brush.start_drawing)
            self.canvas.bind("<ButtonRelease-1>", self.brush.stop_drawing)
            self.canvas.bind("<B1-Motion>", self.brush.draw)

    def on_EraserButton(self):
            # bind mouse events to the canvas
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<B1-Motion>")

            self.canvas.bind("<Button-1>", self.eraser.start_drawing)
            self.canvas.bind("<ButtonRelease-1>", self.eraser.stop_drawing)
            self.canvas.bind("<B1-Motion>", self.eraser.draw)       

    def on_CircleButton(self):
        # bind mouse events to the canvas
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<B1-Motion>")

            self.canvas.bind("<B1-Motion>",self.circle.draw)
            self.canvas.bind("<ButtonRelease-1>",self.circle.stop_drawing)

    def on_RectangleButton(self):
         self.canvas.unbind("<Button-1>")
         self.canvas.unbind("<ButtonRelease-1>")
         self.canvas.unbind("<B1-Motion>")

         self.canvas.bind("<B1-Motion>",self.Rectangle.draw)
         self.canvas.bind("<ButtonRelease-1>",self.Rectangle.stop_drawing)

    def color_picker(self,event):
          x = int(event.x)
          y = int(event.y)
          color = self.canvas.itemcget(self.canvas.find_closest(x, y), "fill")
          self.color=color

          self.brush.change_color(self.color)
          self.circle.change_outline(self.color)
          self.Rectangle.change_outline(self.color)
          self.square.change_outline(self.color)
          self.line.change_outline(self.color)
          self.eraser.change_color(self.color)
          self.Oval.change_outline(self.color)
          self.triangle.change_outline(self.color)
          self.star.change_outline(self.color)
          self.pentagon.change_outline(self.color)
          self.hexagon.change_outline(self.color)
          self.isoceles.change_outline(self.color)
          
    def select_Brushcolor(self):
        selected_color=askcolor()
        if selected_color[1]!=None:
            self.color = selected_color[1]
            self.circle.change_outline(self.color)
            self.Rectangle.change_outline(self.color)
            self.square.change_outline(self.color)
            self.line.change_outline(self.color)
            self.brush.change_color(self.color)
            self.Oval.change_outline(self.color)
            self.triangle.change_outline(self.color)
            self.star.change_outline(self.color)
            self.pentagon.change_outline(self.color)
            self.hexagon.change_outline(self.color)
            self.isoceles.change_outline(self.color)

    def select_Fillcolor(self):
         selected_color=askcolor()
         if selected_color[1]!=None:
              self.fillcolor = selected_color[1]

         

    def select_Erasercolor(self):
      selected_color=askcolor()
      if selected_color[1]!=None:
             self.color = selected_color[1]
             self.eraser.change_color(self.color)
               

    def fill(self, event):
          x, y = event.x, event.y
          pixel_color = self.canvas.itemcget(self.canvas.find_closest(x, y), "fill")

          if pixel_color != self.fillcolor:
               
               item_id = self.canvas.find_closest(x, y)
               self.canvas.itemconfigure(item_id, fill=self.fillcolor)
                         

          self.canvas.update()
    def save_canvas(self):
        filename = asksaveasfilename(defaultextension=".png")
        if filename:
            x = self.screen.winfo_rootx() + self.canvas.winfo_x()
            y = self.screen.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + 1200
            y1 = y + 600
            ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
   
   
    def load_canvas(self):
        filename = askopenfilename(defaultextension=".png")
        if filename:
            self.canvas.delete("all")
            image = PhotoImage()
            real_image = ImageTk.PhotoImage(file=filename)
            self.image=real_image
            self.canvas.create_image(0, 0, image=self.image, anchor=NW)

    def clear(self):
        self.canvas.delete("all")

    def run(self):
        self.screen.mainloop()



PaintApp().run()

