import os
import sys
import unittest


# Configure the root directory path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(root_dir)

from src.data.make_dataset import generate_data

class TestMakeDataset(unittest.TestCase):
    def test_make_dataset_constraints(self):
        """Test case for the generate_data function."""

        length = 100
        min_int = 0
        max_int = 1
        result = generate_data(
            length=length,
            lowest=min_int,
            highest=max_int,
        )

        # Test the returned result is of the correct length
        self.assertEqual(len(result), length, f"Result doesn't contain {length} elements, found {len(result)}")

        # Test the generated data isn't outside of the provided bounds - lower
        self.assertGreaterEqual(min(result), min_int, f"Expected no results less than {min_int}, found {min(result)}")

        # Test the generated data isn't outside of the provided bounds - upper
        self.assertLessEqual(max(result), max_int, f"Expected no results more than {max_int}, found {max(result)}")


if __name__ == "__main__":
    unittest.main()
