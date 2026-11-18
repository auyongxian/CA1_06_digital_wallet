import pytest

from wallet_withdrawal import withdraw

# Values that are NOT plain ints (bool is rejected per General Requirement 2).
INVALID_TYPES = [1.5, 1.0, "1", None, True, False]
INVALID_IDS = ["float_1.5", "float_1.0", "str_1", "None", "True", "False"]


# ---------- Valid withdrawals (returns remaining balance as int) ----------
@pytest.mark.parametrize(
    "balance, amount, expected",
    [
        pytest.param(500, 200, 300, id="TC-001-regular"),
        pytest.param(500, 1, 499, id="TC-002-minimum-amount"),
        pytest.param(500, 500, 0, id="TC-003-exact-balance"),
    ],
)
def test_valid_withdrawal(balance, amount, expected):
    result = withdraw(balance, amount)
    assert result == expected
    assert type(result) is int


# ---------- ValueError: right type, outside permitted range ----------
@pytest.mark.parametrize(
    "balance, amount",
    [
        pytest.param(500, 501, id="TC-004-amount-above-balance"),
        pytest.param(500, 0, id="TC-005-zero-amount"),
        pytest.param(500, -1, id="TC-006-negative-amount"),
        pytest.param(-1, 1, id="TC-007-negative-balance"),
    ],
)
def test_withdraw_value_error(balance, amount):
    with pytest.raises(ValueError):
        withdraw(balance, amount)


# ---------- TypeError: invalid data type ----------
@pytest.mark.parametrize("bad", INVALID_TYPES, ids=INVALID_IDS)
def test_tc_008_invalid_balance_type(bad):
    with pytest.raises(TypeError):
        withdraw(bad, 1)


@pytest.mark.parametrize("bad", INVALID_TYPES, ids=INVALID_IDS)
def test_tc_009_invalid_amount_type(bad):
    with pytest.raises(TypeError):
        withdraw(500, bad)
