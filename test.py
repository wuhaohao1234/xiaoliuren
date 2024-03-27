# 定义十二时辰
shi_chen = ["子时", "丑时", "寅时", "卯时", "辰时", "巳时", "午时", "未时", "申时", "酉时", "戌时", "亥时"]

# 将小时数转换为对应的时辰
def convert_hour_to_shi_chen(hour):
    if 0 <= hour < 2:
        return shi_chen[0], 0
    elif 2 <= hour < 4:
        return shi_chen[1], 1
    elif 4 <= hour < 6:
        return shi_chen[2], 2
    elif 6 <= hour < 8:
        return shi_chen[3], 3
    elif 8 <= hour < 10:
        return shi_chen[4], 4
    elif 10 <= hour < 12:
        return shi_chen[5], 5
    elif 12 <= hour < 14:
        return shi_chen[6], 6
    elif 14 <= hour < 16:
        return shi_chen[7], 7
    elif 16 <= hour < 18:
        return shi_chen[8], 8
    elif 18 <= hour < 20:
        return shi_chen[9], 9
    elif 20 <= hour < 22:
        return shi_chen[10], 10
    elif 22 <= hour < 24:
        return shi_chen[11], 11
    else:
        return "无效的时间"

# 示例用法
hour = int(input("请输入当前时间，小时，24小时\n"))
shi_chen_result, index = convert_hour_to_shi_chen(hour)
print(f"{hour} 对应的时辰是：{shi_chen_result}", f"({index + 1}时)")