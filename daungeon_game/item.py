#アイテムのクラスを記述

"""
・-2F：ポーション(1)
・-1F：ポーション(1)。力の種(3)
・1F ：聖剣(4)、ハイポーション(2)
"""

class Item():
    # アイテムの辞書をクラスレベルで定義
    item_dict = {1: "Potion", 2: "High_Potion", 3: "Power_Seed", 4: "Holy_Sword"}

    def __init__(self, item_id,pos):
        # 指定されたアイテムIDに基づいてアイテムの種類を取得
        self.item_type = Item.item_dict.get(item_id, None)
        if self.item_type is None:
            print(f"無効なアイテムID: {item_id}")
        # アイテムのIDを設定
        self.item_id = item_id
        self.pos = pos
        name_dict = {1: "ポーション", 2: "ハイポーション", 3: "力の種", 4: "聖剣"}
        self.item_name = name_dict[item_id]

    def use_item(self, hero):
        # 指定されたアイテムIDに基づいてアクションを実行
        action = getattr(self, f"use_{self.item_type}", None)
        if action:
            action(hero)
        else:
            print(f"アイテムに対して定義されていないアクション: {self.item_type}")

    def use_Potion(self, hero):
        hero.hero_hp += 10  # 勇者のHPを10回復
        if hero.hero_hp > hero.hero_hp_max:
            hero.hero_hp = hero.hero_hp_max
        print(f"ポーションを使った。HPが10回復した。")

    def use_High_Potion(self, hero):
        hero.hero_hp += 30  # 勇者のHPを30回復
        if hero.hero_hp > hero.hero_hp_max:
            hero.hero_hp = hero.hero_hp_max
        print(f"ハイポーションを使った。HPが30回復した。")

    def use_Power_Seed(self, hero):
        hero.hero_hp_max += 15  # 勇者の最大HPを15増加
        print(f"力の種を使った。最大HPが15増加した。")

    def use_Holy_Sword(self, hero):
        hero.hero_atk += 10  # 勇者のATKを増加
        print(f"聖剣を使った。攻撃力が増加した。")