import random


def generate_schedule(members, weeks):
    """
    随机生成值班表，每人一周 oncall，按周循环。
    :param members: list, 成员列表
    :param weeks: int, 需要生成的周数
    :return: list of dict, 每周值班安排
    """
    random.shuffle(members)  # 随机打乱成员顺序
    schedule = []

    for week in range(weeks):
        oncall_person = members[week % len(members)]
        schedule.append({
            "week": week + 1,
            "oncall": oncall_person
        })

    return schedule


# 示例使用
members = ["李佩", "令伟", "刘涵", "文浩"]  # 4 位成员
weeks = 4  # 需要安排的总周数

schedule = generate_schedule(members, weeks)

# 打印排班表
for entry in schedule:
    print(f"Week {entry['week']}: {entry['oncall']} on-call")
