def test_add():
    from app.calculations import add

    print("Testing add function...")

    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
