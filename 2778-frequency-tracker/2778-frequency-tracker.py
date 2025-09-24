class FrequencyTracker:
    def __init__(self):
        self.tracker = {}            # number -> frequency
        self.freq_map = {}           # frequency -> set of numbers

    def _move(self, number, old_freq, new_freq):
        """Helper to move number from one freq set to another."""
        if old_freq > 0:
            self.freq_map[old_freq].remove(number)
            if not self.freq_map[old_freq]:      # cleanup empty set
                del self.freq_map[old_freq]

        if new_freq > 0:
            if new_freq not in self.freq_map:
                self.freq_map[new_freq] = set()
            self.freq_map[new_freq].add(number)

    def add(self, number: int) -> None:
        old_freq = self.tracker.get(number, 0)
        new_freq = old_freq + 1
        self.tracker[number] = new_freq
        self._move(number, old_freq, new_freq)

    def deleteOne(self, number: int) -> None:
        if number not in self.tracker or self.tracker[number] == 0:
            return  # nothing to delete
        old_freq = self.tracker[number]
        new_freq = old_freq - 1
        self.tracker[number] = new_freq
        self._move(number, old_freq, new_freq)

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_map and bool(self.freq_map[frequency])