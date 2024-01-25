def move_next(hero_ins, enemy_ins, area):
    map = area.map
    hero = hero_ins.pos
    enemy = enemy_ins.ene_now_pos
    
    #移動可能なマス
    can_move = (0, "S", "G") 
    # マンハッタン距離
    distance = abs(hero[0] - enemy[0]) + abs(hero[1] - enemy[1])

    if distance == 1:
        print(f"敵の攻撃！勇者は{enemy_ins.ene_atk}ダメージを受けた")
        hero_ins.hero_hp -= enemy_ins.ene_atk
    elif hero[0] < enemy[0] and map[enemy[0]-1][enemy[1]] in can_move:
        if area.step_pos == [enemy[0], enemy[1]]:
            map[enemy[0]][enemy[1]] = "S"
        else:
            map[enemy[0]][enemy[1]] = 0
        enemy_ins.ene_now_pos = [enemy[0] - 1, enemy[1]]
        map[enemy_ins.ene_now_pos[0]][enemy_ins.ene_now_pos[1]] = "A"
    elif hero[0] > enemy[0] and map[enemy[0]+1][enemy[1]]in can_move:
        if area.step_pos == [enemy[0], enemy[1]]:
            map[enemy[0]][enemy[1]] = "S"
        else:
            map[enemy[0]][enemy[1]] = 0
        enemy_ins.ene_now_pos = [enemy[0] + 1, enemy[1]]
        map[enemy_ins.ene_now_pos[0]][enemy_ins.ene_now_pos[1]] = "A"
    elif hero[1] < enemy[1] and map[enemy[0]][enemy[1]-1] in can_move:
        if area.step_pos == [enemy[0], enemy[1]]:
            map[enemy[0]][enemy[1]] = "S"
        else:
            map[enemy[0]][enemy[1]] = 0
        enemy_ins.ene_now_pos = [enemy[0], enemy[1] - 1]
        map[enemy_ins.ene_now_pos[0]][enemy_ins.ene_now_pos[1]] = "A"
    elif hero[1] > enemy[1] and map[enemy[0]][enemy[1]+1] in can_move:
        if area.step_pos == [enemy[0], enemy[1]]:
            map[enemy[0]][enemy[1]] = "S"
        else:
            map[enemy[0]][enemy[1]] = 0
        enemy_ins.ene_now_pos = [enemy[0], enemy[1] + 1]
        map[enemy_ins.ene_now_pos[0]][enemy_ins.ene_now_pos[1]] = "A"
    else:
        pass