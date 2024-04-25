from typing import List
from functools import lru_cache

def stone_game(values_A: List[int], values_B: List[int]) -> int:
    n = len(values_A)
    initial_state = tuple([True] * n)  # 初期状態をtupleとして保持

    @lru_cache(None)
    def strategy(player: str, state: tuple) -> int:
        if all(not s for s in state):  # 全てFalseの場合、すべての石が取られている
            return 0

        max_value = float("-inf")

        for i in range(n):
            if state[i]:  # 石iが残っている場合
                new_state = list(state)  # 現在の状態をリストに変換
                new_state[i] = False  # 石iを取る
                new_state_tuple = tuple(new_state)  # 新しい状態をtupleに変換

                if player == "A":  # プレーヤーAの場合
                    result = values_A[i] - strategy("B", new_state_tuple)
                else:  # プレーヤーBの場合
                    result = values_B[i] - strategy("A", new_state_tuple)

                max_value = max(max_value, result)  # 最大値を更新

        return max_value

    return strategy("A", initial_state)  # ゲーム開始、プレーヤーAから開始

# この関数を呼び出すときは、適切なvalues_Aとvalues_Bを与える必要があります。
