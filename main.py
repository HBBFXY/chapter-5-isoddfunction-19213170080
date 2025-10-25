def isOdd(value):
    """
    返回 True 当且仅当 value 是严格的 int（排除 bool）且为奇数。
    否则返回 False。
    """
    # 排除 bool（bool 是 int 的子类），只接受严格的 int 类型
    if type(value) is int:
        return value % 2 != 0
    return False
