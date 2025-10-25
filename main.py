def isOdd(param):
    # 第一步：判断输入是否为整数类型
    if not isinstance(param, int):
        return False
    # 第二步：若为整数，判断是否为奇数（奇数对 2 取模结果为 1）
    return param % 2 == 1
