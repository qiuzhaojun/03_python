"""
    游戏逻辑控制器，负责处理游戏核心算法．
"""

class GameCoreController:
    """
        控制游戏核心逻辑
    """

    def __init__(self):
        self.__list_merge = None  # type:list
        self.__map = [
            [2, 0, 4, 4],
            [16, 4, 2, 0],
            [0, 2, 0, 2],
            [2, 0, 0, 2],
        ]

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
            零元素移动到末尾.
        """
        for i in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            合并
        """
        self.__zero_to_end()

        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        """
            向左移动
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        """
            向右移动
        """
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def move_up(self):
        self.__square_matrix_transpose()
        self.move_left()
        self.__square_matrix_transpose()

    def move_down(self):
        self.__square_matrix_transpose()
        self.move_right()
        self.__square_matrix_transpose()

    def __square_matrix_transpose(self):
        """
            方阵转置
        :param sqr_matrix: 二维列表类型的方阵
        """
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]
