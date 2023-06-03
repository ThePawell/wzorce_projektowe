import time
from typing import Any

STEP_DELAY = 3


class Drink:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        for part in self.parts:
            print(f"Dodaję: {part}...")
            time.sleep(STEP_DELAY)
        print("\n______________________________")
        print("Wydawanie zakończone.")
