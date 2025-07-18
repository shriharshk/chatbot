from dataclasses import dataclass


@dataclass
class ChatMessage:
    text: str
    is_user: bool
