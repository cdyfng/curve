import brownie
import pytest

pytestmark = pytest.mark.usefixtures("add_initial_liquidity", "mint_bob", "approve_bob")


def test_add_liquidity(bob, swap, wrapped_coins, pool_token, initial_amounts, base_amount, n_coins):
    swap.add_liquidity(initial_amounts, 0, {'from': bob})

    for coin, amount in zip(wrapped_coins, initial_amounts):
        assert coin.balanceOf(bob) == 0
        assert coin.balanceOf(swap) == amount * 2

    assert pool_token.balanceOf(bob) == n_coins * 10**18 * base_amount
    assert pool_token.totalSupply() == n_coins * 10**18 * base_amount * 2


