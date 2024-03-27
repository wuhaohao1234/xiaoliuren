from help import explain_time
# 规则数组和月份数组
rules = ["大安", "留连", "速喜", "赤口", "小吉", "空亡"]
months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

# 创建一个字典来存储月份和对应的规则
month_rule_mapping = {}

# 使用循环将月份与规则进行匹配
for i, month in enumerate(months):
    # 使用取模运算确保规则循环使用
    rule_index = i % len(rules)
    month_rule_mapping[month] = rules[rule_index]

# 假设用户从键盘输入数字，例如062211
user_input = input("请输入农历日期和时辰（格式为月日时，例如062211）：")

# 从用户输入中提取月份、日期和时辰信息
user_month = months[int(user_input[:2]) - 1]
user_date = int(user_input[2:4])
user_hour = int(user_input[4:6])

# 确定用户输入月份对应的规则
rule_for_user_month = month_rule_mapping.get(user_month, "未知")

# 确定用户输入日期对应的规则索引
month_index = rules.index(rule_for_user_month)
rule_index_for_user_date = (user_date - 1 + month_index) % len(rules)

# 确定用户输入时辰对应的规则索引
rule_index_for_user_hour = (user_hour - 1 + rule_index_for_user_date) % len(rules)

# 获取对应的规则
rule_for_user_date = rules[rule_index_for_user_date]
rule_for_user_hour = rules[rule_index_for_user_hour]

# 输出结果
print(f"{user_month} 对应的规则是：{rule_for_user_month}")
print(f"{user_date}号 对应的规则是：{rule_for_user_date}")
print(f"{user_hour}时辰 对应的规则是：{rule_for_user_hour}")


explain_time(rule_for_user_month)
explain_time(rule_for_user_date)
explain_time(rule_for_user_hour)