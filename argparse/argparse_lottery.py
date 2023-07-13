import random
import argparse


class Lottery:
    def __init__(self , mymoney):
        self.mymoney = mymoney
       
    def game(self):
        betting = int(input("배팅금액을 입력하세요!!")) 
        
        if self.mymoney < betting:
            print("No more Game!!!")
            return
        else: 
            choice = 1
            selct_num = int(input("숫자를 고르세요"))
            random_num = random.randint(1,6)
            if selct_num != random_num:
                print(f'선택하신 숫자는{selct_num}이고 당첨번호는 {random_num}입니다')
                print('게임에서 패배하셨습니다.')
                self.mymoney = self.mymoney - betting
                print(f'현재잔액 {self.mymoney}')
                selct_game = input('게임을 계속 진행하시려면 1 , 중단하시려면 2를 입력하세요!')
                if selct_game == "1":
                    choice =1
                elif selct_game == "2":
                    choice = 0
                    print("게임을 종료합니다")
            elif selct_num == random_num:
                 print(f'선택하신 숫자는{selct_num}이고 당첨번호는 {random_num}입니다')
                 print('게임에서 승리하셨습니다.')
                 self.mymoney = (self.mymoney + betting)*10
                 print(f'현재잔액 {self.mymoney}')
                 selct_game = input('게임을 계속 진행하시려면 1 , 중단하시려면 1를 입력하세요!')
                 if selct_game == "1":
                    choice =1
                 elif selct_game == "2":
                    choice = 0
                    print("게임을 종료합니다")
lottery = Lottery(100000)
lottery.game()