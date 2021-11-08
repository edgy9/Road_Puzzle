from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivy.config import Config
import os
import sys
import time


import random

#from other.main import update_path

Config.set('graphics', 'resizable', False)

Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '860')

#from other.main import input_value
#class mainwidget(Widget):
   # pass
input_value = [1]

input_value = [1]

def numbertoletter(number):
    alphabet = {
        1:'a',
        2:'b',
        3:'c',
        4:'d',
        5:'e',
        6:'f',
        7:'g',
        8:'h',
        9:'i',
        10:'j',
        11:'k',
        12:'l',
        13:'m',
        14:'n',
        15:'o',
        16:'p',
        17:'q',
        18:'r',
        19:'s',
        20:'t',
        21:'u',
        22:'v',
        23:'w',
        24:'x',
        25:'y',
    }
    
    #print(number)
    letter = alphabet[number]
    #letter = alphabet.get(number, default = None)
    #print(letter)
    return letter
def find_direction(key):
    find_direction = {
        'ab':'arbl',
        'af':'adfu',
        'bc':'brcl',
        'cd':'crdl',
        'bg':'bdgu',
        'ch':'cdhu',
        'di':'ddiu',
        'de':'drel',
        'ej':'edju',
        'fg':'frgl',
        'gh':'grhl',
        'hi':'hril',
        'fk':'fdku',
        'gl':'gdlu',
        'hm':'hdmu',
        'ij':'irjl',
        'jo':'jdou',
        'kl':'krll',
        'kp':'kdpu',
        'lm':'lrml',
        'mn':'mrnl',
        'no':'nrol',
        'lq':'ldqu',
        'in':'idnu',
        'ns':'ndsu',
        'mr':'mdru',
        'pq':'prql',
        'rs':'rrsl',
        'ot':'odtu',
        'pu':'pduu',
        'qv':'qdvu',
        'st':'srtl',
        'sx':'sdxu',
        'rw':'rdwu',
        'ty':'tdyu',
        'qr':'qrrl',
        'vw':'vrwl',
        'uv':'urvl',
        'wx':'wrxl',
        'xy':'xryl',
        'ba':'arbl',
        'fa':'adfu',
        'cb':'brcl',
        'dc':'crdl',
        'gb':'bdgu',
        'hc':'cdhu',
        'id':'ddiu',
        'ed':'drel',
        'je':'edju',
        'gf':'frgl',
        'hg':'grhl',
        'ih':'hril',
        'kf':'fdku',
        'lg':'gdlu',
        'mh':'hdmu',
        'ji':'irjl',
        'oj':'jdou',
        'lk':'krll',
        'pk':'kdpu',
        'ml':'lrml',
        'nm':'mrnl',
        'on':'nrol',
        'ql':'ldqu',
        'ni':'idnu',
        'sn':'ndsu',
        'rm':'mdru',
        'qp':'prql',
        'sr':'rrsl',
        'to':'odtu',
        'up':'pduu',
        'vq':'qdvu',
        'ts':'srtl',
        'xs':'sdxu',
        'wr':'rdwu',
        'yt':'tdyu',
        'rq':'qrrl',
        'wv':'vrwl',
        'vu':'urvl',
        'xw':'wrxl',
        'yx':'xryl'   
    }
    value = find_direction[key]
    return value
speed_of_edges = {
    'arbl':'',
    'adfu':'',
    'brcl':'',
    'crdl':'',
    'bdgu':'',
    'cdhu':'',
    'ddiu':'',
    'drel':'',
    'edju':'',
    'frgl':'',
    'grhl':'',
    'hril':'',
    'fdku':'',
    'gdlu':'',
    'hdmu':'',
    'irjl':'',
    'jdou':'',
    'krll':'',
    'kdpu':'',
    'lrml':'',
    'mrnl':'',
    'nrol':'',
    'ldqu':'',
    'idnu':'',
    'ndsu':'',
    'mdru':'',
    'prql':'',
    'rrsl':'',
    'odtu':'',
    'pduu':'',
    'qdvu':'',
    'srtl':'',
    'sdxu':'',
    'rdwu':'',
    'tdyu':'',
    'qrrl':'',
    'vrwl':'',
    'urvl':'',
    'wrxl':'',
    'xryl':''  
}

edges = {
    1: [2, 6], 
    2: [1, 3, 7], 
    3: [2, 4, 8], 
    4: [3, 5, 9],
    5: [4, 10], 
    6: [1, 7, 11], 
    7: [2, 6, 8, 12], 
    8: [3, 7, 9, 13], 
    9: [4, 8, 14, 10], 
    10: [5, 15, 9], 
    11: [6, 12, 16], 
    12: [7, 11, 13, 17], 
    13: [8, 12, 14, 18], 
    14: [9, 13, 15, 19], 
    15: [10, 14, 20], 
    16: [11, 17, 21], 
    17: [12, 16, 18, 22], 
    18: [13, 17, 19, 23], 
    19: [14, 18, 20, 24], 
    20: [15, 19, 25], 
    21: [16, 22], 
    22: [17, 21, 23], 
    23: [18, 22, 24], 
    24: [19, 23, 25], 
    25: [20, 24]
    }


def listToString(s): 

    str1 = "" 
    #print(s)
    value = (str1.join(s))
    #print(value)
    return value



        

def check_if_value_is_touching(value,self):    
    global input_value
    #print(input_value)
    #print(value)
    contains_value = 0
    touching_value = edges[value]
    #print(touching_value)
    for i in touching_value:
        if(i == input_value[-1]):
            for i in input_value:
                if(i == value):
                    contains_value = 1
                    
            if contains_value == 0:
                input_value.append(value)
                print(input_value)
                Test12.update_path(input_value,self)
                return(1)

            


for key in speed_of_edges:
    #print(key)
    delay_list = ['F','M','S']
    
    speed_of_edges[key] = listToString(random.sample(delay_list,1))
    #print(speed_of_edges[key])

    #r,g,b = colour_dict[listToString(random.sample(delay_list,1))]
    #speed_of_edges[key] = (r,g,b)
    #print(r,'   ',g,'   ',b)

class Test11(GridLayout):
    #self.ids.button = ""
    def restart(self):
        print("trying restart")
        self.root.clear_widgets()
        self.stop()
        return Test11().run()
    
class Test12(GridLayout,Image):
    
    total_time = 0
    
    tiles = {
        'a':'S0S0S0S0',
        'b':'S0S0S0S0',
        'c':'S0S0S0S0',
        'd':'S0S0S0S0',
        'e':'S0S0S0S0',
        'f':'S0S0S0S0',
        'g':'S0S0S0S0',
        'h':'S0S0S0S0',
        'i':'S0S0S0S0',
        'j':'S0S0S0S0',
        'k':'S0S0S0S0',
        'l':'S0S0S0S0',
        'm':'S0S0S0S0',
        'n':'S0S0S0S0',
        'o':'S0S0S0S0',
        'p':'S0S0S0S0',
        'q':'S0S0S0S0',
        'r':'S0S0S0S0',
        's':'S0S0S0S0',
        't':'S0S0S0S0',
        'u':'S0S0S0S0',
        'v':'S0S0S0S0',
        'w':'S0S0S0S0',
        'x':'S0S0S0S0',
        'y':'S0S0S0S0'
        }


    def restart_game():
        pass


    def find_total_time(user_path):
        print(user_path)
        len_path = len(user_path)
    
        pair = [user_path[-2], user_path[-1]]
        #print(pair)
        
        pair_list = []
        #c = c+1
        for i in pair:
            i = numbertoletter(i)
            #print(i)
            pair_list.append(i)
        #print(pair_list)
        pair = "".join(pair_list)
        #print(pair)                         #ab
        new_pair = find_direction(pair)
        #print(new_pair)
        speed = speed_of_edges[new_pair]
        #print(speed)
        speed_dict = {
            'F':10,
            'M':20,
            'S':50
        }
        speed = speed_dict[speed]
        Test12.total_time = Test12.total_time + speed
        print(Test12.total_time)

    def update_path(user_path, self):             #update grid with path
        len_path = len(user_path)
        # = 0
        #print(user_path)
        #for i in range(0,len_path-1):
        #print(i)
        pair = [user_path[-2], user_path[-1]]
        #print(pair)
        
        pair_list = []
        #c = c+1
        for i in pair:
            i = numbertoletter(i)
            #print(i)
            pair_list.append(i)
        #print(pair_list)
        pair = "".join(pair_list)
        #print(pair)                         #ab
        new_pair = find_direction(pair)
        #print(new_pair)                     #arbl
        key = new_pair
        new_pair = list(new_pair)

        first_letter = new_pair[0]
        first_letter_direction = new_pair[1]
        second_letter = new_pair[2]
        second_letter_direction = new_pair[3]
        

        first_value = list(Test12.tiles[first_letter])
        second_value = list(Test12.tiles[second_letter])
        #print(first_value,second_value)
        if first_letter_direction == 'r':
            first_value[4] = speed_of_edges[key]
            first_value[5] = 'P'
            #print(first_value)
            first_value = "".join(first_value)
            second_value[0] = speed_of_edges[key]
            second_value[1] = 'P'
            #print(second_value)
            second_value = "".join(second_value)
            #print(second_value)

            Test12.tiles[first_letter] = first_value
            Test12.tiles[second_letter] = second_value

        if first_letter_direction == 'u':
            first_value[2] = speed_of_edges[key]
            first_value[3] = 'P'
            #print(first_value)
            first_value = "".join(first_value)
            second_value[6] = speed_of_edges[key]
            second_value[7] = 'P'
            #print(second_value)
            second_value = "".join(second_value)
            #print(second_value)

            Test12.tiles[first_letter] = first_value
            Test12.tiles[second_letter] = second_value

        if first_letter_direction == 'd':
            first_value[6] = speed_of_edges[key]
            first_value[7] = 'P'
            #print(first_value)
            first_value = "".join(first_value)
            second_value[2] = speed_of_edges[key]
            second_value[3] = 'P'
            #print(second_value)
            second_value = "".join(second_value)
            #print(second_value)

            Test12.tiles[first_letter] = first_value
            Test12.tiles[second_letter] = second_value

        if first_letter_direction == 'l':
            first_value[0] = speed_of_edges[key]
            first_value[1] = 'P'
            #print(first_value)
            first_value = "".join(first_value)
            second_value[4] = speed_of_edges[key]
            second_value[5] = 'P'
            #print(second_value)
            second_value = "".join(second_value)

            Test12.tiles[first_letter] = first_value
            Test12.tiles[second_letter] = second_value

        #print(Test12.tiles)
        #print(first_letter,second_value,first_letter,second_letter)
        self.ids.image1.source = "roads/" + Test12.tiles['a'] + ".png"
        self.ids.image2.source = "roads/" + Test12.tiles['b'] + ".png"
        self.ids.image3.source = "roads/" + Test12.tiles['c'] + ".png"
        self.ids.image4.source = "roads/" + Test12.tiles['d'] + ".png"
        self.ids.image5.source = "roads/" + Test12.tiles['e'] + ".png"
        self.ids.image6.source = "roads/" + Test12.tiles['f'] + ".png"
        self.ids.image7.source = "roads/" + Test12.tiles['g'] + ".png"
        self.ids.image8.source = "roads/" + Test12.tiles['h'] + ".png"
        self.ids.image9.source = "roads/" + Test12.tiles['i'] + ".png"
        self.ids.image10.source = "roads/" + Test12.tiles['j'] + ".png"
        self.ids.image11.source = "roads/" + Test12.tiles['k'] + ".png"
        self.ids.image12.source = "roads/" + Test12.tiles['l'] + ".png"
        self.ids.image13.source = "roads/" + Test12.tiles['m'] + ".png"
        self.ids.image14.source = "roads/" + Test12.tiles['n'] + ".png"
        self.ids.image15.source = "roads/" + Test12.tiles['o'] + ".png"
        self.ids.image16.source = "roads/" + Test12.tiles['p'] + ".png"
        self.ids.image17.source = "roads/" + Test12.tiles['q'] + ".png"
        self.ids.image18.source = "roads/" + Test12.tiles['r'] + ".png"
        self.ids.image19.source = "roads/" + Test12.tiles['s'] + ".png"
        self.ids.image20.source = "roads/" + Test12.tiles['t'] + ".png"
        self.ids.image21.source = "roads/" + Test12.tiles['u'] + ".png"
        self.ids.image22.source = "roads/" + Test12.tiles['v'] + ".png"
        self.ids.image23.source = "roads/" + Test12.tiles['w'] + ".png"
        self.ids.image24.source = "roads/" + Test12.tiles['x'] + ".png"
        self.ids.image25.source = "roads/" + Test12.tiles['y'] + ".png"
        
        Test12.find_total_time(user_path)
#                                draw main grid
    for key in speed_of_edges:
        #print(key)
        first_letter = key[0]
        first_letter_direction = key[1]
        second_letter = key[2]
        second_letter_direction = key[3]
        #print(first_letter,first_letter_direction, second_letter, second_letter_direction)
        
        first_value = list(tiles[first_letter])
        second_value = list(tiles[second_letter])
        #print(first_value,second_value)
        if first_letter_direction == 'r':
            first_value[4] = speed_of_edges[key]
            #print(first_value)
            first_value = "".join(first_value)
            second_value[0] = speed_of_edges[key]
            #print(second_value)
            second_value = "".join(second_value)
            print(second_value)

            tiles[first_letter] = first_value
            tiles[second_letter] = second_value

        if first_letter_direction == 'u':
            first_value[2] = speed_of_edges[key]
            #print(first_value)
            first_value = "".join(first_value)
            second_value[6] = speed_of_edges[key]
            #print(second_value)
            second_value = "".join(second_value)
            print(second_value)

            tiles[first_letter] = first_value
            tiles[second_letter] = second_value

        if first_letter_direction == 'd':
            first_value[6] = speed_of_edges[key]
            #print(first_value)
            first_value = "".join(first_value)
            second_value[2] = speed_of_edges[key]
            #print(second_value)
            second_value = "".join(second_value)
            print(second_value)

            tiles[first_letter] = first_value
            tiles[second_letter] = second_value

        if first_letter_direction == 'l':
            first_value[0] = speed_of_edges[key]
            #print(first_value)
            first_value = "".join(first_value)
            second_value[4] = speed_of_edges[key]
            #print(second_value)
            second_value = "".join(second_value)

            tiles[first_letter] = first_value
            tiles[second_letter] = second_value
    
    #for key in tiles:
        #value =  tiles[key]
        #value = "roads/" + value + ".png"
        #tiles[key] = value
    #first_value = "".join(first_value) 
    #second_value = "".join(second_value)   
    print(tiles)    #x = '1'
    #my_text = StringProperty("hello!")
    #button_1_color1 = NumericProperty(1)
    #button_1_color2 = NumericProperty(0)
    #tes1 = "roads/F0F0F0F0.png"
    
    tile1 = StringProperty("roads/" +tiles['a'] + ".png")
    tile2 = StringProperty("roads/" +tiles['b'] + ".png")
    tile3 = StringProperty("roads/" +tiles['c'] + ".png")
    tile4 = StringProperty("roads/" +tiles['d'] + ".png")
    tile5 = StringProperty("roads/" +tiles['e'] + ".png")
    tile6 = StringProperty("roads/" +tiles['f'] + ".png")
    tile7 = StringProperty("roads/" +tiles['g'] + ".png")
    tile8 = StringProperty("roads/" +tiles['h'] + ".png")
    tile9 = StringProperty("roads/" +tiles['i'] + ".png")
    tile10 = StringProperty("roads/" +tiles['j'] + ".png")
    tile11 = StringProperty("roads/" +tiles['k'] + ".png")
    tile12 = StringProperty("roads/" +tiles['l'] + ".png")
    tile13 = StringProperty("roads/" +tiles['m'] + ".png")
    tile14 = StringProperty("roads/" +tiles['n'] + ".png")
    tile15 = StringProperty("roads/" +tiles['o'] + ".png")
    tile16 = StringProperty("roads/" +tiles['p'] + ".png")
    tile17 = StringProperty("roads/" +tiles['q'] + ".png")
    tile18 = StringProperty("roads/" +tiles['r'] + ".png")
    tile19 = StringProperty("roads/" +tiles['s'] + ".png")
    tile20 = StringProperty("roads/" +tiles['t'] + ".png")
    tile21 = StringProperty("roads/" +tiles['u'] + ".png")
    tile22 = StringProperty("roads/" +tiles['v'] + ".png")
    tile23 = StringProperty("roads/" +tiles['w'] + ".png")
    tile24 = StringProperty("roads/" +tiles['x'] + ".png")
    tile25 = StringProperty("roads/" +tiles['y'] + ".png")
    
    #def on_button_click(self):
    # print("button pressed")
        #self.my_text = " you clock"
    def on_button_click1(self):
        #print("button 1 pressed")
        button_num = 1
        check_if_value_is_touching(button_num,self)
        
    def on_button_click2(self):
        #print("button 2 pressed")
        button_num = 2
        check_if_value_is_touching(button_num,self)
    def on_button_click3(self):
        #print("button 3 pressed")
        button_num = 3
        check_if_value_is_touching(button_num,self)
        
    def on_button_click4(self):
        #print("button 4 pressed")
        button_num = 4
        check_if_value_is_touching(button_num,self)
    def on_button_click5(self):
        #print("button 5 pressed")
        button_num = 5
        check_if_value_is_touching(button_num,self)
    def on_button_click6(self):
        #print("button 6 pressed")
        button_num = 6
        check_if_value_is_touching(button_num,self)
    def on_button_click7(self):
        #print("button 7 pressed")
        button_num = 7
        check_if_value_is_touching(button_num,self)
    def on_button_click8(self):
        #print("button 8 pressed")
        button_num = 8
        check_if_value_is_touching(button_num,self)
    def on_button_click9(self):
        #print("button 9 pressed")
        button_num = 9
        check_if_value_is_touching(button_num,self)
    def on_button_click10(self):
        #print("button 10 pressed")
        button_num = 10
        check_if_value_is_touching(button_num,self)
    def on_button_click11(self):
        #print("button 11 pressed")
        button_num = 11
        check_if_value_is_touching(button_num,self)
    def on_button_click12(self):
        #print("button 12 pressed")
        button_num = 12
        check_if_value_is_touching(button_num,self)
    def on_button_click13(self):
        #print("button 13 pressed")
        button_num = 13
        check_if_value_is_touching(button_num,self)
    def on_button_click14(self):
        #print("button 14 pressed")
        button_num = 14
        check_if_value_is_touching(button_num,self)
    def on_button_click15(self):
        #print("button 15 pressed")
        button_num = 15
        check_if_value_is_touching(button_num,self)
    def on_button_click16(self):
        #print("button 16 pressed")
        button_num = 16
        check_if_value_is_touching(button_num,self)
    def on_button_click17(self):
        #print("button 17 pressed")
        button_num = 17
        check_if_value_is_touching(button_num,self)
    def on_button_click18(self):
        #print("button 18 pressed")
        button_num = 18
        check_if_value_is_touching(button_num,self)
    def on_button_click19(self):
        #print("button 19 pressed")
        button_num = 19
        check_if_value_is_touching(button_num,self)
    def on_button_click20(self):
        #print("button 20 pressed")
        button_num = 20
        check_if_value_is_touching(button_num,self)
    def on_button_click21(self):
        #print("button 21 pressed")
        button_num = 21
        check_if_value_is_touching(button_num,self)
    def on_button_click22(self):
        #print("button 22 pressed")
        button_num = 22
        check_if_value_is_touching(button_num,self)
    def on_button_click23(self):
        #print("button 23 pressed")
        button_num = 23
        check_if_value_is_touching(button_num,self)
    def on_button_click24(self):
        #print("button 24 pressed")
        button_num = 24
        check_if_value_is_touching(button_num,self)
    def on_button_click25(self):
        #print("button 25 pressed")
        button_num = 25
        check_if_value_is_touching(button_num,self)

    









class RoadGameApp(App):
    pass

RoadGameApp().run()



