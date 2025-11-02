"""Tests for CLI module."""

from io import StringIO
from unittest.mock import patch

import pytest

from ramp.cli import main


def test_main_prints_version() -> None:
    """Test that main function prints version information."""
    with patch("sys.stdout", new=StringIO()) as fake_out:
        result = main()
        output = fake_out.getvalue()
        assert "Ramp CLI v0.1.0" in output
        assert result == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

