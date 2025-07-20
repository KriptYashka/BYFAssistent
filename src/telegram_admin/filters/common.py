from aiogram.filters import Filter
from aiogram.types import Message


class TextEqualsFilter(Filter):
    def __init__(self, text: str):
        self.text = text.lower()

    async def __call__(self, message: Message) -> bool:
        return message.text and message.text.lower() == self.text
