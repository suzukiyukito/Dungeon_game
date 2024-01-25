import characters
from characters import Enemies
from characters import Fellow
from characters import King
import item
from item import Item
import random

"""
floor = {id,OBJECT_INFO}
Area  = {id,pos}
これでposでidの情報を導出し、floorで管理している敵情報を持ってくることができる。
"""
tutorial_floor_map = [
            [0,0,0,0],
            [0,0,1,0],
            [0,1,1,0],
            [0,1,0,0]]

#３重配列で初期のマップを生成する。
tutorial_area_map = [
                [
                    [0, 1, 3, 3, 3, 3, 5],
                    [0, 2, 0, 0, 0, 2, 0],
                    [0, 2, 0, 0, 0, 2, 0],
                    [0, 2, 0, 0, 0, 2, 0],
                    [0, 1, 4, 7, 2, 4, 5]
                ],
                [
                    [0, 1, 3, 7, 2, 3, 3, 5],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [3 ,2, 0, "A", 0, 0, 2, 0],
                    [0 ,8, 0, 0, 0, 0, 2, 0],
                    [4 ,2, 0, 0, 0, 0, 2, 0],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0, 1, 4, 4, 4, 4, 4, 5]
                ],
                [
                    [0, 1, 3, 3, 3, 3, 3, 5],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0 ,2, 0, 0, 0, 0, 2, 3],
                    [0 ,2, 0, 0, 0, 0, 8, 0],
                    [0 ,2, 0, "A", 0, 0, 2, 4],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0 ,2, "C", 0, 0, 0, 2, 0],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0, 1, 4, 7, 2, 4, 4, 5]
                ],
                [
                    [0, 1, 3, 7, 2, 3, 3, 5],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0 ,2, 0, "A", 0, 0, 2, 0],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0 ,2, 0, "S", "A", 0, 2, 0],
                    [0 ,2, 0, 0, 0, 0, 2, 0],
                    [0 ,2, 0, 0, 0, "I", 2, 0],
                    [0, 1, 4, 4, 4, 4, 4, 5]
                ]
                ]

#-2Fにおける各部屋の通路のつながり
tutorial_way_to_aisle = [[-1, -1, 1, -1],
                         [0, 2, -1, -1],
                         [-1, -1, 3, 1],
                         [2, -1, -1, -1]]
#-2Fにおける部屋の位置
tutorial_area_pos = [[1, 2], 
                     [2, 2], 
                     [2, 1], 
                     [3, 1]]

#魔王のいるエリア
last_area = [[0, 0, 0, 3, 3, 0, 0, 0],
             [0, 1, 10, "G", 0, 11, 1, 0],
             [0, 2, 0, "M", "M", 0, 2, 0],
             [0, 2, 0, "M", "M", 0, 2, 0],
             [0, 2, 0, 0, 0, 0, 2, 0],
             [0, 2, 0, 0, 0, 0, 2, 0],
             [0, 2, 0, 0, 0, 0, 2, 0],
             [0, 2, 0, 0, 0, 0, 2, 0],
             [0, 1, 4, 7, 2, 4, 4, 5]]

def generate_floor():
    floor = Create_Floor()

    return floor.area_list, floor.area_dict, floor.now_floor, floor.ene_dict

#フロア(階層)を生成する
class Create_Floor():
    #現階層
    now_floor = -3

    def __init__(self):
        self.area_list = [[0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0], 
                          [0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0]]
        
        self.exist_area = set()
        self.exist_area.add(0)
        self.area_dict = {}
        if Create_Floor.now_floor == -1:
            Create_Floor.now_floor = 1
        else:
            Create_Floor.now_floor += 1
        """敵の数情報-2F 4,-1F 6, 1F 10"""
        #個々がフロアごとに変わる部分
        if Create_Floor.now_floor == -2:
                for key, map in enumerate(tutorial_area_map):
                    self.area_dict[key] = Tutorial_area(map, tutorial_way_to_aisle[key], tutorial_area_pos[key])
                self.area_list = tutorial_floor_map
                self.area_dict[0].map[2][3] = 9
                self.ene_dict = [[], [Enemies(3, 5, -2)], [Enemies(3, 4, -2)], [Enemies(3, 4, -2), Enemies(4, 6, -2)]]
                self.area_dict[3].step_pos = [6, 3]
                self.area_dict[3].item_list.append(Item(1,[8, 5]))
        else:
            match(Create_Floor.now_floor):
                case -1:
                    self.ene_num_in_floor = 6
                    self.max_area_num = 5
                    self.max_ene_in_area = 2
                case 1:
                    self.ene_num_in_floor = 10
                    self.max_area_num = 4
                    self.max_ene_in_area = 3
            self.ene_dict = [[] for _ in range(self.max_area_num)]
            for id in range(self.max_area_num):
                self.area_dict[id] = Area()
            
            self.area_dict[0].area_pos = [2, 2]
            self.create_area()
            if Create_Floor.now_floor == 1:
                self.create_last_area()
            for area_ins in range(self.max_area_num):
                self.area_dict[area_ins].creat_aisle() 

            self.generate_enemies()
            self.generate_items()
            self.generate_fellow()
            if Create_Floor.now_floor == -1:
                self.generate_step()

    def create_area(self):
        area_num  = 0
        while True:
            if area_num == self.max_area_num-1:
                break
            area = random.sample(list(self.exist_area),1)[0]
            if Create_Floor.now_floor == 1 and self.area_dict[2].area_pos == [0, 2] and area == 2:
                continue

            while True:
                way_to_aisle = [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]
                if way_to_aisle.count(1) == 1 :
                    break
    
            for j,aisle in enumerate(way_to_aisle,1):
                temp_area_pos = self.area_dict[area].area_pos
                if aisle == 1:
                    match j:
                        case 1:
                            if temp_area_pos[0] == 0 or self.area_list[temp_area_pos[0]-1][temp_area_pos[1]] == 1:
                                pass
                            elif Create_Floor.now_floor == 1 and self.area_list[3][2] == 1 and self.area_dict[area].area_pos == [1, 2]:
                                pass
                            else:
                                self.area_list[temp_area_pos[0]-1][temp_area_pos[1]] = 1
                                area_num += 1
                                self.area_dict[area].way_to_aisle[0] = area_num
                                self.area_dict[area_num].way_to_aisle[2] = area
                                self.area_dict[area_num].area_pos = [temp_area_pos[0]-1, temp_area_pos[1]]
                                self.exist_area.add(area_num) 
                                
                        case 2:
                            if temp_area_pos[1] == 0 or self.area_list[temp_area_pos[0]][temp_area_pos[1]-1] == 1:
                                pass
                            else:
                                self.area_list[temp_area_pos[0]][temp_area_pos[1]-1] = 1
                                area_num += 1
                                self.area_dict[area].way_to_aisle[1] = area_num
                                self.area_dict[area_num].way_to_aisle[3] = area
                                self.area_dict[area_num].area_pos = [temp_area_pos[0], temp_area_pos[1]-1]
                                self.exist_area.add(area_num)

                        case 3:
                            if temp_area_pos[0] == len(self.area_list)-1 or self.area_list[temp_area_pos[0]+1][temp_area_pos[1]] == 1:
                                pass
                            elif Create_Floor.now_floor == 1 and self.area_dict[2].area_pos == [0, 2] and area == 0:
                                pass
                            else:
                                self.area_list[temp_area_pos[0]+1][temp_area_pos[1]] = 1
                                area_num += 1
                                self.area_dict[area].way_to_aisle[2] = area_num
                                self.area_dict[area_num].way_to_aisle[0] = area
                                self.area_dict[area_num].area_pos = [temp_area_pos[0]+1, temp_area_pos[1]]
                                self.exist_area.add(area_num) 

                        case 4:
                            if temp_area_pos[1] == len(self.area_list)-1 or self.area_list[temp_area_pos[0]][temp_area_pos[1]+1] == 1:
                                pass
                            else:
                                self.area_list[temp_area_pos[0]][temp_area_pos[1]+1] = 1
                                area_num += 1
                                self.area_dict[area].way_to_aisle[3] = area_num
                                self.area_dict[area_num].way_to_aisle[1] = area
                                self.area_dict[area_num].area_pos = [temp_area_pos[0], temp_area_pos[1]+1]
                                self.exist_area.add(area_num) 

    #敵の配置
    def generate_enemies(self):
        ene_num_dict = {}
        continue_flag = False
        for id in range(self.max_area_num):
            ene_num_dict[id] = 0
        ene_num = 0
        while True:
            continue_flag = False
            if self.ene_num_in_floor == ene_num:
                break
            ene_pos = random.randint(0,self.max_area_num-1)
            if ene_num_dict[ene_pos] == self.max_ene_in_area:
                continue
            ene_pos_w = random.randint(2,self.area_dict[ene_pos].width+1)
            ene_pos_h = random.randint(1,self.area_dict[ene_pos].height)
            ene_around_pos = [(ene_pos_h-1,ene_pos_w),
                              (ene_pos_h,ene_pos_w-1),(ene_pos_h,ene_pos_w+1),
                              (ene_pos_h+1,ene_pos_w)]
            if self.area_dict[ene_pos].map[ene_pos_h][ene_pos_w] != 0:
                continue
            for ene_around in ene_around_pos:
                if self.area_dict[ene_pos].map[ene_around[0]][ene_around[1]] in [7, 8]:
                    continue_flag = True
                    break 
            if continue_flag:
                continue    
            ene_num_dict[ene_pos] +=1
            self.area_dict[ene_pos].map[ene_pos_h][ene_pos_w] = "A"
            self.ene_dict[ene_pos].append(Enemies(ene_pos_w,ene_pos_h,Create_Floor.now_floor))
            ene_num += 1

    #アイテムの配置
    def generate_items(self):
        if Create_Floor.now_floor == -1:
            item_list = [1,3]
        elif Create_Floor.now_floor == 1:
            item_list = [2,4]
        while True: 
            continue_flag = False
            if not item_list:
                break
            #11/15追加・修正
            item_area_pos = random.randint(0,self.max_area_num-1)
            item_w = random.randint(2,self.area_dict[item_area_pos].width+1)
            item_h = random.randint(1,self.area_dict[item_area_pos].height)
            item_around_pos = [(item_h-1,item_w),
                              (item_h,item_w-1),(item_h,item_w+1),
                              (item_h+1,item_w)]
            if self.area_dict[item_area_pos].map[item_h][item_w] != 0:            
                continue
            for item_around in item_around_pos:
                if self.area_dict[item_area_pos].map[item_around[0]][item_around[1]] in [7, 8]:
                    continue_flag = True
                    break 
            if continue_flag:
                continue
            item_id = item_list.pop()
            self.area_dict[item_area_pos].item_list.append(Item(item_id,[item_h, item_w]))
            self.area_dict[item_area_pos].map[item_h][item_w] = "I"
        #追加・修正ここまで
        
    #仲間の配置
    #11/15追加・修正
    def generate_fellow(self):
        match Create_Floor.now_floor:
            case -2:
                fellow = "C"
            case -1:
                fellow = "D"
            case 1:
                fellow = "E"
        
        while True:
            continue_flag = False     
            fellow_area_pos = random.randint(0,self.max_area_num-1)
            flw_w = random.randint(2,self.area_dict[fellow_area_pos].width+1)
            flw_h = random.randint(1,self.area_dict[fellow_area_pos].height)
            flw_around_pos = [(flw_h-1,flw_w),
                              (flw_h,flw_w-1),(flw_h,flw_w+1),
                              (flw_h+1,flw_w)]
            for flw_around in flw_around_pos:
                if self.area_dict[fellow_area_pos].map[flw_around[0]][flw_around[1]] in [7, 8]:
                    continue_flag = True
                    break
            if continue_flag:
                continue
                
            if self.area_dict[fellow_area_pos].map[flw_h][flw_w] != 0:
                continue
            self.area_dict[fellow_area_pos].map[flw_h][flw_w] = fellow
            break

    #階段の配置　
    def generate_step(self):
        step = Create_Floor.now_floor
        while True:     
            step_area_pos = random.randint(0,self.max_area_num-1)
            stp_w = random.randint(2,self.area_dict[step_area_pos].width+1)
            stp_h = random.randint(1,self.area_dict[step_area_pos].height)
            if self.area_dict[step_area_pos].map[stp_h][stp_w] != 0:
                continue
            self.area_dict[step_area_pos].map[stp_h][stp_w] = "S"
            self.area_dict[step_area_pos].step_pos = [stp_h, stp_w]
            
            break

    #魔王の部屋の配置
    def create_last_area(self):
        while True:

            area = random.sample(list(self.exist_area),1)[0]
            if self.area_dict[area].area_pos[0] != 0 and self.area_dict[area].way_to_aisle[0] == -1 and self.area_list[self.area_dict[area].area_pos[0]-1][self.area_dict[area].area_pos[1]] == 0:
                self.area_dict[area].way_to_aisle[0] = 4
                self.area_dict[4] = Tutorial_area(last_area,
                                                  [-1, -1, area, -1],
                                                  [self.area_dict[area].area_pos[0]-1,
                                                  self.area_dict[area].area_pos[1]])
                self.area_dict[4].step_pos = [1, 3]
                self.area_list[self.area_dict[area].area_pos[0]-1][self.area_dict[area].area_pos[1]] = 1
                self.ene_dict.append([King()])
                break

    

#エリアのクラス
class Area():
    def __init__(self):
        self.width = random.randint(5,7)  # エリアの横幅
        self.height = random.randint(5,7)  # エリアの縦幅
        self.way_to_aisle = [-1, -1, -1, -1]  # 別のエリアに移動する通路がどの方向にあるのかを保管
        self.map = []  # 作成したエリアを保管するためのリスト
        self.area_pos = []  
        self.step_pos = [] #階段の座標を保管する　そのエリアに階段がないなら空
        #11/15追加
        self.item_list =[]
        #追加ここまで        
        self.creat_map()
    
    #簡単な枠組み作成
    def creat_map(self):
        
        for h in range(self.height+2):
            #上枠作成
            if h == 0:
                self.map.append(list("0"+"1"+"3"*(self.width+1)+"5"))
                continue
            #下枠作成
            elif h == self.height+1:
                self.map.append(list("0"+"1"+"4"*(self.width+1)+"5"))
                break
            self.map.append(list("0"+"2"+"0"*self.width+"2"+"0"))
            
    #ここから通路作成
    def creat_aisle(self):
        for num,aisle in enumerate(self.way_to_aisle,1):
            if aisle != -1:#1の時に通路作成
                match num:#それぞれ対応する方向の処理
                    case 1:#W方向
                        tmp_num = random.randint(2,self.width-1)
                        self.map[0][tmp_num] = "7"
                        self.map[0][tmp_num+1] = "2"                       
                    case 2:#A方向
                        tmp_num = random.randint(1,self.height-1)
                        self.map[tmp_num][0] = "3"
                        self.map[tmp_num+1][1] = "8"
                        self.map[tmp_num+2][0] = "4"
                    case 3:#s方向
                        tmp_num = random.randint(2,self.width-1)
                        self.map[self.height+1][tmp_num] = "7"
                        self.map[self.height+1][tmp_num+1] ="2"
                    case 4:#D方向
                        tmp_num = random.randint(1,self.height-1)
                        self.map[tmp_num][self.width+3] = "3"
                        self.map[tmp_num+1][self.width+2] = "8"
                        self.map[tmp_num+2][self.width+3] = "4"

        self.map = [[int(i) for i in x]for x in self.map]

        
class Tutorial_area():
    def __init__(self, map, way_to_aisle, pos):
        self.width = len(map[0])  # エリアの横幅
        self.height = len(map)  # エリアの縦幅
        self.way_to_aisle = way_to_aisle  # 別のエリアに移動する通路がどの方向にあるのかを保管
        self.map = map  # エリアの作成したマップを保管するためのリスト＜＝？
        self.area_pos = pos
        self.step_pos = []
        self.item_list =[]
        
if __name__ == "__main__":
    floor_ins = Create_Floor()
    floor = floor_ins.area_list
    area = floor_ins.area_dict
    for i in area.values():
        map = i.map
        for n in map:
            print(n)
        print("")
    for m in floor:
        print(m)
    