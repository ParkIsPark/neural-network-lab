"""Check the Python environment before implementing the MLP."""

import numpy as np

from common.paths import DATA_DIR, PROCESSED_DATA_DIR, RAW_DATA_DIR


def main() -> None:
    left = np.array([[1.0, 2.0], [3.0, 4.0]])
    right = np.array([[5.0, 6.0], [7.0, 8.0]])
    result = left @ right
    np.testing.assert_allclose(result, [[19.0, 22.0], [43.0, 50.0]])

    for directory in (DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR):
        if not directory.is_dir():
            raise FileNotFoundError(directory)

    print(f"NumPy {np.__version__}")
    print(f"Shared data directory: {DATA_DIR}")
    print(f"Matrix multiplication:\n{result}")
    print("MLP workspace ready.")


if __name__ == "__main__":
    main()
