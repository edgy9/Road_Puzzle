
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.uix.image import Image


import random


#set screen to specific size and remove resizability
Config.set('graphics', 'resizable', False)

Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '860')

#global variables
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
    'xryl':''  }
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
input_value = [1]
total_time = 0

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
    return alphabet[number]

def find_direction(key):
    find_direction_dict = {
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
    return find_direction_dict[key]

def listToString(s): 
    str1 = "" 
    return (str1.join(s))

def check_if_value_is_touching(value,self):    
    contains_value = False
    touching_tiles = edges[value]
    for i in touching_tiles:
        if(i == input_value[-1]):
            for i in input_value:
                if(i == value):
                    contains_value = True
                    
            if contains_value == False:
                input_value.append(value)
                print(input_value)
                main.update_path(input_value,self)
                return(False)

def generate_random_speeds():
    for key in speed_of_edges:
        delay_list = ['F','M','S']                                      #change amount of each letter to change probability
        speed_of_edges[key] = listToString(random.sample(delay_list,1))



class main(GridLayout, BoxLayout):
    generate_random_speeds()
    def find_total_time(user_path):
        global total_time
        print(user_path)
        
    
        last_pair_in_number = [user_path[-2], user_path[-1]]
        last_pair_in_letter = []
        for i in last_pair_in_number:
            i = numbertoletter(i)
            last_pair_in_letter.append(i)
        
        last_pair_string = "".join(last_pair_in_letter)
        last_pair_with_directions = find_direction(last_pair_string)

        speed = speed_of_edges[last_pair_with_directions]
        speed_dict = {
            'F':10,
            'M':20,
            'S':50
        }
        speed = speed_dict[speed]
        total_time = total_time + speed
        print(total_time)
    
    def generate_tile_name(self):
        global tiles
        for directions in speed_of_edges:
            first_letter = directions[0]                #directions form is letter,direction of that letter,second letter, direction of that letter eg arbl(first letter: a,direction: right, second_letter: b, direction: left)
            first_letter_direction = directions[1]
            second_letter = directions[2]
            second_letter_direction = directions[3]
            #print(first_letter,first_letter_direction,second_letter,second_letter_direction)

            first_letter_image_name = list(tiles[first_letter])
            second_letter_image_name = list(tiles[second_letter])
            
            if first_letter_direction == 'r':       #right
                first_letter_image_name[4] = speed_of_edges[directions]
                first_letter_image_name = "".join(first_letter_image_name)

                second_letter_image_name[0] = speed_of_edges[directions]        #if first letter is one direction we know second letter is opposite
                second_letter_image_name = "".join(second_letter_image_name)
                
                tiles[first_letter] = first_letter_image_name       #sets image names in global dictionary
                tiles[second_letter] = second_letter_image_name

            if first_letter_direction == 'u':
                first_letter_image_name[2] = speed_of_edges[directions]
                first_letter_image_name = "".join(first_letter_image_name)

                second_letter_image_name[6] = speed_of_edges[directions]
                second_letter_image_name = "".join(second_letter_image_name)

                tiles[first_letter] = first_letter_image_name
                tiles[second_letter] = second_letter_image_name

            if first_letter_direction == 'd':
                first_letter_image_name[6] = speed_of_edges[directions]
                first_letter_image_name = "".join(first_letter_image_name)

                second_letter_image_name[2] = speed_of_edges[directions]
                second_letter_image_name = "".join(second_letter_image_name)

                tiles[first_letter] = first_letter_image_name
                tiles[second_letter] = second_letter_image_name

            if first_letter_direction == 'l':
                first_letter_image_name[0] = speed_of_edges[directions]
                first_letter_image_name = "".join(first_letter_image_name)

                second_letter_image_name[4] = speed_of_edges[directions]
                second_letter_image_name = "".join(second_letter_image_name)

                tiles[first_letter] = first_letter_image_name
                tiles[second_letter] = second_letter_image_name
        print(tiles)
       
        self.ids.image1.source = "roads/" + tiles['a'] + ".png"
        self.ids.image2.source = "roads/" + tiles['b'] + ".png"
        self.ids.image3.source = "roads/" + tiles['c'] + ".png"
        self.ids.image4.source = "roads/" + tiles['d'] + ".png"
        self.ids.image5.source = "roads/" + tiles['e'] + ".png"
        self.ids.image6.source = "roads/" + tiles['f'] + ".png"
        self.ids.image7.source = "roads/" + tiles['g'] + ".png"
        self.ids.image8.source = "roads/" + tiles['h'] + ".png"
        self.ids.image9.source = "roads/" + tiles['i'] + ".png"
        self.ids.image10.source = "roads/" + tiles['j'] + ".png"
        self.ids.image11.source = "roads/" + tiles['k'] + ".png"
        self.ids.image12.source = "roads/" + tiles['l'] + ".png"
        self.ids.image13.source = "roads/" + tiles['m'] + ".png"
        self.ids.image14.source = "roads/" + tiles['n'] + ".png"
        self.ids.image15.source = "roads/" + tiles['o'] + ".png"
        self.ids.image16.source = "roads/" + tiles['p'] + ".png"
        self.ids.image17.source = "roads/" + tiles['q'] + ".png"
        self.ids.image18.source = "roads/" + tiles['r'] + ".png"
        self.ids.image19.source = "roads/" + tiles['s'] + ".png"
        self.ids.image20.source = "roads/" + tiles['t'] + ".png"
        self.ids.image21.source = "roads/" + tiles['u'] + ".png"
        self.ids.image22.source = "roads/" + tiles['v'] + ".png"
        self.ids.image23.source = "roads/" + tiles['w'] + ".png"
        self.ids.image24.source = "roads/" + tiles['x'] + ".png"
        self.ids.image25.source = "roads/" + tiles['y'] + ".png"



    def update_path(user_path, self):             #update grid with path
        
        
        if len(user_path) < 2: return
        
        last_pair_in_number = [user_path[-2], user_path[-1]]
        last_pair_in_letter = []
        for i in last_pair_in_number:
            i = numbertoletter(i)
            last_pair_in_letter.append(i)
        
        last_pair_string = "".join(last_pair_in_letter)
        last_pair_with_directions = find_direction(last_pair_string)
        
        directions = list(last_pair_with_directions)
        
        
        
        first_letter = directions[0]                #directions form is letter,direction of that letter,second letter, direction of that letter eg arbl(first letter: a,direction: right, second_letter: b, direction: left)
        first_letter_direction = directions[1]
        second_letter = directions[2]
        second_letter_direction = directions[3]
        

        first_letter_image_name = list(tiles[first_letter])
        second_letter_image_name = list(tiles[second_letter])
        
        if first_letter_direction == 'r':       #right
            first_letter_image_name[4] = speed_of_edges[last_pair_with_directions]
            first_letter_image_name[5] = 'P'    #indicates path
            first_letter_image_name = "".join(first_letter_image_name)

            second_letter_image_name[0] = speed_of_edges[last_pair_with_directions]        #if first letter is one direction we know second letter is opposite
            second_letter_image_name[1] = 'P'   
            second_letter_image_name = "".join(second_letter_image_name)
            
            tiles[first_letter] = first_letter_image_name       #sets image names in global dictionary
            tiles[second_letter] = second_letter_image_name

        if first_letter_direction == 'u':
            first_letter_image_name[2] = speed_of_edges[last_pair_with_directions]
            first_letter_image_name[3] = 'P'
            first_letter_image_name = "".join(first_letter_image_name)

            second_letter_image_name[6] = speed_of_edges[last_pair_with_directions]
            second_letter_image_name[7] = 'P'
            second_letter_image_name = "".join(second_letter_image_name)

            tiles[first_letter] = first_letter_image_name
            tiles[second_letter] = second_letter_image_name

        if first_letter_direction == 'd':
            first_letter_image_name[6] = speed_of_edges[last_pair_with_directions]
            first_letter_image_name[7] = 'P'
            first_letter_image_name = "".join(first_letter_image_name)

            second_letter_image_name[2] = speed_of_edges[last_pair_with_directions]
            second_letter_image_name[3] = 'P'
            second_letter_image_name = "".join(second_letter_image_name)

            tiles[first_letter] = first_letter_image_name
            tiles[second_letter] = second_letter_image_name

        if first_letter_direction == 'l':
            first_letter_image_name[0] = speed_of_edges[last_pair_with_directions]
            first_letter_image_name[1] = 'P'
            first_letter_image_name = "".join(first_letter_image_name)

            second_letter_image_name[4] = speed_of_edges[last_pair_with_directions]
            second_letter_image_name[5] = 'P'
            second_letter_image_name = "".join(second_letter_image_name)

            tiles[first_letter] = first_letter_image_name
            tiles[second_letter] = second_letter_image_name

        #update images
        self.ids.image1.source = "roads/" + tiles['a'] + ".png"
        self.ids.image2.source = "roads/" + tiles['b'] + ".png"
        self.ids.image3.source = "roads/" + tiles['c'] + ".png"
        self.ids.image4.source = "roads/" + tiles['d'] + ".png"
        self.ids.image5.source = "roads/" + tiles['e'] + ".png"
        self.ids.image6.source = "roads/" + tiles['f'] + ".png"
        self.ids.image7.source = "roads/" + tiles['g'] + ".png"
        self.ids.image8.source = "roads/" + tiles['h'] + ".png"
        self.ids.image9.source = "roads/" + tiles['i'] + ".png"
        self.ids.image10.source = "roads/" + tiles['j'] + ".png"
        self.ids.image11.source = "roads/" + tiles['k'] + ".png"
        self.ids.image12.source = "roads/" + tiles['l'] + ".png"
        self.ids.image13.source = "roads/" + tiles['m'] + ".png"
        self.ids.image14.source = "roads/" + tiles['n'] + ".png"
        self.ids.image15.source = "roads/" + tiles['o'] + ".png"
        self.ids.image16.source = "roads/" + tiles['p'] + ".png"
        self.ids.image17.source = "roads/" + tiles['q'] + ".png"
        self.ids.image18.source = "roads/" + tiles['r'] + ".png"
        self.ids.image19.source = "roads/" + tiles['s'] + ".png"
        self.ids.image20.source = "roads/" + tiles['t'] + ".png"
        self.ids.image21.source = "roads/" + tiles['u'] + ".png"
        self.ids.image22.source = "roads/" + tiles['v'] + ".png"
        self.ids.image23.source = "roads/" + tiles['w'] + ".png"
        self.ids.image24.source = "roads/" + tiles['x'] + ".png"
        self.ids.image25.source = "roads/" + tiles['y'] + ".png"
        
        main.find_total_time(user_path)


    def reset(self):
        print("reseting")
        global speed_of_edges
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
            'xryl':''  }
        global tiles
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
        global input_value
        input_value = [1]
        global total_time
        total_time = 0
        user_path = [1]
        generate_random_speeds()
        main.generate_tile_name(self)
        main.update_path(user_path,self)
        
    
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

    def on_button_click1(self):
        button_num = 1
        check_if_value_is_touching(button_num,self) #will check if tile pressed touches previous one and if so will add it to user path
        
    def on_button_click2(self):
        button_num = 2
        check_if_value_is_touching(button_num,self)

    def on_button_click3(self):
        button_num = 3
        check_if_value_is_touching(button_num,self)
        
    def on_button_click4(self):
        button_num = 4
        check_if_value_is_touching(button_num,self)

    def on_button_click5(self):
        button_num = 5
        check_if_value_is_touching(button_num,self)

    def on_button_click6(self):
        button_num = 6
        check_if_value_is_touching(button_num,self)

    def on_button_click7(self):
        button_num = 7
        check_if_value_is_touching(button_num,self)

    def on_button_click8(self):
        button_num = 8
        check_if_value_is_touching(button_num,self)

    def on_button_click9(self):
        button_num = 9
        check_if_value_is_touching(button_num,self)

    def on_button_click10(self):
        button_num = 10
        check_if_value_is_touching(button_num,self)

    def on_button_click11(self):
        button_num = 11
        check_if_value_is_touching(button_num,self)

    def on_button_click12(self):
        button_num = 12
        check_if_value_is_touching(button_num,self)

    def on_button_click13(self):
        button_num = 13
        check_if_value_is_touching(button_num,self)

    def on_button_click14(self):
        button_num = 14
        check_if_value_is_touching(button_num,self)

    def on_button_click15(self):
        button_num = 15
        check_if_value_is_touching(button_num,self)

    def on_button_click16(self):
        button_num = 16
        check_if_value_is_touching(button_num,self)

    def on_button_click17(self):
        button_num = 17
        check_if_value_is_touching(button_num,self)

    def on_button_click18(self):
        button_num = 18
        check_if_value_is_touching(button_num,self)

    def on_button_click19(self):
        button_num = 19
        check_if_value_is_touching(button_num,self)

    def on_button_click20(self):
        button_num = 20
        check_if_value_is_touching(button_num,self)

    def on_button_click21(self):
        button_num = 21
        check_if_value_is_touching(button_num,self)

    def on_button_click22(self):
        button_num = 22
        check_if_value_is_touching(button_num,self)

    def on_button_click23(self):
        button_num = 23
        check_if_value_is_touching(button_num,self)

    def on_button_click24(self):
        button_num = 24
        check_if_value_is_touching(button_num,self)

    def on_button_click25(self):
        button_num = 25
        check_if_value_is_touching(button_num,self)


class RoadGameApp(App):
    pass

RoadGameApp().run()