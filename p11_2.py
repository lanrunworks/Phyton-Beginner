class MyClass():
    a = "マイクラス" # クラス変数
    __b = 0         # クラス変数

    def __init__(self, data):
        self.__number = MyClass.__b # クラス変数をインスタンス変数に代入
        self.mydata = data # 初期化関数の引数をインスタンス変数に代入
        print("MyClass Object is created, number: ",
            self.__number)
        
        MyClass.__b += 1

    def show_number(self):
        print(self.__number)


if __name__ == '__main__':
    print("MyClass のクラス変数 a: ", MyClass.a)

    instance1 = MyClass(1)
    instance2 = MyClass(10)

    instance1.show_number()
    instance2.show_number()

    print("mydata_of instance1: ", instance1.mydata)
    print("mydata_of instance2: ", instance2.mydata)
    instance1.mydata += 1
    instance2.mydata += 2
    print("mydata_of instance1: ", instance1.mydata)
    print("mydata_of instance2: ", instance2.mydata)
    
    # print(MyClass.__b) # __bは保護されているのでエラー
