class Dentaku():
    def __init__(self):
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self.operation = "+"

    def do_operation(self):
        if self.operation == "+":
            self.result = self.first_term + self.second_term
        elif self.operation == "-":
            self.result = self.first_term - self.second_term
        elif self.operation == "*":
            self.result = self.first_term * self.second_term
        elif self.operation == "/":
            if self.second_term == 0:
                print("0で除算できません。")
            else:
                self.result = self.first_term / self.second_term
                # self.result = self.first_term // self.second_term


dentaku = Dentaku() # 電卓オブジェクトを生成
while True: # 無限ループ
    f = int(input("First term ")) # 入力した値を整数に変換
    dentaku.first_term = f # 電卓オブジェクトに保存
    o = input("Operation ")
    dentaku.operation = o
    s = int(input("Second term "))
    dentaku.second_term = s
    dentaku.do_operation() # 電卓オブジェクトのメソッドを実行
    r = dentaku.result # 結果を取り出す
    print("Resut ", r)
