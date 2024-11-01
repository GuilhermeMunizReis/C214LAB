import pygame
import global_vars as gv
import config as cf
from math import ceil
from functools import partial

#Base class for all widgets
class Widget():
    def __init__(self, surf, text = None, width = 0, height = 0, background = (255,255,255), textcolor = (0,0,0), img = None, x = 0, y = 0, filled = "full", overcolor=None):
        self._surf = surf
        self._text = text   
        self._width = width
        self._height = height
        self._background = background
        self._overcolor = overcolor
        self._textcolor = textcolor
        self._textrender = None
        self._img = img
        self._x = x
        self._y = y
        self._filled = filled
        self._is_over = False
        self._anchorx = None
        self._anchory = None
        self._posx = None
        self._posy = None
        self._bwidth = width
        self._bheight = height
        #bx and by are x and y declared when object was created
        self._bx = x
        self._by = y

        if self._text != None and self._text != "":
            self._textrender = cf.FONT.render(self._text, True, self._textcolor)

        self.__update()

    def draw(self):
        """  Method to draw widget  """
        if self._is_over == True and self._overcolor != None:
            color = self._overcolor
        else:
            color = self._background

        if self._img == None:
            if self._filled == "full":
                pygame.draw.rect(self._surf, color, (self._x, self._y, self._width, self._height), False)
            elif self._filled == "border":
                pygame.draw.rect(self._surf, color, (self._x, self._y, self._width, self._height), True)   
        else:
            if self._img.get_width() > self._width or self._img.get_height() > self._height:
                img = pygame.transform.scale(self._img, (self._img.get_width() - gv.CAM_Z, self._img.get_height() - gv.CAM_Z)) 
                self._surf.blit(img, (self._x, self._y))
            else:
                self._surf.blit(self.img, (self._x, self._y))
        
        if self._textrender != None:
            self._surf.blit(self._textrender, (self._x, self._y))        
  
    def check(self, pos, events):
        """ Check if mouse is over the widget, using a tuple as a parameter for mouse position """
        if pos[0] >= self._x and pos[0] <= self._x + self._width and pos[1] >= self._y and pos[1] <= self._y + self._height:
            self._is_over = True
        else:
            self._is_over = False

    def position(self, anchorx = None, anchory = None, posx = None, posy = None):
        """
        Method used to place widget on screen
        self._anchorx (W or LEFT or WEST, C or CENTER, E or EAST or RIGHT), self._anchory (N or TOP or NORTH, C or CENTER, S or SOUTH or BOT or BOTTOM)
        """
        self._anchorx = anchorx
        self._anchory = anchory
        self._posx = posx
        self._posy = posy
        
        self.__update()

    def __update(self):
        """  Internal class function, used to update widget in certain conditions  """
        if self._text != None and self._text != "":
            self._textrender = cf.FONT.render(self._text, True, self._textcolor)
            self._width = max(self._bwidth, self._textrender.get_width())
            self._height = max(self._bheight, self._textrender.get_height())

        #if self._anchorx != None or self._anchory != None:
        #    if self._anchorx == "W" or self._anchorx == "WEST" or self._anchorx == "LEFT":
        #        self._x = 0
        #    elif self._anchorx == "C" or self._anchorx == "CENTER":
        #        self._x = (cf.MAX_DISPLAY_x / 2) - (self._height / 2)
        #    elif self._anchorx == "E" or self._anchorx == "EAST" or self._anchorx == "RIGHT":
        #        self._x = cf.MAX_DISPLAY_x
        #
        #    if self._anchory == "N" or self._anchory == "NORTH" or self._anchory == "TOP":
        #        self._y = 0
        #    elif self._anchory == "C" or self._anchory == "CENTER":
        #        self._y = (cf.MAY_DISPLAY_Y / 2) - (self._width / 2)
        #    elif self._anchory == "S" or self._anchory == "SOUTH" or self._anchory == "BOT" or self._anchory == "BOTTOM":
        #        self._y = cf.MAY_DISPLAY_Y

    def get_attr(self, attr):
        if attr[0] != "_":
            attr = "_"  + attr
            
        return self.__dict__[attr]

    def config(self, attribute, value): 
        """ Changes value of specific attribute of specific object """
        if  attribute[0] != "_":
            attribute = "_" + attribute

        attribute.casefold()
        setattr(self, attribute, value)

        self.__update()

    def get_type(self):
        return type(self).__name__

#Class defining buttons on game
class Button(Widget):
    def __init__(self, surf, text = None, width = 0, height = 0, background = (255,255,255), textcolor = (0,0,0), img = None, x = 0, y = 0, filled = "full", overcolor=None, command=None):
        super().__init__(surf, text, width, height, background, textcolor, img, x , y, filled, overcolor)
        super()._Widget__update()
        super().draw
        super().position
        super().config
        super().get_type

        self.command = command

#Class defining info charts popuped if mouse is over it
class InfoChart(Widget):
    def __init__(self, surf, text = None, width = 0, height = 0, background = (255,255,255), textcolor = (0,0,0), img = None, x = 0, y = 0, filled = "full", overcolor=None):
        super().__init__(surf, text, width, height, background, textcolor, img, x , y, filled, overcolor)
        super()._Widget__update()
        super().draw
        super().position
        super().check
        super().config
        super().get_type

#Class defining a text on game
class Text(Widget):
    def __init__(self, surf, text = None, width = 0, height = 0, background = (255,255,255), textcolor = (0,0,0), img = None, x = 0, y = 0, filled = "empty", overcolor=None):
        super().__init__(surf, text, width, height, background, textcolor, img, x , y, filled, overcolor)
        super()._Widget__update()
        super().draw
        super().position
        super().check
        super().config
        super().get_type

    def get(self):
        return self._text
    
#Class defining Text Boxes on game
class TextBox(Widget):
    def __init__(self, surf, text = "", width = 0, height = 0, background = (255,255,255), textcolor = (0,0,0), img = None, x = 0, y = 0, filled = "border", actcolor=(255,0,0), resizable=False):
        super().__init__(surf, text, width, height, background, textcolor, img, x , y, filled, actcolor)
        super().position
        super().config
        super().get_type

        self._resizable = resizable
        self._active = False
        self.command = self.act

    def check(self, pos, events):
        """ Check if mouse is over the widget, using a tuple as a parameter for mouse position """
        if pos[0] >= self._x and pos[0] <= self._x + self._width and pos[1] >= self._y and pos[1] <= self._y + self._height:
            self._is_over = True
        else:
            self._is_over = False

        if self._active:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE and self._text != "":
                        self._text = self._text[:-1]
                    else:
                        self._text += event.unicode                

    def draw(self):
        """  Method to draw widget  """
        #Only TextBox needs to re-render text everytime it is drawed
        self.__update()

        if self._active == True:
            color = self._overcolor
        else:
            color = self._background

        if self._img == None:
            if self._filled == "full":
                pygame.draw.rect(self._surf, color, (self._x, self._y, self._width, self._height), False)
            elif self._filled == "border":
                pygame.draw.rect(self._surf, color, (self._x, self._y, self._width, self._height), True)   
        else:
            if self._img.get_width() > self._width or self._img.get_height() > self._height:
                img = pygame.transform.scale(self._img, (self._img.get_width() - gv.CAM_Z, self._img.get_height() - gv.CAM_Z)) 
                self._surf.blit(img, (self._x, self._y))
            else:
                self._surf.blit(self.img, (self._x, self._y))

        if self._textrender != None:
            self._surf.blit(self._textrender, (self._x, self._y))        

    def __update(self):
        """  Internal class function, used to update widget in certain conditions  """
        if self._text != None and self._text != "":
            self._textrender = cf.FONT.render(self._text, True, self._textcolor)
            
            if self._resizable == True:
                self._width = max(self._bwidth, self._textrender.get_width())
                self._height = max(self._bheight, self._textrender.get_height())
        else: 
            self._textrender = None

        if self._anchorx != None or self._anchory != None:
            if self._anchorx == "N" or self._anchorx == "NORTH" or self._anchorx == "TOP":
                self._x = 0
                self._anchorx = "N"
            elif self._anchorx == "C" or self._anchorx == "CENTER":
                self._x = (cf.MAX_DISPLAY_X / 2) - (self._width / 2)
                self._anchorx = "C"
            elif self._anchorx == "S" or self._anchorx == "SOUTH" or self._anchorx == "BOT" or self._anchorx == "BOTTOM":
                self._x = cf.MAX_DISPLAY_X
                self._anchorx = "S"

            if self._anchory == "W" or self._anchory == "WEST" or self._anchory == "LEFT":
                self._y = 0
                self._anchory = "W"
            elif self._anchory == "C" or self._anchory == "CENTER":
                self._y = (cf.MAX_DISPLAY_Y / 2) - (self._height / 2)
                self._anchory = "C"
            elif self._anchory == "E" or self._anchory == "EAST" or self._anchory == "RIGHT":
                self._y = cf.MAX_DISPLAY_Y
                self._anchory = "E"    

    def act(self):
        self._active = not self._active

    def get(self):
        return self._text

#Class defining a menu
class Menu(Widget):
    """  Menu is a container for multiple widgets that must be drawed only in certain conditions  """
    def __init__(self, surf, text = None, width = 0, height = 0, background = (255,255,255), textcolor = (0,0,0), img = None, x = 0, y = 0, filled = "full", overcolor=None): 
        super().__init__(surf, text, width, height, background, textcolor, img, x , y, filled, overcolor)
        super().position
        super().check
        super().config
        super().get_type

        self._widgets = []
        self._drawmode = None

    def draw(self):
        """  Method to draw widget  """

    def __upadate(self):
        """  Internal class function, used to update widget in certain conditions  """
    
    def insert(self, wid, mode, x, y):
        if mode == "grid" or mode == "place":
            self._widgets.append([wid, x, y])
            
            if self._drawmode == None:
                self._drawmode = mode
        else:
            raise "Invalid draw mode"

#Class defining a popup menu
class PopupMenu(Widget):
    pass

#Class defining a screen
class Screen():
    """
    A object of the class screen is the set of widgets part of a screen
    
    Exemple:
        Main Menu  ====  Button(New game), Button(Load Game), Button(Quit)
    
    dis = display instance of screen
    distx = distance between widgets in x
    disty = distance between widgers in y
    """
    def __init__(self, name = "", dis = None, distx = 10, disty = 10):
        self._name = name 
        self.dis = dis
        self.dist_x = dist_x
        self.dist_y = dist_y
        self._widgets = []
        self.wid_dict = {"N" : {"W": [], "C" : [], "E" : []},
                         "C" : {"W": [], "C" : [], "E" : []},
                         "S" : {"W": [], "C" : [], "E" : []}}
    
    #Function to add a widget to screen
    def add_widget(self, wid):
        if type(wid) == type(list()):
            for w in wid:
                if issubclass(type(w), Widget):
                    self._widgets.append(wid)
        elif issubclass(type(wid), Widget):
            self._widgets.append(wid)
        else:
            raise "Invalid Widget (widget class must be subclass of Widget"

    #Function to pop a widget
    def pop_widget(self, wid):
        for w in self._widgets:
            if w == wid:
                self._widgets.remove(wid)
        else:
            raise "Widget not found"

    #Function to change a specific widget position 
    def widget_position(self, wid, posx, posy):
        """ Function used to set position of widget """
        for w in self._widgets:
            if wid == w:
                wid.position(posx, posy)

    #Function to update and define the widgets position
    def upd_wids_positions(self):
        self.wid_dict = {"N" : {"W": [], "C" : [], "E" : []},
                         "C" : {"W": [], "C" : [], "E" : []},
                         "S" : {"W": [], "C" : [], "E" : []}}    

        for widget in self._widgets:
            self.wid_dict[self._anchorx][self._anchory].append(widget)

        for anchor_x in self.wid_dict.keys():
            for anchor_y in self.wid_dict[anchor_x].keys():
                for widget in self.wid_dict[anchor_x][anchor_y]:
                    for wid in self.wid_dict[anchor_x][anchor_y]:
                        if widget == wid:
                            pass
                        elif widget.get_attr("posy") == widget.get_attr("posy") and widget.get_attr("posx") == widget.get_attr("posx"):
                            raise "Two widgets with same position"

    def upd_wids_coordinates(self):
        for x in self.wid_dict.keys():
            for y in self.wid_dict[x].keys():
                t_wid = len(wid_dict[x][y])
                
                t_dist_x, t_dist_y = self.distx, self.disty
                max_x, max_y = 0, 0

                for wid in self.wid_dict[x][y]:
                    max_x = max(wid.get_attr('posx'), max_x)
                    max_y = max(wid.get_attr('posy'), max_y)

                for i in range(max_x):
                    for j in range(max_y):
                        for wid in self.wid_dict[x][y]:
                            if wid.get_attr("posx") == i and wid.get_attr("posy"):
                                t_dist_x += wid.get_attr("width") + self.distx
                                t_dist_y += wid.get_attr("heigth") + self.disty

                            

def change_resolution(reso):
    if reso == "1600x900":
        cf.ACT_DISPLAY_X = 1600
        cf.ACT_DISPLAY_Y = 900
    elif reso == "1366x728":
        cf.ACT_DISPLAY_X = 1366
        cf.ACT_DISPLAY_Y = 728
    elif reso == "1280x720":
        cf.ACT_DISPLAY_X = 1280
        cf.ACT_DISPLAY_Y = 720       

#Function to change camera position
def scroll_camera(scr_x, scr_y, scr_z, mode):
    if mode == "inc":
        gv.CAM_X += scr_x
        gv.CAM_Y += scr_y
        gv.CAM_Z += scr_z
    elif mode == "set":
        gv.CAM_X = scr_x
        gv.CAM_Y = scr_y
        gv.CAM_Z = scr_z

    if gv.CAM_Z > 10:
            gv.CAM_Z = 10
    elif gv.CAM_Z < 0:
        gv.CAM_Z = 0    

    if gv.CAM_X > (len(gv.TILE_MAP) * (40 - gv.CAM_Z)) - cf.MAX_DISPLAY_X:
        gv.CAM_X = (len(gv.TILE_MAP) * (40 - gv.CAM_Z)) - cf.MAX_DISPLAY_X
    elif gv.CAM_X < 0:
        gv.CAM_X = 0

    if gv.CAM_Y > (len(gv.TILE_MAP[0]) * (40 - gv.CAM_Z)) - cf.MAX_DISPLAY_Y:
        gv.CAM_Y = (len(gv.TILE_MAP[0]) * (40 - gv.CAM_Z)) - cf.MAX_DISPLAY_Y
    elif gv.CAM_Y < 0:
        gv.CAM_Y = 0

#List of lambda functions
bool_inv = lambda x: not x