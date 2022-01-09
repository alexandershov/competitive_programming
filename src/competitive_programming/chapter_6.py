def solve_coins_problem(coins: set[int], amount: int) -> list[int]:
    assert amount >= 0
    for a_coin in coins:
        assert a_coin > 0

    cache = {}  # amount -> solution
    for cur_amount in range(0, amount + 1):
        if cur_amount in coins:
            cache[cur_amount] = [cur_amount]
        else:
            for a_coin in coins:
                prev_solution = cache.get(cur_amount - a_coin)
                if prev_solution is not None:
                    if cur_amount not in cache or len(cache[cur_amount]) > len(prev_solution) + 1:
                        cache[cur_amount] = prev_solution + [a_coin]
    return cache.get(amount, [])
