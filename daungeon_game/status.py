class Hero():
    def __init__(self, pos):
        self.hero_lv = 1
        self.hero_exp = 0
        self.hero_hp = 20
        self.hero_hp_max = 20
        self.hero_atk = 5
        self.hero_pos = pos
        self.excalibur_flag = False
        self.fellow_flag = [False, False, False]

class Status:
    def __init__(self, hero):
        self.hero = hero

    def display_status(self):
        print(f"レベル: {self.hero.hero_lv}")
        print(f"経験値: {self.hero.hero_exp}")
        print(f"HP: {self.hero.hero_hp}/{self.hero.hero_hp_max}")
        print(f"攻撃力: {self.hero.hero_atk}")
        print(f"位置: {self.hero.hero_pos}")
        print(f"エクスカリバー所持: {'はい' if self.hero.excalibur_flag else 'いいえ'}")  # 聖剣を持っているか
        print(f"仲間解放: {' '.join(['はい' if flag else 'いいえ' for flag in self.hero.fellow_flag])}")  # 仲間が解放されているかどうかを表示

# Heroクラスのインスタンスを作成
hero = Hero(pos=(0,0))

# Statusクラスのインスタンスを作成し、display_statusメソッドを呼び出す
status_instance = Status(hero)
status_instance.display_status()
