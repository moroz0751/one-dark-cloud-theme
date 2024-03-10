# /usr/bin/env python
import random
from typing import ClassVar


class Cloud:
    TYPES: ClassVar[list[int]] = ["Cumulus", "Stratus", "Cirrus", "Nimbostratus"]

    def __init__(self, color: str, type: str | None):
        self.color = color
        self.type = type or random.choice(self.TYPES)
        self.altitude = None

    @property
    def altitude(self) -> int:
        if self._altitude is None:
            self.altitude = random.randint(0, 100)
        return self._altitude

    def climb(self, increase: int | None) -> int:
        """One dark but not so stormy night..."""
        if increase:
            self.altitude += increase
        return self.altitude
