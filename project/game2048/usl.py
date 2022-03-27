"""
    游戏界面控制器，负责处理游戏界面逻辑．
"""
import os

from bll import GameCoreController

class GameConsoleView:
    """
        处理界面逻辑
    """

    def __init__(self):
        self.__controller = GameCoreController()

    def __draw_map(self):
        for line in self.__controller.map:
            for item in line:
                print(item, end="\t")
            print()

    def __update(self):
        while True:
            self.__move_map_for_input()
            self.__draw_map()

    def __move_map_for_input(self):
        dir = input("请输入：")
        if dir == "w":
            self.__controller.move_up()
        elif dir == "s":
            self.__controller.move_down()
        elif dir == "a":
            self.__controller.move_left()
        elif dir == "d":
            self.__controller.move_right()

    def main(self):
        self.__draw_map()
        self.__update()