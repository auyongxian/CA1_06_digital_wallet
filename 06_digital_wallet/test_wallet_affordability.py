import pytest

from wallet_affordability import can_afford

INVALID_TYPES = [1.5, 1.0, "1", None, True, False]
INVALID_IDS = ["float_1.5", "float_1.0", "str_1", "None", "True", "False"]


# ---------- Valid: must return the real bool True/False (not 1/0) ----------
@pytest.mark.parametrize(
    "balance, price, expected",
    [
        pytest.param(500, 500, True, id="TC-001-balance-equals-price"),
        pytest.param(499, 500, False, id="TC-002-balance-below-price"),
    ],
)
def test_affordability_result(balance, price, expected):
    result = can_afford(balance, price)
    assert result is expected  # identity check: 1 / 0 would fail


# ---------- ValueError: right type, negative ----------
@pytest.mark.parametrize(
    "balance, price",
    [
        pytest.param(-1, 0, id="TC-003-negative-balance"),
        pytest.param(500, -1, id="TC-004-negative-price"),
    ],
)
def test_can_afford_value_error(balance, price):
    with pytest.raises(ValueError):
        can_afford(balance, price)


# ---------- TypeError: invalid data type ----------
@pytest.mark.parametrize("bad", INVALID_TYPES, ids=INVALID_IDS)
def test_tc_005_invalid_balance_type(bad):
    with pytest.raises(TypeError):
        can_afford(bad, 1)


@pytest.mark.parametrize("bad", INVALID_TYPES, ids=INVALID_IDS)
def test_tc_006_invalid_price_type(bad):
    with pytest.raises(TypeError):
        can_afford(500, bad)
