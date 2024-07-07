#!/usr/bin/env python
import random
from typing import ClassVar


class Cloud:
    TYPES: ClassVar[list[int]] = ["Cumulus", "Stratus", "Cirrus", "Nimbostratus"]

    def __init__(self, color: str, type: str | None = None):
        """One dark but not so stormy night..."""
        self.color = color
        self.type = type or random.choice(self.TYPES)
        self._altitude = None

    @property
    def altitude(self) -> int:
        if self._altitude is None:
            self.altitude = self._gen_altitude()
        return self._altitude

    def climb(self, increase: int | None) -> int:
        if increase:
            self.altitude += increase
        return self.altitude

    def _gen_altitude(self) -> int:
        return random.randint(100, 1000)


my_cloud = Cloud(color="gray")
print(f"New cloud: {my_cloud}\n")
