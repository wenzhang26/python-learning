foods = {
    "鸡胸肉": 165,   # 每100克，千卡
    "米饭": 116,
    "鸡蛋": 143,
    "牛奶": 54,
    "苹果": 52,
    "面包": 265,
}

def read_records():
    records = []
    while True:
        i = input('请输入（食物 克数，输入"结束"退出）：')
        x = i.split()
        food = x[0]
        if food in foods:
            heavy = float(x[1])
            count = foods[food] * heavy / 100
            print(f'已记录：{food} {heavy}g = {count} kcal')
            records.append([food,heavy,count])
        elif i == '结束':
            break
        else:
            print(f'没有"{food}"这个食物，换一个')
            continue
    return records
def show_summary(records):
    print('=== 今日摄入 ===')
    total = 0
    records2 = sorted(records,  reverse=False)
    for j in records2:
        print(f'{j[0]}    {j[1]}g     {j[2]} kcal')
        total += j[2]
    print('------------------------------')
    print(f'合计               {total} kcal')

a = read_records()
show_summary(a)