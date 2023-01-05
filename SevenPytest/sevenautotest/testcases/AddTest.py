# -*- coding: utf-8 -*-
# @Time    : 2022/1/19 10:09
# @Author  : linwei
import pytest
from sevenautotest.basetestcase import BaseTestCase


class AddTest(BaseTestCase):

    @pytest.mark.testcase('计算x+y的结果',author="linwei", editor="")
    def test_add(self,testdata):
        x = int(testdata.get("x"))
        y = int(testdata.get("y"))
        z = int(testdata.get("期望结果"))
        if x+y == z:
            print('测试成功!')
            pass
        else:
            print("测试失败！")

    # @pytest.mark.testcase('计算x+y的结果',author="linwei", editor="")
    # def test_add(self,testdata):
    #     x = 1
    #     y = 2
    #     z = 3
    #     if x+y == z:
    #         print('测试成功!')
    #     else:
    #         print("测试失败！")

if __name__ == "__main__":
    pass