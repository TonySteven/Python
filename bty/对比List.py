# 读取文件中的车牌号
def read_license_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取文件并去掉每一行的换行符
        return [line.strip() for line in file.readlines()]


# 对比两个列表，找出缺少的车牌号
def compare_licenses(list1, list2):
    # 将列表转为集合并进行差集操作
    missing_in_list2 = set(list1) - set(list2)  # list1 中有而 list2 中没有
    missing_in_list1 = set(list2) - set(list1)  # list2 中有而 list1 中没有

    return missing_in_list2, missing_in_list1


# 主函数
def main():
    # 替换为实际的文件路径
    file1_path = '/Users/steven/PycharmProjects/Python/bty/data/file1.txt'
    file2_path = '/Users/steven/PycharmProjects/Python/bty/data/file2.txt'

    # 读取文件
    list1 = read_license_file(file1_path)
    list2 = read_license_file(file2_path)

    # 对比车牌号
    missing_in_file2, missing_in_file1 = compare_licenses(list1, list2)

    # 输出差异
    print("Missing in file2:")
    for item in missing_in_file2:
        print(item)

    print("\nMissing in file1:")
    for item in missing_in_file1:
        print(item)


# 运行主函数
if __name__ == '__main__':
    main()
