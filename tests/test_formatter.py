import unittest

from tidyname import normalize_name


class EmptyInputTests(unittest.TestCase):
    def test_none(self):
        self.assertEqual(normalize_name(None), "")

    def test_empty_string(self):
        self.assertEqual(normalize_name(""), "")

    def test_whitespace_only(self):
        self.assertEqual(normalize_name("  \t \xa0 "), "")


class CasingAndWhitespaceTests(unittest.TestCase):
    def test_all_caps(self):
        self.assertEqual(normalize_name("MARY"), "Mary")

    def test_all_lowercase(self):
        self.assertEqual(normalize_name("james"), "James")

    def test_collapses_internal_whitespace(self):
        self.assertEqual(normalize_name("  jean   VAN DYKE  "), "Jean van Dyke")

    def test_non_breaking_space(self):
        self.assertEqual(normalize_name("john\xa0smith"), "John Smith")

    def test_single_letter_token(self):
        self.assertEqual(normalize_name("j smith"), "J Smith")


class PatternTests(unittest.TestCase):
    def test_mc_prefix(self):
        self.assertEqual(normalize_name("MCDONALD"), "McDonald")

    def test_bare_mc_is_not_mangled(self):
        self.assertEqual(normalize_name("MC"), "Mc")

    def test_mac_is_left_alone(self):
        self.assertEqual(normalize_name("MACY"), "Macy")

    def test_apostrophe(self):
        self.assertEqual(normalize_name("o'brien"), "O'Brien")

    def test_hyphen(self):
        self.assertEqual(normalize_name("ST-PIERRE"), "St-Pierre")

    def test_hyphen_with_mc_part(self):
        self.assertEqual(normalize_name("mcdonald-smith"), "McDonald-Smith")

    def test_particles_stay_lowercase(self):
        self.assertEqual(normalize_name("DE LA CRUZ"), "de la Cruz")
        self.assertEqual(normalize_name("VAN DER BERG"), "van der Berg")


class ReorderTests(unittest.TestCase):
    def test_last_first(self):
        self.assertEqual(normalize_name("SMITH, JOHN"), "John Smith")

    def test_last_first_without_space_after_comma(self):
        self.assertEqual(normalize_name("smith,john"), "John Smith")

    def test_multiple_commas_left_in_place(self):
        self.assertEqual(normalize_name("a, b, c"), "A, B, C")

    def test_trailing_comma_is_not_reordered(self):
        self.assertEqual(normalize_name("smith,"), "Smith,")


class TitleAndSuffixTests(unittest.TestCase):
    def test_title_with_period(self):
        self.assertEqual(normalize_name("DR. JOHN SMITH"), "John Smith")

    def test_title_without_period(self):
        self.assertEqual(normalize_name("mrs jane doe"), "Jane Doe")

    def test_only_one_title_is_stripped(self):
        self.assertEqual(normalize_name("Dr. Prof. Smith"), "Prof. Smith")

    def test_suffix_with_comma(self):
        self.assertEqual(normalize_name("John Smith, Jr."), "John Smith")

    def test_suffix_without_comma(self):
        self.assertEqual(normalize_name("John Smith III"), "John Smith")

    def test_stacked_suffixes(self):
        self.assertEqual(normalize_name("John Smith Jr., PhD"), "John Smith")

    def test_suffix_before_reorder(self):
        self.assertEqual(normalize_name("SMITH, JOHN, JR."), "John Smith")

    def test_title_and_suffix_together(self):
        self.assertEqual(normalize_name("Dr. john smith, md"), "John Smith")


class IdempotenceTests(unittest.TestCase):
    def test_output_is_stable(self):
        samples = [
            "MARY O'BRIEN",
            "  jean   VAN DYKE  ",
            "mcdonald-smith",
            "SMITH, JOHN, JR.",
            "Dr. John Smith",
            "DE LA CRUZ",
        ]
        for sample in samples:
            once = normalize_name(sample)
            self.assertEqual(normalize_name(once), once, sample)


if __name__ == "__main__":
    unittest.main()
