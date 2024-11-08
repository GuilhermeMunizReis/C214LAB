"""
NAME 
    gamelib 

VERSION
    0.6.1

DATE
    28/07/2023 - 22/04/2024

AUTHOR
    Guilherme Muniz de Oliveira Reis

DESCRIPTION
    Game module for Python
    ======================

    gamelib is a python module used as an implementation 
    for pygame, implementing widgets for coding games.
    
CLASSES
   Screen, Button, Textbox, Label, Icon, AnimatedIcon, Sprite, AnimatedSprite, Mixer, Sound.
"""
VERSION = "0.6.1"

import pygame

pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont("Verdana", 20)
pygame.key.set_repeat(500,35)

class Widget:
    def __init__(self, surf = None, text = "", width = 0, height = 0, resizable=False, background = (255,255,255), textcolor = (0,0,0), img = None, x = 0, y = 0, filled = "full", overcolor=None, font = FONT):
        self._surf = surf                   # Surface where widget will be draw
        self._text = text   
        self._width = width
        self._height = height
        self._resizable = resizable         # True=Widget is resizable  False=Widget not resizable
        self._background = background       # Background color
        self._overcolor = background if overcolor == None else overcolor         # Color assumed by widget when mouse is over
        self._textcolor = textcolor
        self._textrender = None             # Object of render, which is writen the text stored in _text
        self._textrender_width = None
        self._textrender_height = None
        self._img = img                     # If different of None, background will render image contained in here
        self._font = font
        self._x = x
        self._y = y
        self._filled = filled
        self._is_over = False
        self._bwidth = width                # Base width
        self._bheight = height              # Base height
        #bx and by are x and y declared when object was created
        self._bx = x
        self._by = y

        if width == 0 or height == 0:
            self._textrender = self._font.render(self._text, True, self._textcolor)
            self._bwidth = self._textrender.get_width()
            self._bheight = self._textrender.get_height()
        
        self.name = ""
            
        self._update()

    def draw(self):
        """  Method to draw widget  """
        if self._is_over == True and self._overcolor != None and self._img == None:
            color = self._overcolor
        else:
            color = self._background

        if self._img == None:
            if self._filled == "full":
                pygame.draw.rect(self._surf, color, (self._x, self._y, self._width, self._height), 0)
            elif self._filled == "border":
                pygame.draw.rect(self._surf, color, (self._x, self._y, self._width, self._height), 2)
            elif self._filled == "void":
                pygame.draw.rect(self._surf, color, (self._x, self._y, self._width, self._height), -1)
        else:
            if self._img.get_width() > self._width or self._img.get_height() > self._height:
                img = pygame.transform.scale(self._img, (self._img.get_width(), self._img.get_height())) 
                self._surf.blit(img, (self._x, self._y))
            else:
                self._surf.blit(self.img, (self._x, self._y))
        
        if self._textrender != None:
            # Textrender on center of widget
            x = self._x + (self._width - self._textrender_width)/2
            y = self._y + (self._height - self._textrender_height)/2
            self._surf.blit(self._textrender, (x, y))        
  
    def check_mouse(self, pos, events:list = []):
        """ Check if mouse is over the widget, using a tuple as a parameter for mouse position """
        if pos[0] >= self._x and pos[0] <= self._x + self._width and pos[1] >= self._y and pos[1] <= self._y + self._height:
            self._is_over = True
        else:
            self._is_over = False

    def set_position(self, x: int | None=None, y: int | None=None):
        """ Set new coordinates position of widget"""
        if x != None:
            self._x = x
        if y != None:
            self._y = y        

    def _update(self):
        """  Internal class function, used to update widget in certain conditions  """
        # Verify if there is a text to be rendered
        if self._text != None:
            self._textrender = self._font.render(self._text, True, self._textcolor)
        
        # Verify if widget can be resized or not and sets the correct size    
        if self._resizable and self._textrender != None:
            self._width = max(self._width, self._textrender.get_width())
            self._height = max(self._height, self._textrender.get_height())
        else:
            self._width = self._bwidth
            self._height = self._bheight
        
        # Transform text render to correct size         
        if self._textrender != None and not self._resizable and (self._textrender.get_height() > self._height or self._textrender.get_width() > self._width):
            self._textrender = pygame.transform.scale(self._textrender, (self._bwidth, self._bheight))
            
        self._textrender_width = self._textrender.get_width()
        self._textrender_height = self._textrender.get_height()
                    
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

        self._update()
        
    def set_width(self, width):
        self._width = width
        
    def set_height(self, height):
        self._height = height
        
    def set_surf(self, surf:pygame.Surface):
        self._surf = surf
        self._update()
        
    def set_text(self, text:str):
        self._text = text
        self._update()

    def get_surf(self):
        return self._surf
    
    def set_resizable(self, value:bool=False):
        self._resizable = value 
        self._update()

    def get_type(self):
        return type(self).__name__

    def get_dimensions(self):
        """ Return widget position
        (X, Y, WIDTH, HEIGHT)
        """
        return self._x, self._y, self._width, self._height

class Label(Widget):
    def __init__(self, surf=None, text = "", width = 0, height = 0, resizable=False, background = (255,255,255), textcolor = (0,0,0), img = None, x = 0, y = 0, filled = "full", overcolor=None, font = FONT):
        super().__init__(surf, text, width, height, resizable, background, textcolor, img, x, y, filled, overcolor, font)
        super().draw
        super().check_mouse
        super().set_position
        super()._update
        super().get_attr
        super().config
        super().get_type
        super().set_width
        super().set_height
        super().set_text
        
        name = ""

class Bar(Widget):
    def __init__(self, surf=None, name = "",text = "", width = 0, height = 0, resizable=False, background = (255,255,255), textcolor = (0,0,0), img = None, x = 0, y = 0, filled = "full", overcolor=None, font = FONT):
        super().__init__(surf, text, width, height, resizable, background, textcolor, img, x, y, filled, overcolor, font)
        super().draw
        super().check_mouse
        super().set_position
        super()._update
        super().get_attr
        super().config
        super().get_type
        super().set_width
        super().set_height

        self.name = name
        self.cont = 0
        self.limit = 0
        
    def set_name(self, name:str=""):
        self.name = name

    def bar_check(self):
        if self.cont == self.limit:
            return True
    
    def add_cont(self):
        self.cont+=1
        
        if self.cont > 50:
            self.cont = 0

class Button(Widget):
    def __init__(self, surf=None, text="", width=0, height=0, resizable=False, background=(255,255,255), textcolor = (0,0,0), img = None, x = 0, y = 0, filled = "full", overcolor=None, font = FONT, command = None):
        super().__init__(surf, text, width, height, resizable, background, textcolor, img, x, y, filled, overcolor, font)
        super().draw
        super().check_mouse
        super().set_position
        super()._update
        super().get_attr
        super().config
        super().get_type
        
        self.command = command              # Function called when the mouse clicks on button
    
    def check_mouse(self, pos, events):
        super().check_mouse(pos, events)
        
        if events == []:
            return
        for event in events: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_left, _, _ = pygame.mouse.get_pressed()

                if mouse_left and self._is_over and self.command != None:
                    self.command()
               
class Textbox(Widget):
    def __init__(self, surf = None, text = "", width = 0, height = 0, resizable=False,background = (255,255,255), textcolor = (0,0,0), img = None, x = 0, y = 0, filled = "full", overcolor=None, font = FONT):
        super().__init__(surf, text, width, height, resizable, background, textcolor, img, x, y, filled, overcolor, font)
        super().check_mouse
        super().set_position
        super()._update
        super().get_attr
        super().config
        super().get_type
        
        self._active = False                # True = Widget selected by user    False = Not selected
    
    def draw(self):
        """  Method to draw widget  """
        if self._active == True and self._overcolor != None and self._img == None:
            color = self._overcolor
        else:
            color = self._background

        if self._img == None:
            if self._filled == "full":
                pygame.draw.rect(self._surf, color, (self._x, self._y, self._width, self._height), 0)
            elif self._filled == "border":
                pygame.draw.rect(self._surf, color, (self._x, self._y, self._width, self._height), 2)
            elif self._filled == "void":
                pygame.draw.rect(self._surf, color, (self._x, self._y, self._width, self._height), -1)
        else:
            if self._img.get_width() > self._width or self._img.get_height() > self._height:
                img = pygame.transform.scale(self._img, (self._img.get_width(), self._img.get_height())) 
                self._surf.blit(img, (self._x, self._y))
            else:
                self._surf.blit(self.img, (self._x, self._y))
        
        if self._textrender != None:            # Textrender on center of widget
            x = self._x + (self._width - self._textrender_width)/2
            y = self._y + (self._height - self._textrender_height)/2
            self._surf.blit(self._textrender, (x, y))        
      
    
    def check_mouse(self, pos, events):
        super().check_mouse(pos, events)
        
        if events == []:
            return
        for event in events: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_left, _, _ = pygame.mouse.get_pressed()

                if mouse_left and self._is_over:
                    self._active = True
                elif mouse_left and not self._is_over:
                    self._active = False                
            elif event.type == pygame.TEXTINPUT and self._active:
                self._text += event.text
                self._update()
            elif event.type == pygame.KEYDOWN and self._active:
                if event.key == pygame.K_BACKSPACE and self._text != "":
                    self._text = self._text[:-1]
                elif event.key == pygame.K_BACKSPACE and self._text == "":
                    self._text = ""

                self._update()
            
class Icon(Widget):
    def __init__(self, surf:pygame.SurfaceType=None, x:int=0, y:int=0, image:pygame.SurfaceType=None, height:int=0, width:int=0, command=None, resizable:bool=False):
        super().set_position
        super().get_attr
        super().config
        super().set_surf
        super().get_type
        super().get_dimensions

        self._surf = surf
        self._image = image
        self._x = x
        self._y = y
        self._bx = x
        self._by = y
        self._height = height
        self._width = width
        self._bheight = height
        self._bwidth = width
        self.command = command
        self._resizable = resizable
        
        self._is_over = False
        self._active = False
               
        self._update()
        
    def draw(self):
        """  Method to draw icon  """
        if self._image == None:
            pass
        else:
            self._surf.blit(self._image, (self._x, self._y))
            
    def check_mouse(self, pos, events):
        super().check_mouse(pos, events)
        
        if events == []:
            return
        for event in events: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_left, _, _ = pygame.mouse.get_pressed()

                if mouse_left and self._is_over and self.command != None:
                    self.command()   
                    self._active = True
                elif mouse_left and not self._is_over:
                    self._active = False                 

    def _update(self):
        """  Internal class function, used to update widget in certain conditions  """        
        # Verify if widget can be resized or not and sets the correct size    
        if self._bwidth == 0 and self._bheight == 0 and self._image != None:
            self._bwidth = self._image.get_width()
            self._bheight = self._image.get_height()
            self._width = self._image.get_width()
            self._height = self._image.get_height()
        else:
            pygame.transform.scale(self._image, (self._width, self._height)) 
        
        if self._resizable and self._image != None:
            self._width = max(self._bwidth, self._image.get_width())
            self._height = max(self._bheight, self._image.get_height())
            pygame.transform.scale(self._image, (self._width, self._height), self._image)
        else:
            self._width = self._bwidth
            self._height = self._bheight
            
class AnimatedIcon(Icon):
    def __init__(self, surf:pygame.SurfaceType=None, x:int=0, y:int=0, image:pygame.SurfaceType=None, height:int=0, width:int=0, command=None, resizable:bool=False, image_list:list=[], framerate:int=None):
        super().__init__(surf, x, y, image, height, width, command, resizable)
        super().set_position
        super().get_attr
        super().config
        super().set_surf
        super().get_surf
        super().get_type
        super().get_dimensions

        self._image_list = image_list
        self._image_list_size = len(self._image_list)
        self._current_index = 0                         # Current image index
        self._current_tick = 0                          # Current tick for next animation image
        self._framerate = framerate                     # Quantity of animation frames drawn in a second
        self._tickrate = 1                              # Quantity of ticks per second of screen     
        self._UPDATE_TICK = Game.get_custom_event()     # Get UPDATE_TICK event from Game class
       
    def draw(self):
        """  Method to draw icon  """
        if self._image_list == None:
            if self._image == None:
                pass
            else:
                self._surf.blit(self._image, (self._x, self._y))            
        else:
            self._surf.blit(self._image_list[self._current_index], (self._x, self._y)) 
            
    def check_mouse(self, pos, events):
        super().check_mouse(pos, events)
        
        if events == []:
            return
        for event in events: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_left, _, _ = pygame.mouse.get_pressed()

                if mouse_left and self._is_over:
                    self.command()
                    self._active = True
                elif mouse_left and not self._is_over:
                    self._active = False                    
            elif event.type == self._UPDATE_TICK:                   # This sets animation process
                self.update_tick()
    
    def update_tick(self):
        self._current_tick += 1
            
        if self._current_tick >= self._tickrate / self._framerate:
            self._current_index += 1
            self._current_tick = 0
            
            if self._current_index > self._image_list_size - 1:
                self._current_index = 0
        
    def _update(self):
        """  Internal class function, used to update widget in certain conditions  """        
        # Verify if widget can be resized or not and sets the correct size    
        if self._resizable and self._image != None:
            self._width = max(self._bwidth, self._image.get_width())
            self._height = max(self._bheight, self._image.get_height())
            pygame.transform.scale(self._image, (self._width, self._height), self._image)
        else:
            self._width = self._bwidth
            self._height = self._bheight
     
    def set_tickrate(self, tickrate:int):
        self._tickrate = tickrate
        
    def set_image_list(self, image_list:list):
        self._image_list = image_list
        self._image_list_size = len(image_list)   
     
    def set_width(self, width):
        super().set_width(width)
        
        for image in self._image_list:
            image = pygame.transform.scale(image, (width, self._height))

    
    def set_height(self, height):
        super().set_height(height)
        
        for image in self._image_list:
            image = pygame.transform.scale(image, (self._width, height))  
        
class Sprite(Widget):
    def __init__(self, surf:pygame.SurfaceType=None, x:int=0, y:int=0, image:pygame.SurfaceType=None, height:int=0, width:int=0, resizable:bool=False):
        super().set_position
        super().get_attr
        super().config
        super().set_surf
        super().get_type
        super().get_dimensions

        self._surf = surf
        self._image = image
        self._x = x
        self._y = y
        self._bx = x
        self._by = y
        self._height = height
        self._width = width
        self._bheight = height
        self._bwidth = width
        self._resizable = resizable
        
        self._is_over = False
        self._active = False
               
        self._update()
        
    def draw(self):
        """  Method to draw icon  """
        if self._image == None:
            pass
        else:
            self._surf.blit(self._image, (self._x, self._y))
            
    def check_mouse(self, pos, events):
        super().check_mouse(pos, events)
        
        if events == []:
            return
        for event in events: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_left, _, _ = pygame.mouse.get_pressed()

                if mouse_left and self._is_over:
                    self._active = True
                elif mouse_left and not self._is_over:
                    self._active = False                   

    def _update(self):
        """  Internal class function, used to update widget in certain conditions  """        
        # Verify if widget can be resized or not and sets the correct size    
        if self._bwidth == 0 and self._bheight == 0 and self._image != None:
            self._bwidth = self._image.get_width()
            self._bheight = self._image.get_height()
            self._width = self._image.get_width()
            self._height = self._image.get_height()
        else:
            pygame.transform.scale(self._image, (self._width, self._height), self._image) 
        
        if self._resizable and self._image != None:
            self._width = max(self._bwidth, self._image.get_width())
            self._height = max(self._bheight, self._image.get_height())
            pygame.transform.scale(self._image, (self._width, self._height), self._image)
        else:
            self._width = self._bwidth
            self._height = self._bheight

class AnimatedSprite(Sprite):
    def __init__(self, surf:pygame.SurfaceType=None, x:int=0, y:int=0, image:pygame.SurfaceType=None, height:int=0, width:int=0, resizable:bool=False, image_list:list=[], framerate:int=None):
        super().__init__(surf, x, y, image, height, width, resizable)
        super().set_position
        super().get_attr
        super().config
        super().set_surf
        super().get_type
        super().get_dimensions

        self._image_list = image_list
        self._image_list_size = len(self._image_list)
        self._current_index = 0                         # Current image index
        self._current_tick = 0                          # Current tick for next animation image
        self._framerate = framerate                     # Quantity of animation frames drawn in a second
        self._tickrate = 1                              # Quantity of ticks per second of screen     
        self._UPDATE_TICK = Game.get_custom_event()     # Get UPDATE_TICK event from Game class
       
    def draw(self):
        """  Method to draw icon  """
        if self._image_list == None:
            if self._image == None:
                pass
            else:
                self._surf.blit(self._image, (self._x, self._y))            
        else:
            self._surf.blit(self._image_list[self._current_index], (self._x, self._y)) 
            
    def check_mouse(self, pos, events):
        super().check_mouse(pos, events)
        
        if events == []:
            return
        for event in events: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_left, _, _ = pygame.mouse.get_pressed()

                if mouse_left and self._is_over:
                     self._active = True
                elif mouse_left and not self._is_over:
                    self._active = False                    
            elif event.type == self._UPDATE_TICK:                   # This sets animation process
                self._current_tick += 1
                
                if self._current_tick >= self._tickrate / self._framerate:
                    self._current_index += 1
                    self._current_tick = 0
                    
                    if self._current_index > self._image_list_size - 1:
                        self._current_index = 0    
        
    def _update(self):
        """  Internal class function, used to update widget in certain conditions  """        
        # Verify if widget can be resized or not and sets the correct size    
        if self._resizable and self._image != None:
            self._width = max(self._bwidth, self._image.get_width())
            self._height = max(self._bheight, self._image.get_height())
            pygame.transform.scale(self._image, (self._width, self._height), self._image)
        else:
            self._width = self._bwidth
            self._height = self._bheight
     
    def set_tickrate(self, tickrate:int):
        self._tickrate = tickrate 
    
    def set_image_list(self, image_list:list):
        self._image_list = image_list
        self._image_list_size = len(image_list)   
        
class Sound():
    sounds_cont = 0
    
    def __init__(self, sound=None, sound_name:str=None, volume:int=0, run:bool=False):
        type(self).sounds_cont += 1
        self._sound = sound
        self._volume = volume
        self._run = run
        
    def __del__(self):
        type(self).sounds_cont -= 1
    
    def start(self):
        self._run = True
        self._sound.start()
        
    def stop(self):
        self._run = False
        self._sound.stop()
    
    def pause(self):
        self._sound.pause()
    
    def unpause(self):
        self._sound.unpause()
    
    def set_volume(self, volume:int):
        self._sound.set_volume(volume)
    
    def fadeout(self, ms:int=1000):
        self._sound.fadeout(ms)
    
    def set_sound(self, sound):
        self._sound = sound
    
    def get_sound(self):
        return self._sound    
        
class Mixer():
    def __init__(self, sound_list:list=[], run=False):
        self._sound_list = sound_list
        self._run = run
    
    def start(self):
        self._run = True
        
    def stop(self):
        self._run = False
        
class Screen():
    def __init__(self, display:pygame.Surface=None):
        self._display = display
        self._tickrate = 0
        self._widget_list = []

    def add(self, wid:Widget=None):
        """
        DESCRIPTION 
            Adds an widget to screen object.
        ARGS
            wid (Widget) => Widget to be add in widget's list
        """
        wid.set_surf(self._display)
        
        try:
            wid.set_tickrate(self._tickrate)
        except:
            pass
        
        self._widget_list.append(wid)

    def remove(self, wid:Widget=None):
        """
        DESCRIPTION 
            Removes an widget to screen object.
        ARGS
            wid (Widget) => Widget to be removed from widget's list
        """
        self._widget_list.remove(wid)
        
    def clear(self):
        """
        DESCRIPTION 
            Remove all widgets in list.
        """
        for widget in self._widget_list:
            self._widget_list.remove(widget)
    
    def get_all_widgets(self):
        """
        DESCRIPTION 
            Return every widget on list.
        """    
        for widget in self._widget_list:
            yield self._widget_list.remove(widget)
    
    def set_surface(self, surf:pygame.Surface):
        for wid in self._widget_list:
            wid.set_surf(surf)
    
    def set_tickrate(self, tickrate:int):
        self._tickrate = tickrate
        
        for wid in self._widget_list:
            try:
                wid.set_tickrate(tickrate)
            except:
                pass
            
    def set_command(self, obj:Button, command):
        self._widget_list[obj].command=command
            
class Game():
    """
        Class for creating an instance of the game. This object is responsable for loading informations 
        to build the screen, in addition of manipulating a few things.
    PARAMETERS
        screen (Screen) => Screen containing every widget on itself
        framerate (int) => Value of FPS displayed 
        resolution (tuple(int, int)) => Resolution of game screen
        tickrate (int) => Value of how many ticks occurs on a second
    """
    _UPDATE_TICK = None
    
    def __init__(self, screen:Screen = Screen(), framerate: int = 30, resolution: tuple = (160,90), tickrate: int = 10):
        self._display = None
        self._screen = screen
        self._framerate = framerate
        self._base_resolution = resolution      # Resolution that game is made
        self.resized_resolution = resolution    # Resizes resolution
        self._tickrate = tickrate               # Ticks per second
        self.running = False                   # Contains flag to keep running the game
                      
        # Setting ticks as 10 per second
        self._clock = pygame.time.Clock()
        self._clock.tick(self._framerate)
        self._UPDATE_TICK = pygame.event.custom_type()                  # Create a custom type of event
        type(self)._UPDATE_TICK = self._UPDATE_TICK
        pygame.time.set_timer(self._UPDATE_TICK, int(1000/tickrate))         # Set to generate an event on time wished
        
        self._TICK = 0
        self._BIG_TICK = 0
        self._BACKGROUND = (70,70,255)        
        
        # Variables storing user inputs
        self.pressed_keys = []               # Store all keys pressed on keyboard in last instant
        self.mouse_button_pressed = []       # Store all butons pressed on mouse in last instant
        
        # Setting caption
        pygame.display.set_caption("gamelib dev %s \tFPS: %d" % (VERSION, self._clock.get_fps()))       
        
        self.fps = []
    
    def start(self):
        """
        DESCRIPTION 
            Verifies if is everything ready for starting the game, then begin running it    
        """ 
        self._display = pygame.display.set_mode(self._base_resolution)
        self._screen.set_surface(self._display)
        self.running = True
        self._run()
    
    def _run(self):
        """
            Starts running the game
        """
        while self.running:
            click = False                # Sinaliza que algum botão do mouse foi pressionado 
            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    self._close_game()
                    return
                else:
                    self._event_handler(event)    
            
            self._display.fill(self._BACKGROUND)
            pos = pygame.mouse.get_pos()
    
            for wid in self._screen._widget_list:
                if type(wid) == type(Label):
                    wid.config("height", 20*self._TICK)
                
                wid.check_mouse(pos, events)
                wid.draw()
                if click == True and wid._is_over == True:
                    wid.command()
                elif click == True and wid.get_type() == "TextBox" and wid._is_over == False:
                    wid.active = False

            self._clock.tick(self._framerate)
            pygame.display.update() 
    
    def _event_handler(self, event):
        """ 
            This method is responsable for treating every event generated by user input or game processing. 
        PARAMETERS
            event (Event): contains type of generated event
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            # | pygame.MOUSEBUTTONUP 
            self.mouse_button_pressed.append([event.button])
        elif event.type == pygame.KEYDOWN:
            self.keys_pressed.append([event.key])
        elif event.type == self._UPDATE_TICK:
            self.mouse_button_pressed = []
            self.keys_pressed = []
            self.update_tick()          
        
    def update_tick(self):
        self._TICK
        self._BIG_TICK

        self._TICK += 1

        if self._TICK == 10:
            #capt = "gamelib dev %s \tFPS: %d" % (VERSION, self._clock.get_fps())  
            self._BIG_TICK += 1
            self._TICK = 0
            
        #pygame.event.post(GAME_TICK)        

    def _close_game(self):
        self.running = False
        pygame.quit()

    def get_screen(self):
        return self._display       
    
    def set_screen(self, screen:Screen):
        if screen == None:
            pass
        else:
            self._screen = screen
            self._screen.set_tickrate(self._tickrate)
            self._screen.set_surface(self._display)

    @classmethod
    def get_custom_event(self):
        """ Returns update tick event """
        return self._UPDATE_TICK
