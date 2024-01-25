#各キャラクターのクラスをここに記述

#仲間のクラス
class Fellow():
    #座標と現在の階層
    def __init__(self, floor_number):
        fellow_dict = {-2:"C",-1:"D",1:"E"}
        #11/15追加
        count_dict = {-2:5, -1:3, 1:3}
        #スキルの残り回数
        self.skill_count = count_dict[floor_number]
        #救出したかのフラグ
        self.fellow_flag = False
        #追加ここまで
        self.fellow = fellow_dict[floor_number]
#敵のクラス
class Enemies:
    def __init__(self, x, y, floor_index):
        # 敵の初期位置を表すリスト
        self.ene_init_pos = [y, x]
        # 敵の現在位置を表すリスト
        self.ene_now_pos =  [y, x]
        # floor_index に基づいて敵の体力と攻撃力を設定する辞書
        enemy_stats = {
            -2: (10, 3),
            -1: (17, 4),
             1: (24, 5)
        }
        # 指定された階の敵の体力と攻撃力を取得。
        # 存在しない階が指定された場合は、体力と攻撃力を0に設定。
        self.ene_hp, self.ene_atk = enemy_stats.get(floor_index, (0, 0))

    #ダメージを受けた時の処理、倒されたかをboolで返す
    def receive_damage(self, damage):
        self.ene_hp -= damage
        if self.ene_hp <= 0:
            return True
        else:
            return False

#魔王のクラス
class King():
    def __init__(self):
        self.king_hp = 250
        self.king_atk = 10
        self.charge = 0

    def receive_damage(self, damage):
        self.king_hp -= damage
        if self.king_hp <= 0:
            return True
        else:
            return False

    def king_attack(self, hero_ins):
        hero = hero_ins.pos
        can_attack = [[2, 2], [3, 2], [2, 5], [3, 5], [4, 3], [4, 4]]

        if [hero[0], hero[1]] in can_attack:
            print(f"魔王の攻撃！勇者は{self.king_atk}ダメージを受けた")
            hero_ins.hero_hp -= self.king_atk
        else:
            if self.charge < 3:
                print("魔王は力を貯めている")
                self.charge += 1
            else:
                print("魔王の波動攻撃！勇者は20ダメージを受けた")
                hero_ins.hero_hp -= 20
                self.charge = 0

if __name__ == "__main__":
    enemy = Enemies(-2)
    print(enemy.ene_hp, enemy.ene_atk)
