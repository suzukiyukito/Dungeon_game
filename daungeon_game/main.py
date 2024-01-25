from hero import Hero
import Area 
from Area import generate_floor

import move_area
import kari_enemy_move
import result
import title
from hero import Color
from hero import viewing_expression
#マップ表示より
big_blank = "　"
small_blank = " "
WITDH_WALL  = "｜"
OVER_WALL = "＿"  
UNDER_WALL = "￣"
NEXT_AREA1 = "｜"
NEXT_AREA2  = "　"
HERO = "勇"
ENEMY = "敵"
ITEM = "宝"
FELLOW1 = "弓"
FELLOW2 = "賢"
FELLOW3 = "癒"
STEP = "階"
GOAL = "出"
HALF_WALL = "＿|"
HALF_WALL2 = "|＿"
KING = "魔"
LAEGE_BLANK = " 　"

def viewing(this_mp, floor_map,step_pos):
    for h,areas  in enumerate(this_mp,1):
        for w,area in enumerate(areas):
            match area:
                case 0:
                    print(big_blank,end="")
                case 1:
                    print(small_blank,end="")
                case 2:
                    print(WITDH_WALL,end="")
                case 3:
                    print(OVER_WALL,end="")
                case 4:
                    print(UNDER_WALL,end="")
                case 7:
                    print(NEXT_AREA1,end="")
                case 8:
                    print(NEXT_AREA2,end="")
                case 9:
                    if not step_pos: 
                        print(HERO,end="")
                    elif (step_pos[0],step_pos[1]) == (h-1,w):
                        print(f"{Color.YELLOW}{HERO}{Color.RESET}", end = "")
                    else:
                        print(HERO,end="")
                case "A":
                    if (areas[w-1] == 9 and w>=1) or (areas[w+1] == 9 and w+1 <= len(areas))or (this_mp[h-2][w] == 9 and h-1>=1 )or (this_mp[h][w] == 9 and h<= len(this_mp)):
                        print(f"{Color.YELLOW}{ENEMY}{Color.RESET}", end = "")
                    else:
                        print(ENEMY, end = "")
                case "C":
                    if (areas[w-1] == 9 and w>=1) or (areas[w+1] == 9 and w+1 <= len(areas))or (this_mp[h-2][w] == 9 and h-1>=1 )or (this_mp[h][w] == 9 and h<= len(this_mp)):
                        print(f"{Color.CYAN}{FELLOW1}{Color.RESET}", end = "")
                    else:
                        print(FELLOW1, end = "")
                case "D":
                    if (areas[w-1] == 9 and w>=1) or (areas[w+1] == 9 and w+1 <= len(areas))or (this_mp[h-2][w] == 9 and h-1>=1 )or (this_mp[h][w] == 9 and h<= len(this_mp)):
                        print(f"{Color.YELLOW}{FELLOW2}{Color.RESET}", end = "")
                    else:
                        print(FELLOW2, end = "")
                case "E":
                    if (areas[w-1] == 9 and w>=1) or (areas[w+1] == 9 and w+1 <= len(areas))or (this_mp[h-2][w] == 9 and h-1>=1 )or (this_mp[h][w] == 9 and h<= len(this_mp)):
                        print(f"{Color.YELLOW}{FELLOW3}{Color.RESET}", end = "")
                    else:
                        print(FELLOW3, end = "")
                case "I":
                    if (areas[w-1] == 9 and w>=1) or (areas[w+1] == 9 and w+1 <= len(areas))or (this_mp[h-2][w] == 9 and h-1>=1 )or (this_mp[h][w] == 9 and h<= len(this_mp)):
                        print(f"{Color.YELLOW}{ITEM}{Color.RESET}", end = "")
                    else:
                        print(ITEM, end = "")
                case "S":
                    print(STEP, end = "")
                case "G":
                    print(GOAL, end = "")
                case 10:
                    print(HALF_WALL, end = "")
                case "M":
                    print(KING, end = "")
                case 11:
                    print(HALF_WALL2, end= "")
                case 5:
                    print(LAEGE_BLANK, end = "")

        print("　　　　",end="")
        if h == 1:
            print("mini map",end="")
        elif len(floor_map)+1 >= h:
            for f in floor_map[h-2]:
                if f == 2:
                    print("🔳",end="")
                elif f == 3:
                    print("🔲",end="")
                else:
                    print("　",end="")
        print("")
    
#-----------------------------------
#動くオブジェクトの位置をマップに反映させる

if __name__ == "__main__":
    title.main_menu()
    floor, area_dict, now_floor, ene_list = generate_floor()
    hero_pos = [2, 3, 0]
    hero = Hero(hero_pos)
    #エリアの情報
    this_area = area_dict[hero.pos[2]]
    floor[this_area.area_pos[0]][this_area.area_pos[1]] = 3
    tutorial_flag = [True, True, True]
    #ゲーム継続フラグ
    game = True
    #説明
    m_1 = list("ここは、どこだ…？」\n")
    m_2 = list("なんだあの化け物は…！」\n")
    m_3 = list("グギギギ…」\n")
    m_5 = list("あれはなんだ…？」\n")
    m_4_1 = list("ぅぁ…たす…け…っ！」")
    m_4_2 = list("…仲間が捕まってる⁉」\n")
    area1_mess = ["\n", "勇者「", m_1, 
                "(移動キーを押して通路まで行き、この部屋から出よう！)\n"]
    area2_mess = ["\n", "勇者「", m_2, "敵「", m_3, 
                "(この部屋には魔物がいる。\n", "近づくと攻撃できるが魔物に攻撃されてしまうから注意しよう！)\n"]
    area3_mess = ["\n",
                  "レンジャー「",m_4_1,"\n",
                  "勇者「", m_4_2, "(この部屋には仲間がいる。\n", 
                "仲間の近くで’E’を押すと仲間にすることができるぞ！)\n"]
    area4_mess = ["\n", "勇者「", m_5, "(この部屋には宝箱がある。\n", 
                "宝箱の近くで’E’を押すとアイテムを入手できるぞ！)\n",
                "(また階段の上に乗った状態で’E’を押すと次のフロアにいけるぞ！)\n"]
    viewing_expression(area1_mess)

    while game:
        while(1):
            viewing(this_area.map, floor,this_area.step_pos)
            #ステータス表記
            print("===============================")
            hero.display_HP()
            print("===============================")
            #勇者の行動
            move_flag = hero.show_option(this_area, now_floor, ene_list)
            if not move_flag[0]:
                break
        if len(move_flag) >= 2:
            if move_flag[1] == -1:
                #フロア移動
                floor, area_dict, now_floor, ene_list = generate_floor()
                hero.set_start_pos(area_dict, now_floor)
                this_area = area_dict[hero.pos[2]]
                floor[this_area.area_pos[0]][this_area.area_pos[1]] = 3
                continue
            elif move_flag[1] == -2:
                result.game_win()
                game = False
            else:
                move_area.move_area(hero, area_dict[move_flag[1]].map, move_flag[2])
                floor[this_area.area_pos[0]][this_area.area_pos[1]] = 2
                this_area = area_dict[hero.pos[2]]
                floor[this_area.area_pos[0]][this_area.area_pos[1]] = 3
                if now_floor == -2:
                    if tutorial_flag[0] == True and hero.pos[2] == 1:
                        # 戦闘のチュートリアル
                        viewing(this_area.map, floor,this_area.step_pos)
                        viewing_expression(area2_mess)
                        tutorial_flag[0] = False
                    elif tutorial_flag[1] == True and hero.pos[2] == 2:
                        viewing(this_area.map, floor,this_area.step_pos)
                        viewing_expression(area3_mess)
                        tutorial_flag[1] = False
                    elif tutorial_flag[2] == True and hero.pos[2] == 3:
                        viewing(this_area.map, floor,this_area.step_pos)
                        viewing_expression(area4_mess)
                        tutorial_flag[2] = False
        else:
            #敵の行動
            if not ene_list[hero.pos[2]]:
                pass
            #魔王の行動
            elif now_floor == 1 and hero.pos[2] == 4:
                if ene_list[4][0].king_hp >= 1:
                    ene_list[4][0].king_attack(hero)
                    if result.game_loss(hero.hero_hp):
                                viewing(this_area.map, floor, this_area.step_pos)
                                game = False
                                break
            else:
                for enemy in ene_list[hero.pos[2]]:
                    if enemy.ene_hp >= 1:
                        kari_enemy_move.move_next(hero, enemy, this_area)
                        if result.game_loss(hero.hero_hp):
                            game = False
                            break
