from app.services.spaced_repetition_stats import calculate_retention_probability


def test_calculate_retention_probability_decay():
    assert calculate_retention_probability(0) == 1.0
    r1 = calculate_retention_probability(1.0, stability=2.0)
    r2 = calculate_retention_probability(4.0, stability=2.0)
    assert r1 > r2
    assert 0.0 < r2 < 1.0
