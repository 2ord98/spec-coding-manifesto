"""Tiny implementation-like file for enforcement smoke checks."""


def create_note(text: str) -> dict[str, str]:
    return {"text": text}


def list_notes(notes: list[dict[str, str]]) -> list[str]:
    return [note["text"] for note in notes]
