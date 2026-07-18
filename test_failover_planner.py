import unittest

from failover_planner import choose_region


class FailoverPlannerTest(unittest.TestCase):
    def test_selects_healthy_capacity_region(self):
        rows = [
            {"region": "a", "health": "green", "free_capacity_pct": "20", "replication_lag_sec": "10"},
            {"region": "b", "health": "green", "free_capacity_pct": "50", "replication_lag_sec": "30"},
        ]
        self.assertEqual(choose_region(rows)["region"], "b")


if __name__ == "__main__":
    unittest.main()
