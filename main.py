from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
import random



#Builder.load_file("roadgamev2.kv")

#set background to white
Window.clearcolor = (1, 1, 1, 1)

#global variables
roads = {
    'horizontal1':'BH.png',
    'horizontal2':'BH.png',
    'horizontal3':'BH.png',
    'horizontal4':'BH.png',
    'horizontal5':'BH.png',
    'horizontal6':'BH.png',
    'horizontal7':'BH.png',
    'horizontal8':'BH.png',
    'horizontal9':'BH.png',
    'horizontal10':'BH.png',
    'horizontal11':'BH.png',
    'horizontal12':'BH.png',
    'horizontal13':'BH.png',
    'horizontal14':'BH.png',
    'horizontal15':'BH.png',
    'horizontal16':'BH.png',
    'horizontal17':'BH.png',
    'horizontal18':'BH.png',
    'horizontal19':'BH.png',
    'horizontal20':'BH.png',
    'vertical1':'BV.png',
    'vertical2':'BV.png',
    'vertical3':'BV.png',
    'vertical4':'BV.png',
    'vertical5':'BV.png',
    'vertical6':'BV.png',
    'vertical7':'BV.png',
    'vertical8':'BV.png',
    'vertical9':'BV.png',
    'vertical10':'BV.png',
    'vertical11':'BV.png',
    'vertical12':'BV.png',
    'vertical13':'BV.png',
    'vertical14':'BV.png',
    'vertical15':'BV.png',
    'vertical16':'BV.png',
    'vertical17':'BV.png',
    'vertical18':'BV.png',
    'vertical19':'BV.png',
    'vertical20':'BV.png'
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

path = {
    'ab':'0000.png',
    'af':'0000.png',
    'bc':'0000.png',
    'cd':'0000.png',
    'bg':'0000.png',
    'ch':'0000.png',
    'di':'0000.png',
    'de':'0000.png',
    'ej':'0000.png',
    'fg':'0000.png',
    'gh':'0000.png',
    'hi':'0000.png',
    'fk':'0000.png',
    'gl':'0000.png',
    'hm':'0000.png',
    'ij':'0000.png',
    'jo':'0000.png',
    'kl':'0000.png',
    'kp':'0000.png',
    'lm':'0000.png',
    'mn':'0000.png',
    'no':'0000.png',
    'lq':'0000.png',
    'in':'0000.png',
    'ns':'0000.png',
    'mr':'0000.png',
    'pq':'0000.png',
    'rs':'0000.png',
    'ot':'0000.png',
    'pu':'0000.png',
    'qv':'0000.png',
    'st':'0000.png',
    'sx':'0000.png',
    'rw':'0000.png',
    'ty':'0000.png',
    'qr':'0000.png',
    'vw':'0000.png',
    'uv':'0000.png',
    'wx':'0000.png',
    'xy':'0000.png' 
}
path_speed = {
    'ab':'',
    'af':'',
    'bc':'',
    'cd':'',
    'bg':'',
    'ch':'',
    'di':'',
    'de':'',
    'ej':'',
    'fg':'',
    'gh':'',
    'hi':'',
    'fk':'',
    'gl':'',
    'hm':'',
    'ij':'',
    'jo':'',
    'kl':'',
    'kp':'',
    'lm':'',
    'mn':'',
    'no':'',
    'lq':'',
    'in':'',
    'ns':'',
    'mr':'',
    'pq':'',
    'rs':'',
    'ot':'',
    'pu':'',
    'qv':'',
    'st':'',
    'sx':'',
    'rw':'',
    'ty':'',
    'qr':'',
    'vw':'',
    'uv':'',
    'wx':'',
    'xy':'' 
}
path_speed_value = {
    'ab':0,
    'af':0,
    'bc':0,
    'cd':0,
    'bg':0,
    'ch':0,
    'di':0,
    'de':0,
    'ej':0,
    'fg':0,
    'gh':0,
    'hi':0,
    'fk':0,
    'gl':0,
    'hm':0,
    'ij':0,
    'jo':0,
    'kl':0,
    'kp':0,
    'lm':0,
    'mn':0,
    'no':0,
    'lq':0,
    'in':0,
    'ns':0,
    'mr':0,
    'pq':0,
    'rs':0,
    'ot':0,
    'pu':0,
    'qv':0,
    'st':0,
    'sx':0,
    'rw':0,
    'ty':0,
    'qr':0,
    'vw':0,
    'uv':0,
    'wx':0,
    'xy':0
}
road_speed = {
    'a': {'b':path_speed_value['ab'], 'f':path_speed_value['af']}, 
    'b': {'a':path_speed_value['ab'], 'c':path_speed_value['bc'], 'g':path_speed_value['bg']}, 
    'c': {'b':path_speed_value['bc'], 'd':path_speed_value['cd'], 'h':path_speed_value['ch']}, 
    'd': {'c':path_speed_value['cd'], 'e':path_speed_value['de'], 'i':path_speed_value['di']},
    'e': {'d':path_speed_value['de'], 'j':path_speed_value['ej']}, 
    'f': {'a':path_speed_value['af'], 'g':path_speed_value['fg'], 'k':path_speed_value['fk']}, 
    'g': {'b':path_speed_value['bg'], 'f':path_speed_value['fg'], 'h':path_speed_value['gh'], 'l':path_speed_value['gl']}, 
    'h': {'c':path_speed_value['ch'], 'g':path_speed_value['gh'], 'i':path_speed_value['hi'], 'm':path_speed_value['hm']}, 
    'i': {'d':path_speed_value['di'], 'h':path_speed_value['hi'], 'n':path_speed_value['in'], 'j':path_speed_value['ij']}, 
    'j': {'e':path_speed_value['ej'], 'o':path_speed_value['jo'], 'i':path_speed_value['ij']}, 
    'k': {'f':path_speed_value['fk'], 'l':path_speed_value['kl'], 'p':path_speed_value['kp']}, 
    'l': {'g':path_speed_value['gl'], 'k':path_speed_value['kl'], 'm':path_speed_value['lm'], 'q':path_speed_value['lq']}, 
    'm': {'h':path_speed_value['hm'], 'l':path_speed_value['lm'], 'n':path_speed_value['mn'], 'r':path_speed_value['mr']}, 
    'n': {'i':path_speed_value['in'], 'm':path_speed_value['mn'], 'o':path_speed_value['no'], 's':path_speed_value['ns']}, 
    'o': {'j':path_speed_value['jo'], 'n':path_speed_value['no'], 't':path_speed_value['ot']}, 
    'p': {'k':path_speed_value['kp'], 'q':path_speed_value['pq'], 'u':path_speed_value['pu']}, 
    'q': {'l':path_speed_value['lq'], 'p':path_speed_value['pq'], 'r':path_speed_value['qr'], 'v':path_speed_value['qv']}, 
    'r': {'m':path_speed_value['mr'], 'q':path_speed_value['qr'], 's':path_speed_value['rs'], 'w':path_speed_value['rw']}, 
    's': {'n':path_speed_value['ns'], 'r':path_speed_value['rs'], 't':path_speed_value['st'], 'x':path_speed_value['sx']}, 
    't': {'o':path_speed_value['ot'], 's':path_speed_value['st'], 'y':path_speed_value['ty']}, 
    'u': {'p':path_speed_value['pu'], 'v':path_speed_value['uv']}, 
    'v': {'q':path_speed_value['qv'], 'u':path_speed_value['uv'], 'w':path_speed_value['vw']}, 
    'w': {'r':path_speed_value['rw'], 'v':path_speed_value['vw'], 'x':path_speed_value['wx']}, 
    'x': {'s':path_speed_value['sx'], 'w':path_speed_value['wx'], 'y':path_speed_value['xy']}, 
    'y': {'t':path_speed_value['ty'], 'x':path_speed_value['xy']}
    }
input_value = [1]
total_time = 0
winning_score = 0
winning_path = []
computer_path = {
    'ab':'0000.png',
    'af':'0000.png',
    'bc':'0000.png',
    'cd':'0000.png',
    'bg':'0000.png',
    'ch':'0000.png',
    'di':'0000.png',
    'de':'0000.png',
    'ej':'0000.png',
    'fg':'0000.png',
    'gh':'0000.png',
    'hi':'0000.png',
    'fk':'0000.png',
    'gl':'0000.png',
    'hm':'0000.png',
    'ij':'0000.png',
    'jo':'0000.png',
    'kl':'0000.png',
    'kp':'0000.png',
    'lm':'0000.png',
    'mn':'0000.png',
    'no':'0000.png',
    'lq':'0000.png',
    'in':'0000.png',
    'ns':'0000.png',
    'mr':'0000.png',
    'pq':'0000.png',
    'rs':'0000.png',
    'ot':'0000.png',
    'pu':'0000.png',
    'qv':'0000.png',
    'st':'0000.png',
    'sx':'0000.png',
    'rw':'0000.png',
    'ty':'0000.png',
    'qr':'0000.png',
    'vw':'0000.png',
    'uv':'0000.png',
    'wx':'0000.png',
    'xy':'0000.png' 
}
#functions
def check_if_new_value_is_touching(new_value,self):
    if input_value[-1] == 25: return
    touching_tiles = edges[new_value] #find other places the new value touches
    for i in touching_tiles:    #itterate through touching places
        if(i == input_value[-1]):   #if touching previous place on user path
            for i in input_value:   #checking if already in user path
                if(i == new_value):
                    return  #already in user path list
                    
            input_value.append(new_value) #add new value to list
            #print(input_value)
            main.update_path(input_value,self)
            return

def listToString(s): 
    str1 = "" 
    return (str1.join(s))


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

def convert_name_to_letter(name):
    convertion_dict = {
        'horizontal1':'ab',
        'horizontal2':'bc',
        'horizontal3':'cd',
        'horizontal4':'de',
        'horizontal5':'fg',
        'horizontal6':'gh',
        'horizontal7':'hi',
        'horizontal8':'ij',
        'horizontal9':'kl',
        'horizontal10':'lm',
        'horizontal11':'mn',
        'horizontal12':'no',
        'horizontal13':'pq',
        'horizontal14':'qr',
        'horizontal15':'rs',
        'horizontal16':'st',
        'horizontal17':'uv',
        'horizontal18':'vw',
        'horizontal19':'wx',
        'horizontal20':'xy',
        'vertical1':'af',
        'vertical2':'bg',
        'vertical3':'ch',
        'vertical4':'di',
        'vertical5':'ej',
        'vertical6':'fk',
        'vertical7':'gl',
        'vertical8':'hm',
        'vertical9':'in',
        'vertical10':'jo',
        'vertical11':'kp',
        'vertical12':'lq',
        'vertical13':'mr',
        'vertical14':'ns',
        'vertical15':'ot',
        'vertical16':'pu',
        'vertical17':'qv',
        'vertical18':'rw',
        'vertical19':'sx',
        'vertical20':'ty'}
    return convertion_dict[name]

def generate_and_set_speeds():
    for key in roads:
        road_src = list(roads[key])
        speed_list = ['B','G','R']
        random_speed = listToString(random.sample(speed_list,1))
        road_src[0] = random_speed
        roads[key] = listToString(road_src)
        new_key = convert_name_to_letter(key)
        path_speed[new_key] = random_speed
        speed_dict = {
            'B':20,
            'G':10,
            'R':50
        }
        speed = speed_dict[random_speed]
        path_speed_value[new_key] = speed
    print(roads)

def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))
        return(path,shortest_distance[goal])
def find_winning_path_and_score():
    road_speed = {
        'a': {'b':path_speed_value['ab'], 'f':path_speed_value['af']}, 
        'b': {'a':path_speed_value['ab'], 'c':path_speed_value['bc'], 'g':path_speed_value['bg']}, 
        'c': {'b':path_speed_value['bc'], 'd':path_speed_value['cd'], 'h':path_speed_value['ch']}, 
        'd': {'c':path_speed_value['cd'], 'e':path_speed_value['de'], 'i':path_speed_value['di']},
        'e': {'d':path_speed_value['de'], 'j':path_speed_value['ej']}, 
        'f': {'a':path_speed_value['af'], 'g':path_speed_value['fg'], 'k':path_speed_value['fk']}, 
        'g': {'b':path_speed_value['bg'], 'f':path_speed_value['fg'], 'h':path_speed_value['gh'], 'l':path_speed_value['gl']}, 
        'h': {'c':path_speed_value['ch'], 'g':path_speed_value['gh'], 'i':path_speed_value['hi'], 'm':path_speed_value['hm']}, 
        'i': {'d':path_speed_value['di'], 'h':path_speed_value['hi'], 'n':path_speed_value['in'], 'j':path_speed_value['ij']}, 
        'j': {'e':path_speed_value['ej'], 'o':path_speed_value['jo'], 'i':path_speed_value['ij']}, 
        'k': {'f':path_speed_value['fk'], 'l':path_speed_value['kl'], 'p':path_speed_value['kp']}, 
        'l': {'g':path_speed_value['gl'], 'k':path_speed_value['kl'], 'm':path_speed_value['lm'], 'q':path_speed_value['lq']}, 
        'm': {'h':path_speed_value['hm'], 'l':path_speed_value['lm'], 'n':path_speed_value['mn'], 'r':path_speed_value['mr']}, 
        'n': {'i':path_speed_value['in'], 'm':path_speed_value['mn'], 'o':path_speed_value['no'], 's':path_speed_value['ns']}, 
        'o': {'j':path_speed_value['jo'], 'n':path_speed_value['no'], 't':path_speed_value['ot']}, 
        'p': {'k':path_speed_value['kp'], 'q':path_speed_value['pq'], 'u':path_speed_value['pu']}, 
        'q': {'l':path_speed_value['lq'], 'p':path_speed_value['pq'], 'r':path_speed_value['qr'], 'v':path_speed_value['qv']}, 
        'r': {'m':path_speed_value['mr'], 'q':path_speed_value['qr'], 's':path_speed_value['rs'], 'w':path_speed_value['rw']}, 
        's': {'n':path_speed_value['ns'], 'r':path_speed_value['rs'], 't':path_speed_value['st'], 'x':path_speed_value['sx']}, 
        't': {'o':path_speed_value['ot'], 's':path_speed_value['st'], 'y':path_speed_value['ty']}, 
        'u': {'p':path_speed_value['pu'], 'v':path_speed_value['uv']}, 
        'v': {'q':path_speed_value['qv'], 'u':path_speed_value['uv'], 'w':path_speed_value['vw']}, 
        'w': {'r':path_speed_value['rw'], 'v':path_speed_value['vw'], 'x':path_speed_value['wx']}, 
        'x': {'s':path_speed_value['sx'], 'w':path_speed_value['wx'], 'y':path_speed_value['xy']}, 
        'y': {'t':path_speed_value['ty'], 'x':path_speed_value['xy']}
    }
    global winning_path
    global winning_score
    winning_path, winning_score = dijkstra(road_speed, 'a', 'y')
    
def find_orientation(key):
    orientation_dict = {
        'ab':'h',
        'af':'v',
        'bc':'h',
        'cd':'h',
        'bg':'v',
        'ch':'v',
        'di':'v',
        'de':'h',
        'ej':'v',
        'fg':'h',
        'gh':'h',
        'hi':'h',
        'fk':'v',
        'gl':'v',
        'hm':'v',
        'ij':'h',
        'jo':'v',
        'kl':'h',
        'kp':'v',
        'lm':'h',
        'mn':'h',
        'no':'h',
        'lq':'v',
        'in':'v',
        'ns':'v',
        'mr':'v',
        'pq':'h',
        'rs':'h',
        'ot':'v',
        'pu':'v',
        'qv':'v',
        'st':'h',
        'sx':'v',
        'rw':'v',
        'ty':'v',
        'qr':'h',
        'vw':'h',
        'uv':'h',
        'wx':'h',
        'xy':'h',
        'ba':'h',
        'fa':'v',
        'bc':'h',
        'dc':'h',
        'gb':'v',
        'hc':'v',
        'id':'v',
        'ed':'h',
        'je':'v',
        'gf':'h',
        'hg':'h',
        'ih':'h',
        'kf':'v',
        'lg':'v',
        'mh':'v',
        'ji':'h',
        'oj':'v',
        'lk':'h',
        'pk':'v',
        'ml':'h',
        'nm':'h',
        'on':'h',
        'ql':'v',
        'ni':'v',
        'sn':'v',
        'rm':'v',
        'qp':'h',
        'sr':'h',
        'to':'v',
        'up':'v',
        'vq':'v',
        'ts':'h',
        'xs':'v',
        'wr':'v',
        'yt':'v',
        'rq':'h',
        'wv':'h',
        'vu':'h',
        'xw':'h',
        'yx':'h' 
    }
    convertion_dict = {
        'ab':'ab',
        'af':'af',
        'bc':'bc',
        'cd':'cd',
        'bg':'bg',
        'ch':'ch',
        'di':'di',
        'de':'de',
        'ej':'ej',
        'fg':'fg',
        'gh':'gh',
        'hi':'hi',
        'fk':'fk',
        'gl':'gl',
        'hm':'hm',
        'ij':'ij',
        'jo':'jo',
        'kl':'kl',
        'kp':'kp',
        'lm':'lm',
        'mn':'mn',
        'no':'no',
        'lq':'lq',
        'in':'in',
        'ns':'ns',
        'mr':'mr',
        'pq':'pq',
        'rs':'rs',
        'ot':'ot',
        'pu':'pu',
        'qv':'qv',
        'st':'st',
        'sx':'sx',
        'rw':'rw',
        'ty':'ty',
        'qr':'qr',
        'vw':'vw',
        'uv':'uv',
        'wx':'wx',
        'xy':'xy',
        'ba':'ab',
        'fa':'af',
        'cb':'bc',
        'dc':'cd',
        'gb':'bg',
        'hc':'ch',
        'id':'di',
        'ed':'de',
        'je':'ej',
        'gf':'fg',
        'hg':'gh',
        'ih':'hi',
        'kf':'fk',
        'lg':'gl',
        'mh':'hm',
        'ji':'ij',
        'oj':'jo',
        'lk':'kl',
        'pk':'kp',
        'ml':'lm',
        'nm':'mn',
        'on':'no',
        'ql':'lq',
        'ni':'in',
        'sn':'ns',
        'rm':'mr',
        'qp':'pq',
        'sr':'rs',
        'to':'ot',
        'up':'pu',
        'vq':'qv',
        'ts':'st',
        'xs':'sx',
        'wr':'rw',
        'yt':'ty',
        'rq':'qr',
        'wv':'vw',
        'vu':'uv',
        'xw':'wx',
        'yx':'xy' 
    }
    key = convertion_dict[key]
    return(key,orientation_dict[key])


class main(GridLayout, BoxLayout):

    generate_and_set_speeds()
    
    find_winning_path_and_score()
    

    def update_path(user_path, self):             #update grid with path

        if len(user_path) < 2:  return

        new_pair = [user_path[-1],user_path[-2]]
        new_pair_in_letters = []
        for i in new_pair:              #convert to letter form
            i = numbertoletter(i)
            new_pair_in_letters.append(i)

        new_pair_key = "".join(new_pair_in_letters)
        key,orientation = find_orientation(new_pair_key)


        if orientation == 'h':
            path[key] = 'PH.png'
            
        if orientation == 'v':
            path[key] = 'PV.png'
        #print(key)

        speed_of_pair = path_speed[key]                             #find speed and add it to total time
        speed_dict = {
            'G':10,
            'B':20,
            'R':50
        }
        speed = speed_dict[speed_of_pair]
        global total_time
        total_time = total_time + speed
        print(total_time)
        self.ids.score_label.text =  str(total_time)
        
        self.ids.winning_score.text =  str(winning_score)

        self.ids.pathhorizontal1.source =  path['ab'] 
        self.ids.pathhorizontal2.source =  path['bc'] 
        self.ids.pathhorizontal3.source =  path['cd'] 
        self.ids.pathhorizontal4.source =  path['de'] 
        self.ids.pathhorizontal5.source =  path['fg'] 
        self.ids.pathhorizontal6.source =  path['gh'] 
        self.ids.pathhorizontal7.source =  path['hi'] 
        self.ids.pathhorizontal8.source =  path['ij'] 
        self.ids.pathhorizontal9.source =  path['kl'] 
        self.ids.pathhorizontal10.source =  path['lm'] 
        self.ids.pathhorizontal11.source =  path['mn'] 
        self.ids.pathhorizontal12.source =  path['no'] 
        self.ids.pathhorizontal13.source =  path['pq'] 
        self.ids.pathhorizontal14.source =  path['qr'] 
        self.ids.pathhorizontal15.source =  path['rs'] 
        self.ids.pathhorizontal16.source =  path['st'] 
        self.ids.pathhorizontal17.source =  path['uv'] 
        self.ids.pathhorizontal18.source =  path['vw'] 
        self.ids.pathhorizontal19.source =  path['wx'] 
        self.ids.pathhorizontal20.source =  path['xy'] 
        self.ids.pathvertical1.source =  path['af'] 
        self.ids.pathvertical2.source =  path['bg'] 
        self.ids.pathvertical3.source =  path['ch'] 
        self.ids.pathvertical4.source =  path['di'] 
        self.ids.pathvertical5.source =  path['ej'] 
        self.ids.pathvertical6.source =  path['fk'] 
        self.ids.pathvertical7.source =  path['gl'] 
        self.ids.pathvertical8.source =  path['hm'] 
        self.ids.pathvertical9.source =  path['in'] 
        self.ids.pathvertical10.source =  path['jo'] 
        self.ids.pathvertical11.source =  path['kp'] 
        self.ids.pathvertical12.source =  path['lq'] 
        self.ids.pathvertical13.source =  path['mr'] 
        self.ids.pathvertical14.source =  path['ns'] 
        self.ids.pathvertical15.source =  path['ot'] 
        self.ids.pathvertical16.source =  path['pu'] 
        self.ids.pathvertical17.source =  path['qv'] 
        self.ids.pathvertical18.source =  path['rw'] 
        self.ids.pathvertical19.source =  path['sx'] 
        self.ids.pathvertical20.source =  path['ty'] 
        

    def reset_path(self):
        self.ids.pathhorizontal1.source =  '0000.png' 
        self.ids.pathhorizontal2.source =  '0000.png' 
        self.ids.pathhorizontal3.source =  '0000.png' 
        self.ids.pathhorizontal4.source =  '0000.png' 
        self.ids.pathhorizontal5.source =  '0000.png' 
        self.ids.pathhorizontal6.source =  '0000.png' 
        self.ids.pathhorizontal7.source =  '0000.png' 
        self.ids.pathhorizontal8.source =  '0000.png' 
        self.ids.pathhorizontal9.source =  '0000.png' 
        self.ids.pathhorizontal10.source =  '0000.png' 
        self.ids.pathhorizontal11.source =  '0000.png' 
        self.ids.pathhorizontal12.source =  '0000.png' 
        self.ids.pathhorizontal13.source =  '0000.png' 
        self.ids.pathhorizontal14.source =  '0000.png' 
        self.ids.pathhorizontal15.source =  '0000.png' 
        self.ids.pathhorizontal16.source =  '0000.png' 
        self.ids.pathhorizontal17.source =  '0000.png' 
        self.ids.pathhorizontal18.source =  '0000.png' 
        self.ids.pathhorizontal19.source =  '0000.png' 
        self.ids.pathhorizontal20.source =  '0000.png' 
        self.ids.pathvertical1.source =  '0000.png' 
        self.ids.pathvertical2.source =  '0000.png' 
        self.ids.pathvertical3.source =  '0000.png' 
        self.ids.pathvertical4.source =  '0000.png' 
        self.ids.pathvertical5.source =  '0000.png' 
        self.ids.pathvertical6.source =  '0000.png' 
        self.ids.pathvertical7.source =  '0000.png' 
        self.ids.pathvertical8.source =  '0000.png' 
        self.ids.pathvertical9.source =  '0000.png' 
        self.ids.pathvertical10.source =  '0000.png' 
        self.ids.pathvertical11.source =  '0000.png' 
        self.ids.pathvertical12.source =  '0000.png' 
        self.ids.pathvertical13.source =  '0000.png' 
        self.ids.pathvertical14.source =  '0000.png' 
        self.ids.pathvertical15.source =  '0000.png' 
        self.ids.pathvertical16.source =  '0000.png' 
        self.ids.pathvertical17.source =  '0000.png' 
        self.ids.pathvertical18.source =  '0000.png' 
        self.ids.pathvertical19.source =  '0000.png' 
        self.ids.pathvertical20.source =  '0000.png' 
    def reset_roads(self): 
        self.ids.horizontal1.source = roads['horizontal1']
        self.ids.horizontal2.source = roads['horizontal2']
        self.ids.horizontal3.source = roads['horizontal3']
        self.ids.horizontal4.source = roads['horizontal4']
        self.ids.horizontal5.source = roads['horizontal5']
        self.ids.horizontal6.source = roads['horizontal6']
        self.ids.horizontal7.source = roads['horizontal7']
        self.ids.horizontal8.source = roads['horizontal8']
        self.ids.horizontal9.source = roads['horizontal9']
        self.ids.horizontal10.source = roads['horizontal10']
        self.ids.horizontal11.source = roads['horizontal11']
        self.ids.horizontal12.source = roads['horizontal12']
        self.ids.horizontal13.source = roads['horizontal13']
        self.ids.horizontal14.source = roads['horizontal14']
        self.ids.horizontal15.source = roads['horizontal15']
        self.ids.horizontal16.source = roads['horizontal16']
        self.ids.horizontal17.source = roads['horizontal17']
        self.ids.horizontal18.source = roads['horizontal18']
        self.ids.horizontal19.source = roads['horizontal19']
        self.ids.horizontal20.source = roads['horizontal20']
        self.ids.vertical1.source = roads['vertical1']
        self.ids.vertical2.source = roads['vertical2']
        self.ids.vertical3.source = roads['vertical3']
        self.ids.vertical4.source = roads['vertical4']
        self.ids.vertical5.source = roads['vertical5']
        self.ids.vertical6.source = roads['vertical6']
        self.ids.vertical7.source = roads['vertical7']
        self.ids.vertical8.source = roads['vertical8']
        self.ids.vertical9.source = roads['vertical9']
        self.ids.vertical10.source = roads['vertical10']
        self.ids.vertical11.source = roads['vertical11']
        self.ids.vertical12.source = roads['vertical12']
        self.ids.vertical13.source = roads['vertical13']
        self.ids.vertical14.source = roads['vertical14']
        self.ids.vertical15.source = roads['vertical15']
        self.ids.vertical16.source = roads['vertical16']
        self.ids.vertical17.source = roads['vertical17']
        self.ids.vertical18.source = roads['vertical18']
        self.ids.vertical19.source = roads['vertical19']
        self.ids.vertical20.source = roads['vertical20']
    def reset_computer_path(self):
        self.ids.cpathhorizontal1.source =  computer_path['ab'] 
        self.ids.cpathhorizontal2.source =  computer_path['bc'] 
        self.ids.cpathhorizontal3.source =  computer_path['cd'] 
        self.ids.cpathhorizontal4.source =  computer_path['de'] 
        self.ids.cpathhorizontal5.source =  computer_path['fg'] 
        self.ids.cpathhorizontal6.source =  computer_path['gh'] 
        self.ids.cpathhorizontal7.source =  computer_path['hi'] 
        self.ids.cpathhorizontal8.source =  computer_path['ij'] 
        self.ids.cpathhorizontal9.source =  computer_path['kl'] 
        self.ids.cpathhorizontal10.source =  computer_path['lm'] 
        self.ids.cpathhorizontal11.source =  computer_path['mn'] 
        self.ids.cpathhorizontal12.source =  computer_path['no'] 
        self.ids.cpathhorizontal13.source =  computer_path['pq'] 
        self.ids.cpathhorizontal14.source =  computer_path['qr'] 
        self.ids.cpathhorizontal15.source =  computer_path['rs'] 
        self.ids.cpathhorizontal16.source =  computer_path['st'] 
        self.ids.cpathhorizontal17.source =  computer_path['uv'] 
        self.ids.cpathhorizontal18.source =  computer_path['vw'] 
        self.ids.cpathhorizontal19.source =  computer_path['wx'] 
        self.ids.cpathhorizontal20.source =  computer_path['xy'] 
        self.ids.cpathvertical1.source =  computer_path['af'] 
        self.ids.cpathvertical2.source =  computer_path['bg'] 
        self.ids.cpathvertical3.source =  computer_path['ch'] 
        self.ids.cpathvertical4.source =  computer_path['di'] 
        self.ids.cpathvertical5.source =  computer_path['ej'] 
        self.ids.cpathvertical6.source =  computer_path['fk'] 
        self.ids.cpathvertical7.source =  computer_path['gl'] 
        self.ids.cpathvertical8.source =  computer_path['hm'] 
        self.ids.cpathvertical9.source =  computer_path['in'] 
        self.ids.cpathvertical10.source =  computer_path['jo'] 
        self.ids.cpathvertical11.source =  computer_path['kp'] 
        self.ids.cpathvertical12.source =  computer_path['lq'] 
        self.ids.cpathvertical13.source =  computer_path['mr'] 
        self.ids.cpathvertical14.source =  computer_path['ns'] 
        self.ids.cpathvertical15.source =  computer_path['ot'] 
        self.ids.cpathvertical16.source =  computer_path['pu'] 
        self.ids.cpathvertical17.source =  computer_path['qv'] 
        self.ids.cpathvertical18.source =  computer_path['rw'] 
        self.ids.cpathvertical19.source =  computer_path['sx'] 
        self.ids.cpathvertical20.source =  computer_path['ty']
    def show_answer(self):
        global winning_path
        if len(winning_path) < 2:  return
        i = 0
        while i < (len(winning_path)-1):
            new_pair = [winning_path[-1-i],winning_path[-2-i]]
           
            

            new_pair_key = "".join(new_pair)
            key,orientation = find_orientation(new_pair_key)


            if orientation == 'h':
                computer_path[key] = 'CH.png'
                
            if orientation == 'v':
                computer_path[key] = 'CV.png'
            i = i+1
            #print(computer_path)
        self.ids.cpathhorizontal1.source =  computer_path['ab'] 
        self.ids.cpathhorizontal2.source =  computer_path['bc'] 
        self.ids.cpathhorizontal3.source =  computer_path['cd'] 
        self.ids.cpathhorizontal4.source =  computer_path['de'] 
        self.ids.cpathhorizontal5.source =  computer_path['fg'] 
        self.ids.cpathhorizontal6.source =  computer_path['gh'] 
        self.ids.cpathhorizontal7.source =  computer_path['hi'] 
        self.ids.cpathhorizontal8.source =  computer_path['ij'] 
        self.ids.cpathhorizontal9.source =  computer_path['kl'] 
        self.ids.cpathhorizontal10.source =  computer_path['lm'] 
        self.ids.cpathhorizontal11.source =  computer_path['mn'] 
        self.ids.cpathhorizontal12.source =  computer_path['no'] 
        self.ids.cpathhorizontal13.source =  computer_path['pq'] 
        self.ids.cpathhorizontal14.source =  computer_path['qr'] 
        self.ids.cpathhorizontal15.source =  computer_path['rs'] 
        self.ids.cpathhorizontal16.source =  computer_path['st'] 
        self.ids.cpathhorizontal17.source =  computer_path['uv'] 
        self.ids.cpathhorizontal18.source =  computer_path['vw'] 
        self.ids.cpathhorizontal19.source =  computer_path['wx'] 
        self.ids.cpathhorizontal20.source =  computer_path['xy'] 
        self.ids.cpathvertical1.source =  computer_path['af'] 
        self.ids.cpathvertical2.source =  computer_path['bg'] 
        self.ids.cpathvertical3.source =  computer_path['ch'] 
        self.ids.cpathvertical4.source =  computer_path['di'] 
        self.ids.cpathvertical5.source =  computer_path['ej'] 
        self.ids.cpathvertical6.source =  computer_path['fk'] 
        self.ids.cpathvertical7.source =  computer_path['gl'] 
        self.ids.cpathvertical8.source =  computer_path['hm'] 
        self.ids.cpathvertical9.source =  computer_path['in'] 
        self.ids.cpathvertical10.source =  computer_path['jo'] 
        self.ids.cpathvertical11.source =  computer_path['kp'] 
        self.ids.cpathvertical12.source =  computer_path['lq'] 
        self.ids.cpathvertical13.source =  computer_path['mr'] 
        self.ids.cpathvertical14.source =  computer_path['ns'] 
        self.ids.cpathvertical15.source =  computer_path['ot'] 
        self.ids.cpathvertical16.source =  computer_path['pu'] 
        self.ids.cpathvertical17.source =  computer_path['qv'] 
        self.ids.cpathvertical18.source =  computer_path['rw'] 
        self.ids.cpathvertical19.source =  computer_path['sx'] 
        self.ids.cpathvertical20.source =  computer_path['ty'] 

    def reset(self):
        print("restarting")
        global path 
        path = {
            'ab':'0000.png',
            'af':'0000.png',
            'bc':'0000.png',
            'cd':'0000.png',
            'bg':'0000.png',
            'ch':'0000.png',
            'di':'0000.png',
            'de':'0000.png',
            'ej':'0000.png',
            'fg':'0000.png',
            'gh':'0000.png',
            'hi':'0000.png',
            'fk':'0000.png',
            'gl':'0000.png',
            'hm':'0000.png',
            'ij':'0000.png',
            'jo':'0000.png',
            'kl':'0000.png',
            'kp':'0000.png',
            'lm':'0000.png',
            'mn':'0000.png',
            'no':'0000.png',
            'lq':'0000.png',
            'in':'0000.png',
            'ns':'0000.png',
            'mr':'0000.png',
            'pq':'0000.png',
            'rs':'0000.png',
            'ot':'0000.png',
            'pu':'0000.png',
            'qv':'0000.png',
            'st':'0000.png',
            'sx':'0000.png',
            'rw':'0000.png',
            'ty':'0000.png',
            'qr':'0000.png',
            'vw':'0000.png',
            'uv':'0000.png',
            'wx':'0000.png',
            'xy':'0000.png' }
        global input_value
        input_value = [1]
        global total_time
        total_time = 0
        user_path = [1]
        self.ids.score_label.text =  '0'
        main.reset_path(self)
        main.update_path(user_path,self)
        global computer_path
        computer_path = {
            'ab':'0000.png',
            'af':'0000.png',
            'bc':'0000.png',
            'cd':'0000.png',
            'bg':'0000.png',
            'ch':'0000.png',
            'di':'0000.png',
            'de':'0000.png',
            'ej':'0000.png',
            'fg':'0000.png',
            'gh':'0000.png',
            'hi':'0000.png',
            'fk':'0000.png',
            'gl':'0000.png',
            'hm':'0000.png',
            'ij':'0000.png',
            'jo':'0000.png',
            'kl':'0000.png',
            'kp':'0000.png',
            'lm':'0000.png',
            'mn':'0000.png',
            'no':'0000.png',
            'lq':'0000.png',
            'in':'0000.png',
            'ns':'0000.png',
            'mr':'0000.png',
            'pq':'0000.png',
            'rs':'0000.png',
            'ot':'0000.png',
            'pu':'0000.png',
            'qv':'0000.png',
            'st':'0000.png',
            'sx':'0000.png',
            'rw':'0000.png',
            'ty':'0000.png',
            'qr':'0000.png',
            'vw':'0000.png',
            'uv':'0000.png',
            'wx':'0000.png',
            'xy':'0000.png' 
        }
        main.reset_computer_path(self)
    def new_game(self):
        print("starting new game")
        global path 
        path = {
            'ab':'0000.png',
            'af':'0000.png',
            'bc':'0000.png',
            'cd':'0000.png',
            'bg':'0000.png',
            'ch':'0000.png',
            'di':'0000.png',
            'de':'0000.png',
            'ej':'0000.png',
            'fg':'0000.png',
            'gh':'0000.png',
            'hi':'0000.png',
            'fk':'0000.png',
            'gl':'0000.png',
            'hm':'0000.png',
            'ij':'0000.png',
            'jo':'0000.png',
            'kl':'0000.png',
            'kp':'0000.png',
            'lm':'0000.png',
            'mn':'0000.png',
            'no':'0000.png',
            'lq':'0000.png',
            'in':'0000.png',
            'ns':'0000.png',
            'mr':'0000.png',
            'pq':'0000.png',
            'rs':'0000.png',
            'ot':'0000.png',
            'pu':'0000.png',
            'qv':'0000.png',
            'st':'0000.png',
            'sx':'0000.png',
            'rw':'0000.png',
            'ty':'0000.png',
            'qr':'0000.png',
            'vw':'0000.png',
            'uv':'0000.png',
            'wx':'0000.png',
            'xy':'0000.png' }
        global input_value
        input_value = [1]
        global total_time
        total_time = 0
        user_path = [1]
        self.ids.score_label.text =  '0'
        generate_and_set_speeds()
        main.reset_roads(self)
        main.reset_path(self)
        main.update_path(user_path,self)
        road_speed = {
            'a': {'b':path_speed_value['ab'], 'f':path_speed_value['af']}, 
            'b': {'a':path_speed_value['ab'], 'c':path_speed_value['bc'], 'g':path_speed_value['bg']}, 
            'c': {'b':path_speed_value['bc'], 'd':path_speed_value['cd'], 'h':path_speed_value['ch']}, 
            'd': {'c':path_speed_value['cd'], 'e':path_speed_value['de'], 'i':path_speed_value['di']},
            'e': {'d':path_speed_value['de'], 'j':path_speed_value['ej']}, 
            'f': {'a':path_speed_value['af'], 'g':path_speed_value['fg'], 'k':path_speed_value['fk']}, 
            'g': {'b':path_speed_value['bg'], 'f':path_speed_value['fg'], 'h':path_speed_value['gh'], 'l':path_speed_value['gl']}, 
            'h': {'c':path_speed_value['ch'], 'g':path_speed_value['gh'], 'i':path_speed_value['hi'], 'm':path_speed_value['hm']}, 
            'i': {'d':path_speed_value['di'], 'h':path_speed_value['hi'], 'n':path_speed_value['in'], 'j':path_speed_value['ij']}, 
            'j': {'e':path_speed_value['ej'], 'o':path_speed_value['jo'], 'i':path_speed_value['ij']}, 
            'k': {'f':path_speed_value['fk'], 'l':path_speed_value['kl'], 'p':path_speed_value['kp']}, 
            'l': {'g':path_speed_value['gl'], 'k':path_speed_value['kl'], 'm':path_speed_value['lm'], 'q':path_speed_value['lq']}, 
            'm': {'h':path_speed_value['hm'], 'l':path_speed_value['lm'], 'n':path_speed_value['mn'], 'r':path_speed_value['mr']}, 
            'n': {'i':path_speed_value['in'], 'm':path_speed_value['mn'], 'o':path_speed_value['no'], 's':path_speed_value['ns']}, 
            'o': {'j':path_speed_value['jo'], 'n':path_speed_value['no'], 't':path_speed_value['ot']}, 
            'p': {'k':path_speed_value['kp'], 'q':path_speed_value['pq'], 'u':path_speed_value['pu']}, 
            'q': {'l':path_speed_value['lq'], 'p':path_speed_value['pq'], 'r':path_speed_value['qr'], 'v':path_speed_value['qv']}, 
            'r': {'m':path_speed_value['mr'], 'q':path_speed_value['qr'], 's':path_speed_value['rs'], 'w':path_speed_value['rw']}, 
            's': {'n':path_speed_value['ns'], 'r':path_speed_value['rs'], 't':path_speed_value['st'], 'x':path_speed_value['sx']}, 
            't': {'o':path_speed_value['ot'], 's':path_speed_value['st'], 'y':path_speed_value['ty']}, 
            'u': {'p':path_speed_value['pu'], 'v':path_speed_value['uv']}, 
            'v': {'q':path_speed_value['qv'], 'u':path_speed_value['uv'], 'w':path_speed_value['vw']}, 
            'w': {'r':path_speed_value['rw'], 'v':path_speed_value['vw'], 'x':path_speed_value['wx']}, 
            'x': {'s':path_speed_value['sx'], 'w':path_speed_value['wx'], 'y':path_speed_value['xy']}, 
            'y': {'t':path_speed_value['ty'], 'x':path_speed_value['xy']}
        }
        global winning_score
        global  winning_path
        winning_path, winning_score = dijkstra(road_speed, 'a', 'y')
        self.ids.winning_score.text =  str(winning_score)
        global computer_path
        computer_path = {
            'ab':'0000.png',
            'af':'0000.png',
            'bc':'0000.png',
            'cd':'0000.png',
            'bg':'0000.png',
            'ch':'0000.png',
            'di':'0000.png',
            'de':'0000.png',
            'ej':'0000.png',
            'fg':'0000.png',
            'gh':'0000.png',
            'hi':'0000.png',
            'fk':'0000.png',
            'gl':'0000.png',
            'hm':'0000.png',
            'ij':'0000.png',
            'jo':'0000.png',
            'kl':'0000.png',
            'kp':'0000.png',
            'lm':'0000.png',
            'mn':'0000.png',
            'no':'0000.png',
            'lq':'0000.png',
            'in':'0000.png',
            'ns':'0000.png',
            'mr':'0000.png',
            'pq':'0000.png',
            'rs':'0000.png',
            'ot':'0000.png',
            'pu':'0000.png',
            'qv':'0000.png',
            'st':'0000.png',
            'sx':'0000.png',
            'rw':'0000.png',
            'ty':'0000.png',
            'qr':'0000.png',
            'vw':'0000.png',
            'uv':'0000.png',
            'wx':'0000.png',
            'xy':'0000.png' 
        }
        main.reset_computer_path(self)

        

    horizontal1 = StringProperty(roads['horizontal1'])
    horizontal2 = StringProperty(roads['horizontal2'])
    horizontal3 = StringProperty(roads['horizontal3'])
    horizontal4 = StringProperty(roads['horizontal4'])
    horizontal5 = StringProperty(roads['horizontal5'])
    horizontal6 = StringProperty(roads['horizontal6'])
    horizontal7 = StringProperty(roads['horizontal7'])
    horizontal8 = StringProperty(roads['horizontal8'])
    horizontal9 = StringProperty(roads['horizontal9'])
    horizontal10 = StringProperty(roads['horizontal10'])
    horizontal11 = StringProperty(roads['horizontal11'])
    horizontal12 = StringProperty(roads['horizontal12'])
    horizontal13 = StringProperty(roads['horizontal13'])
    horizontal14 = StringProperty(roads['horizontal14'])
    horizontal15 = StringProperty(roads['horizontal15'])
    horizontal16 = StringProperty(roads['horizontal16'])
    horizontal17 = StringProperty(roads['horizontal17'])
    horizontal18 = StringProperty(roads['horizontal18'])
    horizontal19 = StringProperty(roads['horizontal19'])
    horizontal20 = StringProperty(roads['horizontal20'])
    vertical1 = StringProperty(roads['vertical1'])
    vertical2 = StringProperty(roads['vertical2'])
    vertical3 = StringProperty(roads['vertical3'])
    vertical4 = StringProperty(roads['vertical4'])
    vertical5 = StringProperty(roads['vertical5'])
    vertical6 = StringProperty(roads['vertical6'])
    vertical7 = StringProperty(roads['vertical7'])
    vertical8 = StringProperty(roads['vertical8'])
    vertical9 = StringProperty(roads['vertical9'])
    vertical10 = StringProperty(roads['vertical10'])
    vertical11 = StringProperty(roads['vertical11'])
    vertical12 = StringProperty(roads['vertical12'])
    vertical13 = StringProperty(roads['vertical13'])
    vertical14 = StringProperty(roads['vertical14'])
    vertical15 = StringProperty(roads['vertical15'])
    vertical16 = StringProperty(roads['vertical16'])
    vertical17 = StringProperty(roads['vertical17'])
    vertical18 = StringProperty(roads['vertical18'])
    vertical19 = StringProperty(roads['vertical19'])
    vertical20 = StringProperty(roads['vertical20'])
    pathhorizontal1 = StringProperty( path['ab'])
    pathhorizontal2 = StringProperty( path['bc'])
    pathhorizontal3 = StringProperty( path['cd'])
    pathhorizontal4 = StringProperty( path['de'])
    pathhorizontal5 = StringProperty( path['fg'])
    pathhorizontal6 = StringProperty( path['gh'])
    pathhorizontal7 = StringProperty( path['hi'])
    pathhorizontal8 = StringProperty( path['ij'])
    pathhorizontal9 = StringProperty( path['kl'])
    pathhorizontal10 = StringProperty( path['lm'])
    pathhorizontal11 = StringProperty( path['mn'])
    pathhorizontal12 = StringProperty( path['no'])
    pathhorizontal13 = StringProperty( path['pq'])
    pathhorizontal14 = StringProperty( path['qr'])
    pathhorizontal15 = StringProperty( path['rs'])
    pathhorizontal16 = StringProperty( path['st'])
    pathhorizontal17 = StringProperty( path['uv'])
    pathhorizontal18 = StringProperty( path['vw'])
    pathhorizontal19 = StringProperty( path['wx'])
    pathhorizontal20 = StringProperty( path['xy'])
    pathvertical1 = StringProperty(path['af'])
    pathvertical2 = StringProperty(path['bg'])
    pathvertical3 = StringProperty(path['ch'])
    pathvertical4 = StringProperty(path['di'])
    pathvertical5 = StringProperty(path['ej'])
    pathvertical6 = StringProperty(path['fk'])
    pathvertical7 = StringProperty(path['gl'])
    pathvertical8 = StringProperty(path['hm'])
    pathvertical9 = StringProperty(path['in'])
    pathvertical10 = StringProperty(path['jo'])
    pathvertical11 = StringProperty(path['kp'])
    pathvertical12 = StringProperty(path['lq'])
    pathvertical13 = StringProperty(path['mr'])
    pathvertical14 = StringProperty(path['ns'])
    pathvertical15 = StringProperty(path['ot'])
    pathvertical16 = StringProperty(path['pu'])
    pathvertical17 = StringProperty(path['qv'])
    pathvertical18 = StringProperty(path['rw'])
    pathvertical19 = StringProperty(path['sx'])
    pathvertical20 = StringProperty(path['ty'])
    cpathhorizontal1 = StringProperty(computer_path['ab'])
    cpathhorizontal2 = StringProperty(computer_path['bc'])
    cpathhorizontal3 = StringProperty(computer_path['cd'])
    cpathhorizontal4 = StringProperty(computer_path['de'])
    cpathhorizontal5 = StringProperty(computer_path['fg'])
    cpathhorizontal6 = StringProperty(computer_path['gh'])
    cpathhorizontal7 = StringProperty(computer_path['hi'])
    cpathhorizontal8 = StringProperty(computer_path['ij'])
    cpathhorizontal9 = StringProperty(computer_path['kl'])
    cpathhorizontal10 = StringProperty(computer_path['lm'])
    cpathhorizontal11 = StringProperty(computer_path['mn'])
    cpathhorizontal12 = StringProperty(computer_path['no'])
    cpathhorizontal13 = StringProperty(computer_path['pq'])
    cpathhorizontal14 = StringProperty(computer_path['qr'])
    cpathhorizontal15 = StringProperty(computer_path['rs'])
    cpathhorizontal16 = StringProperty(computer_path['st'])
    cpathhorizontal17 = StringProperty(computer_path['uv'])
    cpathhorizontal18 = StringProperty(computer_path['vw'])
    cpathhorizontal19 = StringProperty(computer_path['wx'])
    cpathhorizontal20 = StringProperty(computer_path['xy'])
    cpathvertical1 = StringProperty(computer_path['af'])
    cpathvertical2 = StringProperty(computer_path['bg'])
    cpathvertical3 = StringProperty(computer_path['ch'])
    cpathvertical4 = StringProperty(computer_path['di'])
    cpathvertical5 = StringProperty(computer_path['ej'])
    cpathvertical6 = StringProperty(computer_path['fk'])
    cpathvertical7 = StringProperty(computer_path['gl'])
    cpathvertical8 = StringProperty(computer_path['hm'])
    cpathvertical9 = StringProperty(computer_path['in'])
    cpathvertical10 = StringProperty(computer_path['jo'])
    cpathvertical11 = StringProperty(computer_path['kp'])
    cpathvertical12 = StringProperty(computer_path['lq'])
    cpathvertical13 = StringProperty(computer_path['mr'])
    cpathvertical14 = StringProperty(computer_path['ns'])
    cpathvertical15 = StringProperty(computer_path['ot'])
    cpathvertical16 = StringProperty(computer_path['pu'])
    cpathvertical17 = StringProperty(computer_path['qv'])
    cpathvertical18 = StringProperty(computer_path['rw'])
    cpathvertical19 = StringProperty(computer_path['sx'])
    cpathvertical20 = StringProperty(computer_path['ty'])
    score_label = StringProperty('0')
    winning_score = StringProperty('0')

    def on_button_click1(self):
        button_num = 1
        check_if_new_value_is_touching(button_num,self) #will check if tile pressed touches previous one and if so will add it to user path
        
    def on_button_click2(self):
        button_num = 2
        check_if_new_value_is_touching(button_num,self)

    def on_button_click3(self):
        button_num = 3
        check_if_new_value_is_touching(button_num,self)
        
    def on_button_click4(self):
        button_num = 4
        
        check_if_new_value_is_touching(button_num,self)

    def on_button_click5(self):
        button_num = 5
        check_if_new_value_is_touching(button_num,self)

    def on_button_click6(self):
        button_num = 6
        check_if_new_value_is_touching(button_num,self)

    def on_button_click7(self):
        button_num = 7
        check_if_new_value_is_touching(button_num,self)

    def on_button_click8(self):
        button_num = 8
        check_if_new_value_is_touching(button_num,self)

    def on_button_click9(self):
        button_num = 9
        check_if_new_value_is_touching(button_num,self)

    def on_button_click10(self):
        button_num = 10
        check_if_new_value_is_touching(button_num,self)

    def on_button_click11(self):
        button_num = 11
        check_if_new_value_is_touching(button_num,self)

    def on_button_click12(self):
        button_num = 12
        check_if_new_value_is_touching(button_num,self)

    def on_button_click13(self):
        button_num = 13
        check_if_new_value_is_touching(button_num,self)

    def on_button_click14(self):
        button_num = 14
        check_if_new_value_is_touching(button_num,self)

    def on_button_click15(self):
        button_num = 15
        check_if_new_value_is_touching(button_num,self)

    def on_button_click16(self):
        button_num = 16
        check_if_new_value_is_touching(button_num,self)

    def on_button_click17(self):
        button_num = 17
        check_if_new_value_is_touching(button_num,self)

    def on_button_click18(self):
        button_num = 18
        check_if_new_value_is_touching(button_num,self)

    def on_button_click19(self):
        button_num = 19
        check_if_new_value_is_touching(button_num,self)

    def on_button_click20(self):
        button_num = 20
        check_if_new_value_is_touching(button_num,self)

    def on_button_click21(self):
        button_num = 21
        check_if_new_value_is_touching(button_num,self)

    def on_button_click22(self):
        button_num = 22
        check_if_new_value_is_touching(button_num,self)

    def on_button_click23(self):
        button_num = 23
        check_if_new_value_is_touching(button_num,self)

    def on_button_click24(self):
        button_num = 24
        check_if_new_value_is_touching(button_num,self)

    def on_button_click25(self):
        button_num = 25
        check_if_new_value_is_touching(button_num,self)

    def build(self):
        return ScreenManagement()


class ScreenManagement(ScreenManager):
    pass


class RoadGamev2App(App):
    pass

RoadGamev2App().run()