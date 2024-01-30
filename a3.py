import tkinter as tk
# from tkinter import _Cursor, _Relief, _ScreenUnits, _TakeFocusValue, Misc, filedialog # For masters task
from typing import Any, Callable, Union, Optional
from typing_extensions import Literal
from a3_support import *
from model import *
from constants import *

# Implement your classes here


class InfoBar(AbstractGrid):
    SIZE = (700,90)
    DIMENSIONS = (2,3)
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, self.DIMENSIONS, self.SIZE, **kwargs)
        self.master = master

        
        
        self._farmmodel = FarmModel('maps/map1.txt')
        self._player = Player()
        self.annotate_position((0,0), text="Day:", font=HEADING_FONT)
        self.annotate_position((0,1), text="Money:", font=HEADING_FONT)
        self.annotate_position((0,2), text="Energy:", font=HEADING_FONT)
        self.annotate_position((1,0), text=self._farmmodel.get_days_elapsed(), font=HEADING_FONT)
        self.annotate_position((1,1), text='$'+str(self._player.get_money()), font=HEADING_FONT)
        self.annotate_position((1,2), text=str(self._player.get_energy()), font=HEADING_FONT)
        self.pack(side=tk.BOTTOM, fill=tk.X)

    def redraw(self, day: int, money: int, energy: int) -> None:
        self.clear()
        
        self.annotate_position((1,0), text=day, font=HEADING_FONT)
        self.annotate_position((1,1), text=money, font=HEADING_FONT)
        self.annotate_position((1,2), text=energy, font=HEADING_FONT)

# class FarmView(AbstractGrid):
#    def __init__(self, master: tk.Tk | tk.Frame, dimensions: tuple[int, int], size: tuple[int, int], **kwargs):
#        super().__init__
#        self.master = master
#        self.size = size
#        self.dimensions = dimensions
#        self.image = IMAGES
#        self.image_cache =[]
#        self.Farmview = AbstractGrid(master, (10,10),(FARM_WIDTH, FARM_WIDTH))
#        self.Farmview.pack(side=tk.LEFT)
#        self.map = read_map('maps/map1.txt')
#        for i, line in enumerate(map):
#            for j, char in enumerate(line):
#                 x = j*int(FARM_WIDTH/10) + int(FARM_WIDTH/10)/2
#                 y = i*int(FARM_WIDTH/10)
#                 tile_img = get_image('images/' + IMAGES[char], (int(FARM_WIDTH/10), int(FARM_WIDTH/10)))
#                 self.image_cache.append(tile_img)
#                 self.Farmview.create_image(x, y, image =self.image_cache[-1])


#    def redraw(self, ground: list[str], plants: dict[tuple[int, int], 
#                                                    'Plant'], player_position: tuple[int, int], player_direction: str) -> None:
#        self.clear()
#        for row_num, row in enumerate(self.map):
#            for col_num, col in enumerate(row):
#                position = (row_num, col_num)
#                min_max_coords = self.get_bbox(position)
#                self.create_rectangle(min_max_coords)
#                if col is not None:
#                    size= self.get_cell_size()
#                    image_name = plants[col].get_name()
#                    image = get_image(image_name, size, self.image_cache)
#                    midpoint = self.get_midpoint((row_num, col_num))
#                    self.create_image(midpoint, image=image)

#        player_img = get_image('images/' + IMAGES[player_direction], (int(FARM_WIDTH/10), int(FARM_WIDTH/10)))
#        x, y = player_position
#        self.Farmview.create_image(x, y, image =player_img)
#        for plant in plants:
#            plant_img = get_plant_image_name(plant[1])
#            self.Farmview.create_image(plant[0][0],plant[0][1], image= plant_img)

class ItemView(tk.Frame):
    def __init__(self, master: tk.Frame, item_name: str, amount: int, 
                 select_command: Optional[Callable[[str], None]] = None, 
                 sell_command: Optional[Callable[[str], None]] = None, 
                 buy_command: Optional[Callable[[str], None]] = None) -> None:
        pass
def play_game(root: tk.Tk, map_file: str) -> None:
    # Implement your play_game function here
    map_file =read_map('maps/map1.txt')

    



def main() -> None:
# Implement your main function here
    root = tk.Tk()
    root.geometry("710x720")
    root.title('Farm Game') 
    

    header_img= get_image('images/header.png',(FARM_WIDTH+INVENTORY_WIDTH,BANNER_HEIGHT))
    lable_header=tk.Label(image=header_img)
    lable_header.pack(side=tk.TOP, anchor=tk.N,padx=5)
   
    farmmodel = FarmModel('maps/map1.txt')
    button= tk.Button(root,text='Next day',command=farmmodel.new_day)
    button.pack(side=tk.BOTTOM)
    
    # info_bar = AbstractGrid(root,(2,3), (FARM_WIDTH+INVENTORY_WIDTH, INFO_BAR_HEIGHT))
    info = InfoBar(root,(2,3), (FARM_WIDTH+INVENTORY_WIDTH, INFO_BAR_HEIGHT))
    
    # Farmview = AbstractGrid(root, (10,10),(FARM_WIDTH, FARM_WIDTH), bg ='red')
    # Farmview.pack(side=tk.LEFT)
    # farm = FarmView(root, (10,10),(FARM_WIDTH, FARM_WIDTH))
    
    
    # Farm_view = FarmView(root, (10,10),(FARM_WIDTH, FARM_WIDTH))


   


    play_game(root, 'maps/map1.txt')

    root.mainloop()

if __name__ == '__main__':
    main()
