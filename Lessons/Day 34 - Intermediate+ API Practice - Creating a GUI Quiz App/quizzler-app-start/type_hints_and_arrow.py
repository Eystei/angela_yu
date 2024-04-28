age: int = 12
name: str = "12"
height: float = 12.2
is_human: bool = True


def police_check(age: int) -> bool:
    can_drive = True if age > 18 else False
    return can_drive


print("You may pass") if police_check(19) else print("Pay a fine.")
