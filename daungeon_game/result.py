import time

#ゲームクリア表示
def game_win():
    mess = list("GAME CLEAR!!\n")
    win_mess = [mess, "おめでとうございます！！\n", "魔王を倒し、魔宮から脱出することができました！\n"]
    for i in range(len(win_mess)):
        if type(win_mess[i]) == list:
            for j in win_mess[i]:
                print(j, end='', flush=True)
                time.sleep(0.4)
        else:
            print(win_mess[i], end='', flush=True)
            time.sleep(1)
        
#ゲームオーバー表示
def game_loss(hero_hp): #勇者のHP
    mess = list("GAME OVER")
    loss_mess = [mess, "魔物に倒されてしまいました…\n", "仲間や装備を集めてみましょう！\n"]
    #倒された時
    if hero_hp <= 0:
        for i in range(len(loss_mess)):
            if type(loss_mess[i]) == list:
                for j in loss_mess[i]:
                    print(j, end='', flush=True)
                    time.sleep(0.4)
            else:
                print(loss_mess[i], end='', flush=True)
                time.sleep(1)

        return True
    #それ以外
    else:
        return False