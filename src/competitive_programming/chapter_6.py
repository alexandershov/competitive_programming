import collections


def solve_coins_problem(coins: set[int], amount: int) -> list[int]:
    # TODO: make it more elegant
    assert amount >= 0
    for a_coin in coins:
        assert a_coin > 0

    cache = {0: []}  # amount -> solution
    for cur_amount in range(0, amount + 1):
        for a_coin in coins:
            prev_solution = cache.get(cur_amount - a_coin)
            if prev_solution is not None:
                if cur_amount not in cache or len(cache[cur_amount]) > len(prev_solution) + 1:
                    cache[cur_amount] = prev_solution + [a_coin]
    return cache.get(amount)


def solve_coins_count_problem(coins: set[int], amount: int) -> int:
    cache = collections.defaultdict(int, {0: 1})
    for cur_amount in range(1, amount + 1):
        for a_coin in coins:
            prev_count = cache[cur_amount - a_coin]
            cache[cur_amount] += prev_count
    return cache[amount]
