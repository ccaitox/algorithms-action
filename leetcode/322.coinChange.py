# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

"""
    @FileName: 322.coinChange.py
    @Author: charlie.ai
    @CreateTime: 2020/3/8-15:03
    @Description: 
"""
from typing import List

"""
硬币兑换：
    给定不同面额的硬币 coins 和一个总金额 amount。
    编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
    示例 1:
        输入: coins = [1, 2, 5], amount = 11
        输出: 3 
        解释: 11 = 5 + 5 + 1
    示例 2:
        输入: coins = [2], amount = 3
        输出: -1
    说明: 你可以认为每种硬币的数量是无限的。
    标签: 动态规划
"""


class Solution:
    @staticmethod
    def coin_change(coins: List[int], amount: int) -> int:
        # dynamic programming: f(n)=1+min(f(n-c1),f(n-c2),f(n-c3))
        # 自下而上
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        else:
            return int(dp[amount])

    @staticmethod
    def coin_change2(coins: List[int], amount: int) -> int:
        # 自上而下
        res = [0 for _ in range(amount + 1)]

        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, res[i - c] + 1)
            res[i] = cost

        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]


if __name__ == "__main__":
    s = Solution()
    result = s.coin_change(coins=[1, 2, 5], amount=11)
    print(result)
