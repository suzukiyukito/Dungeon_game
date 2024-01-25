def display_help():
    while True:
        print("1) ゲームのルールを表示")
        print("2) 画面表示のヘルプ")
        print("3) ゲームに戻る")
        choice = input("選択内容を入力してください：")
        if choice == "1":
            game_rules()
        elif choice == "2":
            viewing_help()
        elif choice == "3":
            # ゲーム開始のロジックをここに実装
            break
        else:
            print("不正な入力です。")

def viewing_help():
    print("ヘルプメニュー:")
    print("コントロール:")
    print("  w: 上に移動")
    print("  a: 左に移動")
    print("  s: 下に移動")
    print("  d: 右に移動")
    print("  t: ステータス表示")
    print("  f: 攻撃/スキル")
    print("  e: アクション")
    print("  i: アイテム")
    print("  h: ヘルプ")
    
    HERO = "勇"
    ENEMY = "敵"
    ITEM = "宝"
    FELLOW1 = "弓"
    FELLOW2 = "賢"
    FELLOW3 = "癒"
    STEP = "階"
    GOAL = "出"
    KING = "魔"
    print("\nマップ凡例:")
    print(f"{HERO}:勇者(主人公)")
    print(f"{ENEMY}:魔物")
    print(f"{ITEM}:宝箱")
    print(f"{FELLOW1}:レンジャー(仲間)")
    print(f"{FELLOW2}:賢者(仲間)")
    print(f"{FELLOW3}:僧侶(仲間)")
    print(f"{STEP}:階段")
    print(f"{GOAL}:出口")

    print(f"{KING}{KING}\n{KING}{KING}:魔王")

def game_rules():
    while True:
        print("\nゲームのルール:")
        print("1: 基本的なゲームフロー")
        print("2: 戦闘について")
        print("3: 基本的な行動")
        print("4: 自分のステータスについて")
        print("5: 仲間について")
        print("6: アイテムについて")
        print("7: メインメニューに戻る")
        choice = input("選択内容を入力してください：")

        if choice == "1":
            print("\n[基本的なゲームフローについて]")
            print("ターン制のゲーム。\n現在いるエリア内でのみターンが進行。\n勇者が先に動き、その後敵オブジェクトが行動。\n勇者は他のマスに動くか、その場に停滞可能。\nエリア内には魔物、宝箱、階段、仲間が存在。これらは動かない。\n宝箱は上下左右のマスにいることでインタアクション可能。\n宝箱の中身は開けてから判明。\n階段を使い、次のフロアに移動。\n仲間の入手方法は宝箱と同じ。\nゲームはエリアとフロアに分かれており、今回は3フロア(-2F, -1F, 1F)。\n勇者は-2Fに閉じ込められている。\n最終的にはボスを倒し、ゴールに到達する必要がある。")
        elif choice == "2":
            print("\n[戦闘について]")
            print("戦闘は戦うも逃げるも自由。ただし魔王を倒さなければ出口にはたどりつけない。\nHPとATKがステータス。\n勇者は戦闘時、攻撃・アイテム・スキル・逃げるの選択可能。\n攻撃はATK値が敵に反映される。\nアイテムは宝箱から得たものを使用可能。\nスキルは仲間固有のもので使用回数に制限あり。\n逃げる時に勇者を動かす。\n敵のHPはそのままで位置は初期位置に戻る。")
        elif choice == "3":
            print("\n[基本的な行動について]")
            print("勇者は十字方向にのみ行動可能、斜め移動不可。\n通路を通じて別エリアに移動可能。\nエリア内の内容は入ってから判明。")
        elif choice == "4":
            print("\n[自分のステータスについて]")
            print("レベル制で、レベルアップでHPとATK上昇。\nレベルアップでHPを5回復。\n初期HPは20、ATKは5。\nレベルアップでHPは+5、ATKは+3。\nレベルアップには敵の撃破が必要。")
        elif choice == "5":
            print("\n[仲間について]")
            print("救出するとスキル利用可能。\nB2Fのレンジャーのスキルは遠距離攻撃、選択した方向の直線上にいる敵1体に対して10ダメージ、回数制限5回。\nB1Fの賢者のスキルは範囲攻撃、勇者の周囲1マスにいる敵すべてに15ダメージ、回数制限3回。\n1Fの僧侶のスキルは回復、勇者の体力を20回復する、回数制限3回。")
        elif choice == "6":
            print("\n[アイテムについて]")
            print("ポーションはHPを10回復、ハイポーションはHPを30回復。\n力の種は入手すると即座にHPの最大値が増える。\n聖剣は入手するとATKが増加する。魔王に対してはさらにATKが上昇する。")
        elif choice == "7":
            break
        else:
            print("不正な入力です。")

        input("なにかキーを入力して戻る：")  # ここでユーザーに任意のキー入力を促す



if __name__ == "__main__":
    # メインメニューを表示
    display_help()
