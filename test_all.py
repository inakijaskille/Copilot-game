"""
Comprehensive test suite for the space mission project.
"""

from greeting import welcome_message
from translator import alien_translator, decode_message
from inventory import check_inventory, space_station_inventory
from mission_control import assign_mission


def test_welcome_message():
    """Test the welcome_message function."""
    result = welcome_message("Alice", "Navigation")
    assert "Alice" in result
    assert "Navigation" in result
    assert result == "Welcome, Alice! You are enrolled in Navigation."
    print("✓ test_welcome_message passed")


def test_alien_translator():
    """Test the alien_translator function."""
    result = alien_translator("Hello")
    assert result == "H*ll*"
    
    result2 = alien_translator("AEIOU")
    assert result2 == "*****"
    
    result3 = alien_translator("xyz")
    assert result3 == "xyz"
    print("✓ test_alien_translator passed")


def test_decode_message():
    """Test the decode_message function."""
    encoded = "H*ll* W*rld"
    decoded = decode_message(encoded)
    assert "*" not in decoded
    assert "Helle Werld" == decoded
    print("✓ test_decode_message passed")


def test_inventory():
    """Test the inventory dictionary."""
    assert "oxygen_tanks" in space_station_inventory
    assert "water_liters" in space_station_inventory
    assert space_station_inventory["oxygen_tanks"] > 0
    assert space_station_inventory["food_rations"] > 0
    print("✓ test_inventory passed")


def test_assign_mission():
    """Test the assign_mission function."""
    crew = {"name": "Test Pilot", "role": "Pilot"}
    result = assign_mission(crew, "Test Mission")
    assert result["assigned_mission"] == "Test Mission"
    assert result["name"] == "Test Pilot"
    # Original should not be modified
    assert "assigned_mission" not in crew
    print("✓ test_assign_mission passed")


def run_all_tests():
    """Run all tests and report results."""
    print("=" * 50)
    print("RUNNING TEST SUITE")
    print("=" * 50)
    print()
    
    tests = [
        test_welcome_message,
        test_alien_translator,
        test_decode_message,
        test_inventory,
        test_assign_mission
    ]
    
    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
    
    print()
    print("=" * 50)
    print(f"Results: {passed}/{len(tests)} tests passed")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()
