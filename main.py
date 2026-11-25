"""Midnight Fridge Roast: one roast line for a smart fridge.

The fridge hums and eats power all night, yet at midnight it locks
its own door and acts like the owner is the one with the eating problem.
The joke turns the blame around: the appliance, not the human, is the
midnight snacker — petty rule, projected guilt, one tight line.
"""

ENTRY = "My fridge eats power all night, then locks at midnight like I'm the one with the eating problem."


def main():
    assert 1 <= len(ENTRY) <= 200
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
        path = "/output/entry.txt"
    except OSError:
        import os

        os.makedirs("./output", exist_ok=True)
        with open("./output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
        path = "./output/entry.txt"
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
