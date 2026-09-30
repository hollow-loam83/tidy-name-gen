import unittest

from tidyname import RandomNameGenerator


class GeneratorTests(unittest.TestCase):
    def test_same_seed_same_output(self):
        a = RandomNameGenerator(seed=7)
        b = RandomNameGenerator(seed=7)
        self.assertEqual(a.many(20), b.many(20))

    def test_many_returns_requested_count(self):
        gen = RandomNameGenerator(seed=1)
        self.assertEqual(len(gen.many(5)), 5)
        self.assertEqual(gen.many(0), [])

    def test_custom_pools_are_normalized(self):
        gen = RandomNameGenerator(first_names=["ALICE"], last_names=["o'neill"], seed=3)
        self.assertEqual(gen.full_name(), "Alice O'Neill")

    def test_first_and_last_come_from_their_own_pools(self):
        gen = RandomNameGenerator(first_names=["ann", "bo"], last_names=["LEE"], seed=3)
        for _ in range(20):
            self.assertIn(gen.first_name(), {"Ann", "Bo"})
            self.assertEqual(gen.last_name(), "Lee")

    def test_empty_first_pool_raises(self):
        with self.assertRaises(ValueError):
            RandomNameGenerator(first_names=[], last_names=["Lee"])

    def test_empty_last_pool_raises(self):
        with self.assertRaises(ValueError):
            RandomNameGenerator(first_names=["Ann"], last_names=[])

    def test_default_pools_produce_normalized_names(self):
        gen = RandomNameGenerator(seed=11)
        for name in gen.many(50):
            self.assertEqual(name, " ".join(name.split()))
            self.assertNotEqual(name, "")


if __name__ == "__main__":
    unittest.main()
