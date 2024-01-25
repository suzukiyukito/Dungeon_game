#勇者のクラスをここに記述
import random
from characters import Fellow
import time
import msvcrt
import help


class Hero():
    def __init__(self, pos):
        """
        勇者クラスの初期化
        勇者の初期位置posを受け取る
        """
        #勇者の現体力と攻撃力
        self.hero_hp = 20
        self.hero_atk = 5
        #勇者の現在位置 [y, x, roomID]の順
        self.pos = pos
        #勇者の現在保有する経験値とレベル
        self.hero_exp = 0
        self.hero_lv = 1
        #勇者の現最大体力
        self.hero_hp_max = 20
        #聖剣を所有しているか
        self.excalibur_flag = False
        #仲間を開放しているか　弓使い、魔法使い、僧侶の順
        self.fellows = [Fellow(-2), Fellow(-1), Fellow(1)]
        #ポーションの所持
        self.potions = []
        #追加ここまで

    #行動を選択
    def show_option(self, area, now_floor, enemy_list):
        """
        行動を選択させる
        現在のエリアのインスタンスarea、現在階層now_floor, 敵のリストenemy_listを受け取る
        """
        map = area.map
        #繰り返しフラグ
        loop = True
        #移動可能なマス
        can_move = (0, "S", "G") 

        print("(w:上方向、a:左方向、s:下方向、d:右方向、t:ステータス、f:攻撃・スキル、e:アクション、i:アイテム、h:ヘルプ)")
        print("入力して行動を決定せよ")     
        act = input_key()
        match act:
            #勇者の移動
            case "w":
                if map[self.pos[0]-1][self.pos[1]] == 7:
                    to_area = area.way_to_aisle[0]
                    map[self.pos[0]][self.pos[1]] = 0
                    #敵の再配置
                    if enemy_list[self.pos[2]] and (self.pos[2] != 4 or now_floor != 1):
                        for enemy in enemy_list[self.pos[2]]:
                            if enemy.ene_hp >= 1:
                                if enemy.ene_now_pos == area.step_pos:
                                    area.map[enemy.ene_now_pos[0]][enemy.ene_now_pos[1]] = "S"
                                else:    
                                    area.map[enemy.ene_now_pos[0]][enemy.ene_now_pos[1]] = 0
                                area.map[enemy.ene_init_pos[0]][enemy.ene_init_pos[1]] = "A"
                                enemy.ene_now_pos = enemy.ene_init_pos
                    self.pos[2] = to_area
                    return [False, to_area, 2]
                elif self.pos[0] <= 1 or (map[self.pos[0]-1][self.pos[1]] not in can_move):
                    print("その方向には移動できません")
                else:
                    if area.step_pos == [self.pos[0], self.pos[1]]:
                        if now_floor == 1:
                            map[self.pos[0]][self.pos[1]] = "G"
                        else:
                            map[self.pos[0]][self.pos[1]] = "S"
                    else:
                        map[self.pos[0]][self.pos[1]] = 0
                    self.pos[0] -=1
                    map[self.pos[0]][self.pos[1]] = 9
                    
                    loop = False
                    
            case "a":
                if map[self.pos[0]][self.pos[1]-1] == 8:
                    to_area = area.way_to_aisle[1]
                    map[self.pos[0]][self.pos[1]] = 0
                    #敵の再配置
                    if enemy_list[self.pos[2] and (self.pos[2] != 4 or now_floor != 1)]:
                        for enemy in enemy_list[self.pos[2]]:
                            if enemy.ene_hp >= 1:
                                if enemy.ene_now_pos == area.step_pos:
                                    area.map[enemy.ene_now_pos[0]][enemy.ene_now_pos[1]] = "S"
                                else:    
                                    area.map[enemy.ene_now_pos[0]][enemy.ene_now_pos[1]] = 0
                                area.map[enemy.ene_init_pos[0]][enemy.ene_init_pos[1]] = "A"
                                enemy.ene_now_pos = enemy.ene_init_pos
                    self.pos[2] = to_area
                    return [False, to_area, 3]
                elif self.pos[1] <= 2 or (map[self.pos[0]][self.pos[1]-1] not in can_move):
                    print("その方向には移動できません")
                else:
                    if area.step_pos == [self.pos[0], self.pos[1]]:
                        if now_floor == 1:
                            map[self.pos[0]][self.pos[1]] = "G"
                        else:
                            map[self.pos[0]][self.pos[1]] = "S"
                    else:
                        map[self.pos[0]][self.pos[1]] = 0
                    self.pos[1] -=1
                    map[self.pos[0]][self.pos[1]] = 9
                    loop = False

            case "s":
                if map[self.pos[0]+1][self.pos[1]] == 7:
                    to_area = area.way_to_aisle[2]
                    map[self.pos[0]][self.pos[1]] = 0
                    #敵の再配置
                    if enemy_list[self.pos[2]] and (self.pos[2] != 4 or now_floor != 1):
                        for enemy in enemy_list[self.pos[2]]:
                            if enemy.ene_hp >= 1:
                                if enemy.ene_now_pos == area.step_pos:
                                    area.map[enemy.ene_now_pos[0]][enemy.ene_now_pos[1]] = "S"
                                else:    
                                    area.map[enemy.ene_now_pos[0]][enemy.ene_now_pos[1]] = 0
                                area.map[enemy.ene_init_pos[0]][enemy.ene_init_pos[1]] = "A"
                                enemy.ene_now_pos = enemy.ene_init_pos
                    self.pos[2] = to_area
                    return [False, to_area, 0]
                elif self.pos[0] >= len(map) or (map[self.pos[0]+1][self.pos[1]] not in can_move):
                    print("その方向には移動できません")
                else:
                    if area.step_pos == [self.pos[0], self.pos[1]]:
                        if now_floor == 1:
                            map[self.pos[0]][self.pos[1]] = "G"
                        else:
                            map[self.pos[0]][self.pos[1]] = "S"
                    else:
                        map[self.pos[0]][self.pos[1]] = 0
                    self.pos[0] +=1
                    map[self.pos[0]][self.pos[1]] = 9
                    loop = False
                    
            case "d":
                if map[self.pos[0]][self.pos[1]+1] == 8:
                    to_area = area.way_to_aisle[3]
                    map[self.pos[0]][self.pos[1]] = 0
                    #敵の再配置
                    if enemy_list[self.pos[2]] and (self.pos[2] != 4 or now_floor != 1):
                        for enemy in enemy_list[self.pos[2]]:
                            if enemy.ene_hp >= 1:
                                if enemy.ene_now_pos == area.step_pos:
                                    area.map[enemy.ene_now_pos[0]][enemy.ene_now_pos[1]] = "S"
                                else:    
                                    area.map[enemy.ene_now_pos[0]][enemy.ene_now_pos[1]] = 0
                                area.map[enemy.ene_init_pos[0]][enemy.ene_init_pos[1]] = "A"
                                enemy.ene_now_pos = enemy.ene_init_pos
                    self.pos[2] = to_area
                    return [False, to_area, 1]
                elif self.pos[0] >= len(map[0])+1 or (map[self.pos[0]][self.pos[1]+1] not in can_move):
                    print("その方向には移動できません")
                else:                        
                    if area.step_pos == [self.pos[0], self.pos[1]]:
                        if now_floor == 1:
                            map[self.pos[0]][self.pos[1]] = "G"
                        else:
                            map[self.pos[0]][self.pos[1]] = "S"
                    else:
                        map[self.pos[0]][self.pos[1]] = 0
                    self.pos[1] +=1
                    map[self.pos[0]][self.pos[1]] = 9
                    loop = False
            
            case "t":
                self.display_status()
            case "f":
                loop = self.hero_attacking(area, enemy_list)
            
            case "e":
                check = self.hero_action(area, now_floor)
                #1ならフロア移動
                if check == 1:
                    return [False, -1]
                #2なら脱出
                elif check == 2:
                    return [False, -2]
                elif check == 3:
                    loop = False
            case "i":
                loop = self.use_item()
            case "h":
                help.display_help()
            case _:
                print("正しい行動選択しましょうね＾＾")
        return [loop]

    def display_HP(self):
        #自分の体力量によって危険度の示唆を色で示す
        if self.hero_hp/self.hero_hp_max < 0.3:
            print(f"HP: {Color.RED}{self.hero_hp}{Color.RESET}/{self.hero_hp_max}")
        elif 0.3 <= self.hero_hp/self.hero_hp_max and self.hero_hp/self.hero_hp_max <= 0.5:
            print(f"HP: {Color.YELLOW}{self.hero_hp}{Color.RESET}/{self.hero_hp_max}")
        else:
            print(f"HP: {Color.GREEN}{self.hero_hp}{Color.RESET}/{self.hero_hp_max}")

    #勇者のステータスの表示
    def display_status(self):
        print(f"レベル: {self.hero_lv}")
        print(f"経験値: {self.hero_exp}")
        self.display_HP()
        print(f"攻撃力: {self.hero_atk}")
        print(f"エクスカリバー所持: {'はい' if self.excalibur_flag else 'いいえ'}")  # 聖剣を持っているか
        print(f"仲間解放: {' '.join(['はい' if flag.fellow_flag else 'いいえ' for flag in self.fellows])}")  # 仲間が解放されているかどうかを表示
 
    def find_enemy_at_position(self, pos, enemies):
        for enemy in enemies[self.pos[2]]:
            if enemy.ene_now_pos == pos:
                return enemy
        return None
    
    #弓兵の攻撃
    def archer_attack(self,h_pos,w_pos,enemy_list,step_pos,map):
        if map[h_pos][w_pos] == "A":
            enemy = self.find_enemy_at_position([h_pos, w_pos], enemy_list)                                
            if enemy:
                self.fellows[0].skill_count -= 1
                print("レンジャーのスキル発動！敵に10ダメージを与えた！")
                if enemy.receive_damage(10):  # アーチャーの攻撃が10ダメージ
                    print("敵を倒した！")
                    if step_pos == [h_pos, w_pos]:
                        map[h_pos][w_pos] = "S"
                    else:
                        map[h_pos][w_pos] = 0
                    enemy.ene_now_pos = [0, 0]
                    self.get_exp()
                return True
        elif map[h_pos][w_pos] == "M":
            self.fellows[0].skill_count -= 1
            print("レンジャーのスキル発動！魔王に10ダメージを与えた！")
            if enemy_list[4][0].receive_damage(10):
                print("魔王を倒した！")
                map[2][3] = 0
                map[2][4] = 0
                map[3][3] = 0
                map[3][4] = 0
                self.get_exp()
            return True


    #勇者の攻撃・スキル
    def hero_attacking(self, area, enemy_list):
        # 攻撃・スキル選択の処理
        map = area.map
        while True:
            print("攻撃オプション:(選択してください)")
            print("  1: 直接攻撃")
            if self.fellows[0].fellow_flag:  # レンジャーがいる場合
                print(f"  2: 弓を選択(残り{self.fellows[0].skill_count}回)")
            if self.fellows[1].fellow_flag:  # 魔法使いがいる場合
                print(f"  3: 魔法を選択(残り{self.fellows[1].skill_count}回)")
            if self.fellows[2].fellow_flag:  # 僧侶がいる場合
                print(f"  4: 回復を選択(残り{self.fellows[2].skill_count}回)")
            print("  5: 戻る")
            choice = input_key()
            match choice:
                case "1":
                    # 直接攻撃の処理
                    around_hero_pos = [
                        [map[self.pos[0]-1][self.pos[1]]],
                        [map[self.pos[0]][self.pos[1]+i] for i in (-1,1)],
                        [map[self.pos[0]+1][self.pos[1]]]
                    ]

                    for pos in around_hero_pos:
                        if "A" in pos:
                            print("wasdで攻撃先の入力(cでキャンセル)")
                            direct = input_key()
                            match direct:
                                case "w":
                                    if map[self.pos[0]-1][self.pos[1]] == "A":
                                        target = self.find_enemy_at_position([self.pos[0]-1, self.pos[1]], enemy_list)
                                        print(f"勇者の攻撃！敵に{self.hero_atk}ダメージを与えた！")
                                        if target.receive_damage(self.hero_atk):
                                            print("敵を倒した！")
                                            if area.step_pos == [self.pos[0]-1, self.pos[1]]:
                                                map[self.pos[0]-1][self.pos[1]] = "S"
                                            else:
                                                map[self.pos[0]-1][self.pos[1]] = 0
                                            target.ene_now_pos = [0, 0]
                                            self.get_exp()
                                    else:
                                        print("空振り")
                                    break
                                        
                                        
                                case "a":
                                    if map[self.pos[0]][self.pos[1]-1] == "A":
                                        target = self.find_enemy_at_position([self.pos[0], self.pos[1]-1], enemy_list)
                                        print(f"勇者の攻撃！敵に{self.hero_atk}ダメージを与えた！")
                                        if target.receive_damage(self.hero_atk):
                                            print("敵を倒した！")
                                            if area.step_pos == [self.pos[0], self.pos[1]-1]:
                                                map[self.pos[0]][self.pos[1]-1] = "S"
                                            else:
                                                map[self.pos[0]][self.pos[1]-1] = 0
                                            target.ene_now_pos = [0, 0]
                                            self.get_exp()
                                    else:
                                        print("空振り")
                                    break
                                case "s":
                                    if map[self.pos[0]+1][self.pos[1]] == "A":
                                        target = self.find_enemy_at_position([self.pos[0]+1, self.pos[1]], enemy_list)
                                        print(f"勇者の攻撃！敵に{self.hero_atk}ダメージを与えた！")
                                        if target.receive_damage(self.hero_atk):
                                            print("敵を倒した！")
                                            if area.step_pos == [self.pos[0]+1, self.pos[1]]:
                                                map[self.pos[0]+1][self.pos[1]] = "S"
                                            else:
                                                map[self.pos[0]+1][self.pos[1]] = 0
                                            target.ene_now_pos = [0, 0]
                                            self.get_exp()
                                    else:
                                        print("空振り")
                                    break
                                case "d":
                                    if map[self.pos[0]][self.pos[1]+1] == "A":
                                        target = self.find_enemy_at_position([self.pos[0], self.pos[1]+1], enemy_list)
                                        print(f"勇者の攻撃！敵に{self.hero_atk}ダメージを与えた！")
                                        if target.receive_damage(self.hero_atk):
                                            print("敵を倒した！")
                                            if area.step_pos == [self.pos[0], self.pos[1]+1]:
                                                map[self.pos[0]][self.pos[1]+1] = "S"
                                            else:
                                                map[self.pos[0]][self.pos[1]+1] = 0
                                            target.ene_now_pos = [0, 0]
                                            self.get_exp()
                                    else:
                                        print("空振り")
                                    break

                                case _:
                                    return True

                        elif "M" in pos:
                            print("wasdで攻撃先の入力(cでキャンセル)")
                            direct = input_key()
                            match direct:
                                case "w":
                                    if map[self.pos[0]-1][self.pos[1]] == "M":
                                        if self.excalibur_flag:
                                            damage = self.hero_atk + 15
                                        else:
                                            damage = self.hero_atk
                                        print(f"勇者の攻撃！魔王に{damage}ダメージを与えた！")
                                        if enemy_list[4][0].receive_damage(damage):
                                            print("魔王を倒した！")
                                            map[2][3] = 0
                                            map[2][4] = 0
                                            map[3][3] = 0
                                            map[3][4] = 0
                                            self.get_exp()
                                    else:
                                        print("空振り")
                                    break
                                case "a":
                                    if map[self.pos[0]][self.pos[1]-1] == "M":
                                        if self.excalibur_flag:
                                            damage = self.hero_atk + 15
                                        else:
                                            damage = self.hero_atk
                                        print(f"勇者の攻撃！魔王に{damage}ダメージを与えた！")
                                        if enemy_list[4][0].receive_damage(damage):
                                            print("魔王を倒した！")
                                            map[2][3] = 0
                                            map[2][4] = 0
                                            map[3][3] = 0
                                            map[3][4] = 0
                                            self.get_exp()
                                    else:
                                        print("空振り")
                                    break
                                case "s":
                                    if map[self.pos[0]+1][self.pos[1]] == "M":
                                        if self.excalibur_flag:
                                            damage = self.hero_atk + 15
                                        else:
                                            damage = self.hero_atk
                                        print(f"勇者の攻撃！魔王に{damage}ダメージを与えた！")
                                        if enemy_list[4][0].receive_damage(damage):
                                            print("魔王を倒した！")
                                            map[2][3] = 0
                                            map[2][4] = 0
                                            map[3][3] = 0
                                            map[3][4] = 0
                                            self.get_exp()
                                    else:
                                        print("空振り")
                                    break
                                case "d":
                                    if map[self.pos[0]][self.pos[1]+1] == "M":
                                        if self.excalibur_flag:
                                            damage = self.hero_atk + 15
                                        else:
                                            damage = self.hero_atk
                                        print(f"勇者の攻撃！魔王に{damage}ダメージを与えた！")
                                        if enemy_list[4][0].receive_damage(damage):
                                            print("魔王を倒した！")
                                            map[2][3] = 0
                                            map[2][4] = 0
                                            map[3][3] = 0
                                            map[3][4] = 0
                                            self.get_exp()
                                    else:
                                        print("空振り")
                                    break
                                # 他の方向の攻撃処理
                                case _:
                                    return True
                    return False
                
                #弓兵のスキル
                case "2" if self.fellows[0].fellow_flag and self.fellows[0].skill_count > 0:
                    print("wasdで攻撃先の入力(cでキャンセル)")
                    direct = input_key()
                    match direct:
                        case "w":
                            for h_pos in range(self.pos[0]-1,0,-1): 
                                if self.archer_attack(h_pos,self.pos[1],enemy_list,area.step_pos,map):
                                    break
                            else:
                                print("空振り")
                                break 
                        case "a":
                            for w_pos in range(self.pos[1]-1,0,-1): 
                                if self.archer_attack(self.pos[0],w_pos,enemy_list,area.step_pos,map):
                                    break
                            else:
                                print("空振り")
                                break
                        case "s":
                            for h_pos in range(self.pos[0]+1, len(map)-1):
                                if self.archer_attack(h_pos,self.pos[1],enemy_list,area.step_pos,map):
                                    break
                            else:
                                print("空振り")
                                break 
                        case "d":
                            for w_pos in range(self.pos[1]+1, len(map[0])-3): 
                                if self.archer_attack(self.pos[0],w_pos,enemy_list,area.step_pos,map):
                                    break
                            
                            else:
                                print("空振り")
                                break 
                        case "c":
                            return True
                    print(f"弓兵のスキルの残り回数:{self.fellows[0].skill_count}")
                    return False
                
                case "3" if self.fellows[1].fellow_flag and self.fellows[1].skill_count > 0:
                    pos_list =[(self.pos[0]+y,self.pos[1]+x) for x in range(-1,2) for y in range(-1,2) if 0 <= self.pos[0] + y < len(map) and 0 <= self.pos[1] + x < len(map[0])]
                    for y,x in pos_list:
                        if map[y][x] == "A":
                            enemy = self.find_enemy_at_position([y,x], enemy_list)
                            if enemy:
                                print("賢者のスキル発動！敵に15ダメージを与えた")
                                if enemy.receive_damage(15):# メイジの攻撃が15ダメージ
                                    print("敵を倒した！")
                                    if area.step_pos == [y,x]:
                                        map[y][x] = "S"
                                    else:
                                        map[y][x] = 0
                                    enemy.ene_now_pos = [0, 0]
                                    self.get_exp()
                        
                        if map[y][x] == "M":
                            print("賢者のスキル発動！敵に15ダメージを与えた")
                            if enemy_list[4][0].receive_damage(10):
                                    print("魔王を倒した！")
                                    map[2][3] = 0
                                    map[2][4] = 0
                                    map[3][3] = 0
                                    map[3][4] = 0
                                    self.get_exp()
                            break

                    self.fellows[1].skill_count -= 1
                    print(f"賢者のスキルの残り回数:{self.fellows[1].skill_count}")
                    return False
                
                case "4" if self.fellows[2].fellow_flag and self.fellows[2].skill_count > 0:
                    # 僧侶のスキル（回復）
                    self.hero_hp = min(self.hero_hp + 20, self.hero_hp_max)
                    self.fellows[2].skill_count -= 1
                    print("回復しました。現在のHP: " + str(self.hero_hp))
                    print(f"僧侶のスキルの残り回数:{self.fellows[2].skill_count}")
                    return False
                # 他のオプションの処理
                case "5":
                    
                    return True  # 戻る選択
                case _:
                    print("不正な入力です。")
                
    #勇者のアクション
    def hero_action(self, area, now_floor):
        m_1 = list("助かった！！\n")
        m_2 = list("使える弓が少ないから、5回なら矢を打てるぞ！」\n")
        m_3 = list("助かりました！\n")
        m_4 = list("魔力が少ないですが、魔法を3回使うことができます！」\n")
        m_5 = list("助かりました！\n")
        m_6 = list("魔力が少ないですが、ケガを3回治すことができますわ！」\n")
        fel1_mess = ["\n", "弓兵「", m_1, m_2]
        fel2_mess = ["\n", "賢者「", m_3, m_4]
        fel3_mess = ["\n", "僧侶「", m_5, m_6]

        map = area.map
        #これで勇者の周り1マスの情報を取得
        around_hero_pos = [[self.pos[0]-1, self.pos[1]],
                           [self.pos[0], self.pos[1]-1],
                           [self.pos[0], self.pos[1]+1],
                           [self.pos[0]+1, self.pos[1]]]
        if area.step_pos == [self.pos[0], self.pos[1]]:
            #次のエリアへ移動するか確認　Yesなら移動
            if now_floor == 1:
                print("脱出しますか?(Yを入力で脱出)")
                ans = input_key()
                if ans == "Y" or ans == "y":
                    return 2
            else:
                print("次のフロアへ移動しますか?(Yを入力で移動)")
                ans = input_key()
                if ans == "Y" or ans == "y":
                    return 1
                    
        for pos in around_hero_pos:
            if "I" == map[pos[0]][pos[1]]:
                print("アイテムを拾いますか?(Yを入力で拾う)")
                ans = input_key()
                if ans == "Y" or ans == "y":
                    for item in area.item_list:
                        if item.pos == pos:
                            match item.item_id:
                                case 1: #ポーション
                                    print("ポーションを拾った")
                                    self.potions.append(item)
                                case 2: #ハイポーション
                                    print("ハイポーションを拾った")
                                    self.potions.append(item)
                                case 3: #力の種
                                    print("力の種を拾った")
                                    item.use_item(self)
                                case 4: #聖剣
                                    print("聖剣を拾った")
                                    item.use_item(self)
                                    self.excalibur_flag = True
                            map[pos[0]][pos[1]] = 0
                            return 3
            elif "C" == map[pos[0]][pos[1]]:
                print("仲間を救出しますか?(Yを入力で救出)")
                ans = input_key()
                if ans == "Y" or ans == "y":
                    print("弓兵を救出した！")
                    viewing_expression(fel1_mess)
                    self.fellows[0].fellow_flag = True
                    map[pos[0]][pos[1]] = 0
                    return 3
            elif "D" == map[pos[0]][pos[1]]:
                print("仲間を救出しますか?(Yを入力で救出)")
                ans = input_key()
                if ans == "Y" or ans == "y":
                    print("賢者を救出した！")
                    viewing_expression(fel2_mess)
                    self.fellows[1].fellow_flag = True
                    map[pos[0]][pos[1]] = 0
                    return 3
            elif "E" == map[pos[0]][pos[1]]:
                print("仲間を救出しますか?(Yを入力で救出)")
                ans = input_key()
                if ans == "Y" or ans == "y":
                    print("僧侶を救出した！")
                    viewing_expression(fel3_mess)
                    self.fellows[2].fellow_flag = True
                    map[pos[0]][pos[1]] = 0
                    return 3


    #アイテムの使用
    def use_item(self):
        if self.potions:
            print("所持アイテム：")
            for i, item in enumerate(self.potions, 1):
                print(f"{i}:{item.item_name}")
            print("どのアイテムを使いますか？(cでキャンセル)")
            ans = input_key()
            if ans.isdigit():
                ans = int(ans)
                if ans <= len(self.potions):
                    self.potions[ans-1].use_item(self)
                    del self.potions[ans-1]
                    return False
                else:
                    return True
            else:
                return True
        else:
            print("アイテムを所持していません")
            return True

    #勇者の初期位置を決める
    def set_start_pos(self, area_dict, now_floor):
        while True:
            if now_floor == 1:
                start_area = random.randint(0, len(area_dict)-2)
            else:
                start_area = random.randint(0, len(area_dict)-1)
            start_pos_y = random.randint(1, area_dict[start_area].height-2)
            start_pos_x = random.randint(2, area_dict[start_area].width-3)
            if area_dict[start_area].map[start_pos_y][start_pos_x] == 0:
                self.pos = [start_pos_y, start_pos_x, start_area]
                area_dict[start_area].map[start_pos_y][start_pos_x] = 9
                break

    def get_exp(self):
        need_exp_list = [1, 2, 3, 4, 5, 6, 7, 8]
        self.hero_exp += 1
        if self.hero_exp == need_exp_list[self.hero_lv-1]:
            print("レベルアップ！")
            self.hero_exp = 0
            self.hero_lv += 1
            self.hero_atk += 3
            self.hero_hp_max += 5
            self.hero_hp += 5 

def viewing_expression(mess):
    for i in range(len(mess)):
        if type(mess[i]) == list:
            for j in mess[i]:
                print(j, end='', flush=True)
                time.sleep(0.04)
        else:
            print(mess[i], end='', flush=True)
            time.sleep(1)

def input_key():
    while True:
        if msvcrt.kbhit():#キーが押されているか
            msv_input = msvcrt.getch()#キーのコード(バイト列)を取得する
            #矢印キーが入力された時の処理
            if ord(msv_input) == 224:
                pass
            elif ord(msv_input) == 72:
                return "w"
            elif ord(msv_input) == 75:
                return "a"
            elif ord(msv_input) == 80:
                return "s"
            elif ord(msv_input) == 77:
                return "d"
            else: 
                return msv_input.decode()
            
#print文字に色付けする為のクラス(サイトを参照)https://www.nomuramath.com/kv8wr0mp/
class Color:
	BLACK          = '\033[30m'#(文字)黒
	RED            = '\033[31m'#(文字)赤
	GREEN          = '\033[32m'#(文字)緑
	YELLOW         = '\033[33m'#(文字)黄
	BLUE           = '\033[34m'#(文字)青
	MAGENTA        = '\033[35m'#(文字)マゼンタ
	CYAN           = '\033[36m'#(文字)シアン
	WHITE          = '\033[37m'#(文字)白
	COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す
	BOLD           = '\033[1m'#太字
	UNDERLINE      = '\033[4m'#下線
	INVISIBLE      = '\033[08m'#不可視
	REVERCE        = '\033[07m'#文字色と背景色を反転
	BG_BLACK       = '\033[40m'#(背景)黒
	BG_RED         = '\033[41m'#(背景)赤
	BG_GREEN       = '\033[42m'#(背景)緑
	BG_YELLOW      = '\033[43m'#(背景)黄
	BG_BLUE        = '\033[44m'#(背景)青
	BG_MAGENTA     = '\033[45m'#(背景)マゼンタ
	BG_CYAN        = '\033[46m'#(背景)シアン
	BG_WHITE       = '\033[47m'#(背景)白
	BG_DEFAULT     = '\033[49m'#背景色をデフォルトに戻す
	RESET          = '\033[0m'#全てリセット