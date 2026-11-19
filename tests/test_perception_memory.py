import pytest

from ai import perception_memory as mod

CASES = [
    ('in_frustum', [30, 10, 90, 60], True, False),
    ('in_frustum', [30, 40, 90, 60], False, False),
    ('visible_hits', [[False, True, False]], [0, 2], False),
    ('sound_attenuation', [10, 0.5], 0.16666666666666666, True),
    ('memory_decay', [1.0, 2.0, 2.0], 0.5, True),
    ('team_visible', [1, 1], True, False),
    ('team_visible', [1, 2], False, False),
    ('sweep_covers', [0, 90, 45], True, False),
    ('sweep_covers', [0, 90, 120], False, False),
    ('priority_score', [4, 8], 1.6, True),
    ('grass_blocks', [True, False], True, False),
    ('grass_blocks', [False, False], False, False),
    ('state_hysteresis', ['chase', 0.4, 0.8, 0.3], 'chase', False),
    ('state_hysteresis', ['search', 0.5, 0.8, 0.3], 'search', False),
    ('unified_timestamp', [90, 30], 3.0, True),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_perception_memory_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
