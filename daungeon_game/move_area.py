#エリア移動に関するやーつ

def move_area(hero, to_area_map, move_dir):
    """
    移動
    勇者インスタンスhero、移動先のマップto_area_map、現れる通路の方向move_dirを受け取る
    """
    match move_dir:
        #上から現れる
        case 0:
            for j, mass in enumerate(to_area_map[0]):
                if mass == 7:
                    to_area_map[1][j] = 9
                    hero.pos[0] = 1
                    hero.pos[1] = j

        #左から現れる
        case 1:
            for j, mass in enumerate(to_area_map):
                if to_area_map[j][1] == 8:
                    to_area_map[j][2] = 9
                    hero.pos[0] = j
                    hero.pos[1] = 2

        #下から現れる
        case 2:
            for j, mass in enumerate(to_area_map[len(to_area_map)-1]):
                if mass == 7:
                    to_area_map[len(to_area_map)-2][j] = 9
                    hero.pos[0] = len(to_area_map)-2
                    hero.pos[1] = j
        
        #右から現れる
        case 3:
            for j, mass in enumerate(to_area_map):
                if to_area_map[j][len(to_area_map[0])-2] == 8:
                    to_area_map[j][len(to_area_map[0])-3] = 9
                    hero.pos[0] = j
                    hero.pos[1] = len(to_area_map[0])-3

