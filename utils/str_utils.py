__all__ = [
    "StrShortener",
]


class StrShortener:
    """文本缩略"""

    def __init__(self, original: str, max_length: int = 30):
        """
        :param original:
        :param max_length:
        """
        self.original = original
        self.max_length = max_length

    def generate(self) -> str:
        r = self.original.strip()
        if len(r) <= self.max_length:
            return r
        return r[:self.max_length] + " ..."

    def __str__(self):
        return self.generate()
