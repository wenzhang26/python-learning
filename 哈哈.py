foods = {
    "鸡胸肉": 165,   # 每100克，千卡
    "米饭": 116,
    "鸡蛋": 143,
    "牛奶": 54,
    "苹果": 52,
    "面包": 265,
}
records = []
while True:
    i = input('请输入（食物 克数，输入"结束"退出）：')
    x = i.split()
    food = x[0]
    heavy = float(x[1])
    print(foods[food])