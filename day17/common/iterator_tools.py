"""
    可迭代对象工具集
"""


class IterableHelper:
    """
        可迭代对象助手
    """

    @staticmethod
    def find_all(iterable, func_condition):
        """
            在可迭代对象中,根据指定条件查找所有元素.
        :param iterable:可迭代对象
        :param func_condition:函数类型的条件,一个参数,一个bool返回值
        :return:生成器,负责推算满足条件的数据
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable, func_condition):
        """
            在可迭代对象中,根据指定条件查找单个元素.
        :param iterable:可迭代对象
        :param func_condition:函数类型的条件,一个参数,一个bool返回值
        :return:满足条件的元素
        """
        for item in iterable:
            if func_condition(item):
                return item

    @staticmethod
    def select(iterable, func_handle):
        """
            在可迭代对象中,根据某些逻辑,查询元素的成员.
        :param iterable: 可迭代对象
        :param func_handle: 查询元素的逻辑
        :return: 生成器,推算元素
        """
        for item in iterable:
            yield func_handle(item)

    @staticmethod
    def get_count(iterable, func_condition):
        """
            获取可迭代对象中满足条件的元素数量
        :param iterable:可迭代对象
        :param func_condition:条件
        :return:数量
        """
        count = 0
        for item in iterable:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def delete_all(iterable, func_condition):
        """
            根据条件,删除多个元素.
        :param iterable:可迭代对象
        :param func_condition:条件
        :return:删除的数量
        """
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if func_condition(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def get_max(iterable, func_handle):
        """
            根据指定条件在可迭代对象中获取最大的元素
        :param iterable:可迭代对象
        :param func_handle:条件
        :return:最大的元素
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if func_handle(max_value) < func_handle(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def order_by(iterable, func_condition):
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if func_condition(iterable[r]) > func_condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]
